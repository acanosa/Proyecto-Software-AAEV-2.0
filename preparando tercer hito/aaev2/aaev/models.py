# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Alumno(models.Model):
    idalumno = models.IntegerField(db_column='idAlumno')  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    mail = models.CharField(max_length=45)
    dni = models.TextField()
    idlogin = models.ForeignKey('Login', db_column='idLogin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alumno'


class AlumnoHasMateria(models.Model):
    idalumno = models.ForeignKey(Alumno, db_column='idAlumno', primary_key=True)  # Field name made lowercase.
    idmateria = models.ForeignKey('Materia', db_column='idMateria', primary_key=True)  # Field name made lowercase.
    habilitado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alumno_has_materia'


class Carrera(models.Model):
    idcarrera = models.IntegerField(db_column='idCarrera', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    cantidadanios = models.IntegerField(db_column='cantidadAnios')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'carrera'

    def __str__(self):
        return self.nombre


class Docente(models.Model):
    iddocente = models.IntegerField(primary_key=True, db_column='idDocente')  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    mail = models.CharField(max_length=45)
    dni = models.TextField()
    idlogin = models.ForeignKey('Login', db_column='idLogin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'docente'


class DocenteHasMateria(models.Model):
    iddocente = models.ForeignKey('Docente', db_column='idDocente', primary_key=True)  # Field name made lowercase.
    idmateria = models.ForeignKey('Materia', db_column='idMateria', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'docente_has_materia'


class Examen(models.Model):
    idexamen = models.IntegerField(db_column='idExamen')  # Field name made lowercase.
    cantpreguntas = models.IntegerField(db_column='cantPreguntas')  # Field name made lowercase.
    totalpuntos = models.FloatField(db_column='totalPuntos')  # Field name made lowercase.
    descripcion = models.TextField(blank=True)
    duracion = models.TimeField()
    fechacierre = models.DateField(db_column='fechaCierre')  # Field name made lowercase.
    cerrado = models.IntegerField()
    visible = models.IntegerField()
    idmateria = models.ForeignKey('Materia', db_column='idMateria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'examen'


class ExamenHasAlumno(models.Model):
    idexamen = models.ForeignKey(Examen, db_column='idExamen')  # Field name made lowercase.
    idalumno = models.ForeignKey(Alumno, db_column='idAlumno')  # Field name made lowercase.
    nota = models.FloatField()
    nrointentos = models.IntegerField(db_column='nroIntentos')  # Field name made lowercase.
    estado = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'examen_has_alumno'


class Login(models.Model):
    idlogin = models.IntegerField(db_column='idLogin', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(max_length=45)
    clave = models.CharField(max_length=45)
    privilegio = models.IntegerField()
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'

    def __str__(self):
        return self.usuario


class Materia(models.Model):
    idmateria = models.IntegerField(db_column='idMateria', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    aniocarrera = models.IntegerField(db_column='anioCarrera')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materia'

    def __str__(self):
        return self.nombre


class Opcion(models.Model):
    idopcion = models.IntegerField(db_column='idOpcion')  # Field name made lowercase.
    texto = models.CharField(max_length=45)
    correcta = models.IntegerField()
    imagen = models.BinaryField(blank=True)
    descripcionimagen = models.CharField(db_column='descripcionImagen', max_length=45, blank=True)  # Field name made lowercase.
    idopcion_correcta = models.ForeignKey('self', db_column='idOpcion_correcta', blank=True, null=True)  # Field name made lowercase.
    idpregunta = models.ForeignKey('Pregunta', db_column='idPregunta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'opcion'


class Pregunta(models.Model):
    idpregunta = models.IntegerField(db_column='idPregunta')  # Field name made lowercase.
    texto = models.CharField(max_length=45)
    idtipopregunta = models.ForeignKey('Tipopregunta', db_column='idTipoPregunta')  # Field name made lowercase.
    idunidad = models.ForeignKey('Unidad', db_column='idUnidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pregunta'


class SolicitudMateria(models.Model):
    idsolicitud_materia = models.IntegerField(db_column='idSolicitud_materia', primary_key=True)  # Field name made lowercase.
    materia_idmateria = models.ForeignKey(Materia, db_column='Materia_idMateria')  # Field name made lowercase.
    docente_iddocente = models.ForeignKey(Docente, db_column='Docente_idDocente')  # Field name made lowercase.
    fecha = models.DateField()
    mensaje = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'solicitud_materia'


class SolicitudRegistro(models.Model):
    idsolicitud_registro = models.IntegerField(db_column='idSolicitud_Registro', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    mail = models.CharField(max_length=45)
    dni = models.TextField(max_length=30)
    solicitud = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'solicitud_registro'


class Tipopregunta(models.Model):
    idtipopregunta = models.IntegerField(db_column='idTipoPregunta', primary_key=True)  # Field name made lowercase.
    nombretipo = models.CharField(db_column='nombreTipo', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipopregunta'


class Unidad(models.Model):
    idunidad = models.IntegerField(db_column='idUnidad', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    idmateria = models.ForeignKey(Materia, db_column='idMateria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unidad'


class UnidadHasExamen(models.Model):
    examen_idexamen = models.ForeignKey(Examen, db_column='Examen_idExamen')  # Field name made lowercase.
    unidad_idunidad = models.ForeignKey(Unidad, db_column='Unidad_idUnidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unidad_has_examen'


class Universidad(models.Model):
    iduniversidad = models.IntegerField(db_column='idUniversidad', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    dominiomail = models.CharField(db_column='dominioMail', max_length=45)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'universidad'

    def __str__(self):
        return self.nombre


class UniversidadHasCarrera(models.Model):

    universidad_iduniversidad = models.ForeignKey(Universidad, db_column='Universidad_idUniversidad', primary_key=True )  # Field name made lowercase.
    carrera_idcarrera = models.ForeignKey(Carrera, db_column='Carrera_idCarrera', primary_key=True)  # Field name made lowercase.
    materia_idmateria = models.ForeignKey(Materia, db_column='Materia_idMateria', primary_key=True)  # Field name made lowercase.
#Django necesita que las tablas tengan una PK definida, para esto se agrega primery_key=True, sino falla
    class Meta:
        managed = False
        db_table = 'universidad_has_carrera'
    def __str__(self):
        return self.carrera_idcarrera

"""
La consulta en las tablas intermedias es la siguiente
Quiero obtener las carreras de una universidad
carreras_qs = UniversidadHasCarrera.objecs.filter(universidad_iduniversidad=1)
------
osea que primero agarro el queryset de la universidad
luego filtro por el objeto implicito que esta adentro del modelo, si es igual al
queryset saca las carreras que tiene esa uni. Luego se hace:
----
carreras= Carrera.objects.filter(universidadhascarrera=carreras_qs)
"""