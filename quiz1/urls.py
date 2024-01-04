"""
URL configuration for quiz1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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


from quizapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name="home"),
    path('user',views.user,name="user"),
    path('quiztemplate',views.quiztemplate,name="quiztemplate"),
    path('registration1',views.registration1, name="registration1"),
    path('userprofile',views.userprofile,name="userprofile"),
    path('javaquiz',views.javaquiz,name="javaquiz"),
    path('aiquiz',views.aiquiz,name="aiquiz"),
]

