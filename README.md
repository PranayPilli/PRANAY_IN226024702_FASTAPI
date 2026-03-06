# FastAPI Assignment 1

**Name:** Pranay Pilli  
**Intern ID:** IN226024702  

## Description
This project is a simple FastAPI application that provides APIs to manage and view product information.

## Technologies Used
- Python
- FastAPI
- Uvicorn
- GitHub

## Project Structure
```
PRANAY_IN226024702_FASTAPI
│
└── ASSIGNMENT 1
    ├── main.py
    ├── Q1_Output.png
    ├── Q2_Electronics.png
    ├── Q2_Stationery.png
    ├── Q2_Error.png
    ├── Q3_Output.png
    ├── Q4_Output.png
    ├── Q5_Mouse.png
    ├── Q5_Book.png
    ├── Q5_NotFound.png
    └── Bonus_Output.png
```

## API Endpoints
- `/products`
- `/products/category/{category}`
- `/products/instock`
- `/store/summary`
- `/products/search/{keyword}`
- `/products/deals`

## Run the Project

Install dependencies:
```
pip install fastapi uvicorn
```

Run the server:
```
uvicorn main:app --reload
```

Open in browser:
```
http://127.0.0.1:8000/docs
```
