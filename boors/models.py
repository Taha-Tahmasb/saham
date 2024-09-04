from django.db import models
from django.contrib.auth.models import User


class Sandogh(models.Model):
    name = models.CharField(max_length=12)
    Gold = models.IntegerField()
    Silver = models.IntegerField()
    Copper = models.IntegerField()
    Oil = models.IntegerField()
    Steel = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Investment(models.Model):
    user = models.ForeignKey(User , on_delete=models.PROTECT ,related_name="user")
    invest = models.FloatField()
    sandogh = models.CharField(max_length=6)
    start_month = models.ForeignKey(Sandogh , on_delete=models.PROTECT ,related_name="start")
    finish_month = models.ForeignKey(Sandogh , on_delete=models.PROTECT ,related_name="finish")
    

    