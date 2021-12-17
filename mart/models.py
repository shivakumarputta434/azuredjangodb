from django.db import models

class Emp(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField(default=0)

