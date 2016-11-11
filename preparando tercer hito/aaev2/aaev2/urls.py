from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aaev2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^aaev/', include('aaev.urls', namespace='aaev')),  #mis url de la app
    #declaro un namespace para evitar lio al llamar URLs

)
