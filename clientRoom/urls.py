from django.urls import path
from . import views

urlpatterns=[
    path('', view=views.index, name="index"),
    path('<str:room_name>/', views.room, name='room'),
    path('<str:room_name>/checkout', view=views.checkout, name="checkout"),
]

