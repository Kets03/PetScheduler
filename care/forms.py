from django import forms
from .models import Pet, Task
from django.forms.widgets import DateTimeInput

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name','species', 'breed', 'age', 'photo']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_type', 'date', 'notes']
        widgets = {
            'date': DateTimeInput(attrs={'type': 'datetime-local'}),  
        }
