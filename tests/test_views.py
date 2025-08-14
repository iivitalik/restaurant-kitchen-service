from django.test import TestCase, Client
from django.urls import reverse
from kitchen.models import DishType, Dish, Cook, Ingredient


class PublicTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required_for_list_views(self):
        urls = [
            reverse("kitchen:index"),
            reverse("kitchen:dish-type-list"),
            reverse("kitchen:dish-list"),
            reverse("kitchen:cook-list"),
            reverse("kitchen:ingredient-list"),
        ]
        for url in urls:
            res = self.client.get(url)
            self.assertNotEqual(res.status_code, 200)


class PrivateTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = Cook.objects.create_user(
            username="user1", password="pass12345"
        )
        self.client.login(username="user1", password="pass12345")

    def test_index_view_authenticated(self):
        res = self.client.get(reverse("kitchen:index"))
        self.assertEqual(res.status_code, 200)
        self.assertIn("num_dishes", res.context)

    def test_list_views_authenticated(self):
        dish_type = DishType.objects.create(name="T")
        dish = Dish.objects.create(name="D", dish_type=dish_type, price=10)
        Ingredient.objects.create(name="I", dish=dish)
        Cook.objects.create_user(username="c2", password="pass12345")

        urls = [
            ("kitchen:dish-type-list", "dish_type_list"),
            ("kitchen:dish-list", "dish_list"),
            ("kitchen:cook-list", "cook_list"),
            ("kitchen:ingredient-list", "ingredient_list"),
        ]
        for url_name, context_name in urls:
            res = self.client.get(reverse(url_name))
            self.assertEqual(res.status_code, 200)
            self.assertIn(context_name, res.context)

