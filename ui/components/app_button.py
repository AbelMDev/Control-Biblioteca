import flet as ft
from ui.theme import PRIMARY, BORDER_RADIUS

class AppButton(ft.ElevatedButton):
    def __init__(self, text, on_click, expand=False):
        super().__init__(
            text=text,
            on_click=on_click,
            expand=expand,
            bgcolor=PRIMARY,
            color=ft.Colors.WHITE,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS),
                padding=ft.padding.symmetric(horizontal=24, vertical=14)
            )
        )
