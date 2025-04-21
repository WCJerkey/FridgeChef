from PIL import Image
import customtkinter as ctk

class Recipe_widget(ctk.CTkFrame):
    def __init__(self, parent, recipe, color1, color2, textcolor, font1, font2, font3):
        super().__init__(parent, width=850, height=150, fg_color=color2)
        
        name_label = ctk.CTkLabel(self, text=recipe.name, text_color=textcolor, font=font2)
        name_label.place(relx=0.2, rely=0.06)
        ingredient_label = ctk.CTkLabel(self, text="Ingredients: " + ", ".join(recipe.ingredients), text_color=textcolor, font=font3)
        ingredient_label.place(relx=0.2, rely=0.3)
        
        recipe_image = ctk.CTkImage(light_image=Image.open("./pictures/recipes/"+recipe.name+".png"),size=(130,130))
        image_label = ctk.CTkLabel(self, text="", image=recipe_image)
        image_label.place(relx=0.02, rely=0.06)

    