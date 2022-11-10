from django.db import models
from django.utils.translation import gettext_lazy as _

class Mood(models.Model):

    class FeelingChoices(models.TextChoices):
        OTIMISMO = 'OT', _("Otimismo")
        CONFIANTE = "CF", _("Confiante")
        FELICIDADE = "FL", _("Felicidade")
        GRATITUDE = "GR", _("Gratitude")
        INDIFERENCA = "ID", _("Indiferenca")
        CETICO = "CE", _("Cetico")
        DEPRESSAO = "DE", _("Depressao")
        ANSIEDADE = "AN", _("Ansiedade")
        DESANIMO = "DN", _("Desanimo")

    class MoodChoices(models.TextChoices):
        BEM = "BEM", _("Bem")
        NEUTRO = "NEU", _("Neutro")
        MAL = "MAL", _("Mal")

    name = models.CharField(max_length=255, choices=MoodChoices.choices)
    feeling = models.CharField(max_length=255, choices=FeelingChoices.choices)


class Comments(models.Model):
    text = models.TextField()
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)

