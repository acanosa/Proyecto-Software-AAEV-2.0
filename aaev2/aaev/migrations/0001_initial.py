# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idalumno', models.IntegerField(db_column='idAlumno')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('mail', models.CharField(max_length=45)),
                ('dni', models.TextField()),
            ],
            options={
                'db_table': 'alumno',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlumnoHasMateria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('habilitado', models.IntegerField()),
            ],
            options={
                'db_table': 'alumno_has_materia',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('idcarrera', models.IntegerField(serialize=False, primary_key=True, db_column='idCarrera')),
                ('nombre', models.CharField(max_length=45)),
                ('cantidadanios', models.IntegerField(db_column='cantidadAnios')),
            ],
            options={
                'db_table': 'carrera',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iddocente', models.IntegerField(db_column='idDocente')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('mail', models.CharField(max_length=45)),
                ('dni', models.TextField()),
            ],
            options={
                'db_table': 'docente',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocenteHasMateria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'docente_has_materia',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idexamen', models.IntegerField(db_column='idExamen')),
                ('cantpreguntas', models.IntegerField(db_column='cantPreguntas')),
                ('totalpuntos', models.FloatField(db_column='totalPuntos')),
                ('descripcion', models.TextField(blank=True)),
                ('duracion', models.TimeField()),
                ('fechacierre', models.DateField(db_column='fechaCierre')),
                ('cerrado', models.IntegerField()),
                ('visible', models.IntegerField()),
            ],
            options={
                'db_table': 'examen',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExamenHasAlumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nota', models.FloatField()),
                ('nrointentos', models.IntegerField(db_column='nroIntentos')),
                ('estado', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'examen_has_alumno',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('idlogin', models.IntegerField(serialize=False, primary_key=True, db_column='idLogin')),
                ('usuario', models.CharField(max_length=45)),
                ('clave', models.CharField(max_length=45)),
                ('privilegio', models.IntegerField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('idmateria', models.IntegerField(serialize=False, primary_key=True, db_column='idMateria')),
                ('nombre', models.CharField(max_length=45)),
                ('aniocarrera', models.IntegerField(db_column='anioCarrera')),
            ],
            options={
                'db_table': 'materia',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idopcion', models.IntegerField(db_column='idOpcion')),
                ('texto', models.CharField(max_length=45)),
                ('correcta', models.IntegerField()),
                ('imagen', models.BinaryField(blank=True)),
                ('descripcionimagen', models.CharField(max_length=45, db_column='descripcionImagen', blank=True)),
            ],
            options={
                'db_table': 'opcion',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idpregunta', models.IntegerField(db_column='idPregunta')),
                ('texto', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'pregunta',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SolicitudMateria',
            fields=[
                ('idsolicitud_materia', models.IntegerField(serialize=False, primary_key=True, db_column='idSolicitud_materia')),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'solicitud_materia',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SolicitudRegistro',
            fields=[
                ('idsolicitud_registro', models.IntegerField(serialize=False, primary_key=True, db_column='idSolicitud_Registro')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('mail', models.CharField(max_length=45)),
                ('dni', models.TextField()),
                ('solicitud', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'solicitud_registro',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipopregunta',
            fields=[
                ('idtipopregunta', models.IntegerField(serialize=False, primary_key=True, db_column='idTipoPregunta')),
                ('nombretipo', models.CharField(max_length=45, db_column='nombreTipo')),
            ],
            options={
                'db_table': 'tipopregunta',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idunidad', models.IntegerField(db_column='idUnidad')),
                ('nombre', models.CharField(max_length=45, db_column='Nombre')),
            ],
            options={
                'db_table': 'unidad',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnidadHasExamen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'unidad_has_examen',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('iduniversidad', models.IntegerField(serialize=False, primary_key=True, db_column='idUniversidad')),
                ('nombre', models.CharField(max_length=45, db_column='Nombre')),
                ('dominiomail', models.CharField(max_length=45, db_column='dominioMail')),
            ],
            options={
                'db_table': 'universidad',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UniversidadHasCarrera',
            fields=[
                ('universidad_iduniversidad', models.ForeignKey(primary_key=True, db_column='Universidad_idUniversidad', serialize=False, to='aaev.Universidad')),
                ('carrera_idcarrera', models.ForeignKey(primary_key=True, db_column='Carrera_idCarrera', to='aaev.Carrera')),
                ('materia_idmateria', models.ForeignKey(primary_key=True, db_column='Materia_idMateria', to='aaev.Materia')),
            ],
            options={
                'db_table': 'universidad_has_carrera',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
