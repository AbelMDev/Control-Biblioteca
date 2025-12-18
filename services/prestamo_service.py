from datetime import date, timedelta

from models.prestamo import Prestamo
from repositories.prestamo_repository import PrestamoRepository
from repositories.libro_repository import LibroRepository
from repositories.cliente_repository import ClienteRepository
from services.libro_service import LibroService


class PrestamoService:
    def __init__(
        self,
        prestamo_repo: PrestamoRepository,
        libro_repo: LibroRepository,
        cliente_repo: ClienteRepository,
        libro_service: LibroService
    ):
        self.prestamo_repo = prestamo_repo
        self.libro_repo = libro_repo
        self.cliente_repo = cliente_repo
        self.libro_service = libro_service

    def realizar_prestamo(self, libro_id: int, cliente_id: int) -> Prestamo:
        libro = self.libro_repo.get_by_id(libro_id)
        if not libro:
            raise ValueError("Libro no encontrado")

        if libro.estatus == 0:
            raise ValueError("El libro no está disponible")

        cliente = self.cliente_repo.get_by_id(cliente_id)
        if not cliente:
            raise ValueError("Cliente no encontrado")

        prestamo = Prestamo(
            libro_id=libro.id,
            cliente_id=cliente.id,
            fecha_inicio=date.today(),
            fecha_fin=date.today() + timedelta(days=7),
            fecha_creacion=date.today(),
            estatus=1
        )

        prestamo = self.prestamo_repo.create(prestamo)
        self.libro_service.marcar_como_prestado(libro)

        return prestamo

    def devolver_libro(self, libro_id: int):
        prestamo = self.prestamo_repo.get_by_libro(libro_id)
        if not prestamo:
            raise ValueError("Este libro no tiene un préstamo activo")

        prestamo.fecha_entrega = date.today()
        prestamo.estatus = 0
        prestamo.fecha_actualizacion = date.today()

        self.prestamo_repo.update(prestamo)

        libro = self.libro_repo.get_by_id(libro_id)
        self.libro_service.marcar_como_disponible(libro)

        return prestamo

    def listar_prestamos_activos(self):
        return self.prestamo_repo.get_activos()
