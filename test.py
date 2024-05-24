import customtkinter # UI library
import tkinter
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(BASE_DIR, 'resources/icon.ico')

# Main Window settings
Fast_Cut = customtkinter.CTk()
Fast_Cut.title('FastCut')
rootHeight = 500
rootWidth = 1000

# Theme settings
customtkinter.set_appearance_mode('dark') 
Fast_Cut.iconbitmap(icon_path)


# Background frame settings
background = customtkinter.CTkFrame(master=Fast_Cut, width=rootWidth, height=rootHeight, fg_color="black")
background.pack(fill='both', expand=True)


# Side_Panel cless
class SidePanel(customtkinter.CTkFrame):
	def __init__(self, master, start_position, end_position):
		super().__init__(master = master)

		# Launch settings 
		self.start_position = start_position
		self.end_position = end_position
		self.width = abs(start_position - end_position)

        # Animation
		self.pos = self.start_position
		self.in_start_position = True

		# layout
		self.place(relx = self.start_position, rely = 0.05, relwidth = self.width, relheight = 0.9)

	def animate(self):
		if self.in_start_position:
			self.animate_forward()
		else:
			self.animate_backwards()

	def animate_forward(self):
		if self.pos > self.end_position:
			self.pos -= 0.008
			self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
			self.after(10, self.animate_forward)
		else:
			self.in_start_pos = False

	def animate_backwards(self):
		if self.pos < self.start_pos:
			self.pos += 0.008
			self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
			self.after(10, self.animate_backwards)
		else:
			self.in_start_pos = True
side_panel = SidePanel(background, 1.0, 0.2)

button = customtkinter.CTkButton(master=background, text="button", fg_color="#131324", command=side_panel.animate)
button.pack(pady=20)

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