from django.db import models
from location_field.models.plain import PlainLocationField
# Create your models here.
class Chargering_Session(models.Model):
    customer_name=models.CharField(max_length=80)
    customer_mobile_no=models.IntegerField()
    customer_id=models.IntegerField(unique=True,null=False)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    start_date_time=models.DateTimeField()
    end_date_time=models.DateTimeField()
    total_time=models.CharField(max_length=100)
    consume_power=models.CharField(max_length=200)



    
