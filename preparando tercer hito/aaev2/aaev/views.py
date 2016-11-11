# -*- coding: utf-8 -*-
#--------------------METODOS DJANGO --------------------
from django.shortcuts import render #cargar html con contexto
from django.shortcuts import redirect #redireccionar a una url 
from django.views.decorators.csrf import ensure_csrf_cookie #asegurar cookie
from django.http import HttpResponse #envia texto en respuesta
from django import forms #formularios genericos
from django.shortcuts import render_to_response #render de una respuesta
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf #uso de tokens
from django.core.urlresolvers import reverse_lazy #redireccionamiento  (creo que no usado)
from django.forms import ModelForm # formulario basado en modelos
from django.http import Http404 # error 404
from django.views.decorators.csrf import csrf_protect #proteger el csrf
from django.template.defaulttags import register #para uso de metodos en templates
import json #LENGUAJE JSON
from django.template.loader import render_to_string #plantillas a string
from django.template import Template, Context #generacion de plantillas
import datetime #fechas
from django.contrib import messages #mensajes al redirigir la pagina, usado como session, solo que se eliminan al recargar
#--------------------MODELOS ------------------------------
from aaev.models import Login, Universidad, UniversidadHasCarrera
from aaev.models import Carrera, Alumno, SolicitudRegistro, Login
from aaev.models import Docente, DocenteHasMateria, Materia, SolicitudMateria
#--------------------FUNCIONES PROPIAS--------------------
from funciones import validarLogin, traerCantInscriptosMateria, traerDocente
from funciones import traerCantSolicitantesMateria
from funciones import traerCantUnidadesMateria, traerCantExamenesMateria
from funciones import traerCantPreguntasUnidad, traerCantPreguntasMateria
from funciones import verificarMateriasSolicitadas, verificarMateriasObtenidas

# -----------------------------------CONTROLADORES DE VISTAS -------------------------
@csrf_protect
def index(request):
    return render(request, 'index.html', None) #pagina de inicio, sin variables


def envioSolicitudRegistroDocente(request): #el docente completa el formulario de la pagina de registro
    if request.method == 'POST':
        form = solicitudRegistroForm(request.POST)
        if form.is_valid(): #si el campo es valido agarro los datos
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            dni = str(form.cleaned_data['dni']) #aca lo hago texto para la base de datos, que usa VARCHAR
            email = form.cleaned_data['mail']
            solicitudMensaje = form.cleaned_data['solicitud']
            idsolicitud = 0
            try:
                solicitud = SolicitudRegistro.objects.latest('idsolicitud_registro')
                idsolicitud = solicitud.idsolicitud_registro + 1
            except(SolicitudRegistro.DoesNotExist):
                idsolicitud = 1

            try:
                solicitudDniExistente = SolicitudRegistro.objects.get(dni = dni)
                if solicitudDniExistente:
                    messages.add_message(request, messages.INFO, "Ya hay una solicitud o docente registrado con ese DNI")
                    return redirect('aaev:registro')
            except (SolicitudRegistro.DoesNotExist):
                if solicitud: #si se envio mensaje
                    solicitudGuardar = SolicitudRegistro(idsolicitud, nombre, apellido, email, dni, solicitudMensaje)
                else: #si no se envio
                    solicitudGuardar = SolicitudRegistro(idsolicitud, nombre, apellido, email, dni, ' ')
                solicitudGuardar.save()
                messages.add_message(request, messages.INFO, "Solicitud de registro enviada! Tu solicitud se ha enviado al administrador para ser evaluada")
                return redirect('aaev:registro')
        else:
            messages.add_message(request, messages.INFO, "Asegurate de completar todos los campos")
            return redirect('aaev:registro')

    else:
        return redirect('aaev:registro')

def login(request): #inicio de sesion de los usuarios
        if request:
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
                    mensaje="Completa todos los campos"
                    context = {'mensaje': mensaje}
                    return render(request, 'index.html', context)
                    #return redirect('aaev:index')
            else:
                return redirect('aaev:index')
        else:
            redirect('aaev:index')

