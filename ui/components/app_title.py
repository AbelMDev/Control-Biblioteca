import flet as ft

class AppTitle(ft.Text):
    def __init__(self, text):
        super().__init__(
            text,
            size=20,
            weight=ft.FontWeight.BOLD
        )
