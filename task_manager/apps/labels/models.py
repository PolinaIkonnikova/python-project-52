from django.db import models


class Label(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
