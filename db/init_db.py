from db.database import engine
from db.base import Base

from models.libro import Libro
from models.cliente import Cliente
from models.prestamo import Prestamo


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Base de datos inicializada correctamente")
