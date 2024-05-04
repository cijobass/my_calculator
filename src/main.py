import flet as ft
import sympy
import pyperclip as pc

def main(page: ft.Page):
    page.title = "Calculator"
    page.window_width = 620
    page.window_height = 700
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    history_view = ft.ListView(expand=True)
    active_text_field = None

    def set_active_field(text_field):
        nonlocal active_text_field
        active_text_field = text_field

    def evaluate_expression(e=None):  # eをオプショナル引数として追加
        # 現在のアクティブなテキストフィールドがない場合は何もしない
        if not active_text_field:
            return

        expr = active_text_field.value
        if not expr:
            active_text_field.parent.controls[1].value = ""
            page.update()
            return

        try:
            evaluated_expr = sympy.sympify(
                expr,
                locals={
                    'π': sympy.pi,
                    'e': sympy.E,
                    'factorial': sympy.factorial,
                    'ln': sympy.log,  # 自然対数（底 e）
                    'log': lambda x: sympy.log(x, 10)  # 常用対数（底 10）
                }
            )
            if isinstance(evaluated_expr, sympy.Integer):
                result = str(int(evaluated_expr))
            else:
                result = str(float(evaluated_expr))
        except Exception as exc:
            result = "Error: " + str(exc)

        active_text_field.parent.controls[1].value = result
        page.update()


    def on_button_click(e):
        nonlocal active_text_field
        if active_text_field:
            if e.control.text == "C":
                active_text_field.value = ""
            elif e.control.text == "⌫":
                active_text_field.value = active_text_field.value[:-1]
            elif e.control.text == "π":
                active_text_field.value += "π"
            elif e.control.text == "e":
                active_text_field.value += "e"
            elif e.control.text == "x!":
                active_text_field.value += "!"
            elif e.control.text == "^":
                active_text_field.value += "**"
            else:
                active_text_field.value += e.control.text
            evaluate_expression()
        page.update()

    def add_expression(autofocus=False):
        nonlocal active_text_field
        expr_field = ft.TextField(expand=True, on_focus=lambda e: set_active_field(e.control), autofocus=autofocus, on_change=evaluate_expression)
        result_field = ft.TextField(expand=True, read_only=True)
        copy_button = ft.IconButton(icon=ft.icons.CONTENT_COPY, tooltip="Click to copy", on_click=lambda e: copy_to_clipboard(e, result_field))
        row = ft.Row(controls=[expr_field, result_field, copy_button], expand=True)
        history_view.controls.append(row)
        page.update()

    def copy_to_clipboard(e, text_field):
        pc.copy(text_field.value)
        page.update()

    buttons = [
        ["7", "8", "9", {"text": "+", "color": ft.colors.ORANGE, "text_color": ft.colors.WHITE}, "cos", "sin", "tan"],
        ["4", "5", "6", {"text": "-", "color": ft.colors.ORANGE, "text_color": ft.colors.WHITE}, "^", "ln", "log"],
        ["1", "2", "3", {"text": "*", "color": ft.colors.ORANGE, "text_color": ft.colors.WHITE}, "x!", "π", "e"],
        ["C", "0", ".", {"text": "/", "color": ft.colors.ORANGE, "text_color": ft.colors.WHITE}, "(", ")", "⌫"]
    ]

    for row_buttons in buttons:
        row = ft.Row()
        for item in row_buttons:
            if isinstance(item, dict):  # ボタン情報が辞書型の場合、色付きボタン
                btn = ft.ElevatedButton(text=item['text'], on_click=on_button_click, width=75, height=75, color=item['text_color'], bgcolor=item['color'],expand=True)
            else:
                btn = ft.ElevatedButton(text=item, on_click=on_button_click, width=75, height=75,expand=True)
            row.controls.append(btn)
        page.add(row)

    btn_add = ft.FilledButton(text="新しい式を追加", on_click=lambda e: add_expression(autofocus=True))
    page.add(btn_add)
    page.add(history_view)

    add_expression(autofocus=True)

if __name__ == "__main__":
    ft.app(target=main,view=ft.WEB_BROWSER)
