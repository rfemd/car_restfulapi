from rest_framework import serializers

from .models import Car
from .validators import (validate_brand, validate_mileage, validate_model,
                         validate_price)


class CarSerializer(serializers.ModelSerializer):

    brand = serializers.CharField(validators=[validate_brand])
    model = serializers.CharField(validators=[validate_model])
    mileage = serializers.FloatField(validators=[validate_mileage])
    price = serializers.FloatField(validators=[validate_price])

    class Meta:
        model = Car
        fields = "__all__"
