from django.db import models

class Pizza(models.Model):
	"""Type of Pizza"""
	text = models.CharField(max_length=30)

	def __str__(self):
		"""Return a representation of the model"""
		return self.text


class Toppings(models.Model):
	"""Type of topping"""
	pizza = models.ManyToManyField(Pizza)
	topping = models.CharField(max_length=150)

	def __str__(self):
		"""Return a representation of topping"""
		return self.topping
