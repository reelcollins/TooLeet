from rest_framework import serializers
from .models import House, Wishlist, HouseImage



class HouseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImage
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    images = HouseImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = House
        fields = '__all__'
    


class WishlistSerializer(serializers.ModelSerializer):
    """
    Is there a way to show show the images related to the house too
    so that I make only one request to the wishlist to retrieve wishlist houses and their images
    """
    houses = HouseSerializer(many=True, read_only=True)
    images = HouseImageSerializer(many=True, read_only=True)
    class Meta:
        model = Wishlist
        fields = '__all__'

        depth = 1