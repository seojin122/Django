from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseNotAllowed
from django.views import View

def index(request):
    if request.method!="GET":
        raise HttpResponseNotAllowed()
    context = {
        "title":"myTitle",
        "content":"hello"
    }
    return render(request,'main/index.html', context)

def hello(request):
    return HttpResponse("<h1>Hello, World!</h1><h2>Well...</h2>")

def toGoogle(request):
    return redirect("https://google.com")

def not_found(request):
    raise Http404("Sorry... no page here.")

def api_example(request):
    if request.method=="GET":
        data = {
        "message": "Hello, this is a JSON response",
        "status": "success"
        }
        return JsonResponse(data)
    elif request.method=="DELETE":
        return HttpResponse('delete done')
    else:
        raise HttpResponseNotAllowed()
