import flet as ft
from ui.theme import CARD_BG, BORDER_RADIUS

class AppCard(ft.Container):
    def __init__(self, content, width=None):
        super().__init__(
            width=width,
            bgcolor=CARD_BG,
            padding=20,
            border_radius=BORDER_RADIUS,
            shadow=ft.BoxShadow(
                blur_radius=12,
                color=ft.Colors.BLACK12
            ),
            content=content
        )
