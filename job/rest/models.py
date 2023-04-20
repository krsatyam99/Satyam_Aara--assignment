from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     mobile = models.CharField(max_length=15, blank=True)
# from django.db import models

class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)


    name = models.CharField(max_length=100)
    About=models.CharField(max_length=200,null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    address=  models.CharField(max_length=100)
    owner_name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    Email=models.EmailField()
    




    def __str__(self):
        return self.name



class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.author}'s review of {self.shop.shop_id}"