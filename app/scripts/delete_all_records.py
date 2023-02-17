from manufacturers.models import Manufacturer
from products.models import Product
from products.models import ProductCategory


Manufacturer.objects.all().delete()
ProductCategory.objects.all().delete()
Product.objects.all().delete()
