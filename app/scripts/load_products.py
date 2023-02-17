import random
import uuid

from manufacturers.models import Manufacturer
from products.models import Product
from products.models import ProductCategory
from products.models import ProductTypeChoices


def get_random_name(key: str = ""):
    uuid_name = str(uuid.uuid4()).upper()[-10:]
    return f"{key} {uuid_name}" if key else uuid_name


def create_manufacturers(total: int):
    print(f"Creating {total} manufacturers...")
    for i in range(total):
        print(f"[{i + 1} / {total}] creating manufacturer...")
        Manufacturer(name=get_random_name("Manufacturer")).save()


def create_categories(total: int):
    print(f"Creating {total} categories...")
    for i in range(total):
        print(f"[{i + 1} / {total}] creating category...")
        ProductCategory(name=get_random_name("Category")).save()


def create_products(total: int):
    print(f"Creating {total} products...")
    categories = ProductCategory.objects.all()
    manufacturers = Manufacturer.objects.all()
    for i in range(total):
        print(f"[{i + 1} / {total}] creating product...")
        Product(
            name=get_random_name("Product"),
            sku=get_random_name(),
            type=random.choice(ProductTypeChoices.choices)[0],
            category=random.choice(categories),
            manufacturer=random.choice(manufacturers),
        ).save()


create_manufacturers(100)
create_categories(100)
create_products(100_000)

print("Load finished!")
