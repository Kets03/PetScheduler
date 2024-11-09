from django.contrib import admin
from django.contrib import admin
from .models import TaskType,Pet,Task

# Register TaskType model with the admin site
admin.site.register(TaskType)
admin.site.register(Task)
admin.site.register(Pet)