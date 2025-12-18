import flet as ft

def centered_column(controls, spacing=30):
    return ft.Column(
        controls=controls,
        spacing=spacing,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO 
    )