from calculator.gui import main
import flet as ft

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=8000, host="0.0.0.0")
