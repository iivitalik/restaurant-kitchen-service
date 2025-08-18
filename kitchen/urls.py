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
    DishTypeCreateView,
    DishCreateView,
    CookCreateView,
    IngredientCreateView,
    DishTypeUpdateView,
    DishUpdateView,
    CookUpdateView,
    IngredientUpdateView,
    DishTypeDeleteView,
    DishDeleteView,
    CookDeleteView,
    IngredientDeleteView,
    CookAdminCreateView,

)

urlpatterns = [
    path("", index, name="index"),
    path("dishtypes/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("dishtypes/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("ingredients/<int:pk>/", IngredientDetailView.as_view(), name="ingredient-detail"),  # Added slash here
    path("dishtypes/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("dishtypes/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient-update"),
    path("dishtypes/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient-delete"),
    path("cookadmin/create/", CookAdminCreateView.as_view, name="cookadmin-create"),
]


app_name = "kitchen"
