from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name