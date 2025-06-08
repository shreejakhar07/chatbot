from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from models import Base, Product

DATABASE_URL = "sqlite:///./products.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
Base.metadata.create_all(bind=engine)

fake = Faker()
categories = ["Laptops", "Smartphones", "Headphones", "Monitors", "Keyboards", "Tablets"]
brands = ["Sony", "Samsung", "Dell", "HP", "Apple", "Lenovo", "Boat", "Asus", "Realme", "Xiaomi"]

session.query(Product).delete()
session.commit()

for _ in range(100):
    product = Product(
        name=f"{random.choice(brands)} {fake.word().capitalize()}",
        category=random.choice(categories),
        brand=random.choice(brands),
        price=round(random.uniform(500.0, 150000.0), 2),
        image_url=f"https://via.placeholder.com/150?text={fake.word().capitalize()}"
    )
    session.add(product)

session.commit()
session.close()
print("✅ 100+ mock products inserted successfully.")
