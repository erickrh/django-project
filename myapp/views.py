from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import Create_new_task, Create_new_project

# Create your views here.
def index(request):
  title = 'Welcome to my django web'
  return render(request, 'index.html', {
    'title': title
  })

def about(request):
  username = 'e93'
  return render(request, 'about.html', {
    'username': username
  })

def hello(request, username):
  print(username)
  return HttpResponse(f'Go to the hell, {username}')

def projects(request):
  # projects = list(Project.objects.values())
  # return JsonResponse(projects, safe=False)
  
  projects = Project.objects.all()
  return render(request, 'projects/projects.html', {
    'projects': projects
  })

def tasks(request):
  # task = Task.objects.get(title=title)
  # task = get_object_or_404(Task, id=id) # Recomendado
  # task = get_object_or_404(Task, title=title)
  # return HttpResponse(task.title)
  
  tasks = Task.objects.all()
  return render(request, 'tasks/tasks.html', {
    'tasks': tasks,
  })

def create_task(request):
  if request.method == 'GET':
      return render(request, 'tasks/create_task.html', {
      'form': Create_new_task()
      })
  else:
    Task.objects.create(
    title=request.POST['title'],
    description=request.POST['description'],
    project_id=2
    )
    return redirect('/tasks')

def create_project(request):
  if request.method == 'GET':
    return render(request, 'projects/create_project.html', {
      'form': Create_new_project()
    })
  else:
    Project.objects.create(name = request.POST['name'])
    return render(request, 'projects/create_project.html', {
      'form': Create_new_project()
    })