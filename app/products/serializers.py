from rest_framework import serializers

from products.models import Product
from products.models import ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = (
            "id",
            "name",
        )


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "sku",
            "type",
            "category_id",
        )
