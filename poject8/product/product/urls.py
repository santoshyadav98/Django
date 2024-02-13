"""
URL configuration for product project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productdeatail.views import home,insertinput,insertview,Displayview,Deletinput,Deletview,updateinput,updateview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('modelapp/', home.as_view()),
    path('modelapp/insertinput',insertinput.as_view()),
    path('modelapp/insertv/',insertview.as_view()),
    path('modelapp/display/',Displayview.as_view()),
    path('modelapp/deletinput/',Deletinput.as_view()),
    path('modelapp/deletinput/delet',Deletview.as_view()),
    path('modelapp/updateinput/',updateview.as_view()),
    path('modelapp/updateview/',updateinput.as_view()),

]
