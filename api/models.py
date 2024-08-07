from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

FUEL_CHOICES = (
    ("БЕНЗИН", "бензин"),
    ("ДИЗЕЛЬ", "дизель"),
    ("ЭЛЕКТРИЧЕСТВО", "электричество"),
    ("ГИБРИД", "гибрид"),
)

TRANSMISSION_CHOICES = (
    ("МЕХАНИЧЕСКАЯ", "механическая"),
    ("АВТОМАТИЧЕСКАЯ", "автоматическая"),
    ("ВАРИАТОР", "вариатор"),
    ("РОБОТ", "робот"),
)


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    fuel_type = models.CharField(max_length=13, choices=FUEL_CHOICES, default="БЕНЗИН")
    transmission = models.CharField(
        max_length=14, choices=TRANSMISSION_CHOICES, default="АВТОМАТИЧЕСКАЯ"
    )
    mileage = models.FloatField(null=True, blank=True, default=None)
    price = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.brand}-{self.model}"
