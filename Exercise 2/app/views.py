from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.forms import FrontForms, TeenSumForms, ThereForms, CenteredForms

# Create your views here.

def front_times(request:HttpRequest)-> HttpResponse:
    form = FrontForms(request.GET)
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
    
def fix_teen(n):
    if 13 <= n <= 19 and n not in [15, 16]:
        return 0
    return n

def no_teen_sum(request:HttpRequest)-> HttpResponse:
    form = TeenSumForms(request.GET)
    if form.is_valid():
        # a = fix_teen(a)
        a = form.cleaned_data['a']
        # b = fix_teen(b)
        b = form.cleaned_data['b']
        # c = fix_teen(c)
        c = form.cleaned_data['c']
        result = fix_teen(a) + fix_teen(b) + fix_teen(c)
        return render(request, "noteensum.html", {"form":form, "a":a, "b":b, "c":c, "result":result})
    else:
        return render(request, "noteensum.html", {"form":form})
    
def xyz_there(request:HttpRequest)-> HttpResponse:
    form = ThereForms(request.GET)
    if form.is_valid():
        s = form.cleaned_data['s']
        i = 0
        while "xyz" in s[i:]:
            index = s[i:].index("xyz")
            if index == 0 or s[i + index - 1] != '.':
                result = True
                return render(request, "xyzthere.html", {"form":form, "s":s, "i":i, "index":index, "result":result})

            i += index + 1
        result = False
        return render(request, "xyzthere.html", {"form":form, "s":s, "i":i, "index":index, "result":result})
    else:
        return render(request, "xyzthere.html", {"form":form})
    
def centered_average(request: HttpRequest) -> HttpResponse:
   
    form = CenteredForms(request.GET)
    if form.is_valid():
        a = form.cleaned_data["a"]
        b = form.cleaned_data["b"]
        c = form.cleaned_data["c"]
        d = form.cleaned_data["d"]
        e = form.cleaned_data["e"]
        f = form.cleaned_data["f"]
        g = form.cleaned_data["g"]
        if f == None and g == None:
            nums = [a,b,c,d,e]
        elif f!= None and g == None:
            nums = [a,b,c,d,e,f]
        else:
            nums = [a,b,c,d,e,f,g]
        if nums[0] == nums[-1]:
            nums.remove(0)
            nums.remove(-1)
        result = f"{sum(nums) / len(nums):.0f} "
        return render(request, "centeredaverage.html", {"form": form, "result": result})
    else:
        return render(request, "centeredaverage.html", {"form": form})