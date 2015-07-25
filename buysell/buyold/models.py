from django.db import models
from django.utils import timezone
import datetime


from django.db import models


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    house_no = models.IntegerField(blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    town = models.TextField(blank=True, null=True)
    def __str__(self):
    	return str(self.house_no)
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)





class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    items_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('User', blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)

    def __str__(self):
    	return self.cart_id

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    enno = models.IntegerField(blank=True, null=True)
    email_id = models.TextField(blank=True, null=True)
    mob = models.IntegerField(blank=True, null=True)
    address = models.ForeignKey(Address, blank=True, null=True)

    def __unicode__(self):
    	return str(self.name)
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price =models.IntegerField(blank=False, null=True)
    coverphoto = models.ImageField()
    conditions = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    categories=models.ManyToManyField(Category,blank=True, null=True)

    def __str__(self):
        return str(self.name)
class Productimage(models.Model):
    item = models.ForeignKey(Item, blank=True, null=True)
    image = models.ImageField()
class Cartitems(models.Model):
    cartitems_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True)
    item = models.ForeignKey(Item, blank=True, null=True)
    def __str__(self):
        return 'tt'