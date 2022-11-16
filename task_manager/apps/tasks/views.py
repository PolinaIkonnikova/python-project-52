from django.urls import reverse_lazy
from django.views.generic import CreateView,\
    DeleteView, UpdateView, DetailView
from django_filters.views import FilterView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin, \
    UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from .filter import TaskFilter
from task_manager.utils.text import MessageForUser, TitleName


my_messages = MessageForUser()
title_names = TitleName()


class TasksList(LoginRequiredMixin, FilterView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter
    login_url = 'login'

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return redirect(self.login_url)


class ShowTask(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/show_task.html'
    context_object_name = 'task'
    login_url = 'login'

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return redirect(self.login_url)


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = 'crud/create&update.html'
    success_url = reverse_lazy('tasks_list')
    extra_context = {'header': title_names.create_task,
                     'button_name': title_names.create}
    login_url = 'login'

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return redirect(self.login_url)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        messages.success(self.request, my_messages.task_create)
        return super(CreateTask, self).form_valid(form)


class UpdateTask(LoginRequiredMixin, SuccessMessageMixin,
                 UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = 'crud/create&update.html'
    success_url = reverse_lazy('tasks_list')
    success_message = my_messages.task_update
    extra_context = {'header': title_names.update_task,
                     'button_name': title_names.update}
    login_url = 'login'

    def handle_no_permission(self):
        messages.warning(self.request, my_messages.login)
        return redirect(self.login_url)


class DeleteTask(LoginRequiredMixin, SuccessMessageMixin,
                 UserPassesTestMixin, DeleteView):
    model = Task
    login_url = 'login'
    success_url = reverse_lazy('tasks_list')
    template_name = 'crud/delete.html'
    success_message = my_messages.task_delete
    extra_context = {'deltitle': title_names.to_del_task}

    def test_func(self):
        task = self.get_object()
        return self.request.user.id == task.author.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = my_messages.no_delete_task
            url = reverse_lazy('tasks_list')
        else:
            message = my_messages.login
            url = self.login_url
        messages.warning(self.request, message)
        return redirect(url)
