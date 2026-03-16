from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499},
    {"id": 2, "name": "Keyboard", "price": 599},
    {"id": 3, "name": "USB Cable", "price": 199}
]

cart = []

class CartItem(BaseModel):
    product_id: int
    quantity: int


@app.get("/")
def home():
    return {"message": "Shopping Cart API Running"}


@app.post("/cart/add")
def add_to_cart(item: CartItem):

    for product in products:
        if product["id"] == item.product_id:

            cart.append({
                "product_id": item.product_id,
                "name": product["name"],
                "price": product["price"],
                "quantity": item.quantity
            })

            return {"message": "Item added to cart", "cart_item": item}

    raise HTTPException(status_code=404, detail="Product not found")


@app.get("/cart")
def view_cart():

    total = 0

    for item in cart:
        total += item["price"] * item["quantity"]

    return {
        "cart_items": cart,
        "grand_total": total
    }


@app.delete("/cart/remove/{product_id}")
def remove_item(product_id: int):

    for item in cart:
        if item["product_id"] == product_id:
            cart.remove(item)
            return {"message": "Item removed from cart"}

    raise HTTPException(status_code=404, detail="Item not found in cart")


@app.post("/cart/checkout")
def checkout():

    if not cart:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total = sum(item["price"] * item["quantity"] for item in cart)

    cart.clear()

    return {
        "message": "Checkout successful",
        "total_paid": total
    }