from rest_framework import serializers
from .models import Servico, Agendamento

class PrimeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'

class SegundoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'