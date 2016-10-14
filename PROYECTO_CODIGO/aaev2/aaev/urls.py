# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from aaev import views

urlpatterns= patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^ingresar/$',views.login,name='ingresar'),
    url(r'^registro/completar/$', views.registrar, name='formularioRegistro'),
    url(r'^docente/$', views.inicioDocente, name='inicioDocente')
    )