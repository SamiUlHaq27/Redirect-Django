from django.db import models

# Create your models here.

class Article(models.Model):
    categories = [
        ("Insurance", "Insurance"),
        ("Trading", "Trading"),
        ("Softwares", "Softwares")
          ]
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="articles")
    description = models.TextField()
    category = models.CharField(choices=categories, max_length=100)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

class Author(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="authors")
    dob = models.DateField()
    education = models.TextField()


