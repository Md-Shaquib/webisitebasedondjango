"""
URL configuration for mywebpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from home.views import home
from home.views import create_home
from home.views import delete_home
from welcome.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('',welcome,name='welcome'),
    path('createform/',create_home,name='create_home'),
    path('deletedata/<int:id>/',delete_home,name='delete_home')

]
