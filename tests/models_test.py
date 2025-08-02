from django.test import TestCase

from kitchen.models import DishType


class ModelTest(TestCase):
    def test_dishtype(self):
        dishtype = DishType.objects.create(name = "Cookies")
        self.assertEqual(str(dishtype.name), "Cookies")