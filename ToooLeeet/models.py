from django.db import models
import uuid

from pickle import TRUE

from django.contrib.auth import get_user_model

User = get_user_model()


class HouseImage(models.Model):
    #image_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    house = models.ForeignKey('House', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to = "img", blank = True, null=True, default="media\GHOSTS-01.png")


# Create your models here.
class House(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    #owner = models.ForeignKey('Landlord', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    apartment = models.CharField(max_length=200)
    floor = models.PositiveIntegerField()
    housenumber = models.PositiveIntegerField()
    contact = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return self.apartment
    

class Wishlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # User ---> Signed In customer
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='houses')
    

    def __str__(self):
        return f'Wishlist of {self.customer.username}'