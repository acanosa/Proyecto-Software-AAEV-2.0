# -*- coding: utf-8 -*-
from aaev.models import Login,Materia
from aaev.models import Login, Universidad, UniversidadHasCarrera
from aaev.models import Carrera, Alumno, SolicitudRegistro, Login
from aaev.models import Docente, DocenteHasMateria,Materia, AlumnoHasMateria, SolicitudMateria

def validarLogin(usuario, clave):
    try:
        usuario = Login.objects.get(usuario=usuario)
        if clave == usuario.clave:
            return True #si la contraseña coincide
        else:
            return False #si no coincide
    except (Login.DoesNotExist):
        return False #si no existe usuario
def queryCarreras(idBusqueda,docente):
    idBusqueda=iduniversidad #agarro el id de la universidad que envio ajax
    uhc= UniversidadHasCarrera.objects.filter(universidad_iduniversidad=idBusqueda)
    carreras = Carrera.objects.filter(universidadhascarrera=uhc) #consultas
    data = {'carreras': carreras, 'iduniversidad': idBusqueda}

def traerDocente(idDocente):
    try:
        docente= Docente.objects.get(pk=idDocente)
    except:
        docente= None;    
    return docente

def verificarMateriasSolicitadas(docente, materias):
    try: #evito el spam de solicitudes de materia (osea enviar 20 solicitudes para UNLa/Sistemas/Mate I)
        materias_solicitadas = SolicitudMateria.objects.filter(docente_iddocente = docente.iddocente) # agarro materias que estan en solicitud
        materias_models = Materia.objects.filter(solicitudmateria = materias_solicitadas)
        materias_actualizadas = [x for x in materias if x not in materias_models] #agrego las materias que no fueron solicitadas
        return materias_actualizadas
    except(SolicitudMateria.DoesNotExist): #si no hay registros en esa tabla
        return materias

def verificarMateriasObtenidas(docente, materias):
    try: # aca busco las materias que el docente YA imparte, para evitar mandar solicitudes de materias donde ya esta
        materias_docente = DocenteHasMateria.objects.filter(iddocente=docente.iddocente) #filtro por docente, aca tengo los registros
        #de la  tabla varios a varios
        materias_lista = Materia.objects.filter(docentehasmateria = materias_docente)
        #aca arriba comparo la "foreign key" oculta de django a la tabla intermedia donde saco las materias que saque en
        #materias_docente
        materias_actualizadas = [x for x in materias if x not in materias_lista] #agrego las materias qe no estan en las del docente
        return materias_actualizadas 
    except(DocenteHasMateria.DoesNotExist):
        return materias

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

def traerCarrerasId(request):
    iduniversidad=request.POST['iduniversidad'] #agarro el id de la universidad que envio ajax
    try:
        uhc= UniversidadHasCarrera.objects.filter(universidad_iduniversidad=iduniversidad)
        carreras = Carrera.objects.filter(universidadhascarrera=uhc)
    except:
        return None
    return carreras

def diccionarioModelosUltimosId(nombreModelo):
    return {
        'docente': traerUltimoIdDocente(),
        'login': traerUltimoIdLogin(),
        'solicitudmateria': traerUltimoIdSolicitudMateria(),
        'solicitudregistro': traerUltimoIdSolicitudRegistro(),
    }[nombreModelo]

def traerUltimoIdDocente():
    docente = Docente.objects.latest('iddocente')
    return docente.iddocente

def traerUltimoIdLogin():
    login = Login.objects.latest('idlogin')
    return login.idlogin

def traerUltimoIdSolicitudRegistro():
    solicitud = SolicitudRegistro.objects.latest('idsolicitud_registro')


def traerUltimoIdSolicitudMateria():
    solicitud = SolicitudMateria.objects.latest('idsolicitud_materia')
