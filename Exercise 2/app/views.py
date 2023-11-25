from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.

def near_hundred(request: HttpRequest, num: int) -> HttpResponse:
    value = abs(num - 100) <= 10 or abs(num - 200) <= 10
    return HttpResponse(value)


def string_posion(request: HttpRequest, word: str) -> HttpResponse:
    result = ""
    for i in range(len(word)+1):
        result += word[:i]
    return HttpResponse(result)


def cat_dog(request: HttpRequest, pet: str) -> HttpResponse:
    cat_count = pet.count("cat")
    dog_count = pet.count("dog")
    return HttpResponse(cat_count == dog_count)


def lone_sum(request: HttpRequest, a: int, b: int, c: int) -> HttpResponse:
    if a == b and b == c and a == c:
        return HttpResponse(0)
    elif a == b:
        return HttpResponse(c)
    elif b == c:
        return HttpResponse(a)
    elif a == c:
        return HttpResponse(b)
    else:
        return HttpResponse(a+b+c)
    