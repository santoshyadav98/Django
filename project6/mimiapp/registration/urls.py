from django.urls import path
from registration import views

app_name='registration'
urlpatterns = [
    path('',views.reg,name='getinput.html'),
    path('register',views.registration)
]
