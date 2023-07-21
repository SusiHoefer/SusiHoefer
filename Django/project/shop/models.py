from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    kunde = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    orderdate = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False, null=True, blank=True)
    order_id = models.CharField(max_length=200, null=200)
    
    def __str__(self):
        return str(self.id)

class OrderedArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, blank =True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article.name
    
class Adress(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    adress = models.CharField(max_length=200, null=200)
    zip = models.CharField(max_length=200, null=200)
    city = models.CharField(max_length=200, null=200)
    country = models.CharField(max_length=200, null=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adress