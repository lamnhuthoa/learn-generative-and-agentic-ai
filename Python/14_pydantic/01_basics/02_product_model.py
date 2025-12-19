from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=1, name="Laptop", price=999.99, in_stock=True)

product_two = Product(id=2, name="Mouse", price=24.33)

product_three = Product(id=3, name="keyboard", price=49.99, in_stock=False)

print(product_one)
print(product_two)
print(product_three)