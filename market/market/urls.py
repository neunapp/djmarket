"""
Proyecto Final
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.home.urls')),
    # users app
    re_path('', include('applications.users.urls')),
    # producto app
    re_path('', include('applications.producto.urls')),
    # venta app
    re_path('', include('applications.venta.urls')),
    # caja app
    re_path('', include('applications.caja.urls')),
]
