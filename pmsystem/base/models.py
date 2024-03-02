from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


# add a name variable that will carry apartment, bungalow
class House(models.Model):
	topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
	name = models.CharField(max_length= 200)
	tenant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	bedroom = models.IntegerField()
	description = models.TextField()
	price = models.DecimalField(max_digits=1000, decimal_places=2)
	place = models.CharField(max_length=200)
	image = models.ImageField(blank=True, null=True)
	booked = models.BooleanField()
	sold = models.BooleanField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-updated', '-created']
			

	def __str__(self):
		return self.name
