import flet as ft
from ui.theme import BACKGROUND

class MainLayout(ft.Container):
    def __init__(self, content, max_width=900):
        super().__init__(
            expand=True,
            bgcolor=BACKGROUND,
            alignment=ft.alignment.top_center,
            content=ft.Container(
                width=max_width,
                padding=ft.padding.symmetric(vertical=30, horizontal=24),
                content=content
            )
        )
