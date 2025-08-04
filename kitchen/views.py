from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

from kitchen.models import DishType, Dish, Cook, Ingredient


def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_ingredients = Ingredient.objects.count()

    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_ingredients": num_ingredients,
    }
    return HttpResponse(f"<h1>{num_cooks}</h1>")

class DishTypeListView(ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"


class DishListView(ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"

class CookListView(ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"

class IngredientListView(ListView):
    model = Ingredient
    template_name = "kitchen/ingredient_list.html"