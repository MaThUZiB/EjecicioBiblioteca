from django import forms
from .models import *

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre', 'campo01', 'campo02']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre Ciudad'
            }),
            'campo01': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Campo01'
            }),
            'campo02': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Campo02'
            })
        }

class BibliotecaForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ['nombre', 'direccion', 'ciudad_id', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre Biblioteca'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Direccion Biblioteca'
            }),
            'ciudad_id': forms.Select(attrs={
                'class': 'form-control',
            }),
            'telefono': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '+56 9 XXXX XXXX'
            })
        }

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre Genero'
            })
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero_id', 'isbn', 'descripcion', 'biblioteca_id']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titulo Libro'
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Autor Libro'
            }),
            'genero_id': forms.Select(attrs={
                'class': 'form-control'
            }),
            'isbn': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'International Standard Book Number'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripcion de la historia del Libro'
            }),
            'biblioteca_id': forms.Select(attrs={
                'class': 'form-control'
            })
        }
        
class EncargadoBibliotecaForm(forms.ModelForm):
    class Meta:
        model = EncargadoBiblioteca
        fields = ['nombre', 'biblioteca_id', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre Encargado'
            }),
        }
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'libros_prestamo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre Usuario'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Usuario'
            }),
            'libros_prestamo': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check'
            })
        }