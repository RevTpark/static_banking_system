from django.db import models
from django.utils import timezone

# Create your models here.

class LogTracker(models.Model):
    isFrom = models.CharField(max_length=100)
    isTo = models.CharField(max_length=100)
    ofAmount = models.IntegerField()
    atTime = models.DateTimeField(default=timezone.now)
    isSuccess = models.BooleanField(default=True)
