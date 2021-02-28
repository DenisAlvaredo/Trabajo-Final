from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import AuthenticationForm


def Inicio(request):
	return render(request, 'home.html')

def pagina2(request):
	return render(request, 'pagina2.html')

def registrarse(request):
	return render(request, 'registrarse.html')

def login(request):
    return render(request, "login.html")

def salir(request):
    # Finaliza la sesión
    do_logout(request)
    # Redirecciona a home
    return redirect('/')

def login(request):
    # Crea el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añade los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recupera las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Verificam las credenciales del usuario
            user = authenticate(username=username, password=password)
            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hace el login manualmente
                do_login(request, user)
                # Y redirecciona a la portada
                return redirect('/')
    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})