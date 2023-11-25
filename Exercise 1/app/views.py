from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.
def hey_name(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")

def user_age(request: HttpRequest, end: int, birthyear: int) -> HttpResponse:
    age = int(end) - int(birthyear)
    return HttpResponse(f"Your age is: {age}")

def user_order(request: HttpRequest, burgers: int, fries: int, drinks: int) -> HttpResponse:
    total = int(burgers)* 4.50 + int(fries)* 1.50 + int(drinks)* 1.00
    return HttpResponse(f"Total: ${total:.2f}")