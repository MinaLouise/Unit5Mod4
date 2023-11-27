from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.forms import FrontForms

# Create your views here.

def front_times(request:HttpRequest):
    form = FrontForms(request.POST)
    if form.is_valid():
        word = form.cleaned_data['word']
        n = form.cleaned_data['n']
        front = word[:3]
        result = ""
        for i in range(n):
            result += front
        return render(request, "fronttimes.html", {"form":form, "word":word, "n":n, "front":front, "result":result})
    else:
        return render(request, "fronttimes.html", {"form":form})
    
def no_teen_sum(request:HttpRequest):
    form = FrontForms(request.POST)
    if form.is_valid():
        word = form.cleaned_data['word']
        n = form.cleaned_data['n']
        front = word[:3]
        result = ""
        for i in range(n):
            result += front
        return render(request, "fronttimes.html", {"form":form, "word":word, "n":n, "front":front, "result":result})
    else:
        return render(request, "fronttimes.html", {"form":form})