from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import os, json
from database import SessionLocal, engine
from models import Product, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce Sales Chatbot API!"}

@app.get("/products", response_model=List[dict])
def get_all_products(db: Session = next(get_db())):
    products = db.query(Product).all()
    return [product.__dict__ for product in products]

@app.get("/products/search", response_model=List[dict])
def search_products(query: str = Query(...), db: Session = next(get_db())):
    results = db.query(Product).filter(Product.name.ilike(f"%{query}%")).all()
    return [p.__dict__ for p in results]

@app.post("/chat/store")
def store_chat_log(session_id: str, content: List[str]):
    os.makedirs("chat_logs", exist_ok=True)
    filepath = f"chat_logs/{session_id}.json"
    with open(filepath, "w") as f:
        json.dump({"session_id": session_id, "messages": content}, f)
    return {"message": "Chat log saved."}
