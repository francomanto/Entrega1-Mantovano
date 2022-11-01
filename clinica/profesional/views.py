from django.shortcuts import render
from django.contrib import messages

from profesional.models import Profesional
from profesional.forms import ProfesionalForm


def get_profesionals(request):
    profesionals = Profesional.objects.all()
    return profesionals


def create_profesional(request):
    if request.method == "POST":
        profesional_form = ProfesionalForm(request.POST)
        if profesional_form.is_valid():
            data = profesional_form.cleaned_data
            actual_objects = Profesional.objects.filter(
                name=data["name"],
                last_name=data["last_name"],
                email=data["email"],
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El profesional {data['name']} {data['last_name']} ya está creado",
                )
            else:
                profesional = Profesional(
                    name=data["name"],
                    last_name=data["last_name"],
                    email=data["email"],
                    especialidad=data["especialidad"],
                    tel=data["tel"],
                )
                profesional.save()
                messages.success(
                    request,
                    f"Profesional {data['name']} {data['last_name']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"profesionals": get_profesionals(request)},
                template_name="profesional/profesional_list.html",
            )

    profesional_form = ProfesionalForm(request.POST)
    context_dict = {"form": profesional_form}
    return render(
        request=request,
        context=context_dict,
        template_name="profesional/profesional_form.html",
    )


def profesionals(request):
    profesionals = Profesional.objects.all()

    context_dict = {"profesionals": profesionals}

    return render(
        request=request,
        context=context_dict,
        template_name="profesional/profesional_list.html",
    )

