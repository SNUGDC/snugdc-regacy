from django.shortcuts import render
from django.views.generic import View
from member.models import Member

class MemberView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'members': Member.objects.all()
        }
        return render(request, 'member/index.djhtml', context)
