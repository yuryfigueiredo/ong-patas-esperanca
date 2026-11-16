from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Animal, SessionLocal

router = APIRouter(prefix="/api/v1/animais", tags=["animais"])
