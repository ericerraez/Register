from rest_framework import serializers
from .models import Bautizo, Comunion, Confirmacion, Matrimonio, Sepultura, Defuncion


# **Bautizo Serializer**
class BautizoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bautizo
        fields = '__all__'

# **Comunion Serializer**
class ComunionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunion
        fields = '__all__'

# **Confirmacion Serializer**
class ConfirmacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirmacion
        fields = '__all__'

# **Matrimonio Serializer**
class MatrimonioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matrimonio
        fields = '__all__'

# **Sepultura Serializer**
class SepulturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sepultura
        fields = '__all__'

class DefuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defuncion
        fields = '__all__'