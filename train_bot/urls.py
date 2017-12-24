from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^templates/', views.index, name='index'),
    #path('', views.index, name='index'),
]
