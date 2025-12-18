import flet as ft


def show_confirm_dialog(
    page: ft.Page,
    title: str,
    message: str,
    on_confirm,
):
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text(title),
        content=ft.Text(message),
        actions=[
            ft.TextButton(
                "Cancelar",
                on_click=lambda e: cerrar_dialog(page),
            ),
            ft.ElevatedButton(
                "Confirmar",
                bgcolor=ft.Colors.RED_600,
                color=ft.Colors.WHITE,
                on_click=lambda e: confirmar(page, on_confirm),
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.dialog = dialog
    page.overlay.append(dialog)
    dialog.open = True
    page.update()


def confirmar(page: ft.Page, on_confirm):
    page.dialog.open = False
    page.update()
    on_confirm()


def cerrar_dialog(page: ft.Page):
    page.dialog.open = False
    page.update()
