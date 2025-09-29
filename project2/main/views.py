from django.shortcuts import render, redirect
from django.http import *
from . import models
from . import forms

def index(request):
    if request.method == 'GET':
        students = models.Student.objects.all()
        form = forms.StudentForm()
        return render(request,'main/index.html',{'students':students, 'form':form})
    elif request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:students_list")
        else:
            return HttpResponseBadRequest('Bad Request')
    else:
        return HttpResponseNotAllowed("Method not allowed")


def add(request):
    form = forms.StudentForm()
    return render(request,'main/add.html',{'form':form})
