from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.djhtml')


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.djhtml')

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.djhtml')
