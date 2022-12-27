from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from intobi_app.core.models import Menu, Restaurant

User = get_user_model()


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
        read_only_fields = ("created", "updated")


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
        read_only_fields = ("created", "updated", "rating")
