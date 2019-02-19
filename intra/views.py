from django.shortcuts import render
from .forms import EleveForm

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
    questions = [
    ("Pourquoi la junior ?", "Parce que c'est bien."),
    ("On a quel âge ?", "36 ans."),
    ("Question nulle ?", "Réponse nulle."),
    ("Lorem ipsum ?", "Dolor sit amet, consectetur adipiscing elit, \
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad \
    minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea \
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit \
    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat \
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
    ]

    questions =  3*questions

    return render(request, 'intra/faq.html', locals())


def moncompte(request):
    nom = "Tommy Shelby"
    poste = "Chef de projet"
    return render(request, 'intra/moncompte.html', locals())
