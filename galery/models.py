from django.db import models
from datetime import datetime
from PIL import *

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALAXIA", "Galaxia"),
        ("PLANETA", "Planeta")
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=100, null=False, blank=False)
    category= models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    published = models.BooleanField(default=False)
    date_photo = models.DateTimeField(default=datetime.now, blank=False)


    def __str__(self):
       return self.name
    

