import flet as ft

from db.database import SessionLocal
from db.init_db import init_db

from repositories.libro_repository import LibroRepository
from repositories.cliente_repository import ClienteRepository
from repositories.prestamo_repository import PrestamoRepository

from services.libro_service import LibroService
from services.cliente_service import ClienteService
from services.prestamo_service import PrestamoService

from views.main_view import main_view
from ui.theme import PAGE_THEME


def main(page: ft.Page):
    page.title = "Sistema de Biblioteca"

    # ✅ ICONO DE LA VENTANA (Windows)
    page.window.icon = "icon.ico"

    # Tamaño ventana
    page.window.width = 1200
    page.window.height = 800

    page.theme = PAGE_THEME
    page.bgcolor = None
    page.padding = 0

    # DB
    init_db()
    db = SessionLocal()

    # Repositories
    libro_repo = LibroRepository(db)
    cliente_repo = ClienteRepository(db)
    prestamo_repo = PrestamoRepository(db)

    # Services
    libro_service = LibroService(libro_repo)
    cliente_service = ClienteService(cliente_repo)
    prestamo_service = PrestamoService(
        prestamo_repo,
        libro_repo,
        cliente_repo,
        libro_service,
    )

    page.add(
        main_view(
            page,
            libro_service,
            cliente_service,
            prestamo_service,
        )
    )


ft.app(
    target=main,
    assets_dir="assets",
)
