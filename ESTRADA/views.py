from django.shortcuts import render

def inicio (request):
    return render (request, 'estrada/inicio.htmL')
def registro(request):
    return render (request, 'estrada/formregistro.html')