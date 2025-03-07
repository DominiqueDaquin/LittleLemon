from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=255,db_index=True)
class MenuItem(models.Model):
    title=models.CharField(max_length=255,db_index=True)
    price=models.DecimalField(max_digits=6,decimal_places=2,db_index=True)
    featured=models.BooleanField(db_index=True)
    category=models.ForeignKey(Category, on_delete=models.PROTECT, related_name='menu_items')

class Booking(models.Model):
    user=models.Foreignkey(User,on_delete=models.CASCADE)
    menu=models.ForeignKey(MenuItem,on_delete=models.PROTECT)
