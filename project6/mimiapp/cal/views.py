from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'input.html')

def add(request):
    a=request.GET['t1']
    b=request.GET['t2']
    x=int(a)
    y=int(b)
    z=x+y
    return HttpResponse('the sum is :'+str(z))