def inicioDocente(request):
    try:
        if request.session['usuario']:
            nombreUsuario = request.session['usuario']
            usuario = Login.objects.get(usuario=nombreUsuario)
            docente = Docente.objects.get(idlogin = usuario.idlogin)
            mensaje = ''
            try:
                mensaje = request.session['mensajeExito'] #si vengo de una solicitud agarro el mensaje
                del request.session['mensajeExito'] #borro la entrada de diccionario
            except (KeyError): # si no hay mensaje
                mensaje = None
            try:
                materias = DocenteHasMateria.objects.filter(iddocente=docente.iddocente)
                materias = Materia.objects.filter(docentehasmateria=materias) #materias del docente
                universidades = Universidad.objects.all() 
            except (DocenteHasMateria.DoesNotExist, Materia.DoesNotExist):
                materias=None #si no existen agrego None
            context = {'usuario': usuario, 'docente': docente, 'materias': materias, 'universidades': universidades,
            'mensaje': mensaje}
            return render(request,'inicioDocente.html', context)
        else:
            return redirect('aaev:index')
    except ('usuario' not in request.session):
        return redirect('aaev:index')


def logout(request):
    try:#si estoy logeado
        usuario = request.session['usuario']
        usuario = Usuario.objects.get(usuario=usuario)
        privilegio = usuario.privilegio
        if request.method == 'POST': #si es un post
            del request.session['usuario']
            if privilegio == 2:# si soy docente
                del request.session['docente']
            return redirect('aaev:index')
        else: #si entre por URL
            if privilegio == 2: #si soy docente llevo a su inicio
                return redirect('aaev:inicioDocente')  
    except:
        return redirect('aaev:index')


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
        return redirect('aaev:registro')

def traerCarrerasId(request, iduniversidad):
    if request.method == 'POST':
        iddocente=  int(request.session['docente'])
        docente = Docente.objects.get(pk=iddocente)
        idBusqueda=iduniversidad #agarro el id de la universidad que envio ajax
        uhc= UniversidadHasCarrera.objects.filter(universidad_iduniversidad=idBusqueda)
        if uhc:
            carreras = Carrera.objects.filter(universidadhascarrera=uhc) #consultas
            data = {'carreras': carreras, 'iduniversidad': idBusqueda}
            
            #return HttpResponse(json.dumps(data), content_type='application/json') #envio el html guardado como cadena de texto
            return render(request, "AjaxCarreras.html", data)
        else:
            mensaje= "No hay carreras disponibles en esta universidad"
            data = {'mensaje': mensaje}
            return render(request, "AjaxCarreras.html", data)
    else:
        error= "Error al ejecutar el request"
        return HttpResponse(json.dumps(error), content_type='application/json') #envio el html guardado como cadena de texto;

def traerMateriasId(request, iduniversidad, idcarrera): #aca se hace la validacion final de inscripcion
    if request.is_ajax() and request.method=='POST': # si es ajax y post
        materias = Materia.objects.filter(universidadhascarrera=UniversidadHasCarrera.objects.filter(carrera_idcarrera=idcarrera)) # filtro materias por carrera
        docente = traerDocente(int(request.session['docente']))
        materias_noImpartidas = verificarMateriasObtenidas(docente, materias) #saco las materias que tiene acreditadas el docente
        materias_finales = verificarMateriasSolicitadas(docente, materias_noImpartidas) 
        #saco las materias que el docente solicito (evito spam) y termino con una lista con materias limpias
        if materias_finales: #si materias tiene AL MENOS UNA MATERIA
            form = envioSolicitud()
            context = {'materias': materias_finales, 'iduniversidad': iduniversidad, 'idcarrera': idcarrera,
             'mensaje': ''} #agrego uni y carrera para el form
            return render(request, "AjaxMaterias.html", context) #muestro el resultado
        else: # sino...

            mensaje= "No se encentran materias a las que puedas inscribirte en esta carrera"
            context = {'mensaje': mensaje, 'materias': None, 
            'iduniversidad': iduniversidad, 'idcarrera': idcarrera} #agrego el mensaje a mostrar
            return render(request, "AjaxMaterias.html", context) #cargo html con todas las variables.  
    else:
        error = "Error al ejecutar el request"
        return HttpResponse(error)

