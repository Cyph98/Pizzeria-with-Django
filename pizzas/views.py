from django.shortcuts import render
from .models import Pizza, Toppings


def index(request):
	"""The home page of Pizzas"""
	return render(request, 'pizzas/index.html')

def pizzas(request):
	"""Display all pizzas available"""
	pizzas = Pizza.objects.all()
	context = {'pizzas': pizzas}
	return render(request, 'pizzas/pizzas.html', context)

def toppings(request, pizza_id):
	"""Show a single pizza and all its toppings"""
	pizza = Pizza.objects.get(id=pizza_id)
	toppings = pizza.toppings_set.all()
	context = {'pizzas': pizzas, 'toppings': toppings}
	return render(request, 'pizzas/toppings.html', context)
