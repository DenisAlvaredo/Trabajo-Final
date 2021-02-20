from django.http import HttpResponse
from django.shortcuts import render

def Inicio(request):
	return render(request, 'home.html')

def pagina2(request):
	return render(request, 'pagina2.html')