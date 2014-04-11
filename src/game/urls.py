from django.conf.urls import patterns, url
from .views import GameListView, GameItemView

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', GameItemView.as_view(), name='item'),
    url(r'^$', GameListView.as_view(), name='index'),
)
