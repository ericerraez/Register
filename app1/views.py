from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import Bautizo, Comunion, Confirmacion, Matrimonio, Sepultura, Defuncion
from .serializers import BautizoSerializer, ComunionSerializer, ConfirmacionSerializer, MatrimonioSerializer, SepulturaSerializer, DefuncionSerializer

# **Bautizo**
class BautizoList(APIView):
    # GET: Obtener todos los bautizos
    def get(self, request):
        bautizos = Bautizo.objects.all()
        serializer = BautizoSerializer(bautizos, many=True)
        return Response(serializer.data)

    # POST: Crear un nuevo bautizo
    def post(self, request):
        serializer = BautizoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BautizoDetail(APIView):
    # GET: Obtener detalles de un bautizo específico por ID
    def get(self, request, pk):
        try:
            bautizo = Bautizo.objects.get(pk=pk)
        except Bautizo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BautizoSerializer(bautizo)
        return Response(serializer.data)

    # PUT: Actualizar un bautizo por ID
    def put(self, request, pk):
        try:
            bautizo = Bautizo.objects.get(pk=pk)
        except Bautizo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BautizoSerializer(bautizo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Eliminar un bautizo por ID
    def delete(self, request, pk):
        try:
            bautizo = Bautizo.objects.get(pk=pk)
        except Bautizo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        bautizo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# **Comunion**
class ComunionList(APIView):
    def get(self, request):
        comuniones = Comunion.objects.all()
        serializer = ComunionSerializer(comuniones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ComunionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComunionDetail(APIView):
    def get(self, request, pk):
        try:
            comunion = Comunion.objects.get(pk=pk)
        except Comunion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ComunionSerializer(comunion)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            comunion = Comunion.objects.get(pk=pk)
        except Comunion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ComunionSerializer(comunion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            comunion = Comunion.objects.get(pk=pk)
        except Comunion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        comunion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# **Confirmacion**
class ConfirmacionList(APIView):
    def get(self, request):
        confirmaciones = Confirmacion.objects.all()
        serializer = ConfirmacionSerializer(confirmaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConfirmacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmacionDetail(APIView):
    def get(self, request, pk):
        try:
            confirmacion = Confirmacion.objects.get(pk=pk)
        except Confirmacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ConfirmacionSerializer(confirmacion)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            confirmacion = Confirmacion.objects.get(pk=pk)
        except Confirmacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ConfirmacionSerializer(confirmacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            confirmacion = Confirmacion.objects.get(pk=pk)
        except Confirmacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        confirmacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# **Matrimonio**
class MatrimonioList(APIView):
    def get(self, request):
        matrimonios = Matrimonio.objects.all()
        serializer = MatrimonioSerializer(matrimonios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MatrimonioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatrimonioDetail(APIView):
    def get(self, request, pk):
        try:
            matrimonio = Matrimonio.objects.get(pk=pk)
        except Matrimonio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MatrimonioSerializer(matrimonio)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            matrimonio = Matrimonio.objects.get(pk=pk)
        except Matrimonio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MatrimonioSerializer(matrimonio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            matrimonio = Matrimonio.objects.get(pk=pk)
        except Matrimonio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        matrimonio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# **Sepultura**
class SepulturaList(APIView):
    def get(self, request):
        sepulturas = Sepultura.objects.all()
        serializer = SepulturaSerializer(sepulturas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SepulturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SepulturaDetail(APIView):
    def get(self, request, pk):
        try:
            sepultura = Sepultura.objects.get(pk=pk)
        except Sepultura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SepulturaSerializer(sepultura)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            sepultura = Sepultura.objects.get(pk=pk)
        except Sepultura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SepulturaSerializer(sepultura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            sepultura = Sepultura.objects.get(pk=pk)
        except Sepultura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        sepultura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # **Defunción**

class DefuncionList(APIView):
    def get(self, request):
        defunciones = Defuncion.objects.all()
        serializer = DefuncionSerializer(defunciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DefuncionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DefuncionDetail(APIView):
    def get(self, request, pk):
        try:
            defuncion = Defuncion.objects.get(pk=pk)
        except Defuncion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DefuncionSerializer(defuncion)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            defuncion = Defuncion.objects.get(pk=pk)
        except Defuncion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DefuncionSerializer(defuncion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            defuncion = Defuncion.objects.get(pk=pk)
        except Defuncion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        defuncion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
