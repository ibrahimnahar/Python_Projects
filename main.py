import tkinter as tk
from tkinter import ttk
from libretranslatepy import LibreTranslateAPI

lt = LibreTranslateAPI("https://translate.argosopentech.com/")

langauge_data = lt.languages()
print(langauge_data)

app = tk.Tk()
app.geometry("700x400")
