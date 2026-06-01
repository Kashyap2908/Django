from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField()
    release_date=models.DateField()
    rating=models.FloatField()
    def __str__(self):
        return self.name