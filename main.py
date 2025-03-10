import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from PIL import Image
import Ingredient_widget as iw

ingredient_list = ["carrot", 'carrot', 'carrot', 'carrot']
inc_ingredients = []

ctk.set_appearance_mode("light")
#Root of the App
window = ctk.CTk()
window.title('FridgeChef')
window.geometry("600x600")
window.minsize(600, 600)

base = ctk.CTkFrame(window)
base.pack(expand=True,fill='both')



frame1 = ctk.CTkFrame(base, fg_color="#123458")
frame2 = ctk.CTkFrame(base)
bottomleft = ctk.CTkFrame(base)

frame1.place(x=0, y = 0, relwidth=0.8, relheight=1)
frame1.pack_propagate(False)

frame2.place(relx=0.8, y=0, relwidth=0.2, relheight=0.8)
bottomleft.place(relx=0.8, rely=0.8, relwidth=0.2, relheight=0.2)

#ctk.CTkLabel(frame1, text="Hello", fg_color="yellow").pack(expand=True, fill = 'both')
ctk.CTkLabel(frame2, text="test", fg_color="red").pack(expand=True, fill = 'both')



ctk.CTkButton(bottomleft, image=ctk.CTkImage(Image.open("./pictures/assets/cooking_pot.png"), size=(80, 80)), text='').pack(expand=True, fill = 'both')

for i in range(len(ingredient_list)):
    iw.Ingredient_widget(frame1, ingredient_list[i]).grid(row=(i//3), column=(i%3), padx=10, pady=10)

#The program runs here
window.mainloop()