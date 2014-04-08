from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from .views import HomeView, AboutView

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', AboutView.as_view(), name='contact'),
    url(r'^member/$', include('member.urls', namespace='member')),
    url(r'^game/$', include('game.urls', namespace='game')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
