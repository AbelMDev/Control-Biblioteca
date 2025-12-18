from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from db.base import Base


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)

    cedula = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)

    fecha_creacion = Column(Date, nullable=False)
    fecha_actualizacion = Column(Date, nullable=True)

    estatus = Column(Integer, nullable=False, default=1)

    prestamos = relationship("Prestamo", back_populates="cliente")

    def __repr__(self):
        return f"<Cliente(id={self.id}, nombre='{self.nombre} {self.apellido}')>"
