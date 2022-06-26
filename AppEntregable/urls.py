from django.urls import path
from AppEntregable.views import *

urlpatterns = [
    path("sesion_iniciar/", sesion_iniciar, name="sesion_iniciar"),
    path("sesion_cerrar/", sesion_cerrar, name="sesion_cerrar"),
    path("sesion_registrar/", sesion_registrar, name="sesion_registrar"),

    path("", inicio, name="inicio"),
    path("usuario/", usuario, name="Usuario"),
    path("crearUsuario/", usuario_crear, name="Crear_Usuario"),
    path("busquedaUsuario/", usuario_busqueda, name="Busqueda_Usuario"),
    path("buscar/", usuario_resultado, name="Buscar"),
    path("usuario_list/", usuario_list, name="usuario_list"),

    path('bibliotecas/', bibliotecas, name='bibliotecas'),
    # path('biblio_list/', biblio_list, name='biblio_list'), 
    path('biblio_list/', biblio_list.as_view(), name='biblio_list'),
    # path('carga_biblio/', biblio_crear, name='carga_biblio'),
    path('carga_biblio/', biblio_crear.as_view(), name='carga_biblio'),
    path('busca_biblio/', biblio_busqueda, name='busca_biblio'),
    # path('biblio_detalle/<int:pk>/', biblio_detalle, name='biblio_detalle'),
    path('biblio_detalle/<int:pk>/', biblio_detalle.as_view(), name='biblio_detalle'),
    # path('biblio_eliminar/<int:pk>/', biblio_eliminar, name='biblio_eliminar'),
    path('biblio_eliminar/<int:pk>/', biblio_eliminar.as_view(), name='biblio_eliminar'),
    path('biblio_editar/<int:pk>/', biblio_editar.as_view(), name='biblio_editar'),
    
    path("textos/", textos, name="textos"),
    path("hansel-gretel/", hanselYGretel, name="hansel_gretel"),
    path("gato-con-botas/", gatoConBotas, name="gato_con_botas"),
    path("tres-cerditos/", tresCerditos, name="tres_cerditos"),
    path("crear_libro/", texto_crear, name="crear_libro"),
    path("buscar_libro/", texto_buscador, name="texto_buscador"),
    path("texto_busqueda/", texto_busqueda, name="texto_busqueda"),
] 