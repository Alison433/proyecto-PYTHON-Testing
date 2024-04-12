# En registroUsuario/views.py
from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import CustomUser

def registro_view(request):
    print("function view")
    if request.method == 'POST':
        print("metodo post registro")
        form = RegistroForm(request.POST)
        if form.is_valid():
            # El formulario ya maneja la validación de contraseñas
            # No es necesario verificarlo aquí nuevamente
            # Crea un nuevo usuario utilizando el modelo CustomUser
            print("from valid")
            CustomUser.objects.create_user(
                username = form.cleaned_data['username'],
                second_name = form.cleaned_data['second_name'],
                second_last_name = form.cleaned_data['second_last_name'],
                password = form.cleaned_data['password'],
                password2 = form.cleaned_data['password2'],
                email = form.cleaned_data['email'],
                phone = form.cleaned_data['phone'],
                role = form.cleaned_data['role'],
            )
            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})







