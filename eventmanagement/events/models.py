from django.db import models

# Create your models here.
class Events(models.Model):
    EventName=models.CharField()
    EventDate=models.DateField()
    Location=models.CharField()
    Category=models.CharField()
    
    def __str__(self):
        return self.EventName