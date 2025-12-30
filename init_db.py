from app.database import engine, Base
from app import models

#Creating all tables defined in my model
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")