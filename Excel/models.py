from django.db import models

# Create your models here.
class Documento(models.Model):
    file = models.FileField(upload_to='', null=False)