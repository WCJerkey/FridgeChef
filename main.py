import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from utils import load_ingredients, load_recipes, recipe_search

import math

from PIL import Image
import Ingredient_widget as iw
import Ingredient_Counter_widget as icw

#This is the main file of the app

#Some config variables
color1 = "#252c30"  #Background color
color2 = "#2b563c"  #Main Theme color
color3 = "#384740" #Secondary Theme color
textcolor1 = 'white'


#Setting the appearance mode or "theme"
ctk.set_appearance_mode("light")

#Root of the App
window = ctk.CTk()
window.title('FridgeChef')
window.geometry("820x600")
window.minsize(820, 600)


#Some variables
ingredient_list = []
inc_ingredients = []
recipe_list = []

load_ingredients(ingredient_list)
load_recipes(recipe_list)


#Variable storing the font for future use
my_font = ctk.CTkFont(family='Comic Sans MS', size=14, weight='bold')


#Creating the base frame
base = ctk.CTkFrame(window)
base.pack(expand=True,fill='both')


#Creating different frames 
frame1 = ctk.CTkFrame(base, fg_color=color1)
frame2 = ctk.CTkFrame(base,fg_color=color1)
bottomleft = ctk.CTkFrame(base, fg_color=color1)
mainframe = ctk.CTkScrollableFrame(frame1, fg_color= color1, label_text="Ingredients", label_fg_color=color2, label_text_color=textcolor1, label_font=my_font, scrollbar_button_color=color2)


#Setting the frames
frame1.place(x=0, y = 0, relwidth=0.8, relheight=1)
frame1.pack_propagate(False)
frame2.place(relx=0.8, y=0, relwidth=0.2, relheight=0.8)
bottomleft.place(relx=0.8, rely=0.8, relwidth=0.2, relheight=0.2)
mainframe.place(relx=0, rely=0, relwidth=1, relheight=1)


#Creating the widgets
ctk.CTkLabel(frame2, text="LET'S COOK",font= my_font,).pack(expand=True, fill = 'both')
ctk.CTkButton(bottomleft,image=ctk.CTkImage(Image.open("./pictures/assets/cooking_pot.png"), size=(80, 80)), text='', fg_color=color2, command= lambda: recipe_search(inc_ingredients,recipe_list)).pack(expand=True, fill = 'both')

counter_widget = icw.Ingredient_Counter(bottomleft, color2, inc_ingredients, my_font, textcolor1)
counter_widget.place(relx=0.8, rely=0.8, anchor='center')

for i in range(len(ingredient_list)):
    iw.Ingredient_widget(mainframe, ingredient_list[i], color2, color3, my_font, inc_ingredients, counter_widget.counter).grid(row=(i//4), column=(i%4), padx=10, pady=10)

#The program runs here
window.mainloop()