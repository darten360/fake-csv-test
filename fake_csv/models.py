from django.contrib.auth.models import AbstractUser
from django.db import models
from fake_csv.functions import *


class User(AbstractUser):

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}, {self.first_name} {self.last_name}"


class Schema(models.Model):
    COMMA = ","
    POINT = "."
    SEMICOLON = ";"
    HORIZONTAL_TAB = r"\t"
    COLON = ":"

    SEPARATOR_CHOICES = [
        (COMMA, "Comma (,)"),
        (POINT, "Point (.)"),
        (SEMICOLON, "Semicolon (;)"),
        (HORIZONTAL_TAB, r"Horizontal tab (\t)"),
        (COLON, "Colon (:)")
    ]

    DOUBLE_QUOTES = '""'
    SINGLE_QUOTES = "''"

    QUOTES_CHOICES = [
        (DOUBLE_QUOTES, 'Double quotes (")'),
        (SINGLE_QUOTES, "Single quotes (')")
    ]

    name = models.CharField(max_length=60)
    separator = models.CharField(max_length=15, choices=SEPARATOR_CHOICES, default=COMMA)
    string = models.CharField(max_length=10, choices=QUOTES_CHOICES, default=DOUBLE_QUOTES)
    modified = models.DateField(auto_now_add=True)
    full_name = models.CharField(max_length=255, default=random_fullname)
    phone = models.CharField(max_length=14, default=random_phone)
    integer = models.IntegerField(default=random_int)
    domain = models.CharField(max_length=16, default=random_domain)
    email = models.EmailField(default=random_email)
    company = models.CharField(max_length=30, default=random_company)
    text = models.TextField(default=random_text)
    address = models.CharField(max_length=255, default=random_address)
    date = models.DateField(default=random_date)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.name}"

