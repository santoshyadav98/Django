from django.urls import path
from cal import views
app_name='cal'
urlpatterns=[
    path('',views.home,name="input.html"),
    path('add',views.add),
]