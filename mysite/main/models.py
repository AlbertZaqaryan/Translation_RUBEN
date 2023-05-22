from django.db import models

# Create your models here.

class Person(models.Model):

    name = models.CharField('Person name', max_length=60)
    about = models.TextField('Person about')
    img = models.ImageField('Person image', upload_to='images')

    def __str__(self):
        return self.name