from django.urls import path
from .  import views

urlpatterns = [
    path('', views.registrations,name="registrations"),
    path('delete/<int:sid>',views.delete_student),
    path('register',views.register,name="register"),
    path('update_form/<int:stuid>',views.update_form,name="update_form")
]