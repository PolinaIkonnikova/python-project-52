# from django import forms
# from task_manager.apps.tasks.models import Task
# from task_manager.utils.text import TitleName
#
# field_name = TitleName()
#
#
# class TaskCreateUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ('name', 'description', 'status',
#                   'executor', 'label')
#         labels = {'name': field_name.name,
#                   'description': field_name.descr,
#                   'status': field_name.status,
#                   'label': field_name.label,
#                   'executor': field_name.executor}
