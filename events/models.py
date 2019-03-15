from django.db import models
from datetime import datetime

class Event(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=200)
    detail = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title