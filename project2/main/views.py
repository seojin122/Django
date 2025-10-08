from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from . import models, forms

def index(request):
    students = models.Student.objects.all()
    return render(request, 'main/index.html', {'students': students})

def add(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:student_index')  
        else:
            return HttpResponseBadRequest('입력값이 올바르지 않습니다.')
    else:
        form = forms.StudentForm()
    return render(request, 'main/add.html', {'form': form})
