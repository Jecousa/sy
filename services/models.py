from django.db import models

#Original Model
class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    detail = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, default='')
    is_published = models.BooleanField(default=True)

#main Field that is displayed
def __str__(self):
    return self.title

#Graphql Query Test
class PlayMusic(models.Model):
    name = models.CharField(max_length=25)
    music_type = models.CharField(max_length=10)
    id = models.IntegerField

    def __str__(self):
        return self.name

class SearchMusic(models.Model):
    name = models.CharField(max_length=25)
    id = models.IntegerField

    def __str__(self):
        return self.name