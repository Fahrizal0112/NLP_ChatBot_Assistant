from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    customer_name = Column(String(100), nullable=False)
    flavor = Column(String(50), nullable=False)
    size = Column(String(10), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    address = Column(String, nullable=False)
    status = Column(String(20), default='pending')
    created_at = Column(DateTime, default=datetime.now)
    
    def calculate_price(self):
        price_list = {
            'S': 150000,
            'M': 250000,
            'L': 350000
        }
        return price_list.get(self.size, 0) * self.quantity

def init_db():
    try:
        from config.database import DATABASE_URL
        
        print(f"DEBUG - Trying to connect to database...")
        
        engine = create_engine(DATABASE_URL)
        engine.connect()  
        
        print("DEBUG - Database connection successful")
        Base.metadata.create_all(engine)
        
        return sessionmaker(bind=engine)
        
    except Exception as e:
        print(f"ERROR - Database connection failed: {str(e)}")
        return None 