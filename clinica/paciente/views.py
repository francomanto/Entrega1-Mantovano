from django.shortcuts import render
from django.contrib import messages

from paciente.models import Paciente
from paciente.forms import PacienteForm


def get_pacientes(request):
    pacientes = Paciente.objects.all()
    return pacientes


def create_paciente(request):
    if request.method == "POST":
        paciente_form = PacienteForm(request.POST)
        if paciente_form.is_valid():
            data = paciente_form.cleaned_data
            actual_objects = Paciente.objects.filter(
                name=data["name"],
                last_name=data["last_name"],
                dni=data["dni"],
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El paciente {data['name']} {data['last_name']} ya está creado",
                )
            else:
                paciente = Paciente(
                    name=data["name"],
                    last_name=data["last_name"],
                    email=data["email"],
                    dni=data["dni"],
                    tel=data["tel"],
                )
                paciente.save()
                messages.success(
                    request,
                    f"Paciente {data['name']} {data['last_name']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"pacientes": get_pacientes(request)},
                template_name="paciente/paciente_list.html",
            )

    paciente_form = PacienteForm(request.POST)
    context_dict = {"form": paciente_form}
    return render(
        request=request,
        context=context_dict,
        template_name="paciente/paciente_form.html",
    )


def pacientes(request):
    pacientes = Paciente.objects.all()

    context_dict = {"pacientes": pacientes}

    return render(
        request=request,
        context=context_dict,
        template_name="paciente/paciente_list.html",
    )


