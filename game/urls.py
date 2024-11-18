from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('player-setup/', views.player_setup, name='player_setup'),
]
