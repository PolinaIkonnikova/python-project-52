from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,\
    DeleteView, UpdateView
from .models import Status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from task_manager.utils.text import MessageForUser, TitleName
from django.shortcuts import redirect


my_messages = MessageForUser()
title_names = TitleName()


class StatusesList(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'lists/statuses_list.html'
    login_url = 'login'

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return redirect(self.login_url)


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    fields = ['name']
    login_url = 'login'
    template_name = 'crud/create&update.html'
    success_url = reverse_lazy('statuses')
    success_message = my_messages.status_create
    extra_context = {'header': title_names.create_status,
                     'button_name': title_names.create}

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return redirect(self.login_url)


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['name']
    login_url = 'login'
    template_name = 'crud/create&update.html'
    success_url = reverse_lazy('statuses')
    success_message = my_messages.status_update
    extra_context = {'header': title_names.update_status,
                     'button_name': title_names.update}

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return redirect(self.login_url)


class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = Status
    login_url = 'login'
    success_url = reverse_lazy('statuses')
    template_name = 'crud/delete.html'
    extra_context = {'deltitle': title_names.to_del_status}

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return redirect(self.login_url)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, my_messages.status_delete)
        except ProtectedError:
            messages.warning(self.request, my_messages.no_delete_status)
        finally:
            return HttpResponseRedirect(success_url)
