from django.db import models
from django.utils import timezone

class Task(models.Model):
    title=models.CharField(max_length=100)
    details=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    task_approved=models.BooleanField(default=False)