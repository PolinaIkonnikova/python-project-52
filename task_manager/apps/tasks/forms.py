from django import forms
from task_manager.apps.tasks.models import Task


class TaskCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status',
                  'executor', 'label')
