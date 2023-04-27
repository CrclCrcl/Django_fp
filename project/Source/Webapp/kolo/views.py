from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm


# Create your views here.
def home(request):
    return render(render, 'main.html')

def contact(request):
    if request.method == 'POST':
        student = StudentForm(request.POST)
        if student.is_valid():
            model_instance = student.save(commit=False)
            model_instance.save()
            return render(render, 'main.html')
    else:
        student=StudentForm()
        return render(render,'contact.html',{'form': student})

def events(request):
    return render(render, 'events.html')

def projects(request):
    return render(render,'projects.html')

def info(request):
    return render(render,'info.html')