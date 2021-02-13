from django.http import HttpResponse

def saludo(request):
	return HttpResponse("Puto el que lee")

def chaucha(request):
	return HttpResponse("es una verdura que tiene miku")