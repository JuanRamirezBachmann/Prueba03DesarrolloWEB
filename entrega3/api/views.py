from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from core.models import Clientes
from .serializers import Entrega3Serializer

class Entrega3ListApiView(APIView):


    def get(self, request, *args, **kwargs):

        clientes = Clientes.objects.all()
        serializer = Entrega3Serializer(clientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Entrega3DetailApiView(APIView):

    def get(self, request, clienteID, *args, **kwargs):

        cliente = self.get_object(clienteID)

        if not cliente:
            return Response(
                {"res": "Objeto no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = Entrega3Serializer(cliente)
        return Response(serializer.data, status=status.HTTP_200_OK)

 
    def get_object(self, cliente_id):

        try:
            return Clientes.objects.get(idMascota = cliente_id)
        except Clientes.DoesNotExist:
            return None
