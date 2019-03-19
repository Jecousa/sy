from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    detail = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, default='')
    is_published = models.BooleanField(default=True)

#main Field that is displayed
def __str__(self):
    return self.title