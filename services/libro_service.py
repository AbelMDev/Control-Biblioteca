from datetime import date
from models.libro import Libro
from repositories.libro_repository import LibroRepository


class LibroService:
    def __init__(self, libro_repo: LibroRepository):
        self.libro_repo = libro_repo

    def registrar_libro(self, titulo: str, autor: str, isbn: str) -> Libro:
        if self.libro_repo.get_by_isbn(isbn):
            raise ValueError("Ya existe un libro con este ISBN")

        libro = Libro(
            titulo=titulo,
            autor=autor,
            isbn=isbn,
            estatus=1,
            fecha_creacion=date.today()
        )
        return self.libro_repo.create(libro)

    def listar_libros(self):
        return self.libro_repo.get_all()

    def listar_disponibles(self):
        return self.libro_repo.get_disponibles()

    def marcar_como_prestado(self, libro: Libro):
        libro.estatus = 0
        libro.fecha_actualizacion = date.today()
        return self.libro_repo.update(libro)

    def marcar_como_disponible(self, libro: Libro):
        libro.estatus = 1
        libro.fecha_actualizacion = date.today()
        return self.libro_repo.update(libro)