import customtkinter # UI libraries

import pytube # YouTube Downloader

from threading import Thread # Threading

import moviepy # Video processing and editing

from PIL import Image, ImageTk # Pillow libraries

import os
from tkinter.filedialog import askdirectory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(BASE_DIR, 'resources/icon.ico')
font_path = os.path.join(BASE_DIR, 'resources/font.ttf')
folder_icon_path = os.path.join(BASE_DIR, 'resources/folder_icon.png')
download_icon_path = os.path.join(BASE_DIR, 'resources/download_icon.png')
save_path = BASE_DIR

# Default path settings
def set_default_path():
    global save_path
    save_path = askdirectory(title='Select a place to save', initialdir=BASE_DIR)
    print(save_path)

# Main Window settings
Fast_Cut = customtkinter.CTk()
Fast_Cut.resizable(width=True, height=True)
Fast_Cut.title('FastCut')
rootHeight = 600
rootWidth = 1200
Fast_Cut.minsize(rootWidth, rootHeight)
#Fast_Cut.maxsize(rootWidth+200, rootHeight+200)

# Theme settings
customtkinter.set_appearance_mode('dark') 
Fast_Cut.iconbitmap(icon_path)
normal_font = customtkinter.CTkFont(family=font_path, size=16, weight='normal')
bold_font = customtkinter.CTkFont(family=font_path, size=16, weight='bold')


# Link checking function for call a video title
def link_check():
    link = link_entry.get()
    if link != "":
        try:
            yt = pytube.YouTube(link, on_progress_callback = None)
            video_title = yt.title
            video_title_label.configure(text = video_title)
        except pytube.exceptions.RegexMatchError:
            video_title_label.configure(text = "Wrog link")
# Threading for link checking
def link_check_thread(event):
    thread = Thread(target = link_check, daemon = True)
    thread.start()
    return thread


