from django.shortcuts import render
from django.views.generic import View

class MemberView(View):
    def get(self, request, *args, **kwargs):
        context = {
        }
        return render(request, 'member/index.djhtml', context)
