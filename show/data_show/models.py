from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE



# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255 , blank=True, null=True, default='qq')
    catchPhrase = models.CharField(max_length=255 , blank=True, null=True, default='qq')
    bs = models.CharField(max_length=255 , blank=True, null=True, default='qq')


#как я понял PointField в версии более новой
class Geo(models.Model):
    lat = models.CharField(max_length=255 , blank=True, null=True, default="w ")
    lng = models.CharField(max_length=255 , blank=True, null=True, default="w ")

class Address(models.Model):
    street = models.CharField(max_length=255 , blank=True, null=True, default="w")
    suite = models.CharField(max_length=255 , blank=True, null=True, default="w")
    city = models.CharField(max_length=255 , blank=True, null=True, default="w")
    zipcode = models.CharField(max_length=255 , blank=True, null=True, default="w")
    geo = models.ForeignKey(Geo, on_delete=CASCADE, blank=True, null=True )


    def __str__(self):
        return self.street


class User(AbstractUser):
    
    
    name = models.CharField(max_length=255 , blank=True, null=True, default="w")
    username = models.CharField(max_length=255 , blank=True, null=True, default="w", unique=True)
    address = models.ForeignKey(Address, on_delete=CASCADE, blank=True, null=True)
    phone =  models.CharField(max_length=255 , blank=True, null=True, default="w")
    website = models.CharField(max_length=255 , blank=True, null=True, default="w")
    company = models.ForeignKey(Company, on_delete=CASCADE, blank=True, null=True)



    


class Post(models.Model):
    userId = models.PositiveIntegerField()
    title = models.CharField(max_length=255 , blank=True, null=True, default="w")
    body = models.TextField(blank=True, null=True, default="w")







