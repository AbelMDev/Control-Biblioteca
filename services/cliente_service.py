from datetime import date
from models.cliente import Cliente
from repositories.cliente_repository import ClienteRepository


class ClienteService:
    def __init__(self, cliente_repo: ClienteRepository):
        self.cliente_repo = cliente_repo

    def registrar_cliente(self, nombre: str, apellido: str, cedula: str) -> Cliente:
        if self.cliente_repo.get_by_cedula(cedula):
            raise ValueError("Ya existe un cliente con esta cédula")

        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            cedula=cedula,
            estatus=1,
            fecha_creacion=date.today()
        )
        return self.cliente_repo.create(cliente)

    def listar_clientes(self):
        return self.cliente_repo.get_all()
