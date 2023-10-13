from django.urls import path

from . import views

urlpatterns = [
    path("houses/", views.houses, name="houses"),
    path("houseimages/", views.houseimages, name="houseimages"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("house_detail/<str:house_id>/", views.house_detail, name="house_detail"),
    path("update_house/<str:house_id>/", views.update_house, name="update_house"),
    path("delete_house/<str:house_id>/", views.delete_house, name="delete_house"),
    
]
