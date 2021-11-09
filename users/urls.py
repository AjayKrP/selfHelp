"""selfHelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from users import views as user_views

urlpatterns = [
    path('', user_views.home, name='login.home'),
    path('login', user_views.Login, name='login'),
    path('signup', user_views.signup, name='signup'),
    path('logout', user_views.logout_user, name='logout'),
    path('dashboard', user_views.dashboard, name='dashboard')
]
