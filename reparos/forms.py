from django import forms
from .models import Reparo

class ReparoForm(forms.ModelForm):
    class Meta:
        model = Reparo
        fields = ['equipamento', 'sintoma', 'causa', 'solucao', 'tecnico_nome']
        # Adicionamos classes CSS para manter o estilo moderno
        widgets = {
            'equipamento': forms.Select(attrs={'class': 'input-moderno'}),
            'sintoma': forms.Textarea(attrs={'class': 'input-moderno', 'rows': 3}),
            'causa': forms.Textarea(attrs={'class': 'input-moderno', 'rows': 3}),
            'solucao': forms.Textarea(attrs={'class': 'input-moderno', 'rows': 3}),
            'tecnico_nome': forms.TextInput(attrs={'class': 'input-moderno'}),
        }
class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'modelo', 'marca', 'serie']
        # Adicione classes CSS para manter o Dark Mode
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'}) 
            for field in ['nome', 'modelo', 'marca', 'serie']
        }
