#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        'panel/', 
        views.PanelHomeView.as_view(),
        name='index',
    ),
    path(
        'panel/admin/', 
        views.PanelAdminView.as_view(),
        name='index-admin',
    ),
    path(
        'panel/admin-reporte/', 
        views.ReporteAdmin.as_view(),
        name='admin-reporte',
    ),
    path(
        'panel/admin-liquidacion/', 
        views.ReporteLiquidacion.as_view(),
        name='admin-liquidacion',
    ),
    path(
        'panel/admin-resumen-ventas/', 
        views.ReporteResumenVentas.as_view(),
        name='admin-resumen_ventas',
    ),
]