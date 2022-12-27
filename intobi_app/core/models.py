from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Menu(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="pdf/menu/%Y/%m/%d")
    restaurant = models.ForeignKey(
        "core.Restaurant", blank=True, null=True, on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


"""
Optional
Instead of using pdf uploading

class Dish(models.Model):
    class DishCategory:
        SOUP = "SOUP"
        DESSERT = "DESSERT"
        HOT_DISH = "HOT_DISH"
        COLD_DISH = "COLD_DISH"
        SIDE = "SIDE"
        DRINK = "DRINK"
        ALCOHOL_DRINK = "ALCOHOL_DRINK"

        CHOICES = (
            (SOUP, "SOUP"),
            (DESSERT, "DESSERT"),
            (HOT_DISH, "HOT_DISH"),
            (COLD_DISH, "COLD_DISH"),
            (SIDE, "SIDE"),
            (DRINK, "DRINK"),
            (ALCOHOL_DRINK, "ALCOHOL_DRINK")
        )

    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey("core.Menu", blank=True, null=True)
    category = models.CharField(max_length=20, choices=DishCategory.CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Component(models.Model):
    name = models.CharField(max_length=255)
    dish = models.ManyToManyField("core.Dish", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
"""
