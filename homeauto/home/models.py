from django.db import models

# Create your models here.
class Leds(models.Model):
    device_id = models.TextField(max_length=10,primary_key=True)
    led1_status   = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    led2_status   = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    led3_status   = models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)