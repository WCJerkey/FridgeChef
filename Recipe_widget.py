from PIL import Image
import customtkinter as ctk

class Recipe_widget(ctk.CTkFrame):
    def __init__(self, parent, recipe, color1, color2, textcolor, font1, font2, font3):
        super().__init__(parent, width=850, fg_color=color2)
        
        container = ctk.CTkFrame(self, fg_color=color2, width=680)
        container_image = ctk.CTkFrame(self, fg_color=color2, width=130)

        name_label = ctk.CTkLabel(container, text=recipe.name, text_color=textcolor, font=font2, width=680)
        ingredient_label = ctk.CTkLabel(container, text="Ingredients: " + ", ".join(recipe.ingredients), text_color=textcolor, font=font3, wraplength=680)
        instruction_label = ctk.CTkLabel(container, text="Instructions: " + ", ".join(recipe.instructions), text_color=textcolor, font=font3, wraplength=680)
        time_label = ctk.CTkLabel(container, text="Time: " + ", ".join(recipe.time), text_color=textcolor, font=font3, wraplength=680)


        # Load the image
        recipe_image = ctk.CTkImage(light_image=Image.open("./pictures/recipes/"+recipe.name+".png"),size=(130,130))
        image_label = ctk.CTkLabel(container_image, text="", image=recipe_image).pack()
        

        #image_label.place(relx=0.02, rely=0.06)
        #time_label.place(relx=0.2, rely=0.7)
        #instruction_label.place(relx=0.2, rely=0.5)
        #ingredient_label.place(relx=0.2, rely=0.3)
        #name_label.place(relx=0.2, rely=0.06)
        
        
        container_image.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        container.grid(row=0, column=1, padx=10, pady=10 ,sticky="nsew")
        name_label.pack()
        ingredient_label.pack()
        instruction_label.pack()
        time_label.pack()
       


    