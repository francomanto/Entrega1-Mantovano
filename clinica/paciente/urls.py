from django.urls import path

from paciente import views

app_name = "paciente"
urlpatterns = [
    path("pacientes", views.pacientes, name="paciente-list"),
    path("paciente/add", views.create_paciente, name="paciente-add"),
]
