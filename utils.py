import customtkinter as ctk
from Ingredient_widget import Ingredient_widget as iw
from CTkMessagebox import CTkMessagebox
from Ingredient import Ingredient
from Recipe import Recipe
from Recipe_widget import Recipe_widget

#Some config variables
color1 = "#252c30"  #Background color
color2 = "#2b563c"  #Main Theme color
color3 = "#384740" #Secondary Theme color
textcolor1 = 'white'

def instruction_box(master):
    CTkMessagebox(message="1. Select the ingredients you have.\n2. Click on the cooking pot to see available recipes.\n3. Enjoy your meal!", 
                  icon="info", 
                  title="Instructions", 
                  fg_color=color1, 
                  bg_color='#21272b', 
                  text_color='white',
                  title_color='white', 
                  master=master)
    
def coming_soon_box(master):
    CTkMessagebox(message="This function is still in development.\n\nPlease check back later for updates!", 
                  icon="warning", 
                  title="Coming Soon!", 
                  fg_color=color1, 
                  bg_color='#21272b', 
                  text_color='white',
                  title_color='white', 
                  master=master)

def load_ingredients(list):
    
    Beef = Ingredient("Beef")
    list.append(Beef)

    Black_Pepper = Ingredient("Black Pepper")
    list.append(Black_Pepper)

    Butter = Ingredient("Butter")
    list.append(Butter)

    Carrots = Ingredient("Carrots")
    list.append(Carrots)

    Eggs = Ingredient("Eggs")
    list.append(Eggs)

    Garlic = Ingredient("Garlic")
    list.append(Garlic)

    Green_Pepper = Ingredient("Green Pepper")
    list.append(Green_Pepper)

    Milk = Ingredient("Milk")
    list.append(Milk)

    Onions = Ingredient("Onions")
    list.append(Onions)

    Salt = Ingredient("Salt")
    list.append(Salt)

    Soy_Sauce = Ingredient("Soy Sauce")
    list.append(Soy_Sauce)

    Tomato_Sauce = Ingredient("Tomato Sauce")
    list.append(Tomato_Sauce)

    Oregano = Ingredient("Oregano")
    list.append(Oregano)

    Basil = Ingredient("Basil")
    list.append(Basil)

    Rice = Ingredient("Rice")
    list.append(Rice)

    Chili = Ingredient("Chili")
    list.append(Chili)

    Green_Onion = Ingredient("Green Onion")
    list.append(Green_Onion)

    Oil = Ingredient("Oil")
    list.append(Oil)

    Tomato = Ingredient("Tomato")
    list.append(Tomato)


def load_recipes(list):
    list.append(Recipe("Spaghetti",
                       ["Beef", "Onions", "Garlic", "Green Pepper", "Tomato", "Tomato Sauce","Oregano","Basil","Salt", "Pepper"],
                       ["Combine ground beef, onion, garlic, and green pepper in a large saucepan over medium-high heat."
                       "Cook and stir until meat is browned and crumbly and vegetables are tender, 5 to 7 minutes. "
                       "Drain grease.Stir diced tomatoes, tomato sauce, and tomato paste into the pan."
                       "Season with oregano, basil, salt, and pepper. "
                       "Simmer spaghetti sauce for 1 hour, stirring occasionally."
                       "Boil noodles"
                       "Combine spaghetti sauce and cooked noodles."],
                       ["10 minutes"]))
    list.append(Recipe("Fried Rice",
                       ["Rice", "Eggs", "Carrots","Soy sauce", "Onions","Green onions"],
                       ["Cook rice with soy sauce, Cut veggies and add to put with eggs, and mix"]
                       ,["10 minutes"]))
                       
    list.append(Recipe("Indian Chicken Curry",
                       ["Chicken", "Onion", 'Tomatos', "Garlic", "Chili", "Oil"],
                       ["Marinate chicken with chili, and salt.Heat oil and cloves,. Sauté onions until golden.Add garlic, ginger, green chili, and spices. Cook 1-2 mins.Add chicken, cook until browned.Add tomatoes,cook until soft.Add water, simmer 20-25 mins until chicken is tender. Serve with rice or naan"],
                       ["30 minutes"]))
                                          
    list.append(Recipe("Scrambled Eggs",
                       ["Eggs", "Milk", "Butter", "Salt", "Black Pepper"], 
                       ["First crack and whisk the eggs while adding water or milk", "Preheat the pan, and put butter or olive oil in the pan", "Lastly, Pour in the egg mixture, and let it cook for a few seconds, undisturbed. Then, pull a rubber spatula across the bottom of the pan to form large, soft curds of scrambled eggs."],
                       ["5 minutes"]))
    list.append(Recipe("Well Cooked Jerky", ["Beef", "Salt", "Soy Sauce"],["Open a grill and grill to perfection", "Then cook it to medium rare"],
                       ["15 minutes"]))


def recipe_search(ilist, rlist):
    inc_recipes = []
    for ingredient in ilist:
        for recipe in rlist:
            if ingredient.name in recipe.ingredients:
                if recipe not in inc_recipes:
                    inc_recipes.append(recipe)


    #Window stuff
    recipe_window = ctk.CTkToplevel()
    recipe_window.title("Available Recipes")
    recipe_window.geometry("900x600")
    recipe_window.minsize(900, 600)
    
    base = ctk.CTkFrame(recipe_window) 
    base.pack(expand=True,fill='both')

    my_font = ctk.CTkFont(family='Comic Sans MS', size=14, weight='bold')
    my_font2 = ctk.CTkFont(family='Comic Sans MS', size=26, weight='bold')
    my_font3 = ctk.CTkFont(family='Comic Sans MS', size=17, weight='bold')

    mainframe = ctk.CTkScrollableFrame(base, fg_color= color1, label_text="Recipes", label_fg_color=color2, label_text_color=textcolor1, label_font=my_font3, scrollbar_button_color=color2)
    mainframe.place(relx=0, rely=0, relwidth=1, relheight=1)

    if len(inc_recipes) == 0:
        no_recipes_label = ctk.CTkLabel(mainframe, text="No recipes available for the selected ingredients.", text_color=textcolor1, font=my_font3)
        no_recipes_label.pack(pady=20)

    for recipe in inc_recipes:
        recipe_widget = Recipe_widget(mainframe, recipe, color1, color2, textcolor1, my_font, my_font2, my_font3)
        recipe_widget.pack(pady=5, padx=10)