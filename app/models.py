from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

DATABASE_URL = "sqlite:///./ong_patas.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    especie = Column(String(50), nullable=False)  # Canino, Felino
    porte = Column(String(50), nullable=False)    # Pequeno, Médio, Grande
    idade_meses = Column(Integer, nullable=True)
    temperamento = Column(String(255), nullable=False)
    status_adocao = Column(String(50), default="Disponível", nullable=False)  # Disponível, Adotado, Em Tratamento
    castrado = Column(Boolean, default=False, nullable=False)
    vacinas_em_dia = Column(Boolean, default=False, nullable=False)
    tipo_alocacao = Column(String(50), default="Abrigo Sede", nullable=False)
    foto_url = Column(String(500), nullable=False)
    data_resgate = Column(DateTime, default=datetime.utcnow)

    candidaturas = relationship("Candidatura", back_populates="animal", cascade="all, delete-orphan")

class Candidatura(Base):
    __tablename__ = "candidaturas"

    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animais.id"), nullable=False)
    nome_candidato = Column(String(150), nullable=False)
    email_candidato = Column(String(120), nullable=False)
    telefone_whatsapp = Column(String(20), nullable=False)
    tipo_moradia = Column(String(50), nullable=False)  # Casa, Apartamento
    possui_telas_protecao = Column(Boolean, nullable=False)
    status_triagem = Column(String(50), default="Em Análise", nullable=False)  # Em Análise, Aprovado, Reprovado
    data_submissao = Column(DateTime, default=datetime.utcnow)

    animal = relationship("Animal", back_populates="candidaturas")

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    cargo = Column(String(50), default="Voluntário", nullable=False)

Base.metadata.create_all(bind=engine)
