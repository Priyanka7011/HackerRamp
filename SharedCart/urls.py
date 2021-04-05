from django.urls import path
from . import views

urlpatterns=[
    path(route='', view=views.index, name="index"),
    path(route='checkout', view=views.checkout, name="checkout"),
]