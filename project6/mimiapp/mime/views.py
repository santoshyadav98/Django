from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
data ="""<table> <tr><th> eid </th> <th> ename</th><th> esal </th></tr>
        <tr><td>101</td><td>santosh</td><td>100000</td></tr>
        <tr><td>102</td><td>ram</td><td>400000</td></tr>
        <tr><td>103</td><td>nilesh</td><td>500000</td></tr></table> """

class htmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/html")

class excelview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/ms-excel")

class xmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="application/xml")
    
