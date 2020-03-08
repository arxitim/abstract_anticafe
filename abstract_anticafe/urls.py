"""abstract_anticafe URL Configuration

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
from django.urls import path, re_path, include
from core.views import HomePage, PageNotFound, Table, MyRegisterFormView

urlpatterns = [
    path('', HomePage.as_view(), name='homePage'),
    path('admin/', admin.site.urls),
    path('accounts/register/', MyRegisterFormView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tables/<int:table_id>', Table.as_view()),
    re_path(r'.*', PageNotFound.as_view()),
]
