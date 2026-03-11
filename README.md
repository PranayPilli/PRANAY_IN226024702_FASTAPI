# FastAPI Assignments

**Name:** Pranay Pilli
**Intern ID:** IN226024702

## Project Overview

This repository contains two FastAPI assignments that demonstrate building REST APIs for a simple product store. The APIs allow users to view products, filter them, submit feedback, and place bulk orders.

## Technologies Used

* Python
* FastAPI
* Uvicorn
* GitHub

## Project Structure

```
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
└── README.md
```

## Assignment 1 – Product APIs

APIs to manage and view product information.

**Endpoints**

* `/products`
* `/products/category/{category}`
* `/products/instock`
* `/store/summary`
* `/products/search/{keyword}`
* `/products/deals`

## Assignment 2 – Advanced APIs

Additional APIs for filtering products, submitting feedback, and placing bulk orders.

**Endpoints**

* `/products/filter`
* `/feedback`
* `/orders/bulk`

## Run the Project

Install dependencies:

```
pip install fastapi uvicorn
```

Run the server:

```
uvicorn main:app --reload
```

Open API documentation:

```
http://127.0.0.1:8000/docs
```
