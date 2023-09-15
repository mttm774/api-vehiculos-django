from django.urls import path

from .views import VehicleApiView

urlpatterns = [
    path ('list',VehicleApiView.as_view())
]
