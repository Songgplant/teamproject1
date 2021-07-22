"""config URL Configuration

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
from django.urls import path, include
from django.views.generic import TemplateView

from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AgeChart', TemplateView.as_view(template_name='AgeChart.html'), name='AgeChart'),
    path('ages', views.ages, name='ages'),
    path('ScatterPlot', TemplateView.as_view(template_name='ScatterPlot.html'), name='ScatterPlot'),
    path('sp', views.sp, name='sp'),

    # 추가 기능 구현 0722
    path('imrate', views.imrate, name='imrate'),
    path('imdbrate', TemplateView.as_view(template_name='imdbrate.html'), name='imdbrate')
]
