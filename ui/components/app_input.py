import flet as ft
from ui.theme import BORDER_RADIUS
class AppInput(ft.TextField):
    def __init__(self, label):
        super().__init__(
            label=label,
            bgcolor=ft.Colors.WHITE,
            border_radius=BORDER_RADIUS,
            border_color=ft.Colors.GREY_300,
            focused_border_color=ft.Colors.BLUE,
            filled=True,
            dense=True,
            expand=True, 
            content_padding=14, 
        )