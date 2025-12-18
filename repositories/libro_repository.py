from sqlalchemy.orm import Session
from models.libro import Libro
from repositories.base_repository import BaseRepository


class LibroRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, libro: Libro):
        return self.add(libro)

    def get_by_id(self, libro_id: int):
        return self.db.query(Libro).filter(Libro.id == libro_id).first()

    def get_by_isbn(self, isbn: str):
        return self.db.query(Libro).filter(Libro.isbn == isbn).first()

    def get_all(self):
        return self.db.query(Libro).all()

    def get_disponibles(self):
        return self.db.query(Libro).filter(Libro.estatus == 1).all()

    def update(self, libro: Libro):
        self.db.commit()
        self.db.refresh(libro)
        return libro
