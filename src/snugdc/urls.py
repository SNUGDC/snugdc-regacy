from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'snugdc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^member/$', include('member.urls'), name='member'),
    url(r'^admin/', include(admin.site.urls)),
)
