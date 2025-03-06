from .models import VectorProduct
import requests



def get_products(number):
    url = f"https://dummyjson.com/products?limit={number}"
    response = requests.get(url)
    data = response.json()

    try:
        for product_data in data["products"]:
            if not all(key in product_data for key in ("title", "brand", "category")):
                continue
            
            VectorProduct.objects.update_or_create(
                title=product_data["title"],
                brand=product_data["brand"],
                category=product_data["category"],
                defaults={
                    "description": product_data["description"],
                    "price": product_data["price"],
                    "sku": product_data.get("sku", ""),
                    "thumbnail": product_data["thumbnail"],
                }
            )
        return "Products processed successfully"
    except Exception as e:
        return e