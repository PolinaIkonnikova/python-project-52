from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,\
    DeleteView, UpdateView
from .models import User
from .forms import Register
from django.contrib.auth.mixins import LoginRequiredMixin,\
    UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from task_manager.utils.text import MessageForUser, TitleName
from django.contrib.auth import authenticate, login


my_messages = MessageForUser()
title_names = TitleName()


class UserList(ListView):
    model = User
    context_object_name = 'users_list'
    template_name = 'lists/users_list.html'


class RegisterUser(SuccessMessageMixin, CreateView):
    model = User
    form_class = Register
    template_name = 'crud/create&update.html'
    success_url = reverse_lazy('login')
    success_message = my_messages.user_create
    extra_context = {'header': title_names.reg,
                     'button_name': title_names.to_reg}


class UpdateUser(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = Register
    template_name = 'crud/create&update.html'
    success_url = reverse_lazy('users_list')
    extra_context = {'header': title_names.update_user,
                     'button_name': title_names.update}

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, my_messages.user_update)
        return redirect(self.success_url)

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = my_messages.no_rigths_for_user
            url = reverse_lazy('users_list')
        else:
            message = my_messages.login
            url = self.success_url
        messages.warning(self.request, message)
        return redirect(url)


class DeleteUser(LoginRequiredMixin, UserPassesTestMixin,
                 DeleteView,):
    model = User
    success_url = reverse_lazy('users_list')
    template_name = 'crud/delete.html'
    extra_context = {'deltitle': title_names.to_del_user}

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = my_messages.no_rigths_for_user
            url = self.success_url
        else:
            message = my_messages.login
            url = self.login_url
        messages.warning(self.request, message)
        return redirect(url)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, my_messages.user_delete)
            return redirect(self.success_url)
        except ProtectedError:
            messages.warning(self.request,
                             my_messages.no_delete_user)
            return redirect(success_url)
