import flet as ft
from ui.theme import PRIMARY, BORDER_RADIUS

def navbar(on_change):

    def nav_button(text, index, icon):
        return ft.Container(
            border_radius=BORDER_RADIUS,
            bgcolor=ft.Colors.TRANSPARENT,
            padding=12,
            ink=True,
            on_click=lambda e: on_change(index),
            content=ft.Row(
                controls=[
                    ft.Icon(icon, color=PRIMARY),
                    ft.Text(text, weight=ft.FontWeight.W_500),
                ]
            )
        )

    return ft.Container(
        width=220,
        padding=16,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column(
            spacing=8,
            controls=[
                    ft.Row(
                        spacing=10,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Image(
                                src="icon.ico",
                                width=28,
                                height=28,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text(
                                "Biblioteca UIP",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                    ),
                ft.Divider(),
                nav_button("Libros", 0, ft.Icons.BOOK),
                nav_button("Clientes", 1, ft.Icons.PERSON),
                nav_button("Préstamos", 2, ft.Icons.SWAP_HORIZ),
            ]
        )
    )
