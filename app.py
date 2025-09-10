import tkinter as tk
from datetime import datetime

# Create window
root = tk.Tk()
root.title("My Tkinter App")

# Set window size
root.geometry("400x200")
root.configure(bg="black")

# Add a clock label
def update_time():
    now = datetime.now().strftime("%H:%M:%S")
    label.config(text=now)
    root.after(1000, update_time)

label = tk.Label(root, text="", font=("Helvetica", 40), fg="white", bg="black")
label.pack(expand=True)

# Start clock update
update_time()

# Run the window
root.mainloop()
