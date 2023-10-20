import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

def close_splash():
    window.destroy()

window = tk.Tk()
window.geometry("710x340")
tk.Entry(window).pack()
window.focus_force()
bg_image = Image.open("splach2.jpg")  # Replace with your image file
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)
background_image = ImageTk.PhotoImage(bg_image)

# Create a Label widget to display the image
background_label = tk.Label(window, image=background_image)
background_label.pack()

duration = 7000
window.after(duration, close_splash)

# Retain the reference to the image globally
window.image = background_image

window.mainloop()
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
'''
def calculate_calories(species, weight, age, activity_level):
    calorie_factors = {
        'dog': 110,
        'cat': 100,
        'rabbit': 30,  # Adjust these values as needed
    }

    if species not in calorie_factors:
        return "Invalid species"

    mer = (weight ** 0.75) * calorie_factors[species]

    if age < 1:
        mer *= 3
    elif age <= 7:
        mer *= 1.6
    else:
        mer *= 1.2

    if activity_level == 'sedentary':
        mer *= 1.2
    elif activity_level == 'moderate':
        mer *= 1.5
    elif activity_level == 'active':
        mer *= 2.0

    return mer

def get_info():
    species = species_entry.get().lower()
    weight = float(weight_entry.get())
    age = float(age_entry.get())
    activity_level = activity_entry.get().lower()

    calories = calculate_calories(species, weight, age, activity_level)

    if isinstance(calories, str):
        result_label.config(text=calories)
    else:
        result_label.config(text=f"Estimated daily calorie requirement: {calories:.2f} kcal")

root = tk.Tk()
root.title("Animal Information")
root.geometry("710x340")
bg_image = Image.open("mam.jpg")  # Replace with your image file
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

frame = ttk.Frame(root, padding=10)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

species_label = ttk.Label(frame, text="Enter the species (dog, cat, rabbit):")
species_entry = ttk.Entry(frame)

weight_label = ttk.Label(frame, text="Enter the weight of the animal in kilograms:")
weight_entry = ttk.Entry(frame)

age_label = ttk.Label(frame, text="Enter the age of the animal in years:")
age_entry = ttk.Entry(frame)

activity_label = ttk.Label(frame, text="Enter the activity level (sedentary, moderate, active):")
activity_entry = ttk.Entry(frame)

submit_button = ttk.Button(frame, text="Submit", command=get_info)
result_label = ttk.Label(frame, text="")

species_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
species_entry.grid(row=0, column=1, padx=10, pady=5)

weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
weight_entry.grid(row=1, column=1, padx=10, pady=5)

age_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
age_entry.grid(row=2, column=1, padx=10, pady=5)

activity_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
activity_entry.grid(row=3, column=1, padx=10, pady=5)

submit_button.grid(row=4, column=0, columnspan=2, pady=10)
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

