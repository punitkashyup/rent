from sqlite3 import Date
from django.db import models
from django import forms

# MONTH_CHOICES =(
#     ("1", "January"),
#     ("2", "February"),
#     ("3", "March"),
#     ("4", "April"),
#     ("5", "May"),
#     ("6", "June"),
#     ("7", "July"),
#     ("8", "August"),
#     ("9", "September"),
#     ("10", "October"),
#     ("11", "November"),
#     ("12", "Decemeber"),
# )


class user(models.Model):
    id=models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20, unique=True)
    user_email = models.EmailField(max_length=200)
    user_password = models.CharField(max_length=200)


class rent(models.Model):
    id=models.IntegerField(primary_key=True)
    rent_date = models.DateField(auto_now_add=True)
    rentmonth = models.CharField(max_length=30)
    # rentmonth = models.CharField(max_length=2, choices=MONTH_CHOICES)
    rent_amount = models.FloatField()
    bijli_bill = models.FloatField()
    other_amount = models.FloatField(blank=True)
    other_commnet = models.CharField(blank=True, max_length=200)