from django import forms
from task_manager.apps.statuses.models import Status
from task_manager.utils.text import TitleName

field_name = TitleName()


class StatusCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name',)
        labels = {'name': field_name.name}