# Progress bar function
def progress_bar(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    download_progress_bar.set((round(pct_completed))/100)
    print(f"Status: {round(pct_completed)} %")
    link_entry.configure(state='disabled')
    if pct_completed == 100:
        video_title_label.configure(text = "Download complete")
        link_entry.place(anchor = 'center', relx = 0.5, rely = 0.89)
        link_entry.configure(state='normal')
        video_frame_call()
        download_progress_bar.set(0)
        download_progress_bar.place(anchor = 'center', relx = 0.5, rely = 0.89)  
# Download function
def download(save_path):
        url = link_entry.get()
        link_entry.delete(0, 'end')
        yt = pytube.YouTube(url, on_progress_callback=progress_bar)
                            #use_oauth=True,                                      # use_oauth=True if you want to use OAuth
                            # allow_oauth_cache=None                              # allow_oauth_cache=True if you want to use OAuth
        out = yt.streams\
            .filter(progressive=True, file_extension='mp4')\
            .order_by('resolution')\
            .desc()\
            .first()\
            .download(save_path)
        print(yt.title)
        print(f"Download complete: {out}")
# Download button callback
def download_button():
    if save_path != "":
        #print('Path is ready')
        try:
            download_thread(save_path)
            link_entry.place_forget()
        except:
            print('Something went wrong')
    else:
        print('Path is None')
# Threading for downloading
def download_thread(save_path):
    thread = Thread(target = download, args=(save_path,), daemon = True)
    thread.start()
    return thread


    
def video_frame_call():
    y_position = 300
    video_frame.grid(column=1, row=1, columnspan=3, rowspan=2, sticky='nswe', ipady= 30)
    #video_frame.place(anchor='center', relx = 0.5, y = y_position)
    #def video_frame_animation():
    #    nonlocal y_position
    #    if y_position >= 0.4:
    #        y_position -= 0.1
    #        video_frame.place(anchor='n', relx = 0.5, y = y_position)
    #        Fast_Cut.after(10, lambda: video_frame_animation())     
    #video_frame_animation()



# Background frame settings
background = customtkinter.CTkFrame(master=Fast_Cut, width=rootWidth, height=rootHeight, fg_color="black")
background.pack(fill='both', expand=True)

# Lower frame settings
lower_frame = customtkinter.CTkFrame(master=background, width=520, height=300, fg_color="black", border_color="#6558FF", border_width=2)
lower_frame.place(relx=0.5, rely=0.98, anchor='n')

def call_lower_frame_func():
    y_position = 0
    def lower_frame_call_animation():
        nonlocal y_position
        if y_position >= -120:
            y_position -= 10
            lower_frame.place(anchor='n', relx = 0.5, y = y_position)
            Fast_Cut.after(10, lambda: lower_frame_call_animation())
            if y_position <= -120:
                hide_lower_frame_button.place(anchor= 'n', relx = 0.5, rely = 0)     
    lower_frame_call_animation()

def hide_lower_frame_func():
    y_position = -130
    def lower_frame_hide_animation():
        nonlocal y_position
        if y_position <= -10:
            y_position += 10
            lower_frame.place(anchor='n', relx = 0.5, y = y_position)
            Fast_Cut.after(10, lambda: lower_frame_hide_animation())
            if y_position >= 0:
                hide_lower_frame_button.place_forget()
                call_lower_frame_button.place(anchor= 'n', relx = 0.5, rely = 0)
    lower_frame_hide_animation()
            
        

call_lower_frame_button = customtkinter.CTkButton(master=lower_frame, width=520, height=25, text="", fg_color="#131324", command=call_lower_frame_func)
call_lower_frame_button.place(anchor= 'n', relx = 0.5, rely = 0)

hide_lower_frame_button = customtkinter.CTkButton(master=lower_frame, width=520, height=25, text="", fg_color="#131324", command=hide_lower_frame_func)

# Download bar settings
download_progress_bar = customtkinter.CTkProgressBar(master=lower_frame, width=500, height=20, fg_color="#131324", progress_color='#6558FF')
download_progress_bar.set(0)
download_progress_bar.place(anchor = 'center', relx = 0.5, rely = 0.27)

# Video Title settings
video_title_label = customtkinter.CTkLabel(master=lower_frame, text='VIDEO TITLE', bg_color="#131324", fg_color="#131324", text_color="#6558FF", font=bold_font, width=500, height=30)
video_title_label.place(anchor = 'center', relx = 0.5, rely = 0.15)

# Link entry settings
link_entry = customtkinter.CTkEntry(master=lower_frame, width=500, height=30, placeholder_text="Enter link", fg_color='#131324',)
link_entry.place(anchor = 'center', relx = 0.5, rely = 0.27)
link_entry.bind("<KeyRelease>", link_check_thread)

# Path button settings
path_button_image = customtkinter.CTkImage(Image.open(folder_icon_path), size=(20, 20))
path_button = customtkinter.CTkButton(master=lower_frame, width=30, text="", fg_color="#131324", command=set_default_path, image=path_button_image)
path_button.place(anchor= 'e', relx = 0.98, rely = 0.4)

# Download button settings
download_button_image = customtkinter.CTkImage(Image.open(download_icon_path), size=(20, 20))
download_button = customtkinter.CTkButton(master=lower_frame, width=30, text="", fg_color="#131324", command=download_button, image=download_button_image)
download_button.place(anchor= 'w', relx = 0.02, rely = 0.4)

show_player_debug = customtkinter.CTkButton(master=background, width=30, text="", fg_color="#131324", command=video_frame_call)
show_player_debug.place(anchor= 'w', relx = 0.02, rely = 0.2)

# Video Player Frame settings
video_frame = customtkinter.CTkFrame(master=background, width=900, height=460, fg_color="grey3", corner_radius=10)

# The window and grid settings
Fast_Cut.geometry(f'{rootWidth}x{rootHeight}')
Fast_Cut.attributes('-alpha', 1.0)

background.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
background.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

# Mainloop start
Fast_Cut.mainloop()


# TODO: Add progress bar --- Done
# TODO: Progress Bar need to appear on the link entry, and disable after finishing download --- Done

# TODO: Figure out how to use OAuth in my interface for age restricted videos
# TODO: Add frame for video, that will apear from the bottom of the window
# TODO: Change the interface positions areas, make it more flexible with allowed windos's size option https://youtu.be/p7I92IMFa3c?si=PdSvvNBtIwEC7Msz