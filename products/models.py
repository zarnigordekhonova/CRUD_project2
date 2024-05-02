from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    model = models.CharField(max_length=150)
    make = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='conf/', blank=True, null=True)


    def __str__(self):
        return f'{self.model} {self.make}'


