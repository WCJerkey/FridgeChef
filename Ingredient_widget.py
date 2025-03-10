from PIL import Image
import customtkinter as ctk


class Ingredient_widget(ctk.CTkButton):
    def __init__(self, parent, name):
        
        self.image = ctk.CTkImage(light_image=Image.open("./pictures/ingredients/"+name+".png"), size=(80, 80))
        self.text = name 
        self.compound = "bottom"

        super().__init__(parent, image= self.image, text=self.text, compound=self.compound, fg_color="#225081")
        self.pack(side="left", anchor="nw")
        
