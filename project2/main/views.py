from django.shortcuts import render, redirect
from django.http import *
from . import models
from . import forms

def home(request):
    return HttpResponse("Hello from main!")


def index(request):
    students = models.Student.objects.all()
    return render(request,'main/index.html',{'students':students})
def add(request):
    if request.method == 'GET':
        form = forms.StudentForm()
        return render(request,'main/add.html',{'form':form})
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        return HttpResponseNotAllowed('Method not allowed')