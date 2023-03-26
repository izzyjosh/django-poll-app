from django.urls import path
from . import views

urlpatterns = [
        path("index/<int:q_id>/", views.index, name="index"), 
        path("", views.welcome, name="welcome"), 
        path("previous/<int:q_id>/", views.previous, name="previous"), 
        path("finish/", views.finish, name="finish")
]
