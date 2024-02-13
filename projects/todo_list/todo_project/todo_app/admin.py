from django.contrib import admin
from .models import ToDoItem,ToDoList

# Register your models here.
from django.contrib import admin
from .models import Reg

# Register your models here.
class regisadmin(admin.ModelAdmin):
    list_display=['firstName','lastname','email','username','password','confpassword']
admin.site.register(Reg,regisadmin)


class ToDoItemadmin(admin.ModelAdmin):
    list_display=['title','description', 'created_date','due_date','todo_list']
admin.site.register(ToDoItem,ToDoItemadmin)
admin.site.register(ToDoList)