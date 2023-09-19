from django.urls import path
from . import views


urlpatterns = [
    path('', views.EmployeeAPI.as_view()),
    path('<str:pk>', views.EmployeeAPI.as_view()),
]