import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models import QuerySet


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=255, blank=True, null=True)
    pages_amount = models.PositiveIntegerField(default=1)

    source = models.FileField(upload_to='uploads/%Y/%m/%d')

    user = models.ForeignKey(User)

    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=datetime.datetime.now, blank=True)

    @staticmethod
    def all_to_user(user: User) -> QuerySet:
        return Book.objects.filter(user=user)

    def __str__(self):
        return self.title
