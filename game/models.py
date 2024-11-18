from django.db import models

class Game(models.Model):
    player1_name = models.CharField(max_length=50)
    player2_name = models.CharField(max_length=50)
    board = models.JSONField(default=list)
    active_player = models.CharField(max_length=50)
    winner = models.CharField(max_length=50, null=True, blank=True)
