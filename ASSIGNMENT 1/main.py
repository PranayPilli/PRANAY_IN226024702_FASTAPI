from fastapi import FastAPI, Query

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


@app.get("/")
def home():
    return {"message": "Welcome to my store API"}


@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }


@app.get("/products/category/{category_name}")
def get_category(category_name: str):

    result = [p for p in products if p["category"].lower() == category_name.lower()]

    if not result:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }


@app.get("/products/instock")
def get_instock():

    available = [p for p in products if p["in_stock"] == True]

    return {
        "in_stock_products": available,
        "count": len(available)
    }


@app.get("/store/summary")
def store_summary():

    total = len(products)
    in_stock = len([p for p in products if p["in_stock"]])
    out_stock = total - in_stock

    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": total,
        "in_stock": in_stock,
        "out_of_stock": out_stock,
        "categories": categories
    }


@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = [p for p in products if keyword.lower() in p["name"].lower()]

    if not results:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }


@app.get("/products/deals")
def product_deals():
    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }


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

from pydantic import BaseModel
from typing import Optional

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

from typing import List

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