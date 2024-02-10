import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import cv2

# Assuming you have the function to get available camera indices


# Create the Tkinter window
root = tk.Tk()
root.title("Camera Options")

# Get the available camera options
camera_options = get_available_cameras()

# Create an OptionMenu with the camera options
camera_var = tk.StringVar(root)
camera_var.set(camera_options[0])  # Set the default value
camera_dropdown = tk.OptionMenu(root, camera_var, *camera_options)
camera_dropdown.pack()

root.mainloop()
