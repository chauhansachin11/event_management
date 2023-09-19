from django.urls import path
from . import views


urlpatterns = [
    path('',views.studentApi),
    path('<str:pk>',views.studentApi),

]