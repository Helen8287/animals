from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('whisper/', views.whisper, name='whisper'),
    path('animals/', views.animals, name='animals'),
    path('birds/', views.birds, name='birds'),
    path('insects/', views.insects, name='insects'),
]