import tkinter as tk
from PIL import Image,ImageTk
class homepage(object):

	def __init__(self):
		self.createUI()
		self.db = None


	def seehotel(self):
		pass

	def writereview(self):
		pass

	def createUI(self):
		top = tk.Tk()
		top.geometry('600x600')

		canvasWidth = 600
		canvasHeight = 600
		canvas = tk.Canvas(top,width=canvasWidth,height=canvasHeight)
		image = Image.open("homepage.jpg")
		backgroundImage = ImageTk.PhotoImage(image)

		frame1 = tk.Frame()
		frame1.place(x=0,y=0,relwidth=1,relheight=1)

		label = tk.Label(frame1, image=backgroundImage, bd = 2, font=("Courier", 30), text = "HOME", fg = "green", padx = 1.0, pady = 1.0, width = 10, height = 5)
		label.place(x=0,y=1,relwidth=1,relheight=1)
		canvas.pack()

		label = tk.Label(frame1, bd = 2, font=("Courier", 50), text = "HOME",fg = "black", padx = 20, pady = 40)
		label.pack()

		hotelbutton = tk.Button(frame1, font=("Ariel", 40), text = "SEE HOTEL", fg = "green", padx = 15, pady = 10,width=11,height=3)
		hotelbutton.pack()
		reviewbutton = tk.Button(frame1, font=("Ariel", 40), text = "WRITE REVIEW", fg = "green", padx = 15, pady = 10,width=11,height=3)
		reviewbutton.pack()

		top.mainloop()



hpg = homepage()