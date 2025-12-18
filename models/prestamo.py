from sqlalchemy import Column, Integer, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from db.base import Base


class Prestamo(Base):
    __tablename__ = "prestamo"

    id = Column(Integer, primary_key=True, index=True)

    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    libro_id = Column(Integer, ForeignKey("libro.id"), nullable=False)

    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    fecha_entrega = Column(Date, nullable=True)

    fecha_creacion = Column(Date, nullable=False)
    fecha_actualizacion = Column(Date, nullable=True)

    estatus = Column(Integer, nullable=False, default=1)

    __table_args__ = (
        CheckConstraint("estatus IN (0,1)", name="ck_prestamo_estatus"),
    )

    cliente = relationship("Cliente", back_populates="prestamos")
    libro = relationship("Libro", back_populates="prestamos")

    def __repr__(self):
        return f"<Prestamo(id={self.id}, cliente_id={self.cliente_id}, libro_id={self.libro_id})>"
