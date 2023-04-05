from .views import *
from django.urls import path

urlpatterns = [
    path('image_upload', hotel_image_view, name='image_upload'),
    path('hotel_images', display_hotel_images, name = 'hotel_images'),
    path('success', success, name='success'),
    path('', home, name='home'),
    path('register', register, name="register"),
    path('login', login, name="login"),
    path('feeds', feeds, name = 'feeds'),
     path('create_post/', create_post, name='create_post'),
     path("logout",logout_request, name= "logout"),
     path("comment",create_comment, name= "comment"),


]