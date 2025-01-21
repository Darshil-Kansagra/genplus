from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class user_master(models.Model):
    username=models.CharField(('username'),max_length=50,primary_key=True)
    password=models.CharField(max_length=50,null=False)
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=254,unique=True,null=False)
    phone_no=models.IntegerField(null=False)
    address=models.CharField(max_length=50,null=True)
    postalcode=models.IntegerField(null=True)
    city=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.username


class category_master(models.Model):
    cat_id=models.IntegerField(('cat_id'),null=False,primary_key=True)
    cat_name=models.CharField(max_length=350)

    def __str__(self):
        return self.cat_name 
    
class component_master(models.Model):
    con_id=models.ForeignKey("category_master", verbose_name=("con_id"), on_delete=models.CASCADE)
    con_name=models.CharField(max_length=350)
    con_price=models.IntegerField(null=False)
    mp_date=models.DateField(auto_now_add=True)
    exp_date=models.DateField(auto_now_add=False)

    def __str__(self):
        return self.con_name 

    

class order_master(models.Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    order_no=models.AutoField(primary_key=True)
    order_name=models.CharField(max_length=50)
    order_price=models.IntegerField(null=False)
    order_date=models.DateField(auto_now_add=True)
    order_time=models.TimeField(auto_now_add=True)
    city=models.CharField(max_length=50)
    paymethod=models.CharField(max_length=50,default="COD")
    

    def __str__(self):
        return self.order_name

class city_master(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name    

class card_payment(models.Model):
    CardNumber=models.IntegerField()    
    CardHolder=models.CharField(max_length=16)
    expiresmonth=models.IntegerField()
    expiresyear=models.IntegerField()
    cvv=models.IntegerField()
    balance=models.PositiveIntegerField()

    def __str__(self):
        return self.CardHolder

class contactfrom(models.Model):
    username=models.CharField(max_length=50)    
    name=models.CharField(max_length=16)
    message=models.TextField()
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class games(models.Model):
    gameimg=models.ImageField(upload_to='images/')
    gamename=models.CharField(('gamename'),max_length=50,primary_key=True)

    def __str__(self):
        return self.gamename

class gamespc(models.Model):
    gamename=models.ForeignKey("games", verbose_name=("gamename"), on_delete=models.CASCADE)
    Cabinets=models.CharField(max_length=50)
    Motherboard=models.CharField(max_length=50)
    Processor=models.CharField(max_length=50)
    GraphicCard=models.CharField(max_length=50)
    SMPS=models.CharField(max_length=50)
    RAM=models.CharField(max_length=50)
    SSD=models.CharField(max_length=50)
    HDD=models.CharField(max_length=50)
    price=models.IntegerField(null=False)
    ProcessorBrand=models.CharField(max_length=50,choices=[('Intel','Intel'), ('AMD','AMD')])


