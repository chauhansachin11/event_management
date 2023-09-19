"""event_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from events import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='index'),
    path('signup/', views.signup, name='signup'),
    path('user_home/', login_required(views.user_home), name='user_home'),
    path('event/<int:event_id>/', views.view_summary, name='event_details'),
    path('book_event/<int:event_id>/', views.book_event, name='book_event'),
    path('ticket/<int:ticket_id>/', views.view_ticket, name='view_ticket'),
    path('admin/home/', views.admin_home, name='admin_home'),
    path('admin/create_event/', views.create_event, name='create_event'),
    path('admin/update_event/<int:event_id>/', views.update_event, name='update_event'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('student/', include('students.urls')),
    path("employee/",include('employee.urls')),
]
