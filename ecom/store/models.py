from django.db import models
import datetime

# Create your models here.
#catagories
class Catagory(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="catagories"

#customers
class Customer(models.Model):

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=11)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)


    def __str__(self):
        return f'{self.first_name} + {self.last_name}'
    


#products

class Products(models.Model):

    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE,default=1)
    description=models.TextField(max_length=250,default='',null=True,blank=True)
    image=models.ImageField(upload_to='uploads/products/')
    
    #sales stuff

    is_sales=models.BooleanField(default=False)
    sales_price=models.DecimalField(default=0,decimal_places=2,max_digits=6)


    def __str__(self):
        return self.name

#order
class Order(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quntity=models.IntegerField(default=1)
    address=models.CharField(max_length=200,blank=True,default='')
    phone=models.CharField(max_length=11,blank=True,default='')
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.product


    
