from .models import consulta
from rest_framework import serializers

class consulta(serializers.ModelSerializer):
    class Meta :
        model = consulta
        fields = '__all__'