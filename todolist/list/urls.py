from django.urls import path
from . import views

urlpatterns = [
    path("",views.todolist,name="todolist"),
    path("todolist",views.todolist,name="todolist"),
    path("save",views.save,name="save"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("update/<int:id>",views.update,name="update"),
    path("update_form/<int:id>",views.update_form,name="update_form"),
]