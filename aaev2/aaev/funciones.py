# -*- coding: utf-8 -*-
from aaev.models import Login,Materia
from aaev.models import Login, Universidad, UniversidadHasCarrera
from aaev.models import Carrera, Alumno, SolicitudRegistro, Login
from aaev.models import Docente, DocenteHasMateria,Materia, AlumnoHasMateria

def validarLogin(usuario, clave):
    try:
        usuario = Login.objects.get(usuario=usuario)
        if clave == usuario.clave:
            return True #si la contraseña coincide
        else:
            return False #si no coincide
    except (Login.DoesNotExist):
        return False #si no existe usuario

"""
def traerInscriptosMateria(materia):
    try:
        lista_alumnos_habilitados= AlumnoHasMateria.objects.filter(idmateria=materia).exclude(habilitado = False)
        lista_solicitantes = AlumnoHasMateria.objects.filter(idmateria=materia).exclude(habilitado = True)
        #traigo alumnos y excluyo a los que ya estan habilitados
        unidades = materia.unidad_set.all()
        totalExamenes = 0
        for unidad in unidades:
            totalExamenes = totalExamenes + len(unidad.examen_set.all())
        diccionario = {'alumnosHabilitados' : len(lista_alumnos_habilitados),
        'lista_solicitantes' : len(lista_solicitantes), 'unidades': len(unidades),
        'examenes': totalExamenes}
    except (AlumnoHasMateria.DoesNotExist):
         diccionario = {'alumnosHabilitados' : 0,
        'lista_solicitantes' : 0, 'unidades': len(unidades),
        'examenes': totalExamenes}
    return diccionario
"""

def traerInscriptosMateria(materia):
    try:
        lista_alumnos_habilitados= AlumnoHasMateria.objects.filter(idmateria=materia).exclude(habilitado = False)
        habilitados = Alumno.objects.filter(alumnohasmateria=lista_alumnos_habilitados)
        #traigo alumnos y excluyo a los que ya estan habilitados
    except:
        return None
    return habilitados

def traerCantInscriptosMateria(materia):
    try:
        lista = traerInscriptosMateria(materia)
        cantidad = len(lista)
    except:
        return 0
    return cantidad


def traerSolicitantesMateria(materia):
    try:
        lista_solicitantes = AlumnoHasMateria.objects.filter(idmateria=materia).exclude(habilitado = True)
        solicitantes = Alumno.objects.filter(alumnohasmateria=lista_solicitantes)
        #traigo alumnos y excluyo a los que ya estan habilitados
    except:
        return None
    return solicitantes

def traerCantSolicitantesMateria(materia):
    try:
        lista = traerSolicitantesMateria(materia)
        cantidad = len(lista)
    except:
        return 0
    return cantidad

def traerCantUnidadesMateria(materia): #traigo cantidad de unidades
    try:
        unidades = materia.unidad_set.all()
        unidadesCant=len(unidades)
    except:
        return 0
    return unidadesCant

def traerUnidadesMateria(materia): #traigo las unidades
    try:
        unidades = materia.unidad_set.all()
    except:
        return None
    return unidades

def traerExamenesMateria(materia): #traigo examenes
    try:
        examenes = materia.pregunta_set.all()
    except:
        return None
    return examenes

def traerCantExamenesMateria(materia): #obtengo cantidad de examenes
    try:
        examenes= materia.examenes_set.all()
        examenesCant= len(examenes)
    except:
        return 0
    return examenesCant


def traerPreguntasUnidad(unidad): #traigo la lista de preguntas
    try:
        preguntas= unidad.preguntas_set.all()
    except:
        return None
    return preguntas

def traerCantPreguntasUnidad(unidad): #traigo cantidad de preguntas
    try:
        preguntas = unidad.pregunta_set.all()
        preguntasCant=len(preguntas)
    except:
        return 0
    return preguntasCant

def traerCantPreguntasMateria(materia):
    try:
        unidades = materia.unidad_set.all()
        cantPreguntas=0
        for unidad in unidades:
            try:
                preguntas = unidad.preguntas_set.all()
            except:
                cantPreguntas = 0
            cantPreguntas = len(preguntas)
    except:
        return 0
    return cantPreguntas