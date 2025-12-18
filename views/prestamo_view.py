import flet as ft
from ui.layout.centered_layout import centered_column
from ui.layout.main_layout import MainLayout
from ui.components.app_title import AppTitle
from ui.components.app_card import AppCard
from ui.components.app_button import AppButton
from ui.components.app_dropdown import AppDropdown
from ui.components.app_snackbar import show_snackbar
from ui.components.confirm_dialog import show_confirm_dialog

from services.prestamo_service import PrestamoService
from services.libro_service import LibroService
from services.cliente_service import ClienteService


def prestamo_view(
    page: ft.Page,
    prestamo_service: PrestamoService,
    libro_service: LibroService,
    cliente_service: ClienteService,
):

    libro_dropdown = AppDropdown("Libro disponible")
    cliente_dropdown = AppDropdown("Cliente")

    prestamos_container = ft.Column()


    def validar_dropdown(dropdown: AppDropdown) -> bool:
        valid_keys = {opt.key for opt in dropdown.options}

        if dropdown.value not in valid_keys:
            dropdown.value = None
            dropdown.error_text = "Seleccione una opción válida"
            dropdown.border_color = ft.Colors.RED_600
            dropdown.focused_border_color = ft.Colors.RED_700
            return False

        dropdown.error_text = None
        dropdown.border_color = ft.Colors.GREY_400
        dropdown.focused_border_color = ft.Colors.BLUE_600
        return True

    def cargar_dropdowns():
        libro_dropdown.value = None
        cliente_dropdown.value = None

        libro_dropdown.options = [
            ft.dropdown.Option(
                key=str(l.id),
                text=f"{l.titulo} - {l.autor}",
            )
            for l in libro_service.listar_disponibles()
        ]

        cliente_dropdown.options = [
            ft.dropdown.Option(
                key=str(c.id),
                text=f"{c.nombre} {c.apellido} ({c.cedula})",
            )
            for c in cliente_service.listar_clientes()
        ]

        page.update()

    def cargar_prestamos():
        prestamos_container.controls.clear()

        for p in prestamo_service.listar_prestamos_activos():
            prestamos_container.controls.append(
                AppCard(
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                f"{p.libro.titulo} → "
                                f"{p.cliente.nombre} {p.cliente.apellido}"
                            ),
                            AppButton(
                                "Devolver",
                                lambda e, libro_id=p.libro_id: confirmar_devolucion(libro_id),
                            ),
                        ],
                    ),
                    width=780,
                )
            )

        page.update()

    def confirmar_prestamo():
        try:
            prestamo_service.realizar_prestamo(
                int(libro_dropdown.value),
                int(cliente_dropdown.value),
            )
        except Exception as ex:
            show_snackbar(page, str(ex))
            return

        show_snackbar(page, "Préstamo realizado correctamente", success=True)
        cargar_dropdowns()
        cargar_prestamos()

    def confirmar_devolucion(libro_id: int):
        show_confirm_dialog(
            page,
            title="Confirmar devolución",
            message="¿Está seguro que desea devolver este libro?",
            on_confirm=lambda: ejecutar_devolucion(libro_id),
        )

    def ejecutar_devolucion(libro_id: int):
        try:
            prestamo_service.devolver_libro(libro_id)
        except Exception as ex:
            show_snackbar(page, str(ex))
            return

        show_snackbar(page, "Libro devuelto correctamente", success=True)
        cargar_dropdowns()
        cargar_prestamos()

    def realizar_prestamo(e):
        libro_ok = validar_dropdown(libro_dropdown)
        cliente_ok = validar_dropdown(cliente_dropdown)

        if not libro_ok or not cliente_ok:
            show_snackbar(page, "Seleccione un libro y un cliente válidos")
            return

        show_confirm_dialog(
            page,
            title="Confirmar préstamo",
            message="¿Está seguro que desea realizar este préstamo?",
            on_confirm=confirmar_prestamo,
        )


    libro_dropdown.on_change = lambda e: validar_dropdown(libro_dropdown)
    cliente_dropdown.on_change = lambda e: validar_dropdown(cliente_dropdown)

    cargar_dropdowns()
    cargar_prestamos()

    content = centered_column(
        controls=[
            AppTitle("🔄 Préstamos"),
            AppCard(
                ft.Column(
                    spacing=12,
                    controls=[
                        libro_dropdown,
                        cliente_dropdown,
                        AppButton(
                            "Prestar Libro",
                            realizar_prestamo,
                            expand=True,
                        ),
                    ],
                ),
                width=780,
            ),
            AppTitle("📖 Préstamos Activos"),
            prestamos_container,
        ]
    )

    return MainLayout(content)
