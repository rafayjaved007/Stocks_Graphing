from django.db import models


class Stocks(models.Model):
    us_500 = models.FloatField(max_length=30)
    us_tech_100 = models.FloatField(max_length=30)
    timestamp = models.DateTimeField(primary_key=True, auto_now_add=True)
