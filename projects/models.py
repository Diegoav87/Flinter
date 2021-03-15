from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField()

    def __str__(self):
        return self.name
    