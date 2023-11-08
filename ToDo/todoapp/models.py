from django.contrib.auth import get_user_model
from django.core.serializers.json import DjangoJSONEncoder

from .choice import StatusChoice
from django.db import models

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    description = models.TextField(default="")
    status = models.CharField(choices=StatusChoice.CHOICE_LIST, max_length=16)
    due_date = models.DateField(blank=True, null=True)
    due_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    extras = models.JSONField(default=dict, encoder=DjangoJSONEncoder)

    def __str__(self) -> str:
        return self.title
