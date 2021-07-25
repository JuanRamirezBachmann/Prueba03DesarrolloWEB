from rest_framework import serializers
from core.models import Clientes

class Entrega3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ("idMascota", "tipoAnimal", "detalles" )