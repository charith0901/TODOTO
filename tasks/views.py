from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title, user=request.user, completed=False)
        return redirect('/')
    return redirect('/')

@login_required
# @permission_required('tasks.delete_task', raise_exception=True)
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not (task.completed)
    task.save()
    return redirect('/')
