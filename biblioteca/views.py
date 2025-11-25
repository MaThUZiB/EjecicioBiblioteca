from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
#~~Inicio~~
def index(request):
    return render(request, 'index.html')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~Ciudad~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def listar_ciudades(request):
    ciudades = Ciudad.objects.all()
    return render(request, 'listar_ciudades.html', {
        'ciudades': ciudades
    })

def agregar_ciudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ciudades')
    else:
        form = CiudadForm()
    return render(request, 'formulario_ciudad.html',{
        'form': form
    })

def editar_ciudad(request, id):
    ciudad = get_object_or_404(Ciudad, pk=id)
    if request.method == 'POST':
        form = CiudadForm(request.POST, instance=ciudad)
        if form.is_valid():
            form.save()
            return redirect ('listar_ciudades')
    else:
        form = CiudadForm(instance=ciudad)
    return render(request, 'formulario_ciudad.html', {
        'form':form
    })

def eliminar_ciudad(request, id):
    ciudad = get_object_or_404(Ciudad, pk=id)
    ciudad.delete()
    return redirect ('listar_ciudades')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~Genero~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def listar_generos(request):
    generos = Genero.objects.all()
    return render (request, 'listar_generos.html', {
        'generos': generos
    })

def agregar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('listar_generos')
    else:
        form = GeneroForm()
    return render(request, 'formulario_genero.html', {
        'form': form
    })

def editar_genero(request, id):
    genero = get_object_or_404(Genero, pk=id)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('listar_generos')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'formulario_genero.html', {
        'form':form
    })

def eliminar_genero(request, id):
    genero = get_object_or_404(Genero, pk=id)
    genero.delete()
    return redirect ('listar_generos')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~Biblioteca~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def listar_bibliotecas(request):
    bibliotecas = Biblioteca.objects.all()
    return render(request, 'listar_bibliotecas.html', {
        'bibliotecas': bibliotecas
    })

def agregar_biblioteca(request):
    if request.method=='POST':
        form = BibliotecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('listar_bibliotecas')
    else:
        form = BibliotecaForm()
    return render (request, 'formulario_biblioteca.html', {
        'form': form
    })

def editar_biblioteca(request, id):
    biblioteca = get_object_or_404(Biblioteca, pk=id)
    if request.method=='POST':
        form = BibliotecaForm(request.POST, instance=biblioteca)
        if form.is_valid():
            form.save()
            return redirect ('listar_bibliotecas')
    else:
        form = BibliotecaForm(instance=biblioteca)
    return render(request, 'formulario_biblioteca.html', {
        'form': form
    })

def eliminar_biblioteca(request, id):
    biblioteca = get_object_or_404(Biblioteca, pk=id)
    biblioteca.delete()
    return redirect ('listar_bibliotecas')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~Libros~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'listar_libros.html', {
        'libros': libros
    })

def agregar_libro(request):
    if request.method=='POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'formulario_libro.html', {
        'form': form
    })

def editar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect ('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'formulario_libro.html', {
        'form': form
    })

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    libro.delete()
    return redirect( 'listar_libros')