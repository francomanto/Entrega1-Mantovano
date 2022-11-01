from django import forms


class PacienteForm(forms.Form):
    name = forms.CharField(
        label="Nombre del Paciente",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "paciente-name",
                "placeholder": "Nombre de paciente",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido del paciente",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "paciente-last-name",
                "placeholder": "Apellido del paciente",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "paciente-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )
    dni = forms.IntegerField(
        label="Dni:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "paciente-dni",
                "placeholder": "Dni",
                "required": "True",
            }
        ),
    )
    tel = forms.IntegerField(
        label="Telefono:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "paciente-tel",
                "placeholder": "Telefono",
                "required": "True",
            }
        ),
    )