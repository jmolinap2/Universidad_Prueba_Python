from django.shortcuts import render, redirect
from .models import Alumno
from django.contrib import messages

# Create your views here.


def home(request):
    AlumnosListados = Alumno.objects.all()
    messages.success(request, '¡Alumnos listados!')
    return render(request, "gestionAlumnos.html", {"Alumnos": AlumnosListados})


def registrarAlumno(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    nombre2 = request.POST['txtNombre2']
    iD = request.POST['numiD']
    edad =request.POST['numEdad']

    Registro = Alumno.objects.create(
        codigo=codigo, nombre=nombre, nombre2=nombre2, iD=iD, edad=edad)
    messages.success(request, '¡Alumno registrado!')
    return redirect('/')


def edicionAlumno(request, codigo):
    Registro = Alumno.objects.get(codigo=codigo)
    return render(request, "edicionAlunmo.html", {"Alumno": Registro})


def editarAlumno(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    nombre2 = request.POST['txtNombre2']
    iD = request.POST['numiD']
    edad =request.POST['numEdad']

    Registro = Alumno.objects.get(codigo=codigo)
    Registro.nombre = nombre
    Registro.nombre2 = nombre2
    Registro.iD = iD
    Registro.edad= edad
    Registro.save()

    messages.success(request, '¡Alumno actualizado!')

    return redirect('/')


def eliminarAlumno(request, codigo):
    Registro = Alumno.objects.get(codigo=codigo)
    Registro.delete()

    messages.success(request, '¡Alumno eliminado!')

    return redirect('/')
