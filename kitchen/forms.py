from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from .models import Cook


class CookAdminCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience",)

        def clean_username(self):
            years_of_experience = self.cleaned_data["years_of_experience"]
            if years_of_experience <= 0:
                raise ValidationError("Please enter a positive integer")
            return years_of_experience


class DishSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(attrs={"placeholder": "Search by name"})
                           )