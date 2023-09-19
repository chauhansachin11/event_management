from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('department',views.DepartmentAPI)


urlpatterns = [
    path('', views.EmployeeAPI.as_view()),
    path('<str:pk>', views.EmployeeAPI.as_view()),
    path('',include(router.urls))
]