def enviarSolicitudMateria(request):
    if request.method == 'POST':
        form = envioSolicitud(request.POST)
        if form.is_valid():
            iddocente = int(request.session['docente'])
            docente = traerDocente(iddocente)
            
            mensaje = form.cleaned_data['mensaje']
            if mensaje == '': #si el docente decidio no enviar ningun mensaje...
                mensaje='El docente no ha enviado ningun mensaje'
            ultimo_id = 0 #el ultimo id de la tabla
            try:
                ultima_solicitud = SolicitudMateria.objects.latest('idsolicitud_materia')
                ultimo_id = ultima_solicitud.idsolicitud_materia
            except(SolicitudMateria.DoesNotExist): #si este es la primera solicitud en la tabla...
                ultimo_id = 0
            idsolicitud = ultimo_id + 1
            materia = form.cleaned_data['materia_idmateria']
            diaHoy = datetime.datetime.now().date() #fecha de hoy (DD/MM/AAAA)
            #datetime.datetime.strptime(str(diaHoy), "%Y-%m-%d").strftime("%d-%m-%Y") #formateo fecha de YYYY/MM/DD a DD/MM/YYYY
            solicitud = SolicitudMateria(idsolicitud, materia.idmateria,iddocente,diaHoy,mensaje)
            solicitud.save() #guardo en base de datos
            request.session['mensajeExito'] = "Tu solicitud se ha enviado con exito"
            return redirect('aaev:inicioDocente') #vuelvo a cargar el inicio de docente (como si fuera un submit)
        else:
            request.session['mensajeExito'] = "Error validando formulario "
            return redirect('aaev:inicioDocente')
    else:
        return redirect('aaev:inicioDocente')



##-------------------------FORM DE MODELOS PARA ABM--------------------
class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['usuario', 'clave']

class envioSolicitud(ModelForm): #no hereda de Models.form
    class Meta:
        model = SolicitudMateria
        fields= ['materia_idmateria','mensaje']
    
    def clean(self): #limpio datos y verifico si es valido
        cleaned_data= super(envioSolicitud, self).clean()
        try:
            idmateria = self.cleaned_data.get('materia_idmateria')
            if idmateria:
                return cleaned_data
            else: 
                raise forms.ValidationError("Selecciona el id de materia correcto")
        except:
            raise forms.ValidationError("Completa todos los campos")

class solicitudRegistroForm(ModelForm):
    class Meta:
        model = SolicitudRegistro
        fields = ['nombre','apellido','mail', 'dni', 'solicitud']

    def clean(self):
        cleaned_data = super(solicitudRegistroForm, self).clean()
        nombre = self.cleaned_data.get('nombre')
        apellido = self.cleaned_data.get('apellido')
        email = self.cleaned_data.get('mail')
        dni = self.cleaned_data.get('dni')
        solicitud = self.cleaned_data.get('solicitud')
        return cleaned_data
        


#------------------------METODOS PARA TEMPLATES--------------------
@register.filter
def contarPreguntas(materia):
    return traerCantPreguntasMateria(materia)

@register.filter
def contarUnidades(materia):
    return traerCantUnidadesMateria(materia)

@register.filter
def contarInscriptos(materia):
    return traerCantInscriptosMateria(materia)

@register.filter
def contarSolicitantes(materia):
    return traerCantSolicitantesMateria(materia)

@register.filter
def contarExamenes(materia):
    return traerCantExamenesMateria(materia)

@register.filter
def vacio(numero):
    if numero==0:
        return True
    else:
        return False

@register.filter
def traerCarreras(universidad):
    try:
        uhc= UniversidadHasCarrera.objects.filter(universidad_iduniversidad=universidad.iduniversidad)
        carreras = Carrera.objects.filter(universidadhascarrera=uhc)
    except:
        return None
    return carreras

@register.filter
def traerMaterias(carrera):
    try:
        uhc = UniversidadHasCarrera.objects.filter(carrera_idcarrera=carrera.idcarrera)
        materias = Materia.objects.filter(universidadhascarrera=uhc)
    except:
        pass
    return materias



