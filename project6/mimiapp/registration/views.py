from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def reg(request):
    return render(request,'getinput.html')

def registration(request):
    a=request.GET['t1']
    b=request.GET['t2']
    c=request.GET['t3']
    d=request.GET['t4']
    e=request.GET['t5']
    z=a+b+c

    return HttpResponse("the first name is:  "+str(a)  + "\n"+"last name is :"+str(b)+" \n the email address is: " + str(c) + " \nRegistration successfuly: "+str(z))
    #return HttpResponse("the last name is: "+str(b))
    #return HttpResponse("the email address is: "+str(c))
    #return HttpResponse("the password is: "+str(d))
    #return HttpResponse("Registration successfuly: "+str(z))