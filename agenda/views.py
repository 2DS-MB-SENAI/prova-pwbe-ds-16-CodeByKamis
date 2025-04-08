from django.shortcuts import render, redirect
from .models import Servico, Agendamento #importei as minhas classes
from .serializers import PrimeiroSerializer, SegundoSerializer #importei a minha classe convertora
from rest_framework.response import Response #importei o response que serve para dar uma resposta
from rest_framework.decorators import api_view #importei uma tag que mostra quais metodos http eu vou usar
from rest_framework import status #importei o status que mostra os status das coisas
# Create your views here.

# de serviço

@api_view(['GET','POST'])
def criar_ver(request):
    if request.method == 'GET':
            servico = Servico.objects.all()
            serializer =  PrimeiroSerializer(servico, many=True)
            return Response(serializer.data)
    if request.method == 'POST':
        serializer = PrimeiroSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# pesquisar consultas por id
@api_view(['GET'])
def detalhes_servico(request,pk):
    try:
        servicos = Servico.objects.get(pk=pk)
    except Servico.DoesNotExist:
        return Response({'erro': 'Esse serviço é inexistente'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PrimeiroSerializer(servicos)
    return Response(serializer.data)

# # ver todos os servicos
# @api_view(['GET'])
# def servicos(request):
#     servico = Servico.objects.all()
#     serializer =  PrimeiroSerializer(servico, many=True)
#     return redirect ("servicos")

# # criar servico
# @api_view(['POST'])
# def criar_servico(request):
#     if request.method == 'POST':
#         serializer = PrimeiroSerializer(data=request.data, many=isinstance(request.data, list))
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# pesquisar consultas por id
# @api_view(['GET'])
# def detalhes_servico(request,pk):
#     try:
#         servicos = Servico.objects.get(pk=pk)
#     except Servico.DoesNotExist:
#         return Response({'erro': 'Esse serviço é inexistente'}, status=status.HTTP_404_NOT_FOUND)
#     serializer = PrimeiroSerializer(servicos)
#     return Response(serializer.data)



# de agendamento



@api_view(['GET','POST'])
def creat_read(request):
    if request.method == 'GET':
            Agendamentos = Agendamento.objects.all()
            serializer =  SegundoSerializer(Agendamentos, many=True)
            return Response(serializer.data)
    if request.method == 'POST':
        serializer = SegundoSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# pesquisar agendamento por id
@api_view(['GET'])
def detalhes_agentamento(request,pk):
    try:
        agendamentos = Agendamento.objects.get(pk=pk)
    except Agendamento.DoesNotExist:
        return Response({'erro': 'Esse agendamento é inexistente'}, status=status.HTTP_404_NOT_FOUND)
    serializer = SegundoSerializer(agendamentos)
    return Response(serializer.data)









# # ver todos os agendamentos
# @api_view(['GET'])
# def agendamentos(request):
#     agendamentos = Agendamento.objects.all()
#     serializer =  SegundoSerializer(agendamentos, many=True)
#     return redirect ("agendamentos")

# # criar agendamento
# @api_view(['POST'])
# def criar_agendamento(request):
#     if request.method == 'POST':
#         serializer = SegundoSerializer(data=request.data, many=isinstance(request.data, list))
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# # pesquisar agendamento por id
# @api_view(['GET'])
# def detalhes_agentamento(request,pk):
#     try:
#         agendamentos = Agendamento.objects.get(pk=pk)
#     except Agendamento.DoesNotExist:
#         return Response({'erro': 'Esse serviço é inexistente'}, status=status.HTTP_404_NOT_FOUND)
#     serializer = SegundoSerializer(agendamentos)
#     return Response(serializer.data)