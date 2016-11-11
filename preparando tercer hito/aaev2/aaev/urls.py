# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from aaev import views



urlpatterns= patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^ingresar/$',views.login,name='ingresar'),
    url(r'^registro/registrarAlumno/$', views.registrar, name='registrarAlumno'),
    url(r'^registro/enviarDatos/$', views.envioSolicitudRegistroDocente, name='registrarDocente'),
    url(r'^docente/$', views.inicioDocente, name='inicioDocente'),
    url(r'^docente/(?P<iduniversidad>\d+)/$', views.traerCarrerasId ,name='traerCarrerasId'),
    url(r'^docente/(?P<iduniversidad>\d+)/(?P<idcarrera>\d+)/$', views.traerMateriasId, name='traerMateriasId'),
    url(r'^docente/enviarSolicitud/$', views.enviarSolicitudMateria, name='enviarSolicitudMateria'),
    url(r'^salir/$', views.logout, name='cerrarSesion'),
    #url(r'^docente/(?P<iduniversidad>\d+)/$', views.traerCarrerasId, name='traerCarrerasId'),
    )