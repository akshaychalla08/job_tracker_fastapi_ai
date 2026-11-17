from pydantic import BaseModel


class Product(BaseModel):
    product_name: str
    price: int
    in_stock: bool = True


product = Product(product_name="keyboard", price="90", in_stock=False)
print(product.model_dump_json())