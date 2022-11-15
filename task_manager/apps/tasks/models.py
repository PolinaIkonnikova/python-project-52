from django.db import models
from task_manager.apps.users.models import User
from task_manager.apps.statuses.models import Status
from task_manager.apps.labels.models import Label
from task_manager.utils.text import NameForField

names = NameForField()


class Task(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name=names.name)

    description = models.TextField(null=True,
                                   verbose_name=names.descr)

    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               verbose_name=names.author)

    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               verbose_name=names.status)

    executor = models.ForeignKey(User, on_delete=models.PROTECT,
                                 null=True,
                                 related_name='executor',
                                 verbose_name=names.executor
                                 )

    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name=names.date)

    label = models.ManyToManyField(Label, through='LabelForTask',
                                   verbose_name=names.label)

    def __str__(self):
        return self.name


class LabelForTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    label = models.ForeignKey(Label, on_delete=models.PROTECT, null=True)
