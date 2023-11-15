from rest_framework import serializers
from delivery.models import Delivery
from message.models import Message
from location.models import Location
from orderItem.models import OrderItem
from product.models import Product
from Category.models import Category
from order.models import Order
from user.models import User, WasteCollector, WasteRecycler
from rest_framework import serializers
from user.models import User



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

# ORDER SERIaLIZERS


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

#  create order


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['quantity', 'status', 'total_price',
                  'total_amount_order', 'product']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

# PRODUCT


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "image_url",
                  "quantity", "company_name", "category", "created_at"]

# create product


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "image_url",
                  "quantity", "company_name", "category"]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = "__all__"

class WasteCollectorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    def validate(self, attrs):
        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if password == confirm_password:
            return attrs
        else:
            raise serializers.ValidationError(detail="Passwords do not match")

    class Meta:
        model = WasteCollector
        fields = ['id', 'username', 'first_name', 'last_name', 'email',
                  'phonenumber', 'location', 'password', 'confirm_password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        user = User.objects.create(
            is_wastecollector=True, email=validated_data['email'], username=validated_data['username'], password=password)
        wastecollector = WasteCollector.objects.create(
            user=user, **validated_data)
        return wastecollector


class WasteRecyclerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(
        write_only=True, style={'input_type': 'password'})

    def validate(self, attrs):
        password = attrs['password']
        confirm_password = attrs['confirm_password']
        if password == confirm_password:
            return attrs
        else:
            raise serializers.ValidationError(detail="Passwords do not match")

    class Meta:
        model = WasteRecycler
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email', 'phonenumber', 'password', 'confirm_password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        user = User.objects.create(
            is_wasterecycler=True, email=validated_data['email'], username=validated_data['username'], password=password)
        wasterecycler = WasteRecycler.objects.create(
            user=user, **validated_data)
        return wasterecycler
