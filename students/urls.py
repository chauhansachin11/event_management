from django.urls import path
from . import views


urlpatterns = [
    path('',views.studentList),
    path('<str:pk>',views.studentDetails),
    path('create/', views.studentCreate),
    path('update/<str:pk>', views.studentUpdate),
    path('delete/<str:pk>', views.studentDelete),

]