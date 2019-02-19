from django import forms

class EleveForm(forms.Form):
    nom = forms.CharField(max_length=15, label="Nom", required=True)
    prenom = forms.CharField(max_length=15, label="Prénom", required=True)
    naissance = forms.DateTimeField(label="Date de naissance", required=True)

    mail_edu = forms.EmailField(max_length=40, label="Adresse email ESIEE")
    promo = forms.CharField(max_length=10, label="Promo")
