from django.shortcuts import render
from django.views.generic import View
from game.models import Game

class GameView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'games': Game.objects.all()
        }
        return render(request, 'game/index.djhtml', context)
