from django.urls import path

from . import views # right now it has index method 

urlpatterns = [
    path('',views.index,name='index'),
]
