from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView

from .forms import CookAdminCreationForm
from .models import *

from kitchen.models import DishType, Dish, Cook, Ingredient


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_ingredients = Ingredient.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_ingredients": num_ingredients,
        "num_visits": num_visits,  # This was missing
    }
    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 4


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"
    context_object_name = "dish_list"
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 4


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"
    context_object_name = "cook_list"
    paginate_by = 4


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    template_name = "kitchen/ingredient_list.html"
    context_object_name = "ingredient_list"
    paginate_by = 4


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "kitchen/dish_type_detail.html"
    context_object_name = "dish_type"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"
    context_object_name = "dish"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"
    context_object_name = "cook"


class IngredientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ingredient
    template_name = "kitchen/ingredient_detail.html"
    context_object_name = "ingredient"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"
    fields = "__all__"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_form.html"
    fields = "__all__"

class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    template_name = "kitchen/cook_form.html"
    form_class = CookAdminCreationForm


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/ingredient_form.html"
    fields = "__all__"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_form.html"



class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    fields = "__all__"
    template_name = "kitchen/cook_form.html"



class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/ingredient_form.html"



class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "kitchen/dish_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-list")



class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "kitchen/cook_confirm_delete.html"
    success_url = reverse_lazy("kitchen:cook-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    template_name = "kitchen/ingredient_confirm_delete.html"
    success_url = reverse_lazy("kitchen:ingredient-list")


class CookAdminCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookAdminCreationForm

