from django.db import models
from projects.models import Project

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=30)


class Task(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='tasks')
    category = models.ManyToManyField(Category)
    due_date = models.DateTimeField()
    complete = models.BooleanField()
