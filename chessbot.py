import tkinter as tk 
from tkinter import filedialog, Text
import os

root = tk.Tk()

#setup window (AKA canvas)
canvas = tk.Canvas(root, width=500, height=500, bg="#FFFFFF")
canvas.pack()

#insert img of chessboard into the canvas
bg_img=tk.PhotoImage(file = "img/board.png")
bg_label=tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()
