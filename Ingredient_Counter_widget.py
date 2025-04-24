import customtkinter as ctk

class Ingredient_Counter(ctk.CTkFrame):
    def __init__(self, parent, color, list, font, textcolor):
        

        super().__init__(parent, corner_radius=100, width=30, height=30, fg_color=color)

        self.counter = ctk.CTkLabel(self, text=len(list), font=font, text_color=textcolor)
        self.counter.pack()