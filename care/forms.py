from django import forms
from .models import Pet, Task

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'breed', 'age', 'photo']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['pet', 'task_type', 'date', 'completed', 'notes']
