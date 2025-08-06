"""
URL configuration for restaurant_kitchen_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from kitchen.views import (
    DishTypeListView,
    CookListView,
    DishListView,
    IngredientListView,
    index,
    DishTypeDetailView,
    DishDetailView,
    CookDetailView,
    IngredientDetailView,

)

urlpatterns = [
    path("", index, name="index"),
    path("dishtypes/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("dishtypes/<int:pk>", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("ingredients/<int:pk>", IngredientDetailView.as_view(), name="ingredient-detail"),
]


app_name = "kitchen"
