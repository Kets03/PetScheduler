from django.db import models
class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    BIRD = 'bird'
    FISH = 'fish'
    SNAKE ='snake'
    SPECIES_CHOICES = [
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (BIRD, 'Bird'),
        (FISH, 'Fish'),
        (SNAKE, 'Snake')
    ]
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()
    species = models.CharField(
        max_length=100,
        choices=SPECIES_CHOICES,  
        blank=True,
        null=True
    )    
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class TaskType(models.Model):
    type_name = models.CharField(max_length=50)  

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