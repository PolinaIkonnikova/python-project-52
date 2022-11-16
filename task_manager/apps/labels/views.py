from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,\
    DeleteView, UpdateView
from .models import Label
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import ProtectedError
from task_manager.utils.text import MessageForUser, \
    TitleName
from django.shortcuts import redirect


my_messages = MessageForUser()
title_names = TitleName()


class LabelsList(LoginRequiredMixin, ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'lists/labels_list.html'
    login_url = 'login'

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return redirect(self.login_url)


class CreateLabel(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'crud/create&update.html'
    success_url = reverse_lazy('labels')
    login_url = 'login'
    success_message = my_messages.label_create
    extra_context = {'header': title_names.create_label,
                     'button_name': title_names.create}

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.label_create)
        return redirect(self.login_url)


class UpdateLabel(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    fields = ['name']
    login_url = 'login'
    template_name = 'crud/create&update.html'
    success_url = reverse_lazy('labels')
    success_message = my_messages.label_update
    extra_context = {'header': title_names.update_label,
                     'button_name': title_names.update}

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return redirect(self.login_url)


class DeleteLabel(LoginRequiredMixin, DeleteView):
    model = Label
    login_url = 'login'
    success_url = reverse_lazy('labels')
    template_name = 'crud/delete.html'
    extra_context = {'deltitle': title_names.to_del_label}

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return redirect(self.login_url)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, my_messages.label_delete)
        except ProtectedError:
            messages.warning(self.request, my_messages.no_delete_label)
        finally:
            return redirect(success_url)
