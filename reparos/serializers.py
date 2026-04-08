from rest_framework import serializers
from .models import Reparo

class ReparoSerializer(serializers.ModelSerializer):
    # Converte o relacionamento com o equipamento em texto legível [cite: 204]
    equipamento_nome = serializers.CharField(source='equipamento.__str__', read_only=True)

    class Meta:
        model = Reparo
        fields = ['id', 'equipamento_nome', 'sintoma', 'causa', 'solucao', 'tecnico_nome']