from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from typing import List, Optional
from passlib.context import CryptContext
from app.models import SessionLocal, Animal, Candidatura, Usuario

app = FastAPI(title="API ONG Patas & Esperança", version="1.0.0")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schemas
class AnimalCreate(BaseModel):
    nome: str
    especie: str
    porte: str
    temperamento: str
    castrado: bool = False
    vacinas_em_dia: bool = False
    foto_url: str = "https://images.unsplash.com/photo-1543466835-00a7907e9de1"

class AnimalResponse(AnimalCreate):
    id: int
    status_adocao: str
    class Config:
        from_attributes = True

class CandidaturaCreate(BaseModel):
    animal_id: int
    nome_candidato: str
    email_candidato: EmailStr
    telefone_whatsapp: str
    tipo_moradia: str
    possui_telas_protecao: bool

class CandidaturaResponse(CandidaturaCreate):
    id: int
    status_triagem: str
    class Config:
        from_attributes = True

# Routes
@app.get("/")
def read_root():
    return {"message": "API ONG Patas & Esperança no ar!", "status": "online"}

@app.get("/api/animais", response_model=List[AnimalResponse])
def listar_animais(especie: Optional[str] = None, porte: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Animal).filter(Animal.status_adocao == "Disponível")
    if especie:
        query = query.filter(Animal.especie == especie)
    if porte:
        query = query.filter(Animal.porte == porte)
    return query.all()

@app.post("/api/animais", response_model=AnimalResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    db_animal = Animal(**animal.model_dump())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

@app.post("/api/candidaturas", response_model=CandidaturaResponse, status_code=status.HTTP_201_CREATED)
def submeter_candidatura(cand: CandidaturaCreate, db: Session = Depends(get_db)):
    animal = db.query(Animal).filter(Animal.id == cand.animal_id, Animal.status_adocao == "Disponível").first()
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não disponível para adoção.")
    
    db_cand = Candidatura(**cand.model_dump())
    db.add(db_cand)
    db.commit()
    db.refresh(db_cand)
    return db_cand
