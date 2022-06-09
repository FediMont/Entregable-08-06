from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppEntregable.forms import *
from AppEntregable.models import *
# Create your views here.

#Pestaña de inicio
def inicio(self):
    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

#Seccion USUARIOS
#Pestaña de usuario
def usuario(request):
    return render(request, "usuario.html")

#Pestaña para crear usuario con formulario
def usuario_crear(request):
    if request.method == "POST":
        miFormulario = UsuarioForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            nombre_de_usuario= informacion["nombre_de_usuario"]
            email= informacion["email"]
            password= informacion["password"]
            fecha_de_nacimiento= informacion["fecha_de_nacimiento"]
            usuario = Usuario (nombre=nombre, apellido=apellido, nombre_de_usuario=nombre_de_usuario, email=email, password=password, fecha_de_nacimiento=fecha_de_nacimiento)
            usuario.save()
            return render(request, "inicio.html")

    else:
        miFormulario = UsuarioForm()
    
    return render(request, "usuario_crear.html", {"miFormulario":miFormulario})

#Pestaña con listado de usuarios 
def usuario_list(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios':usuarios}
    return render(request, "usuario_list.html", context=context)

#Pestaña para buscar usuario 
def usuario_busqueda(request):
    return render(request, "usuario_busqueda.html")

#funcion para buscar usuario
def usuario_resultado(request):
    if request.GET["nombre_de_usuario"]:
        nombre_de_usuario = request.GET["nombre_de_usuario"]
        nombre = Usuario.objects.filter(nombre_de_usuario = nombre_de_usuario)
        return render(request, "usuario_resultado.html", {"nombre":nombre})
    else:
        respuesta = "no se encontro ningun usuario"
    return HttpResponse(respuesta)


#Seccion BIBLIOTECAS

def bibliotecas(request):
    return render(request,'bibliotecas.html')

def biblio_busqueda(request):
    biblioteca = Bibliotecas.objects.filter(nombre__icontains = request.GET['search'])
    context = {'biblioteca':biblioteca}
    return render(request,'biblio_busqueda.html', context=context)

def biblio_list(request):
    bibliotecas = Bibliotecas.objects.all()
    context = {'bibliotecas':bibliotecas}
    return render(request,'biblio_list.html', context=context)

def biblio_crear(request):
    if request.method == 'GET':
        form = Biblio_form()
        context = {'form':form}
        return render(request,'biblio_crear.html', context=context)
    else:
        form = Biblio_form(request.POST)
        if form.is_valid():
            nueva_biblio = Bibliotecas.objects.create(
                nombre = form.cleaned_data['nombre'],
                provincia = form.cleaned_data['provincia'],
                localidad = form.cleaned_data['localidad'],
                direccion = form.cleaned_data['direccion'],
                apertura = form.cleaned_data['apertura'],
                link = form.cleaned_data['link'],
                imagen = form.cleaned_data['imagen'],
                )   
            context={'nueva_biblio':nueva_biblio}
        return render(request,'biblio_crear.html', context=context)

#Seccion TEXTOS

def textos(request):
    textos = Libro.objects.all()
    context = {'textos':textos}
    return render(request,'textos.html', context=context)

def texto_crear(request):
    if request.method == 'GET':
        form = Libro_form()
        context = {'form':form}
        return render(request,'texto_crear.html', context=context)
    else:
        form = Libro_form(request.POST)
        if form.is_valid():
            nuevo_texto = Libro.objects.create(
                nombre_libro = form.cleaned_data['nombre_libro'],
                autor = form.cleaned_data['autor'],
                link_autor = form.cleaned_data['link_autor'],
                link_texto = form.cleaned_data['link_texto'],
                descripcion = form.cleaned_data['descripcion'],
                )   
            textos = Libro.objects.all()
            context = {'textos':textos}
            return render(request,'textos.html', context=context)

def texto_buscador(request):
    return render(request,'texto_buscador.html')

def texto_busqueda(request):
    texto = Libro.objects.filter(nombre_libro__icontains = request.GET['search'])
    context = {'texto':texto}
    return render(request,'texto_busqueda.html', context=context)
    
def hanselYGretel(self):
    plantilla = loader.get_template("texto_hansel_gretel.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def gatoConBotas(self):
    plantilla = loader.get_template("texto_gato_con_botas.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def tresCerditos(self):
    plantilla = loader.get_template("texto_tres_cerditos.html")
    documento = plantilla.render()
    return HttpResponse(documento)