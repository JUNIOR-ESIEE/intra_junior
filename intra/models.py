from django.db import models
from django.utils import timezone



class QnA(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "QnA"
        verbose_name_plural = "QnA"
