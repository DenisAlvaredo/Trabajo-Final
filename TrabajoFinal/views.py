from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login


def Inicio(request):
	return render(request, 'home.html')

def pagina2(request):
	return render(request, 'pagina2.html')

def register(request):
	return render(request, 'register.html')

def login(request):
    return render(request, "login.html")

def logout(request):
    # Finaliza la sesión
    do_logout(request)
    # Redirecciona a home
    return redirect('/')

def login(request):
    # Si ya está autenticado, redirige a home, sino dirige a login
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
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
                # Verifica las credenciales del usuario
                user = authenticate(username=username, password=password)
                # Si existe un usuario con ese nombre y contraseña
                if user is not None:
                    # Hace el login manualmente
                    do_login(request, user)
                    # Y redirecciona a la portada
                    return redirect('/')
        # Si llega al final renderiza el formulario
        return render(request, "login.html", {'form': form})

def register(request):
    # Crea el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añade los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Crea la nueva cuenta de usuario
            user = form.save()
            # Si el usuario se crea correctamente 
            if user is not None:
                # Hace el login manualmente
                do_login(request, user)
                # Y redirecciona a la portada
                return redirect('/')
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    # Si llega al final renderiza el formulario
    return render(request, "register.html", {'form': form})
