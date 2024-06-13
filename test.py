import tkinter
import tkinter.filedialog as filedialog
from moviepy.editor import VideoFileClip
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self):
        self.clip = None

        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root)
        self.canvas.pack()

        self.menu = tkinter.Menu(self.root)
        self.root.config(menu=self.menu)
        self.file_menu = tkinter.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open Video", command=self.open_video)

    def open_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            if self.clip:
                self.clip.reader.close()
            self.clip = VideoFileClip(file_path)
            self.canvas.config(width=self.clip.size[0],
                height=self.clip.size[1])

    def play(self):
        if self.clip:
            try:
                frame = self.clip.get_frame(self.clip.duration * self.canvas.coords(self.img)[0] / self.canvas.winfo_width())
            except:
                self.clip.reader.close()
                self.clip = None
                return
            im = Image.fromarray(frame)
            self.photo = ImageTk.PhotoImage(im)
            self.canvas.itemconfig(self.img, image=self.photo)
        self.root.after(30, self.play)

    def run(self):
        if self.clip:
            self.img = self.canvas.create_image(0, 0, anchor=tkinter.NW)
        self.play()
        self.root.mainloop()

player = VideoPlayer()
player.run()