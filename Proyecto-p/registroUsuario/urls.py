# En nombre_app/urls.py
from django.urls import path
from .views import registro_view


urlpatterns = [
    path('', registro_view, name='registro'),
    # Otras URLs necesarias
]

