from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.api),
    path('movies/<uuid:pk>/', views.api),

]