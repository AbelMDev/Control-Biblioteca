from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from db.base import Base


class Libro(Base):
    __tablename__ = "libro"

    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(String(13), unique=True, nullable=False)

    autor = Column(String(255), nullable=False)
    titulo = Column(String(255), nullable=False)

    fecha_creacion = Column(Date, nullable=False)
    fecha_actualizacion = Column(Date, nullable=True)

    estatus = Column(Integer, nullable=False, default=1)

    prestamos = relationship("Prestamo", back_populates="libro")

    def __repr__(self):
        return f"<Libro(id={self.id}, titulo='{self.titulo}')>"
