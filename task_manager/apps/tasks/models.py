from django.db import models
from django.contrib.auth.models import User
from task_manager.apps.statuses.models import Status
from task_manager.apps.labels.models import Label


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name='author')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, on_delete=models.PROTECT,
                                 null=True, related_name='executor')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    label = models.ManyToManyField(Label, through='LabelForTask')

    def __str__(self):
        return self.name


# сделать необязательным поле вода
class LabelForTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    label = models.ForeignKey(Label, on_delete=models.PROTECT, null=True)
