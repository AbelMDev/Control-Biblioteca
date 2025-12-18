from sqlalchemy.orm import Session
from models.cliente import Cliente
from repositories.base_repository import BaseRepository


class ClienteRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, cliente: Cliente):
        return self.add(cliente)

    def get_by_id(self, cliente_id: int):
        return self.db.query(Cliente).filter(Cliente.id == cliente_id).first()

    def get_by_cedula(self, cedula: str):
        return self.db.query(Cliente).filter(Cliente.cedula == cedula).first()

    def get_all(self):
        return self.db.query(Cliente).all()

    def update(self, cliente: Cliente):
        self.db.commit()
        self.db.refresh(cliente)
        return cliente
