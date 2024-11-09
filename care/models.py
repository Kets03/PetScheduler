from django.db import models
# care/models.py
class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class TaskType(models.Model):
    type_name = models.CharField(max_length=50)  # e.g., Feeding, Grooming, etc.

    def __str__(self):
        return self.type_name

class Task(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.task_type} for {self.pet.name} on {self.date.strftime('%Y-%m-%d')}"