from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

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
  return render(request, 'projects.html', {
    'projects': projects
  })


def tasks(request):
  # task = Task.objects.get(title=title)
  # task = get_object_or_404(Task, id=id) # Recomendado
  # task = get_object_or_404(Task, title=title)
  # return HttpResponse(task.title)
  return render(request, 'tasks.html')