from sqlmodel import SQLModel, create_engine
from .model import *
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True) 

# Função para criar o banco de dados e as tabelas :D
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Cria a tabela de rodar diretamente
if __name__ == "__main__":
    create_db_and_tables()
