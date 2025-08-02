from django.test import TestCase
from kitchen.models import DishType, Cook, Dish, Ingredient


class TestModel(TestCase):
    def test_dishtype(self):
        dishtype = DishType.objects.create(name="Dessert")
        self.assertEqual(str(dishtype), "Dessert")
        self.assertEqual(DishType.objects.count(), 1)

    def test_cook(self):
        cook = Cook.objects.create(
            username="chef_bob",
            first_name="Bob",
            last_name="Smith",
            years_of_experience=5
        )
        self.assertEqual(cook.username, "chef_bob")
        self.assertEqual(Cook.objects.count(), 1)

    def test_dish(self):
        dish_type = DishType.objects.create(name="Main Course")
        dish = Dish.objects.create(
            name="Burger",
            dish_type=dish_type,
            description="Tasty burger",
            price=8.99
        )
        self.assertEqual(dish.name, "Burger")
        self.assertEqual(Dish.objects.count(), 1)

    def test_ingredient(self):
        dish_type = DishType.objects.create(name="Dessert")
        dish = Dish.objects.create(
            name="Cake",
            dish_type=dish_type,
            description="Sweet cake",
            price=7.99
        )
        ingredient = Ingredient.objects.create(
            name="Flour",
            dish=dish
        )
        self.assertEqual(ingredient.name, "Flour")
        self.assertEqual(Ingredient.objects.count(), 1)
