from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def player_setup(request):
    return render(request, 'player_setup.html')
# Create your views here.
