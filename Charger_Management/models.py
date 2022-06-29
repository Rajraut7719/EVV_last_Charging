from distutils.command.upload import upload
from django.db import models
from location_field.models.plain import PlainLocationField
# Create your models here.
class Charger_Management(models.Model):
    charger_name=models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    charger_id=models.IntegerField(unique=True,null=False)
    charger_photo=models.ImageField(upload_to='Charger')
    on_off=models.BooleanField(default=False)

