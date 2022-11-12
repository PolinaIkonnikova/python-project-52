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


my_messages = MessageForUser()
title_names = TitleName()


class StatusesList(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'lists/statuses_list.html'

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return super().handle_no_permission()


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    fields = ('name',)
    model = Status
    template_name = 'crud/create&update.html'
    success_url = reverse_lazy('statuses')
    success_message = my_messages.status_create
    extra_context = {'header': title_names.create_status,
                     'button_name': title_names.save}

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return super().handle_no_permission()


class UpdateStatus(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    fields = ('name',)
    model = Status
    template_name = 'crud/create&update.html'
    success_url = reverse_lazy('statuses')
    success_message = my_messages.status_update
    extra_context = {'header': title_names.update_status,
                     'button_name': title_names.save}

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.status_update)
        return super().handle_no_permission()


class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy('statuses')
    template_name = 'crud/delete.html'

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return super().handle_no_permission()

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, my_messages.status_delete)
        except ProtectedError:
            messages.warning(self.request, my_messages.no_delete_status)
        finally:
            return HttpResponseRedirect(success_url)