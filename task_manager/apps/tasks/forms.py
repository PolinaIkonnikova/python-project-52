from django import forms
from task_manager.apps.tasks.models import Task
from task_manager.utils.text import NameForField
from task_manager.apps.labels.models import Label

names = NameForField()


# class TaskCreateUpdateForm(forms.ModelForm):
#
#     # labels = forms.ModelMultipleChoiceField(
#     #     label=names.labels,
#     #     label_suffix='',
#     #     required=False,
#     #     widget=forms.SelectMultiple(
#     #         attrs={'placeholder': names.labels}),
#     #     queryset=Label.objects.all())
#
#     class Meta:
#         model = Task
#         fields = ('name', 'description', 'status',
#                   'executor', 'labels')
