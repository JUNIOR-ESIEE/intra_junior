from django import forms
from .models import Eleve

class EleveForm(forms.ModelForm):


    class Meta:
        model = Eleve
        fields=('nom','prenom','naissance','mail_edu','promo')

    def clean_mail_edu(self):
        mail_edu = self.cleaned_data['mail_edu']
        if("@" not in mail_edu or "edu.esiee.fr" not in mail_edu):
            raise forms.ValidationError("Not a correct email")

        return mail_edu
