from django.shortcuts import render
from .forms import ProjectForm

# Create your views here.

def project(request):
    form = ProjectForm()
    print(request, "===")
    data = request.POST
    print(data, "===data===")
    if request.method =="POST":
        form = ProjectForm(data=data)
        if form.is_valid:
            form.save()
        else:
            print(form.errors)    
    return render(request, 'project.html', {"form": form})
