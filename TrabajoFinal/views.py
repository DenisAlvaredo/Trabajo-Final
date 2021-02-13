from django.http import HttpResponse

def saludo(request):
	return HttpResponse("Puto el que lee")