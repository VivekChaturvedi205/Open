from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=['title','details','date',]

class TaskForm1(forms.ModelForm):
    class Meta:
        model = Task
        fields=['title','details','date','task_approved']
