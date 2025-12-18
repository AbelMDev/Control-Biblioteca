import flet as ft
from ui.theme import BORDER_RADIUS

class AppDropdown(ft.Dropdown):
    def __init__(self, label, options=None, on_change=None):
        super().__init__(
            label=label,
            options=options or [],
            bgcolor=ft.Colors.WHITE,
            border_radius=BORDER_RADIUS,
            border_color=ft.Colors.GREY_300,
            focused_border_color=ft.Colors.BLUE,
            dense=True,
            expand=True,
            editable=True,
            enable_filter=True,
            enable_search=True,
            content_padding=14,
            on_change=on_change,
        )
