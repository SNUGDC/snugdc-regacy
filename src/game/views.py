from django.shortcuts import render
from django.views.generic import View
from game.models import Game

class GameListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'games': Game.objects.all()
        }
        return render(request, 'game/index.djhtml', context)


class GameItemView(View):
    def get(self, request, pk, *args, **kwargs):
        context = {
            'game': Game.objects.get(pk=pk)
        }
        return render(request, 'game/item.djhtml', context)
