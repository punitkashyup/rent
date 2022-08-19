from sqlite3 import Date
from django.db import models
from django import forms
from django.contrib.auth.models import User




class rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # id=models.IntegerField(primary_key=True)
    rent_date = models.DateField(auto_now_add=True)
    rentmonth = models.CharField(max_length=30)
    rent_amount = models.FloatField()
    bijli_bill = models.FloatField()
    other_amount = models.FloatField(blank=True)
    other_commnet = models.CharField(blank=True, max_length=200)