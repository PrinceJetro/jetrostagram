# forms.py
from django import forms
from .models import *
 
 
class HotelForm(forms.ModelForm):
 
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','post_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [ 'content',]