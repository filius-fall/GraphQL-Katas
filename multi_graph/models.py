from django.db import models

# Create your models here.



class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name




class Article(models.Model):
    title = models.CharField(max_length=200)
    published_year = models.CharField(max_length=5)
    author = models.ForeignKey(Person,on_delete=models.CASCADE)

    def __str__(self):
        return self.title