# -*- coding: utf-8 -*-
from django.shortcuts import render
from aaev.models import Login, Universidad, UniversidadHasCarrera
from aaev.models import Carrera, Alumno, SolicitudRegistro, Login
from aaev.models import Docente, DocenteHasMateria,Materia
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template.loader import render_to_string
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm
from django.http import Http404
from funciones import validarLogin
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core import serializers

# Create your views here.
@csrf_protect
def index(request):
    return render(request, 'index.html', None)

@csrf_protect
def login(request):
        if request.method == 'POST':
            form = LoginForm(request.POST) #agarro el formulario de ingreso
            if form.is_valid():
                nombre = form.cleaned_data['usuario']
                clave = form.cleaned_data['clave']
                if validarLogin(nombre,clave):
                    usuario = Login.objects.get(usuario=nombre)
                    request.session['usuario'] = str(usuario.usuario)
                    if usuario.privilegio == 2:
                        mensaje="Sesion iniciada"
                        docente = Docente.objects.get(idlogin = usuario.idlogin)
                        request.session['docente'] = str(docente.iddocente)
                        context = {'mensaje': mensaje,
                                   'docente': docente}
                        return redirect('aaev:inicioDocente')
                        pass
                    else:
                        pass
                else:
                        mensaje="Usuario y/o clave incorrectos"
                        context = {'mensaje': mensaje}
                        return render(request, 'index.html', context)
            else:
              return render_to_response('index.html', {'form': form})
        else:
            form = UserCreationForm()
            token = {}
            token.update(csrf(request))
            token['form'] = form

            return render_to_response('index.html', token)

def inicioDocente(request):
    nombreUsuario = request.session['usuario']
    usuario = Login.objects.get(usuario=nombreUsuario)
    docente = Docente.objects.get(idlogin = usuario.idlogin)
    try:
        materias = DocenteHasMateria.objects.filter(iddocente=docente.iddocente)
        materias = Materia.objects.filter(docentehasmateria=materias) #materias del docente
    except (DocenteHasMateria.DoesNotExist, Materia.DoesNotExist):
        materias=None #si no existen agrego None
    context = {'usuario': usuario, 'docente': docente, 'materias': materias}
    return render(request,'inicioDocente.html', context)

@ensure_csrf_cookie
def registro(request):
    lista_universidades= Universidad.objects.all()
     #traigo las carreras de la universidad

    context= {  }
    return render(request, 'Registro.html', context)


def registrar(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             if form.privilegio==1:
                 alumno = Alumno(form.nombre, form.apellido, form.dni, form.email, form.clave, form.clave2)

                 return HttpResponseRedirect(reverse_lazy('aaev:formularioRegistro'))
             else:
                 solicitudDocente = SolicitudRegistro(form.nombre, form.apellido, form.dni, form.emailDocente, form.mensaje)
                 solicitudDocente.save()
                 return HttpResponseRedirect(reverse_lazy('aaev:formularioRegistro'))
    else:
         form = UserCreationForm()
         token = {}
         token.update(csrf(request))
         token['form'] = form

         return render_to_response('Registro_completo.html', token)



class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['usuario', 'clave']




"""
 context= {'universidades': lista_universidades,
        'carreras': None,
        'materias': None,
             }
    #context={'carreras': carreras_lista}
    if request.method == 'POST':
        return ajaxRegistroCarreras(request,universidad.iduniversidad)


@ensure_csrf_cookie
def ajaxRegistroCarreras(request,id):
    universidad = Universidad.objects.get(pk=id) #traigo las carreras de la universidad
    carreras_queryset = UniversidadHasCarrera.objects.filter(universidad_iduniversidad=universidad.iduniversidad)
    carreras_lista = Carrera.objects.filter(universidadhascarrera=carreras_queryset)
    #context={'carreras': carreras_lista}
    print(carreras_lista)
    num= 1
    context={
    'carreras': carreras_lista,
    'num': num,
    }
    html = render_to_string('ajaxRegistroCarreras.html',context)
    return render(request,'ajaxRegistroCarreras.html',context)
    #return HttpResponse(html, content_type="application/json")

class RegistrarSolicitudForm(ModelForm):
    class Meta:
         model = SolicitudRegistro
         fields = ['nombre','apellido','dni','email']

        """