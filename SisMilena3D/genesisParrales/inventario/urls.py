from django.contrib import admin
from django.urls import path
from .import views
from .views import grupolistar,grupoguardar,grupomodificar
from .views import clientelistar,clienteguardar,clientemodificar
from .views import proveedorlistar,proveedorguardar,proveedormodificar
from .views import productolistar,productoguardar,productomodificar
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('Grupolistar', grupolistar.as_view(), name='grupolistar'),
    path('Grupoguardar', grupoguardar.as_view(), name='grupoguardar'),
    path('Grupomodificar/<int:pk>', grupomodificar.as_view(),name='grupomodificar'),
    path('Holapdf', views.hello_pdf, name='holapdf'),
    path('Grupospdf', views.grupos_print, name='grupospdf'),
    path('Grupoindividual/<int:pk>', views.grupos_print, name='grupoindividual'),
    #######################cliente#########################################
    path('Clientelistar', clientelistar.as_view(), name='clientelistar'),
    path('Clienteguardar', clienteguardar.as_view(), name='clienteguardar'),
    path('Clientemodificar/<int:pk>', clientemodificar.as_view, name='clientemodificar'),
    path('Clientespdf', views.clientes_print, name='clientespdf'),
    path('Clienteindividual/<int:pk>', views.clientes_print, name='clienteindividual'),
    #######################proveedor#########################################
    path('Proveedorlistar', proveedorlistar.as_view(), name='proveedorlistar'),
    path('Proveedorguardar', proveedorguardar.as_view(), name='proveedorguardar'),
    path('Proveedormodificar/<int:pk>', proveedormodificar.as_view(), name='proveedormodificar'),
    path('Proveedorespdf', views.proveedores_print, name='proveedorespdf'),
    path('Provedorindividual/<int:pk>', views.proveedores_print, name='proveedorindividual'),
    #######################producto#########################################
    path('Productolistar', productolistar.as_view(), name='productolistar'),
    path('Productoguardar', productoguardar.as_view(), name='productoguardar'),
    path('Productomodificar/<int:pk>', productomodificar.as_view(), name='productomodificar'),
    path('Productospdf', views.productos_print, name='productospdf'),
    path('Productoindividual/<int:pk>', views.productos_print, name='productoindividual'),
    #############################login########################################
    path('', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuario/login.html'), name='logout'),
]
