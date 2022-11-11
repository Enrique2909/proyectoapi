
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Cliente
import json
# Create your views here.
 
class ClienteView (View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args , **kwargs):
        return super().dispatch(request, *args, **kwargs)
 
    def get(self, request, id=0):
        if (id>0):
            cliente=list(Cliente.objects.filter(id=id).values())
            if len(cliente)>0:
                cliente=cliente[0]
                datos = {'message': "Success", 'cliente': cliente}
            else:
                datos = {'message': "Cliente no existe..."}
            return JsonResponse(datos)
        else:
            cliente =list(Cliente.objects.values ())
            if len(cliente)>0:
                datos={'message':"Success",'cliente':cliente}
            else:
                datos={'message':"Cliente no existe..."}
            return JsonResponse(datos)
 
    def post(self, request):
        jd = json.loads(request.body)
        Cliente.objects.create(nombre=jd['nombre'], paterno=jd['paterno'],materno=jd['materno'],telefono=jd['telefono'],direccion=jd['direccion'],)

        datos ={'message':"Success"}
        return JsonResponse(datos)
 
    def put(self, request, id):
        jd = json.loads(request.body)
        cliente=list(Cliente.objects.filter(id=id).values())
        if len(cliente)>0:
            cliente=Cliente.objects.get(id=id)
            cliente.nombre =jd ['nombre']
            cliente.paterno=jd ['paterno']
            cliente.materno=jd ['materno']
            cliente.telefono=jd ['telefono']
            cliente.direccion=jd ['direccion']
            cliente.save()
            datos ={'message':"Success"}
        else:
            datos = {'message': "Cliente no existe..."}
        return JsonResponse(datos)
 
    def delete(self, request, id):
        cliente=list(Cliente.objects.filter(id=id).values())
        if len(cliente) > 0:
            Cliente.objects.filter(id=id).delete()
            datos ={'message':"Success"}
        else:
            datos = {'message': "Cliente no existe..."}
        return JsonResponse(datos)

# Create your views here.