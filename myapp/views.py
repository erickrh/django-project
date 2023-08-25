from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def hello(request, username):
  print(username)
  return HttpResponse(f'Go to the hell, {username}')

def projects(request):
  projects = list(Project.objects.values())
  return JsonResponse(projects, safe=False)


def tasks(request, title):
  # task = Task.objects.get(title=title)
  # task = get_object_or_404(Task, id=id) # Recomendado
  task = get_object_or_404(Task, title=title)
  return HttpResponse(task.title)