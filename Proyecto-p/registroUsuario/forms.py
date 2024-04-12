from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser

class RegistroForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirmar contraseña')
    
    class Meta:
        model = CustomUser
        fields = ['username', 'second_name', 'last_name', 'second_last_name', 'password', 'password2', 'email', 'phone', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'username': 'Usuario',
            'second_name': 'Segundo nombre (Opcional)',
            'last_name': 'Primer Apellido',
            'second_last_name': 'Segundo apellido (Opcional)',
            'password': 'Contraseña',
            'password2': 'Confirmar contraseña',
            'email': 'Correo electrónico',
            'phone': 'Teléfono',
        }
        error_messages = {
            'password_mismatch': 'Las contraseñas no coinciden.',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['second_name'].required = False
        self.fields['second_last_name'].required = False
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya ha sido registrado.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

