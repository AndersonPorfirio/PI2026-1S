from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from reparos.models import Reparo
from reparos.forms import ReparoForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from reparos.serializers import ReparoSerializer
from django.shortcuts import redirect, get_object_or_404

@login_required
def index(request):
    dados_reparos = Reparo.objects.all()
    return render(request, 'index.html', {'reparos': dados_reparos})
    
def detalhe(request, pk):
    reparo = get_object_or_404(Reparo, pk=pk)
    return render(request, 'reparo_detalhe.html', {'reparo': reparo})

def sobre(request):
    return render(request, 'sobre.html')

def novo_reparo(request):
    if request.method == 'POST':
        form = ReparoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') # Volta para o painel após salvar
    else:
        form = ReparoForm()
    return render(request, 'novo_reparo.html', {'form': form})

# Função para verificar se é admin
def e_admin(user):
    return user.is_superuser

@user_passes_test(e_admin)
def painel_admin(request):
    reparos = Reparo.objects.all().order_by('-id')
    usuarios = User.objects.all()
    return render(request, 'admin_custom.html', {
        'reparos': reparos,
        'usuarios': usuarios
    })

@user_passes_test(e_admin)
def excluir_reparo(request, pk):
    reparo = get_object_or_404(Reparo, pk=pk)
    reparo.delete()
    return redirect('painel_admin')

@user_passes_test(e_admin)
def excluir_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if not usuario.is_superuser: # Impede você de se excluir por erro
        usuario.delete()
    return redirect('painel_admin')

@user_passes_test(e_admin)
def novo_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('painel_admin')
    else:
        form = UserCreationForm()
    return render(request, 'novo_usuario.html', {'form': form})

@api_view(['GET']) # Define que a API aceita apenas requisições de leitura
@permission_classes([permissions.AllowAny]) # Define o acesso como público
def api_reparos_list(request):
    """
    Retorna a lista de todos os reparos efetuados no formato JSON.
    """
    reparos = Reparo.objects.all().order_by('-id') # Busca os dados no MySQL [cite: 89, 110]
    serializer = ReparoSerializer(reparos, many=True)
    return Response(serializer.data)