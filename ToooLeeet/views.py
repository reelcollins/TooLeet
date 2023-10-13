
from rest_framework import status
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)

from rest_framework.request import Request
from rest_framework.response import Response


"""
    # can I get a list by passing a list of ids???
    from django.shortcuts import get_list_or_404,
"""
from django.shortcuts import get_object_or_404

from .models import House, Wishlist, HouseImage
from .serializers import HouseSerializer, WishlistSerializer, HouseImageSerializer

# CRUD FUNCTIONALITY ...DON'T JUST COPY PASTE SHIT & DON'T GUESS



# Houses
@api_view(http_method_names=["GET", "POST"])
# only user signed as Landlord can make a POST or PUT
@permission_classes([AllowAny])
def houses(request: Request):
    houses = House.objects.all()

    if request.method == 'POST':
        data = request.data

        serializer = HouseSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "House Added",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = HouseSerializer(instance=houses, many=True)

    response = {"message": "Houses",
                "data": serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)




# HouseImages
@api_view(http_method_names=["GET", "POST"])
# Landlord permissions
@permission_classes([AllowAny])
def houseimages(request: Request):
    """
        Have the images as links so that I can load them easily
        Be able to retrieve houses' images by house id
    
    """

    houseimages = HouseImage.objects.all()

    if request.method == 'POST':
        data = request.data

        serializer = HouseImageSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "House Image Added",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = HouseImageSerializer(instance=houseimages, many=True)

    response = {"message": "House images",
                "data": serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)





# Wishlists
@api_view(http_method_names=["GET", "POST"])
# permission to the user signed in only
@permission_classes([AllowAny])
def wishlist(request: Request):
    wishlist = Wishlist.objects.all()

    if request.method == 'POST':
        data = request.data

        serializer = WishlistSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "House Added To Wishlist",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = WishlistSerializer(instance=wishlist, many=True)

    response = {"message": "wishlist",
                "data": serializer.data}
    return Response(data=response, status=status.HTTP_200_OK)



# I think the best way to do this is use the id's of the houses in wishlist
# to filter the houses in the wishlist screen rather than starting to work with images again
# when the user deletes the house from the wishlist only the id is deleted




# Wishlist_list
@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
# the house id is not an integer
def house_detail(request: Request, house_id: int):
    house = get_object_or_404(House, pk=house_id)

    serializer = HouseSerializer(instance=house)

    response = {"message": "post", "data": serializer.data}

    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["PUT"])
@permission_classes([AllowAny])
def update_house(request: Request, house_id: int):
    """
        pass the house_id: house_id is not an integer
    """

    house = get_object_or_404(House, pk=house_id)

    data = request.data

    serializer = HouseSerializer(instance=house, data=data)

    if serializer.is_valid():
        serializer.save()

        response = {
            "message": "House details updated successfully"
        }

        return Response(data=response, status=status.HTTP_200_OK)
    
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(http_method_names=["DELETE"])
@permission_classes([AllowAny])
def delete_house(request: Request, house_id: str):
    """
        pass the house_id: house_id is not an integer
    """

    house = get_object_or_404(House, pk=house_id)

    house.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
