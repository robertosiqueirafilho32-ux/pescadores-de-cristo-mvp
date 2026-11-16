
from django.shortcuts import render
from .models import Beneficiario


def home(request):
    total_beneficiarios = Beneficiario.objects.count()
    beneficiarios_ativos = Beneficiario.objects.filter(ativo=True).count()
    beneficiarios_inativos = Beneficiario.objects.filter(ativo=False).count()

    context = {
        'total_beneficiarios': total_beneficiarios,
        'beneficiarios_ativos': beneficiarios_ativos,
        'beneficiarios_inativos': beneficiarios_inativos,
    }

    return render(request, 'beneficiarios/home.html', context)
