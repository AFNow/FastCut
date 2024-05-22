import customtkinter # UI library
import tkinter


import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(BASE_DIR, 'resources/icon.ico')
#font_path = os.path.join(BASE_DIR, 'font.ttf')
#theme_path = os.path.join(BASE_DIR, 'theme.json')

# Main Window settings
Fast_Cut = customtkinter.CTk()
Fast_Cut.title('FastCut')
rootHeight = 500
rootWidth = 1000

# Theme settings
customtkinter.set_appearance_mode('dark') 
Fast_Cut.iconbitmap(icon_path)

def show_side_frame():
    side_frame.configure(relwidth=0.3)

# Background frame settings
background = customtkinter.CTkFrame(master= Fast_Cut, width= rootWidth, height= rootHeight, fg_color="black")
background.pack(fill='both', expand=True)


side_frame = customtkinter.CTkFrame(master= background, width= 300, height= rootHeight, corner_radius=0, fg_color="#131324", border_color='black')
side_frame.place(x=0, y=0, anchor=tkinter.NW, relx=0.0, rely=0.0, relwidth=0, relheight=1)


button = customtkinter.CTkButton(master= background, text="button", fg_color="#131324", command= show_side_frame)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# The window and grid settings
Fast_Cut.geometry(str(rootWidth) + 'x' + str(rootHeight))
Fast_Cut.attributes('-alpha', 1.0)

background.grid_rowconfigure(0, weight=1)
background.grid_columnconfigure(0, weight=1)
background.grid_columnconfigure(1, weight=1)
background.grid_columnconfigure(2, weight=1)
background.grid_columnconfigure(3, weight=1)

# Mainloop start
Fast_Cut.mainloop()