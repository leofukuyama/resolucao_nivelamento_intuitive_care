from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/operadoras_ativas_ans"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DadosAtivos(Base):
    __tablename__ = "dados_ativos"

    Registro_ANS = Column(Integer, primary_key=True, index=True)
    CNPJ = Column(String(14), index=True)
    Razao_Social = Column(String(255))
    Nome_Fantasia = Column(String(255), index=True)
    Modalidade = Column(String(100))
    Logradouro = Column(String(255))
    Numero = Column(String(10))
    Complemento = Column(String(255))
    Bairro = Column(String(100))
    Cidade = Column(String(100))
    UF = Column(String(2))
    CEP = Column(String(8))
    DDD = Column(String(2))
    Telefone = Column(String(15))
    Fax = Column(String(15))
    Endereco_eletronico = Column(String(255))
    Representante = Column(String(255))
    Cargo_Representante = Column(String(100))
    Regiao_de_comercializacao = Column(Integer)
    Data_Registro_ANS = Column(Date)

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

@app.get("/buscar/")
def buscar_operadora(termo: str, db: Session = Depends(get_db)):
    operadoras = db.query(DadosAtivos).filter(DadosAtivos.Nome_Fantasia.like(f"%{termo}%")).all()
    return operadoras

