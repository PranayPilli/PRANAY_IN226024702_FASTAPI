# FastAPI Assignments

**Name:** Pranay Pilli
**Intern ID:** IN226024702

## Project Overview

This repository contains multiple FastAPI assignments demonstrating how to build REST APIs using Python and FastAPI. The project includes APIs for product management and a simple shopping cart system.

## Technologies Used

* Python
* FastAPI
* Uvicorn
* GitHub

## Project Structure

PRANAY_IN226024702_FASTAPI
│
├── ASSIGNMENT 1
│   ├── main.py
│   ├── Q1_Output.png
│   ├── Q2_Output.png
│   ├── Q3_Output.png
│   ├── Q4_Output.png
│   └── Q5_Output.png
│
├── ASSIGNMENT 2
│   ├── main.py
│   ├── Q1_Output(1).png
│   ├── Q2_Output(1).png
│   ├── Q3_Output.png
│   ├── Q4_Output.png
│   └── Q5_Output.png
│
├── ASSIGNMENT 4
│   ├── main.py
│   ├── Q1_Output(1).png
│   ├── Q1_Output(2).png
│   ├── Q2_Output.png
│   ├── Q3_Output.png
│   ├── Q4_Output.png
│   └── Q5_Output.png
│
└── README.md

---

## Assignment 1 – Product APIs

Basic APIs to manage and view product information.

**Endpoints**

* `/products`
* `/products/category/{category}`
* `/products/instock`
* `/store/summary`
* `/products/search/{keyword}`
* `/products/deals`

---

## Assignment 2 – Advanced APIs

Additional APIs for filtering products, submitting feedback, and placing bulk orders.

**Endpoints**

* `/products/filter`
* `/feedback`
* `/orders/bulk`

---

## Assignment 4 – Shopping Cart API

APIs to simulate a simple shopping cart system.

**Endpoints**

* `/cart/add`
* `/cart`
* `/cart/remove/{product_id}`
* `/cart/checkout`

---

## Run the Project

Install dependencies:

pip install fastapi uvicorn

Run the server:

uvicorn main:app --reload

Open API documentation:

http://127.0.0.1:8000/docs
