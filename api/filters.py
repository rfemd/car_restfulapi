from django_filters import rest_framework as filters
from django_filters.widgets import RangeWidget

from .models import Car


class CarFilterSet(filters.FilterSet):
    brand = filters.CharFilter(field_name="brand", lookup_expr="contains")
    model = filters.CharFilter(field_name="model", lookup_expr="contains")
    fuel_type = filters.CharFilter(field_name="fuel_type", lookup_expr="contains")
    transmission = filters.CharFilter(field_name="transmission", lookup_expr="contains")

    mileage_max = filters.NumberFilter(field_name="mileage", lookup_expr="gt")
    mileage_min = filters.NumberFilter(field_name="mileage", lookup_expr="lt")

    price_max = filters.NumberFilter(field_name="price", lookup_expr="gt")
    price_min = filters.NumberFilter(field_name="price", lookup_expr="lt")

    year = filters.NumberFilter(field_name="year")

    class Meta:
        model = Car
        fields = [
            "brand",
            "model",
            "year",
            "fuel_type",
            "transmission",
        ]
