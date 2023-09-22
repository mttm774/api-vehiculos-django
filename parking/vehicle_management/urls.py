from django.urls import path

from .views import VehicleApiView

urlpatterns = [
    path ('list',VehicleApiView.as_view()),
    path ('list/<int:pkid>/',VehicleApiView.as_view(),name='actualizar_vehiculo')
]
