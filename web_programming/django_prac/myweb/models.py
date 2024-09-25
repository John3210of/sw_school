from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=64,unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=64)

class Brand(models.Model):
    brand_name = models.CharField(max_length=128,unique=True)

class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=128)

class Car(models.Model):
    car_number = models.CharField(max_length=128)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel,on_delete=models.CASCADE)

class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=20)
    picture = models.CharField(max_length=20)