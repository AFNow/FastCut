import customtkinter # UI library

import pytube # YouTube Downloader

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(BASE_DIR, 'resources/icon.ico')


# Main Window settings
Fast_Cut = customtkinter.CTk()
Fast_Cut.resizable(width=False, height=False)
Fast_Cut.title('FastCut')
rootHeight = 600
rootWidth = 1200

# Theme settings
customtkinter.set_appearance_mode('dark') 
Fast_Cut.iconbitmap(icon_path)





# Background frame settings
background = customtkinter.CTkFrame(master=Fast_Cut, width=rootWidth, height=rootHeight, fg_color="black")
background.pack(fill='both', expand=True)

# Download bar settings
download_bar = customtkinter.CTkProgressBar(master=background, width=500, height=20, fg_color="#131324", progress_color='#6558FF')
download_bar.place(anchor = 'center', relx = 0.5, rely = 0.42)

# Link entry settings
link_entry = customtkinter.CTkEntry(master=background, width=500, height=30, placeholder_text="Enter link", fg_color='#131324')
link_entry.place(anchor = 'center', relx = 0.5, rely = 0.5)

# Download button settings
button = customtkinter.CTkButton(master=background, text="Download", fg_color="#131324", command=None)
button.place(anchor= 'center', relx = 0.5, rely = 0.6)

# The window and grid settings
Fast_Cut.geometry(f'{rootWidth}x{rootHeight}')
Fast_Cut.attributes('-alpha', 1.0)

background.grid_rowconfigure(0, weight=1)
background.grid_columnconfigure(0, weight=1)
background.grid_columnconfigure(1, weight=1)
background.grid_columnconfigure(2, weight=1)
background.grid_columnconfigure(3, weight=1)

# Mainloop start
Fast_Cut.mainloop()