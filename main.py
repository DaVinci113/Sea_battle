from tkinter import *
from tkinter import messagebox
import time


tk = Tk()
app_run = True
size_canvas_x = 1448
size_canvas_y = 655
size_table=10
step_table=size_canvas_y//(1.25*size_table)
indent_x=10
indent_y=30

def draw_table():
	for i in range(size_table+1):
		canvas.create_line(indent_x+step_table*i, indent_y, indent_x+step_table*i, indent_y+step_table*size_table)
	for i in range(size_table+1):
		canvas.create_line(indent_x, indent_y+step_table*i, indent_x+step_table*size_table, indent_y+step_table*i)

def on_closing():
	global app_run
	if messagebox.askokcancel("Выход из игры", "Вы хотите выйти?"):
		app_run = False
		tk.destroy()
	
#tk.protocol("WM_DELETE_WINDOW", on_closing())
tk.title("Sea battle")
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.pack()

draw_table()

def add_all(event):
	_type=0
	if event == 3:
		_type=1
	mouse_x = canvas.winfo_pointerx()-canvas.winfo_rootx()-indent_x
	mouse_y = canvas.winfo_pointery()-canvas.winfo_rooty()-indent_y
	ip_x=mouse_x//step_table
	ip_y=mouse_y//step_table
	
canvas.bind_all("<Button-1>", add_all)
canvas.bind_all("<Button-3>", add_all)

while app_run:
	tk.update_idletasks()
	tk.update()
	time.sleep(1)
