import re
from simplepygui import FloatBox


class Calculator:
    def __init__(self):
        self.expression = ""
        self.window = FloatBox("Calculadora FloatBox",
                               width=380, height=580, bg="#111")
        self.window.add_label(
            "display",
            "0",
            x=10,
            y=10,
            width=360,
            height=120,
            font=("Arial", 32, "bold"),
            fg="#7CFC00",
            bg="#000",
        )

        buttons = [
            ("C", 10, 140, 80, 70, "#FF6B6B"),
            ("√", 100, 140, 80, 70, "#FFD93D"),
            ("%", 190, 140, 80, 70, "#FFD93D"),
            ("//", 280, 140, 80, 70, "#FFD93D"),
            ("÷", 10, 220, 80, 70, "#FFD93D"),
            ("7", 100, 220, 80, 70, "#E9E9E9"),
            ("8", 190, 220, 80, 70, "#E9E9E9"),
            ("9", 280, 220, 80, 70, "#E9E9E9"),
            ("×", 10, 300, 80, 70, "#FFD93D"),
            ("4", 100, 300, 80, 70, "#E9E9E9"),
            ("5", 190, 300, 80, 70, "#E9E9E9"),
            ("6", 280, 300, 80, 70, "#E9E9E9"),
            ("-", 10, 380, 80, 70, "#FFD93D"),
            ("1", 100, 380, 80, 70, "#E9E9E9"),
            ("2", 190, 380, 80, 70, "#E9E9E9"),
            ("3", 280, 380, 80, 70, "#E9E9E9"),
            ("+", 10, 460, 80, 70, "#FFD93D"),
            ("0", 100, 460, 170, 70, "#E9E9E9"),
            (".", 280, 460, 80, 70, "#E9E9E9"),
            ("^", 10, 540, 170, 70, "#FFD93D"),
            ("=", 190, 540, 170, 70, "#6BCB77"),
        ]

        for text, x, y, width, height, bg in buttons:
            self.window.add_button(
                name=text,
                text=text,
                x=x,
                y=y,
                width=width,
                height=height,
                bg=bg,
                fg="#000",
                command=lambda value=text: self.on_button_click(value),
            )

    def on_button_click(self, value: str):
        if value == "C":
            self.clear()
            return
        if value == "=":
            self.calculate_result()
            return
        if value == "√":
            self.calculate_sqrt()
            return
        if value in {"÷", "×", "^", "//", "%", "+", "-"}:
            self.append_operator(value)
            return
        self.append_digit(value)

    def append_digit(self, value: str):
        if self.expression == "0":
            self.expression = value
        else:
            self.expression += value
        self.update_display()

    def append_operator(self, operator: str):
        if not self.expression:
            return
        if self.expression.endswith(("+", "-", "*", "/", "%")):
            self.expression = self.expression[:-1]

        symbol_map = {"÷": "/", "×": "*", "^": "**", "//": "//"}
        self.expression += symbol_map.get(operator, operator)
        self.update_display()

    def calculate_sqrt(self):
        try:
            value = self.safe_eval(self.expression)
            if value is None or value < 0:
                raise ValueError
            self.expression = str(value ** 0.5)
            self.update_display(raw=True)
        except Exception:
            self.show_error()

    def calculate_result(self):
        try:
            result = self.safe_eval(self.expression)
            self.expression = str(result)
            self.update_display(raw=True)
        except Exception:
            self.show_error()

    def safe_eval(self, expression: str):
        if not expression:
            return 0
        cleaned = expression.replace(" ", "")
        if not re.fullmatch(r"[0-9\.\+\-\*\/\%()]+", cleaned):
            raise ValueError("Expressão inválida")
        return eval(cleaned, {"__builtins__": None}, {})

    def update_display(self, raw: bool = False):
        if raw:
            display_text = self.expression
        else:
            display_text = self.expression.replace("**", "^")
        if not display_text:
            display_text = "0"
        self.window.set_text("display", display_text)

    def clear(self):
        self.expression = ""
        self.window.set_text("display", "0")

    def show_error(self):
        self.window.set_text("display", "Erro")
        self.expression = ""

    def run(self):
        self.window.run()


if __name__ == "__main__":
    Calculator().run()
