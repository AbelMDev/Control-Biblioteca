import flet as ft

from ui.components.navbar import navbar
from views.libro_view import libro_view
from views.cliente_view import cliente_view
from views.prestamo_view import prestamo_view

from services.libro_service import LibroService
from services.cliente_service import ClienteService
from services.prestamo_service import PrestamoService


def main_view(
    page: ft.Page,
    libro_service: LibroService,
    cliente_service: ClienteService,
    prestamo_service: PrestamoService
):

    content = ft.Container(expand=True)

    def cambiar_vista(index):
        if index == 0:
            content.content = libro_view(page, libro_service)
        elif index == 1:
            content.content = cliente_view(page, cliente_service)
        else:
            content.content = prestamo_view(
                page,
                prestamo_service,
                libro_service,
                cliente_service
            )
        page.update()

    content.content = libro_view(page, libro_service)

    return ft.Row(
        expand=True,
        controls=[
            navbar(cambiar_vista),
            ft.VerticalDivider(width=1),
            content
        ]
    )
