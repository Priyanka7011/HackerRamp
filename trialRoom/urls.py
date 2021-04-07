from django.urls import path
from . import views

urlpatterns=[
    path(route='', view=views.start, name="index"),
    path(route='shirt', view=views.shirt, name="shirt"),
    path(route='pant', view=views.pant, name="pant"),
    
]