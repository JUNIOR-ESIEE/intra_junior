from django.db import models
from django.utils import timezone


class Eleve(models.Model):
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    naissance = models.DateTimeField()

    mail_edu = models.CharField(max_length=40)
    mail_junior =  models.CharField(default=None,max_length=40)

    promo = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date d'inscription")

    def save(self, *args, **kwargs):
        if self.mail_junior:
            self.mail_junior = self.mail_edu.split('@')[0]+"@junioresiee.com"
        else:
            self.mail_junior = '.'.join([self.nom,self.prenom])+"@junioresiee.com"
        super(Eleve, self).save(*args, **kwargs)
