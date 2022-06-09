from django.urls import path
from AppEntregable import views
from AppEntregable.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("usuario/", usuario, name="Usuario"),
    path("crearUsuario/", usuario_crear, name="Crear_Usuario"),
    path("busquedaUsuario/", usuario_busqueda, name="Busqueda_Usuario"),
    path("buscar/", usuario_resultado, name="Buscar"),
    path("usuario_list/", usuario_list, name="usuario_list"),

    path('bibliotecas/', bibliotecas, name='bibliotecas'),
    path('biblio_list/', biblio_list, name='biblio_list'),
    path('carga_biblio/', biblio_crear, name='carga_biblio'),
    path('busca_biblio/', biblio_busqueda, name='busca_biblio'),
    
    path("textos/", textos, name="textos"),
    path("hansel-gretel/", hanselYGretel, name="hansel_gretel"),
    path("gato-con-botas/", gatoConBotas, name="gato_con_botas"),
    path("tres-cerditos/", tresCerditos, name="tres_cerditos"),
    path("crear_libro/", texto_crear, name="crear_libro"),
    path("buscar_libro/", texto_buscador, name="texto_buscador"),
    path("texto_busqueda/", texto_busqueda, name="texto_busqueda"),
] 