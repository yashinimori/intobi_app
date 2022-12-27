from datetime import date

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.settings import api_settings

from intobi_app.vote.models import Vote

User = get_user_model()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
        read_only_fields = ("created", "updated")


class VoteNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
        read_only_fields = ("created", "updated")

    def validate(self, attrs):
        if Vote.objects.filter(
            created__day=date.today().day, user=attrs.get("user")
        ).exists():
            message = "U already voted today"
            raise ValidationError(
                {api_settings.NON_FIELD_ERRORS_KEY: message}, code="already_voted"
            )

        if attrs.get("user").restaurant != attrs.get("menu").restaurant:
            message = "Unknown Menu"
            raise ValidationError(
                {api_settings.NON_FIELD_ERRORS_KEY: message}, code="unknown_menu"
            )
        return attrs

    def create(self, validated_data):
        if Vote.objects.filter(
            created__day=date.today().day,
            user=validated_data.get("user"),
            menu=validated_data.get("menu"),
        ).exists():
            message = "Wrong menu value"
            raise ValidationError(message)
        print(validated_data)
        return super().create(validated_data)


class VoteOldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
        read_only_fields = ("rating", "created", "updated")

    def validate(self, attrs):
        if Vote.objects.filter(
            created__day=date.today().day, user=attrs.get("user")
        ).exists():
            message = "U already voted today"
            raise ValidationError(
                {api_settings.NON_FIELD_ERRORS_KEY: message}, code="already_voted"
            )
        if attrs.get("user").restaurant != attrs.get("menu").restaurant:
            message = "Unknown Menu"
            raise ValidationError(
                {api_settings.NON_FIELD_ERRORS_KEY: message}, code="unknown_menu"
            )
        return attrs
