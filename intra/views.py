from django.shortcuts import render
from .models import QnA



def faq(request):

    questions = QnA.objects.all()

    return render(request, 'intra/faq.html', locals())


def moncompte(request):
    nom = "Tommy Shelby"
    poste = "Chef de projet"
    return render(request, 'intra/moncompte.html', locals())
