from sqlalchemy.orm import Session
from models.prestamo import Prestamo
from repositories.base_repository import BaseRepository


class PrestamoRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, prestamo: Prestamo):
        return self.add(prestamo)

    def get_by_id(self, prestamo_id: int):
        return self.db.query(Prestamo).filter(Prestamo.id == prestamo_id).first()

    def get_activos(self):
        return (
            self.db.query(Prestamo)
            .filter(Prestamo.fecha_entrega.is_(None))
            .all()
        )

    def get_by_libro(self, libro_id: int):
        return (
            self.db.query(Prestamo)
            .filter(
                Prestamo.libro_id == libro_id,
                Prestamo.fecha_entrega.is_(None)
            )
            .first()
        )

    def update(self, prestamo: Prestamo):
        self.db.commit()
        self.db.refresh(prestamo)
        return prestamo
