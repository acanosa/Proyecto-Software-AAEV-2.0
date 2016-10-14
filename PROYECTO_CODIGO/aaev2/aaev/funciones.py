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

def traerDatosMateria(materia):
    try:
        lista_alumnos_habilitados= AlumnoHasMateria.objects.filter(idmateria=materia).exclude(habilitado = False)
        lista_solicitantes = AlumnoHasMateria.objects.filter(idmateria=materia).exclude(habilitado = True)
        #traigo alumnos y excluyo a los que ya estan habilitados
        unidades = materia.unidad_set.all()
        totalExamenes = 0
        for unidad in unidades:
            totalExamenes = totalExamenes + len(unidad.examen_set.all())
        diccionario = {'alumnosHabilitados' : len(lista_alumnos_habilitados),
        'lista_solicitantes' : len(lista_solicitantes), 'unidades': len(unidades)}
    except (AlumnoHasMateria.DoesNotExist):
        pass
    return diccionario

