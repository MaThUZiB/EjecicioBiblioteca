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
    q = request.GET.get("q", "")

    if q:
        ciudades = Ciudad.objects.filter(nombre__icontains=q)
    else:
        ciudades = Ciudad.objects.all()

    return render(request, "listar_ciudades.html", {
        "ciudades": ciudades,
        "q": q
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
        'form': form,
        'titulo': 'Agregar Ciudad'
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
        'form':form,
        'titulo': 'Editar Ciudad'
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
    q = request.GET.get("q", "")
    if q:
        generos = generos.filter(nombre__icontains=q)
    else:
        generos = Genero.objects.all()

    return render (request, 'listar_generos.html', {
        'generos': generos,
        'q': q
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
        'form': form,
        'titulo': 'Agregar Género'
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
        'form':form,
        'titulo': 'Editar Género'
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
    q = request.GET.get("q", "")
    if q:
        bibliotecas = Biblioteca.objects.filter(nombre__icontains=q)
    else:
        bibliotecas = Biblioteca.objects.all()
    return render(request, 'listar_bibliotecas.html', {
        'bibliotecas': bibliotecas,
        'q': q
    })

def agregar_biblioteca(request):
    ciudades = Ciudad.objects.all()
    if request.method=='POST':
        form = BibliotecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('listar_bibliotecas')
    else:
        form = BibliotecaForm()
    return render (request, 'formulario_biblioteca.html', {
        'form': form,
        'ciudades': ciudades,
        'titulo': 'Agregar Biblioteca'
    })

def editar_biblioteca(request, id):
    ciudades = Ciudad.objects.all()
    biblioteca = get_object_or_404(Biblioteca, pk=id)
    if request.method=='POST':
        form = BibliotecaForm(request.POST, instance=biblioteca)
        if form.is_valid():
            form.save()
            return redirect ('listar_bibliotecas')
    else:
        form = BibliotecaForm(instance=biblioteca)
    return render(request, 'formulario_biblioteca.html', {
        'form': form,
        'ciudades': ciudades,
        'titulo': 'Editar Biblioteca'
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
    query = request.GET.get("q", "")  # Obtener lo que escribe el usuario
    libros = Libro.objects.all()

    if query:
        libros = libros.filter(
            titulo__icontains=query
        ) | libros.filter(
            autor__icontains=query
        ) | libros.filter(
            descripcion__icontains=query
        )

    return render(request, "listar_libros.html", {
        "libros": libros,
        "query": query
    })

def agregar_libro(request):
    generos = Genero.objects.all()
    bibliotecas = Biblioteca.objects.all()
    if request.method=='POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'formulario_libro.html', {
        'form': form,
        'generos': generos,
        'bibliotecas': bibliotecas,
        'titulo': 'Agregar Libro'
    })

def editar_libro(request, id):
    generos = Genero.objects.all()
    bibliotecas = Biblioteca.objects.all()
    libro = get_object_or_404(Libro, pk=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect ('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'formulario_libro.html', {
        'form': form,
        'generos': generos,
        'bibliotecas': bibliotecas,
        'titulo': 'Editar Libro'
    })

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    libro.delete()
    return redirect( 'listar_libros')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~Usuario~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def listar_usuarios(request):
    q= request.GET.get("q", "")
    if q:
        usuarios = Usuario.objects.filter(nombre__icontains=q)
    else:
        usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {
        'usuarios': usuarios, 
        'q': q
        })
    
def agregar_usuario(request):
    libros = Libro.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'formulario_usuario.html', {
        'form': form,
        'titulo': 'Agregar Usuario',
        'libros': libros
    })
    
def editar_usuario(request, id):
    libros = Libro.objects.all()
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'formulario_usuario.html', {
        'form': form,
        'titulo': 'Editar Usuario',
        'libros': libros
    })

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    usuario.delete()
    return redirect('listar_usuarios')

def detalle_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    libros_usuario = usuario.libros_prestamo.all()
    return render(request, 'detalle_usuario.html', {
        'usuario': usuario,
        'libros_usuario': libros_usuario
    })
    
    