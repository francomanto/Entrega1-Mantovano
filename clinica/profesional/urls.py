from django.urls import path

from profesional import views

app_name = "profesional"
urlpatterns = [
    path("profesionals", views.profesionals, name="profesional-list"),
    path("profesional/add", views.create_profesional, name="profesional-add"),
]
