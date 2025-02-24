import tkinter as tk
from tkinter import ttk

#Root of the App
window = tk.Tk()
window.title('FridgeChef')
window.geometry("600x600")
window.minsize(600, 600)

#Styling ttk widgets
style = ttk.Style()
style.theme_use('classic') # Any style other than aqua.

style.configure("new.TFrame", background='#022b5f')

base = ttk.Frame(window)
base.pack(expand=True,fill='both')


frame1 = ttk.Frame(base,padding=8, style="new.TFrame")
frame2 = ttk.Frame(base)

frame1.place(x=0, y = 0, relwidth=0.4, relheight=1)
frame2.place(relx=0.4, y=0, relwidth=0.6, relheight=1)
ttk.Label(frame1, text="Hello", background= 'red').pack(expand=True, fill = 'both')
ttk.Label(frame2, text="bye", background= 'blue').pack(expand=True, fill = 'both')


#The program runs here
window.mainloop()