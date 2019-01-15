from django.db import models

# Create your models here.



class Sample_Data(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField(null=True)
