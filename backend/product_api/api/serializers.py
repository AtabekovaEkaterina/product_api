from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product

    def validate_name(self, value):
        if Product.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                f'Product named {value} already exists.'
            )
        if len(value) > 256:
            raise serializers.ValidationError(
                'Length of the name cannot exceed 256 characters.'
            )
        return value

    def validate_description(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                'Length of the name cannot exceed 500 characters.'
            )
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'Price must be a positive number.'
            )
        return value
