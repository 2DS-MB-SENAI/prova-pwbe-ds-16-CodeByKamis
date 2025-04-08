from rest_framework import serializers
from .models import Medico, Consulta

class PrimeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class SegundoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'