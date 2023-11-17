from django.shortcuts import render

# Create your views here.
def root(request):
    print(request.POST)
    return render(request, "root.html")

def add(request):
    if request.GET:
        x = int(request.GET['x'])
        y = int(request.GET['y'])
        answer = x+y
        return render(request,"add.html", {"x": x, "y": y, "answer": answer})
    else:
        return render(request,"add.html")
