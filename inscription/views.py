from django.shortcuts import render
from .forms import EleveForm
from .models import Eleve


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
        form.save()

    return render(request, 'inscription/rejoindre.html', locals())
