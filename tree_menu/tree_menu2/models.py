from django.db import models

# Create your models here


SEX = [
    ('m', 'male'),
    ('f', 'female')

]

class Users(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX)
    city = models.CharField(max_length=100, default='Minsk')

    def __str__(self):
        return self.name