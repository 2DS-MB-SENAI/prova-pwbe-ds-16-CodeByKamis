from django.shortcuts import render, redirect
from .models import Medico, Consulta #importei as minhas classes
from .serializers import PrimeiroSerializer, SegundoSerializer #importei a minha classe convertora
from rest_framework.response import Response #importei o response que serve para dar uma resposta
from rest_framework.decorators import api_view #importei uma tag que mostra quais metodos http eu vou usar
from rest_framework import status #importei o status que mostra os status das coisas
from datetime import datetime, timedelta #importei para conseguir filtrar os eventos de hoje até os prox 7 dias
# Create your views here.




def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos})

def form_consulta(request):
    consultas = Consulta.objects.all()
    return render(request, 'clinica/form_consulta.html', {'consultas': consultas})

# ver todos os medicos
# @api_view(['GET'])
# def listar_medicos(request):
#     medicos = Medico.objects.all()
#     serializer =  PrimeiroSerializer(medicos, many=True)
#     return redirect ("listar_medicos")

# criar consulta
@api_view(['POST'])
def criar_consulta(request):
    if request.method == 'POST':
        serializer = SegundoSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# pesquisar consultas por id
@api_view(['GET'])
def detalhes_consulta(request,pk):
    try:
        consulta = Consulta.objects.get(pk=pk)
    except Consulta.DoesNotExist:
        return Response({'erro': 'Consulta inexistente'}, status=status.HTTP_404_NOT_FOUND)
    serializer = SegundoSerializer(consulta)
    return Response(serializer.data)
