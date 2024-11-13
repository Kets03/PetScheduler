# care/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet, Task
from .forms import PetForm, TaskForm

def get_started(request):
    return render(request, 'get_started.html')

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pet_list.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    tasks = Task.objects.filter(pet=pet)
    return render(request, 'pet_detail.html', {'pet': pet, 'tasks': tasks})

def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pet_form.html', {'form': form})

def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)
    return render(request, 'pet_form.html', {'form': form, 'pet': pet})

def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.delete()
    return redirect('pet_list')

# Task CRUD
def task_create(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.pet = pet
            task.save()
            return redirect('pet_detail', pk=pet_id)
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form, 'pet': pet})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    pet = task.pet
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('pet_detail', pk=pet.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form, 'task': task, 'pet': pet})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    pet_id = task.pet.id
    task.delete()
    return redirect('pet_detail', pk=pet_id)

def mark_task_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.completed = True
        task.save()
    return redirect('pet_detail', pk=task.pet.id)