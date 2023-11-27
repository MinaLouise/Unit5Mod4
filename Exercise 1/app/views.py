from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.forms import HelloForm, AgeForm, OrderForm

# Create your views here.
def hey_name(request: HttpRequest) -> HttpResponse:
    form = HelloForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']

        return render(request, "heyname.html", {"form": form, "name":name})
    else:
        return render(request, "heyname.html", {"form":form})

def user_age(request: HttpRequest) -> HttpResponse:
    form = AgeForm(request.POST)
    if form.is_valid():
        end = form.cleaned_data['end']
        birth = form.cleaned_data['birth']
        age = end - birth
        return render(request, "yourage.html", {"form": form, "end":end, "birth":birth, "age":age})
    else:
        return render(request, "yourage.html", {"form": form,})

def user_order(request: HttpRequest) -> HttpResponse:
    form = OrderForm(request.POST)
    if form.is_valid():
        burger = form.cleaned_data['burger']
        fries = form.cleaned_data['fries']
        drink = form.cleaned_data['drink']
        total = burger*4.5 + fries*1.5 + drink*1
        return render(request, "takeorder.html", {"form": form, "burger": burger, "fries":fries, "drink":drink, "total":total})
    else:
        return render(request, "takeorder.html", {"form": form})