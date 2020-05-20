#
from django.urls import path
from . import views

app_name = "caja_app"

urlpatterns = [
    path(
        'cierre-caja/index/', 
        views.ReporteCierreCajaView.as_view(),
        name='caja-index',
    ),
    path(
        'cierre-caja/cerrar/', 
        views.ProcesoCerrarCajaView.as_view(),
        name='caja-cerrar',
    ),
]