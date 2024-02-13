from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home (request):
    return render(request,"input.html")

def add(request):
    i=request.GET['t1']
    j=request.GET['t2']
    k=request.GET['operation']
    x=int(i)
    y=int(j)
    r=0
    if k=="add":
        r=x+y
    elif k=="sub":
        r=x-y
    elif k=="mul":
        r=x*y
      
    else:
        r=x/y
    res=HttpResponse("the sum is :"+str(r))
    return res