from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Configure the API key from the environment variable
genai.configure(api_key=os.environ["API_KEY"])

# SQLAlchemy setup
DATABASE_URL = os.getenv("DATABASE_URL")  # e.g., "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class GeminiResponse(Base):
    __tablename__ = "gemini_responses"
    
    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(String, index=True)
    response = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/gemini/summarize")
async def summarize_text(input: TextInput):
    model = genai.GenerativeModel("gemini-1.5-flash")
    db = SessionLocal()
    try:
        response = model.generate_content(input.text)
        
        # Save to the database
        db_response = GeminiResponse(
            input_text=input.text,
            response=response.text
        )
        db.add(db_response)
        db.commit()
        db.refresh(db_response)
        
        return {"summary": response.text}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

# New endpoint to retrieve stored data
@app.get("/gemini/insights/stored")
async def get_stored_data():
    db = SessionLocal()
    try:
        responses = db.query(GeminiResponse).all()
        return {"responses": [{"id": res.id, "input_text": res.input_text, "response": res.response, "created_at": res.created_at} for res in responses]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
