from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('player-setup/', views.player_setup, name='player_setup'),
    path('game/<int:game_id>/', views.game, name='game'),
    path('start-game/', views.start_game, name='start_game'),
]
