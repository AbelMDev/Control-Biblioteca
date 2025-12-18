import flet as ft


def show_snackbar(page: ft.Page, message: str, success: bool = False):
    snackbar = ft.SnackBar(
        content=ft.Text(message),
        bgcolor=ft.Colors.GREEN_600 if success else ft.Colors.RED_600,
        behavior=ft.SnackBarBehavior.FLOATING,
    )

    page.overlay.append(snackbar)
    snackbar.open = True
    page.update()