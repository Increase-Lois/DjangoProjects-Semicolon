from django.shortcuts import render
from .forms import ProjectForm

# Create your views here.

def project(request):
    form = ProjectForm()
    return render(request, 'project.html', {"form": form})
