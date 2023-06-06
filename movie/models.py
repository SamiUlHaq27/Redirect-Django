from django.db import models

# Create your models here.

class Link(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    movie_id = models.CharField(max_length=100)
    target_link = models.TextField()