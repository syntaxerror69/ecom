from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField()
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    brand = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Register(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=10, null=True, blank=True)

class Login(models.Model):
    email = models.EmailField(max_length=200, null=True, blank=True)
    password =models.CharField(max_length=20,blank=True, null=True) 