import customtkinter # UI libraries
from tkinter.filedialog import askdirectory

import pytube # YouTube Downloader

from threading import Thread

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

#def progress_bar_function(stream, chunk, bytes_remaining):
#    download_bar.set(float(stream.filesize - bytes_remaining) / stream.filesize * 100)
#    download_bar.update()

save_path = BASE_DIR
def set_default_path():
    global save_path
    save_path = askdirectory(title='Select a place to save', initialdir=BASE_DIR)

def download(save_path):
        link = link_entry.get()
        link_entry.delete(0, 'end')
        yt = pytube.YouTube(link, on_progress_callback = None)                     # progress_bar_function
                            # on_complete_callback=None                            # on_complete_editing_function
                            # use_oauth=None,                                      # use_oauth=True if you want to use OAuth
                            # allow_oauth_cache=None                               # allow_oauth_cache=True if you want to use OAuth
        print(yt.title)
        stream = yt.streams.first()
        stream.download(save_path)
        print('Downloaded')

def download_button():
    global save_path
    if save_path != "":
        print('Path is ready')
        try:
            download_thread(save_path)
        except:
            print('Something went wrong')
    else:
        print('Path is None')

# Threading for downloading
def download_thread(save_path):
    thread = Thread(target = download, args=(save_path,), daemon = True)
    thread.start()
    return thread



# Background frame settings
background = customtkinter.CTkFrame(master=Fast_Cut, width=rootWidth, height=rootHeight, fg_color="black")
background.pack(fill='both', expand=True)

# Download bar settings
download_bar = customtkinter.CTkProgressBar(master=background, width=500, height=20, fg_color="#131324", progress_color='#6558FF')
download_bar.place(anchor = 'center', relx = 0.5, rely = 0.42)

# Link entry settings
link_entry = customtkinter.CTkEntry(master=background, width=500, height=30, placeholder_text="Enter link", fg_color='#131324',)
link_entry.place(anchor = 'center', relx = 0.5, rely = 0.5)

path_button = customtkinter.CTkButton(master=background, width=50, text="Path", fg_color="#131324", command=set_default_path)
path_button.place(anchor= 'center', relx = 0.687, rely = 0.6)

# Download button settings
button = customtkinter.CTkButton(master=background, text="Download", fg_color="#131324", command=download_button)
button.place(anchor= 'center', relx = 0.35, rely = 0.6)

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