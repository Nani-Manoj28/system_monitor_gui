import tkinter as tk
from tkinter import ttk
import psutil

# Create main window
root = tk.Tk()
root.title("System Monitor Dashboard")
root.geometry("400x300")
root.resizable(False, False)

# Title Label
title = tk.Label(root, text="System Monitor", font=("Arial", 16, "bold"))
title.pack(pady=10)

# CPU Section
cpu_label = tk.Label(root, text="CPU Usage", font=("Arial", 12))
cpu_label.pack()

cpu_progress = ttk.Progressbar(root, orient="horizontal",
                                length=300, mode="determinate")
cpu_progress.pack(pady=5)

# RAM Section
ram_label = tk.Label(root, text="RAM Usage", font=("Arial", 12))
ram_label.pack()

ram_progress = ttk.Progressbar(root, orient="horizontal",
                                length=300, mode="determinate")
ram_progress.pack(pady=5)

# Disk Section
disk_label = tk.Label(root, text="Disk Usage", font=("Arial", 12))
disk_label.pack()

disk_progress = ttk.Progressbar(root, orient="horizontal",
                                 length=300, mode="determinate")
disk_progress.pack(pady=5)
refresh_button = tk.Button(root, text="Refresh Now", command=lambda: update_usage())
refresh_button.pack(pady=5)

# Update Function
def update_usage():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    if disk > 80:
        title.config(text="High Disk Usage!", fg="red")
    elif cpu > 80:
        title.config(text="High CPU Usage!", fg="red")
    else:     
        title.config(text="System Monitor", fg="black")

    cpu_progress['value'] = cpu
    ram_progress['value'] = ram
    disk_progress['value'] = disk

    cpu_label.config(text=f"CPU Usage: {cpu}%")
    ram_label.config(text=f"RAM Usage: {ram}%")
    disk_label.config(text=f"Disk Usage: {disk}%")
    root.after(1000, update_usage)  # Update every second

# Start updating
update_usage()

# Run app
root.mainloop()