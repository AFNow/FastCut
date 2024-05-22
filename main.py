import customtkinter # UI library
import tkinter


import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(BASE_DIR, 'resources/icon.ico')
#font_path = os.path.join(BASE_DIR, 'font.ttf')
#theme_path = os.path.join(BASE_DIR, 'theme.json')


Fast_Cut = customtkinter.CTk()
Fast_Cut.title('FastCut')
rootHeight = 500
rootWidth = 1000

customtkinter.set_appearance_mode('dark') 
Fast_Cut.iconbitmap(icon_path)


# The window and grid settings
Fast_Cut.geometry(str(rootWidth) + 'x' + str(rootHeight))
Fast_Cut.attributes('-alpha', 1.0)

Fast_Cut.grid_rowconfigure(0, weight=1)
Fast_Cut.grid_columnconfigure(1, weight=0)
Fast_Cut.grid_columnconfigure(0, weight=1)


# Mainloop start
Fast_Cut.mainloop()