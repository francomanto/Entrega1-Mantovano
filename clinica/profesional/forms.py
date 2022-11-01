from django import forms


class ProfesionalForm(forms.Form):
    name = forms.CharField(
        label="Nombre del Profesional",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesional-name",
                "placeholder": "Nombre de profesional",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido del profesional",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesional-last-name",
                "placeholder": "Apellido del profesional",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesional-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )
    especialidad = forms.CharField(
        label="Especialidad:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesional-especialidad",
                "placeholder": "Especialidad",
                "required": "True",
            }
        ),
    )
    tel = forms.IntegerField(
        label="Telefono:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "profesional-tel",
                "placeholder": "Telefono",
                "required": "True",
            }
        ),
    )