import flet as ft
from ui.layout.centered_layout import centered_column
from ui.layout.main_layout import MainLayout
from ui.components.app_title import AppTitle
from ui.components.app_card import AppCard
from ui.components.app_button import AppButton
from ui.components.form_fields import nombre_field, apellido_field, cedula_field
from ui.components.app_snackbar import show_snackbar

from services.cliente_service import ClienteService


def cliente_view(page: ft.Page, cliente_service: ClienteService):

    nombre_input = nombre_field()
    apellido_input = apellido_field()
    cedula_input = cedula_field()

    table_container = ft.Column()

    def validar_input(field: ft.TextField, label: str) -> bool:
        if not field.value or not field.value.strip():
            field.error_text = f"{label} es obligatorio"
            field.border_color = ft.Colors.RED_600
            field.focused_border_color = ft.Colors.RED_700
            return False

        field.error_text = None
        field.border_color = ft.Colors.GREY_400
        field.focused_border_color = ft.Colors.BLUE_600
        return True

    def cargar_tabla():
        clientes = cliente_service.listar_clientes()
        table_container.controls.clear()

        table_container.controls.append(
            AppCard(
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Nombre")),
                        ft.DataColumn(ft.Text("Apellido")),
                        ft.DataColumn(ft.Text("Cédula")),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(c.nombre)),
                                ft.DataCell(ft.Text(c.apellido)),
                                ft.DataCell(ft.Text(c.cedula)),
                            ]
                        )
                        for c in clientes
                    ],
                ),
                width=780,
            )
        )
        page.update()

    def registrar_cliente(e):
        nombre_ok = validar_input(nombre_input, "Nombre")
        apellido_ok = validar_input(apellido_input, "Apellido")
        cedula_ok = validar_input(cedula_input, "Cédula")

        if not (nombre_ok and apellido_ok and cedula_ok):
            show_snackbar(page, "Complete todos los campos obligatorios")
            return

        try:
            cliente_service.registrar_cliente(
                nombre_input.value.strip(),
                apellido_input.value.strip(),
                cedula_input.value.strip(),
            )
        except Exception as ex:
            show_snackbar(page, str(ex))
            return

        show_snackbar(page, "Cliente registrado correctamente", success=True)

        for field in (nombre_input, apellido_input, cedula_input):
            field.value = ""
            field.error_text = None
            field.border_color = ft.Colors.GREY_400
            field.focused_border_color = ft.Colors.BLUE_600

        cargar_tabla()
        page.update()

    nombre_input.on_change = lambda e: validar_input(nombre_input, "Nombre")
    apellido_input.on_change = lambda e: validar_input(apellido_input, "Apellido")
    cedula_input.on_change = lambda e: validar_input(cedula_input, "Cédula")
    
    cargar_tabla()

    content = centered_column(
        controls=[
            AppTitle("👤 Gestión de Clientes"),
            AppCard(
                ft.Column(
                    spacing=12,
                    controls=[
                        nombre_input,
                        apellido_input,
                        cedula_input,
                        AppButton(
                            "Registrar Cliente",
                            registrar_cliente,
                            expand=True,
                        ),
                    ],
                ),
                width=780,
            ),
            table_container,
        ]
    )

    return MainLayout(content)
