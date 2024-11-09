from django import forms
from .models import Pet, Task
from django.forms.widgets import DateTimeInput

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'age', 'photo']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['pet', 'task_type', 'date', 'completed', 'notes']
        widgets = {
            'date': DateTimeInput(attrs={'type': 'datetime-local'}),  # Adds a datetime-local widget
        }
