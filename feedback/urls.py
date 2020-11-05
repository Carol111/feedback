"""feedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views

from apps.core.views import home, about
from apps.userprofile.views import register, settings
from apps.period.views import add_period, list_period
from apps.course.views import add_course, list_course, course_overview, course_messages, course_frequent_words

urlpatterns = [
    #FRONTPAGE
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),

    # LOGGED AREA
    path('settings/', settings, name='settings'),
    path('period/add', add_period, name='add_period'),
    path('period/list', list_period, name='list_period'),
    path('course/add', add_course, name='add_course'),
    path('course/list', list_course, name='list_course'),
    path('course/<slug:course_code>/overview/', course_overview, name='course_overview'),
    path('course/<slug:course_code>/messages/', course_messages, name='course_messages'),
    path('course/<slug:course_code>/frequent-words/', course_frequent_words, name='course_frequent_words'),

    # AUTH
    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
