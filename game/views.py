from django.shortcuts import render, redirect
from .models import Game
def home(request):
    return render(request, 'home.html')
def player_setup(request):
    return render(request, 'player_setup.html')
def start_game(request):
    if request.method == 'POST':
        player1 = request.POST['player1']
        player2 = request.POST['player2']
        game = Game.objects.create(
            player1_name=player1,
            player2_name=player2,
            active_player=player1,
            board=[['' for _ in range(3)] for _ in range(3)]
        )
        return redirect('game', game_id=game.id)
    return render(request, 'player_setup.html')
def game(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'game.html', {'game': game})

