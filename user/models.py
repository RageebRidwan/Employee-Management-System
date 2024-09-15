from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError("Please enter numeric value.")


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, validators=[validate_phone_number])
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
