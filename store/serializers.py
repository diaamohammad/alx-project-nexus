from rest_framework import serializers
from .models import (
    CustomUser,
    Category,
    Product,
)





class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = ['username','email','phone_number']



class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        
        model = CustomUser
        fields = ['id','email','username','password','phone_number']

    def create(self,validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number')
        )  
        return user
    


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name','created_at']




class ProductReadSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()

    class Meta:

        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'created_at']

    



class ProductWriteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ['id','name', 'description', 'price', 'stock', 'category']







        