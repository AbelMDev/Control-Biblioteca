import flet as ft
from ui.layout.centered_layout import centered_column
from ui.layout.main_layout import MainLayout
from ui.components.app_title import AppTitle
from ui.components.app_card import AppCard
from ui.components.app_button import AppButton
from ui.components.form_fields import titulo_field, autor_field, isbn_field
from ui.components.app_snackbar import show_snackbar

from services.libro_service import LibroService


def libro_view(page: ft.Page, libro_service: LibroService):

    titulo_input = titulo_field()
    autor_input = autor_field()
    isbn_input = isbn_field()

    table_container = ft.Column()

    def cargar_tabla():
        libros = libro_service.listar_libros()
        table_container.controls.clear()

        table_container.controls.append(
            AppCard(
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("ISBN")),
                        ft.DataColumn(ft.Text("Título")),
                        ft.DataColumn(ft.Text("Autor")),
                        ft.DataColumn(ft.Text("Estado")),
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(l.isbn)),
                                ft.DataCell(ft.Text(l.titulo)),
                                ft.DataCell(ft.Text(l.autor)),
                                ft.DataCell(
                                    ft.Text("Disponible" if l.estatus == 1 else "Prestado")
                                ),
                            ]
                        )
                        for l in libros
                    ]
                ),
                width=780
            )
        )
        page.update()

    def registrar_libro(e):
        try:
            libro_service.registrar_libro(
                titulo_input.value,
                autor_input.value,
                isbn_input.value
            )
            titulo_input.value = ""
            autor_input.value = ""
            isbn_input.value = ""
            cargar_tabla()
            show_snackbar(page, "Libro registrado correctamente", success=True)

        except ValueError as ex:
            show_snackbar(page, str(ex))

    cargar_tabla()

    content = centered_column(
        controls=[
            AppTitle("📚 Gestión de Libros"),

            AppCard(
                ft.Column(
                    spacing=12,
                    controls=[
                        isbn_input,
                        titulo_input,
                        autor_input,
                        AppButton("Registrar Libro", registrar_libro, expand=True),
                    ]
                ),
                width=780
            ),

            table_container
        ]
    )

    return MainLayout(content)
