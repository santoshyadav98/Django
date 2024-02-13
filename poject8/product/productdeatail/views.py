from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import product

# Create your views here.

class home(View):
    def get(self,request):
        return render(request,'home.html')
    
class insertinput(View):
    def get(self,request):
        return render(request,'productinput.html')

class insertview(View):
    def get(self,request):
        p_id=int(request.GET['t1'])
        p_name=request.GET['t2']
        p_cost=int(request.GET['t3'])
        p_mfdt=request.GET['t4']
        p_expdt=request.GET['t5']
        pi=product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        pi.save()
        res=HttpResponse("product inserted successful")
        return res
    
class Displayview(View):
    def get(self,request):
        qs=product.objects.all()
        con_dic={"record":qs}
        return render(request,'display.html',con_dic)
class Deletinput(View):
    def get(self,request):
        return render(request,'deletinput.html')
    
class Deletview(View):
    def get(self,request):
        p_id=int(request.GET['t1'])
        p_name=request.GET['t2']
        prod=product.objects.filter(pid=p_id)
        prod=product.object.filter(pname=p_name)
        prod.delet()
        resp=HttpResponse("product delete successful")
        return resp
    
class updateinput(View):

    def get(self,request):
        return render(request,'updateinput.html')
class updateview(View):
    def post(self,request):
        p_id=int(request.POST['t1'])
        p_name=request.POST['t2']
        p_cost=float(request.POST['t3'])
        p_name=request.POST['t4']
        p_mfdt=request.POST['t5']
        p_expdt=request.POST['t6']
        prod=product.object.filter(pid=p_id)
        prod.p_name=p_name
        prod.p_mfdt=p_mfdt
        prod.p_expdt=p_expdt
        prod.save()
        resp=HttpResponse("delete successful")
        return resp