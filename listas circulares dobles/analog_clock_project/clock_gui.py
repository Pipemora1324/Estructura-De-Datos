# clock_gui.py

import tkinter as tk
import math
import time
import datetime
from clock_linked_list import HourClockList

# Constants
WIDTH = 400
HEIGHT = 450
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
RADIUS = 150

# Theme colors
theme = {
    "light": {"bg": "white", "fg": "black"},
    "dark": {"bg": "black", "fg": "white"}
}
current_theme = "light"

# Create window
root = tk.Tk()
root.title("Analog Clock - Lista Circular Doble")

# Canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=theme[current_theme]["bg"])
canvas.pack()

# Linked list for clock hours
clock = HourClockList()
clock.create_clock()

# Digital time label
digital_label = tk.Label(root, font=("Helvetica", 12), bg=theme[current_theme]["bg"], fg=theme[current_theme]["fg"])
digital_label.pack()

# Date label
date_label = tk.Label(root, font=("Helvetica", 10), bg=theme[current_theme]["bg"], fg=theme[current_theme]["fg"])
date_label.pack()

# Flags for optional features
show_digital = False
show_date = False

# Draw hour numbers
def draw_clock_numbers():
    node = clock.head
    angle_step = 360 / 12
    angle = -60
    for _ in range(12):
        rad = math.radians(angle)
        x = CENTER_X + math.cos(rad) * (RADIUS - 20)
        y = CENTER_Y + math.sin(rad) * (RADIUS - 20)
        canvas.create_text(x, y, text=str(node.hour), font=("Helvetica", 14, "bold"), fill=theme[current_theme]["fg"], tags="hands")
        node = node.next
        angle += angle_step

# Get coordinates for hand
def get_hand_coords(angle_deg, length):
    rad = math.radians(angle_deg)
    x = CENTER_X + math.cos(rad) * length
    y = CENTER_Y + math.sin(rad) * length
    return CENTER_X, CENTER_Y, x, y

# Update clock
def update_clock():
    canvas.delete("hands")

    current_time = time.localtime()
    hour = current_time.tm_hour % 12
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Angles
    second_angle = (second / 60) * 360 - 90
    minute_angle = (minute / 60) * 360 - 90
    hour_angle = ((hour + minute / 60) / 12) * 360 - 90

    # Hands
    canvas.create_line(*get_hand_coords(hour_angle, 60), width=5, fill=theme[current_theme]["fg"], tags="hands")
    canvas.create_line(*get_hand_coords(minute_angle, 90), width=3, fill="blue", tags="hands")
    canvas.create_line(*get_hand_coords(second_angle, 110), width=1, fill="red", tags="hands")

    draw_clock_numbers()
    canvas.create_oval(CENTER_X - 5, CENTER_Y - 5, CENTER_X + 5, CENTER_Y + 5, fill=theme[current_theme]["fg"], tags="hands")

    if show_digital:
        digital_label.config(text=time.strftime("%H:%M:%S", current_time))
    else:
        digital_label.config(text="")

    if show_date:
        now = datetime.datetime.now()
        date_label.config(text=now.strftime("%A, %d %B %Y"))
    else:
        date_label.config(text="")

    root.after(1000, update_clock)

# Toggle theme
def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    canvas.config(bg=theme[current_theme]["bg"])
    digital_label.config(bg=theme[current_theme]["bg"], fg=theme[current_theme]["fg"])
    date_label.config(bg=theme[current_theme]["bg"], fg=theme[current_theme]["fg"])
    update_clock()

# Toggle digital time
def toggle_digital():
    global show_digital
    show_digital = not show_digital

# Toggle date
def toggle_date():
    global show_date
    show_date = not show_date

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

btn_theme = tk.Button(button_frame, text="Cambiar Tema", command=toggle_theme)
btn_theme.grid(row=0, column=0, padx=5)

btn_digital = tk.Button(button_frame, text="Mostrar Hora Digital", command=toggle_digital)
btn_digital.grid(row=0, column=1, padx=5)

btn_date = tk.Button(button_frame, text="Mostrar Fecha", command=toggle_date)
btn_date.grid(row=0, column=2, padx=5)

# Start
draw_clock_numbers()
update_clock()
root.mainloop()
