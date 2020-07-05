"""hohoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include

from blog import views
from blog.views import *

urlpatterns = [
    path('', main, name='main'),
    path('signup', signup, name='signup'),
    path('junghoo/', junghoo, name='junghoo'),
    path('login/', login, name='login'),
    path('photo/', photo, name='photo'),
    path('yonghoo/', yonghoo, name='yonghoo'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='user_signup'),
    path('login/', views.signin, name='user_login'),
    path('logout/', views.signout, name='user_logout'),

]


