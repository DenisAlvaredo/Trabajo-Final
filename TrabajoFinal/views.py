from django.http import HttpResponse

def saludo(request):
	return HttpResponse("Puto el que lee")

def puerro(request):
	return HttpResponse("es la verdura que tiene miku")
