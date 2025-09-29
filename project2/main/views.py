from django.shortcuts import render, redirect
from django.http import *
from . import models
from . import forms

def index(request):
    students = models.Student.objects.all()
    return render(request,'main/index.html',{'students':students})
def add(request):
    if request.method == 'GET':
        form = forms.StudentForm()
        return render(request,'main/add.html',{'form':form})
    elif request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:students_list")
        return render(request, 'main/add.html', {'form': form}, status=400)
    else:
        return HttpResponseNotAllowed('Method not allowed')