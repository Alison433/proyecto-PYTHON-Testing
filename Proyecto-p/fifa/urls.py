"""
URL configuration for fifa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from registroUsuario import urls
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
# from .views import logout_view




urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
    path('', views.index, name='index'),
    path('cliente/', include('cliente.urls'), name="store"),
    path('login/', views.login_view, name='login'),
    path('admin/logout/', views.logout_view, name='logout'),
    path('cerrar/', views.logout_view, name='cerrar'),
    path('registro/' , include('registroUsuario.urls'), name='registro'),
    path('quienessomos/' , views.quienessomos_view, name='quienessomos'),
    path('camaras/' , views.camaras_view, name='camaras'),
    path('discos/' , views.discos_view, name='discos'),
    path('dvr/' , views.dvr_view, name='dvr'),
    path('fuentes/' , views.fuentes_view, name='fuentes'),
    path('ups/' , views.ups_view, name='ups'),
    path('contacto/' , views.contacto_view, name='contacto'),
    path('roles/' , views.roles_view, name='roles'),
    path('administrador/consultar_ventas/', views.consultar_ventas, name='consultar_ventas'),
    path('administrador/indexadmin/', views.indexadmin, name='indexadmin'),
    path('administrador/crear_orden_compra/', views.crear_orden_compra, name='crear_orden_compra'),
    path('administrador/listar_empleado/', views.listar_empleado, name='listar_empleado'),
    path('administrador/listar_orden_compra/', views.listar_orden_compra, name='listar_orden_compra'),
    path('administrador/listar_producto/', views.listar_producto, name='listar_producto'),
    path('administrador/listar_proveedor/', views.listar_proveedor, name='listar_proveedor'),
    path('administrador/registrar_empleado/', views.registrar_empleado, name='registrar_empleado'),
    path('administrador/registrar_producto/', views.registrar_producto, name='registrar_producto'),
    path('administrador/registrar_proveedor/', views.registrar_proveedor, name='registrar_proveedor'),
    path('administrador/registrar/', views.registrar, name='registrar'),
    path('administrador/servicios_tecnicos', views.servicios_tecnicos, name='servicios_tecnicos'),
    path('gerente/consultar_ventasG/', views.consultar_ventasG, name='consultar_ventasG'),
    path('gerente/crear_orden_compraG/', views.crear_orden_compraG, name='crear_orden_compraG'),
    path('gerente/indexgerente/', views.indexgerente, name='indexgerente'),
    path('gerente/listar_empleadoG/', views.listar_empleadoG, name='listar_empleadoG'),
    path('gerente/listar_orden_compraG/', views.listar_orden_compraG, name='listar_orden_compraG'),
    path('gerente/listar_productoG/', views.listar_productoG, name='listar_productoG'),
    path('gerente/listar_proveedorG/', views.listar_proveedorG, name='listar_proveedorG'),
    path('gerente/registrar_empleadoG/', views.registrar_empleadoG, name='registrar_empleadoG'),
    path('gerente/registrar_productoG/', views.registrar_productoG, name='registrar_productoG'),
    path('gerente/registrar_proveedorG/', views.registrar_proveedorG, name='registrar_proveedorG'),
    path('gerente/registrar_Ge/', views.registrar_Ge, name='registrar_Ge'),
    path('gerente/servicios_tecnicosG', views.servicios_tecnicosG, name='servicios_tecnicosG'),
    path('vendedor/comprobante.html', views.comprobante, name='comprobante'),
    path('vendedor/consultar_clientes', views.consultar_clientes, name='consultar_clientes'),
    path('vendedor/consultar_estado_inventario', views.consultar_estado_inventario, name='consultar_estado_inventario'),
    path('vendedor/consultar_orden_pedido', views.consultar_orden_pedido, name='consultar_orden_pedido'),
    path('vendedor/consultar_ventasV', views.consultar_ventasV, name='consultar_ventasV'),
    path('vendedor/crear_orden_pedido', views.crear_orden_pedido, name='crear_orden_pedido'),
    path('vendedor/indexvendedor', views.indexvendedor, name='indexvendedor'),
    path('vendedor/registrar_ventas', views.registrar_ventas, name='registrar_ventas'),
    path('tecnico/indextecnico', views.indextecnico, name='indextecnico'),
    path('tecnico/consultar_servicio_tecnico', views.consultar_servicio_tecnico, name='consultar_servicio_tecnico'),
    path('tecnico/registrar_novedad_servicios', views.registrar_novedad_servicios, name='registrar_novedad_servicios'),
    path('cliente/indexcliente', views.indexcliente, name='indexcliente'),
    path('cliente/crear_orden_compraC', views.crear_orden_compraC, name='crear_orden_compraC'),
    path('cliente/catalogo', views.catalogo, name='catalogo'),
    path('mensajero/indexmensajero', views.indexmensajero, name='indexmensajero'),
    path('mensajero/consultar_orden_compraMen', views.consultar_orden_compraMen, name='consultar_orden_compraMen'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
