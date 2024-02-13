from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def getinput(request):
    return render(request,'getinput.html')

def postinput(request):
    return render(request,'postinput.html')

def add(request):
    if request.method=="GET":
        a=request.GET['t1']
        b=request.GET['t2']
        c=request.GET['operation']
        x=int(a)
        y=int(b)
        r=0
        if c=='add':
            r=x+y
        else:
            r=x-y
        return HttpResponse("the sum is :"+str(r))
    else:
        a=request.POST['t1']
        b=request.POST['t2']
        c=request.POST['operation']
        x=int(a)
        y=int(b)
        r=0
        if c=='mul':
            r=x*y
        else:
            r=x/y
        return HttpResponse("the sum is :"+str(r))