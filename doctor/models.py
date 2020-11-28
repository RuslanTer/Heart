from django.db import models
from patient.models import Patient

class Doctor(models.Model):
    ID = models.CharField(max_length=254, null = True)
    name = models.CharField(max_length=254, null = True)


