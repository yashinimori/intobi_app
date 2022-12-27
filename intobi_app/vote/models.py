from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Vote(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    menu = models.ForeignKey("core.Menu", on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=3, validators=[MaxValueValidator(3), MinValueValidator(1)]
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
