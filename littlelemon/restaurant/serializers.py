from rest_framework.serializers import ModelSerializer
from .models import MenuItem,Category
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields=['id','title','slug']

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model=MenuItem
        fields=['id','category','category_id','title','price','featured']