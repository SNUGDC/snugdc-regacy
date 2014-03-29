from django.conf.urls import patterns, url
from .views import MemberView

urlpatterns = patterns('',
    url(r'^$', MemberView.as_view(), name='index')
)
