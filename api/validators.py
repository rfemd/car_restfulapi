from rest_framework import serializers

from .models import Car


def validate_brand(value):
    if not isinstance(value, str):
        raise serializers.ValidationError(f"{value} is not a string!")
    return value


def validate_model(value):
    if not isinstance(value, str):
        raise serializers.ValidationError(f"{value} is not a string!")
    return value


def validate_mileage(value):
    if not isinstance(value, float):
        raise serializers.ValidationError(f"{value} is not a float!")
    return value


def validate_price(value):
    if not isinstance(value, float):
        raise serializers.ValidationError(f"{value} is not a float!")
    return value
