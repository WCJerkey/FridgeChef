from PIL import Image
import customtkinter as ctk

class Ingredient_widget(ctk.CTkButton):
    def __init__(self, parent, ingredient, color2, color3, font, list, counter):
        
        self.ingredient = ingredient
        self.image = ctk.CTkImage(light_image=Image.open("./pictures/ingredients/"+ingredient.name+".png"),size=(80, 80))
        self.text = ingredient.name 
        self.compound = "bottom"

        def add_ingredient():
            if self.ingredient in list:
                list.remove(self.ingredient)
                counter.configure(text=len(list))
                self.configure(fg_color=color2)
            else:
                list.append(self.ingredient)
                counter.configure(text=len(list))
                self.configure(fg_color=color3)
                
        #Calls the constructor of the parent class 
        super().__init__(parent, image= self.image, text=self.text, font=font, compound=self.compound, fg_color=color2, command=add_ingredient)
        
