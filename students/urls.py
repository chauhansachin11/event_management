from django.urls import path
from . import views


urlpatterns = [
    path('',views.student),
    path('<str:pk>',views.student),

]