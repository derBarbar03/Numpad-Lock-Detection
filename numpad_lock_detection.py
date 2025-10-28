import ctypes
import time
import tkinter as tk
from threading import Thread

def get_numlock_state():
    return bool(ctypes.WinDLL("User32.dll").GetKeyState(0x90))

def show_popup():
    root = tk.Tk()
    root.title("Num Lock Warning")
    root.geometry("300x100")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates for the window to be centered
    x = (screen_width // 2) - (300 // 2)
    y = (screen_height // 2) - (100 // 2)

    root.geometry(f"{300}x{100}+{x}+{y}")
    
    root.resizable(False, False)
    root.attributes("-topmost", True)
    label = tk.Label(root, text="Num Lock is OFF!", font=("Arial", 14), fg="red")
    label.pack(pady=20)
    # Auto-close after 5 seconds
    root.after(5000, root.destroy)
    root.mainloop()

def monitor_numlock():
    while True:
        if not get_numlock_state():
            Thread(target=show_popup).start()
        time.sleep(60)  # Wait for 1 minute

if __name__ == "__main__":
    monitor_numlock()
