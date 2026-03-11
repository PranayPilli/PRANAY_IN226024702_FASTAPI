from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

products = [
    {"id":1,"name":"Notebook","price":50,"category":"Stationery","in_stock":True},
    {"id":2,"name":"Pen","price":10,"category":"Stationery","in_stock":True},
    {"id":3,"name":"Headphones","price":1500,"category":"Electronics","in_stock":True},
    {"id":4,"name":"Mouse","price":700,"category":"Electronics","in_stock":False},
    {"id":5,"name":"Laptop Stand","price":1299,"category":"Electronics","in_stock":True},
    {"id":6,"name":"Mechanical Keyboard","price":2499,"category":"Electronics","in_stock":True},
    {"id":7,"name":"Webcam","price":1899,"category":"Electronics","in_stock":False}
]

@app.get("/products/filter")
def filter_products(
    min_price: int = Query(None),
    max_price: int = Query(None)
):

    result = products

    if min_price:
        result = [p for p in result if p["price"] >= min_price]

    if max_price:
        result = [p for p in result if p["price"] <= max_price]

    return {"filtered_products": result}

feedback_list = []

class Feedback(BaseModel):
    customer_name: str
    product_id: int
    rating: int
    comment: Optional[str] = None

@app.post("/feedback")
def submit_feedback(data: Feedback):

    feedback_list.append(data.dict())

    return {
        "message": "Feedback submitted successfully",
        "data": data
    }

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class BulkOrder(BaseModel):
    company_name: str
    contact_email: str
    items: List[OrderItem]

@app.post("/orders/bulk")
def bulk_order(order: BulkOrder):

    total = 0

    for item in order.items:
        for product in products:
            if product["id"] == item.product_id:
                total += product["price"] * item.quantity

    return {
        "company": order.company_name,
        "grand_total": total
    }