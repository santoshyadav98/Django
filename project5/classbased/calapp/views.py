from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class GetInput(View):
    def get(self,request):
        return render(request,'getiput.html')
class PostInput(View):
    def get(self,request):
        return render(request,'postinput.html')

class add(View):
    def get(self,request):

            a=request.GET['t1']
            b=request.GET['t2']
            
            x=int(a)
            y=int(b)
        
            z=x+y
            return HttpResponse('the sum is :'+str(z))
    def post(self,request):
            a=request.POST['t1']
            b=request.POST['t2']
            
            x=int(a)
            y=int(b)
        
            z=x-y
            return HttpResponse('the sum is :'+str(z))