from django.urls import path

from .views import VehicleApiView, VehicleQueryApiView

urlpatterns = [
    path ('crear-vehiculo',VehicleApiView.as_view()),
    path ('list',VehicleApiView.as_view()),
    path ('actualizar-vehiculo/<int:pkid>',VehicleApiView.as_view(),name='actualizar_vehiculo'),
    path ('consultar/<int:id>/',VehicleQueryApiView.as_view(),name='obtener_vehiculo')
    
]
