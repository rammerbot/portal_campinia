from django import forms

from .models import Contact
 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')

        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nombre...',
                    'class':'form-control'
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese apellido...',
                    'class':'form-control'
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'placeholder':'Correo...',
                    'class':'form-control'
                }
            ),
            'phone' : forms.TextInput(
                attrs={
                    'placeholder':'N° de telefono...',
                    'class':'form-control'
                }
            ),
            'street' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese direccion...',
                    'class':'form-control'
                }
            ),
            'message' : forms.Textarea(
                attrs={
                    'placeholder':'Escriba su mensaje...',
                    'class':'form-control'
                }
            ),
            }