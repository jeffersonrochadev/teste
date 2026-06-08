import tkinter as tk
from typing import Callable


class FloatBox:
    def __init__(self, title: str = "FloatBox", width: int = 360, height: int = 520, bg: str = "#111"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.root.configure(bg=bg)
        self.widgets = {}
        self.bg = bg

    def add_label(
        self,
        name: str,
        text: str,
        x: int,
        y: int,
        width: int,
        height: int,
        font=("Arial", 24),
        fg: str = "#FFFFFF",
        bg: str | None = None,
        anchor: str = "e",
    ):
        bg = bg if bg is not None else self.bg
        label = tk.Label(
            self.root,
            text=text,
            font=font,
            fg=fg,
            bg=bg,
            anchor=anchor,
            relief="flat",
        )
        label.place(x=x, y=y, width=width, height=height)
        self.widgets[name] = label
        return label

    def add_button(
        self,
        name: str,
        text: str,
        x: int,
        y: int,
        width: int,
        height: int,
        command: Callable[[], None],
        font=("Arial", 18),
        fg: str = "#000000",
        bg: str = "#DDD",
    ):
        button = tk.Button(
            self.root,
            text=text,
            font=font,
            fg=fg,
            bg=bg,
            command=command,
            relief="raised",
            bd=2,
        )
        button.place(x=x, y=y, width=width, height=height)
        self.widgets[name] = button
        return button

    def set_text(self, name: str, text: str):
        widget = self.widgets.get(name)
        if widget is not None:
            widget.config(text=text)

    def get_text(self, name: str) -> str:
        widget = self.widgets.get(name)
        if widget is None:
            return ""
        return str(widget.cget("text"))

    def run(self):
        self.root.mainloop()
