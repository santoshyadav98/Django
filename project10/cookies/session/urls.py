from django.urls import path
from session import views

app_name="session"
urlpatterns=[
    path('',views.input,name="input"),
    path('add',views.add,name='add'),
    path('display',views.display,name='display'),
]