from .import views
from django.urls import path
app_name='mime'
urlpatterns = [
    path('html',views.htmlview.as_view(),name='htmlview'),
    path('excel',views.excelview.as_view(),name='ms-excelview'),
    path('xml',views.xmlview.as_view(),name='xmlview'),
]
