import tkinter as tk
from tkinter import messagebox

def calculate_height():
    try:
        v = int(entry_velocity.get())
        pHeight = float(entry_player_height.get())
        
        a = -16
        t = -v / (2 * a)
        h = (v * t) + (0.5 * a * t ** 2)
        
        totHeight = h + pHeight
        
        label_player_height_result.config(text=f"Player height: {pHeight}")
        label_total_height_result.config(text=f"Total height: {totHeight}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values")

# Create the main window
root = tk.Tk()
root.title("Basketball Height Calculator")

# Create and place the labels, entries, and button
label_velocity = tk.Label(root, text="Enter the velocity:")
label_velocity.pack()

entry_velocity = tk.Entry(root)
entry_velocity.pack()

label_player_height = tk.Label(root, text="Enter height of basketball player:")
label_player_height.pack()

entry_player_height = tk.Entry(root)
entry_player_height.pack()

button_calculate = tk.Button(root, text="Calculate Height", command=calculate_height)
button_calculate.pack()

label_player_height_result = tk.Label(root, text="Player height: ")
label_player_height_result.pack()

label_total_height_result = tk.Label(root, text="Total height: ")
label_total_height_result.pack()

# Start the Tkinter event loop
root.mainloop()

