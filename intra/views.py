from django.shortcuts import render
from .forms import EleveForm
from .models import QnA

def rejoindre(request):
    form = EleveForm(request.POST or None)
    creation = False

    if form.is_valid():
        nom = form.cleaned_data['nom']
        prenom = form.cleaned_data['prenom']
        naissance = form.cleaned_data['naissance']
        mail_edu = form.cleaned_data['mail_edu']
        promo = form.cleaned_data['promo']

        creation = True

    return render(request, 'intra/rejoindre.html', locals())


def faq(request):
    
    questions = QnA.objects.all()

    return render(request, 'intra/faq.html', locals())


def moncompte(request):
    nom = "Tommy Shelby"
    poste = "Chef de projet"
    return render(request, 'intra/moncompte.html', locals())
