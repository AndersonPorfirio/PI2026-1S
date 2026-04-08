from django.db import models

class Equipamento(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.marca} - {self.modelo}"

class Reparo(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='reparos')
    sintoma = models.TextField()
    causa = models.TextField()
    solucao = models.TextField()
    tecnico_nome = models.CharField(max_length=100)

    def __str__(self):
        return f"Reparo {self.id} - {self.equipamento.modelo}"