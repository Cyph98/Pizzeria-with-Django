"""Urls for pizzas"""
from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
	#homepage
	path('', views.index, name='index'),

	#page that shows all pizzas
	path('pizzas/', views.pizzas, name='pizzas'),

	#page that displays toppings for each pizza
	path('toppings/<int:pizza_id>/', views.toppings, name='toppings'), # the topping for this pizza id
	]