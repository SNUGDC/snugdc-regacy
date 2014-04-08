from django.conf.urls import patterns, url
from .views import GameView

urlpatterns = patterns('',
    url(r'^$', GameView.as_view(), name='index')
)
