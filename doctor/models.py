from django.db import models
from patient import Patient

class Doctor(models.Model):
    ID = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    id_patiend = models.ManyToManyField(Patient)
