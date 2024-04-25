from django.db import models

from django.utils import timezone

class Book(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.author} | {self.title}'