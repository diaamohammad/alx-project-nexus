from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    email = models.EmailField(unique=True,blank=False)
    phone_number = models.CharField(max_length=11,blank=True,null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    

class Category(models.Model):

    name = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name



class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category,related_name='products',on_delete=models.PROTECT)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        indexes=[
            models.Index(fields=['price']),
            models.Index(fields=['name']),

        ]
    
    def __str__(self):

        return self.name

