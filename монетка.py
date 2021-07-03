import random as rdm
from tkinter import *
root = Tk()


class Main(Frame):
	def __init__(self, root):
		super(Main, self).__init__(root)
		self.start()

	def start(self):
		btn = Button(root, text="бросок", bg="black", fg="white", font=("Marker Felt", 10),
					command=lambda x=1: self.run())
		btn.place(x=122, y=110, width=60, height=25)
		
		self.lbl1 = Label(root, text="☀избавь себя от мук выбора🌙",
					bg="DarkGray", font=("Times New Roman", 14, "bold"))
		self.lbl1.place(x=5, y=10)
		self.lbl3 = Label(root, text="🦄", bg="DarkGray", font=("Times New Roman", 35, "bold"))
		self.lbl3.place(x=5, y=60)
		self.lbl4 = Label(root, text="🐲", bg="DarkGray", font=("Times New Roman", 37, "bold"))
		self.lbl4.place(x=240, y=60)
		self.lbl = Label(root, text="❶❷❶❷❶", bg="DarkGray", font=("Times New Roman", 10, "bold"))
		self.lbl.place(x=110, y=40)
		self.lbl2 = Label(root, text="подброс монетки",
					bg="DarkGray", fg="DarkGray", font=("Times New Roman", 10, "bold"))
		self.lbl2.place(x=100, y=80)

	def run(self):
		self.lbl2 = Label(root, text="подброс монетки", bg="DarkGray", fg="black")
		self.lbl2.place(x=100, y=80)
		root.after(100, self.run1)
		root.after(200, self.run2)
		root.after(300, self.run3)
		root.after(400, self.run1)
		root.after(500, self.run2)
		root.after(600, self.run3)
		root.after(1000, self.choice)

	def run1(self):
		self.lbl2 = Label(root, text="подброс монетки.", bg="DarkGray", fg="black")
		self.lbl2.place(x=100, y=80)

	def run2(self):
		self.lbl2 = Label(root, text="подброс монетки..", bg="DarkGray", fg="black")
		self.lbl2.place(x=100, y=80)

	def run3(self):
		self.lbl2 = Label(root, text="подброс монетки...", bg="DarkGray", fg="black")
		self.lbl2.place(x=100, y=80)

	def choice(self):
		flip = rdm.randint(1, 2)
		if flip == 1:
			self.lbl.configure(text="орел🐦", bg="DarkGray", font=("Impact", 20, "bold"))
		if flip == 2:
			self.lbl.configure(text="решка🐧 ", bg="DarkGray", font=("Impact", 20, "bold"))
		else:
			pass


if __name__ == '__main__':
	root.geometry("300x150")
	root.title('монетка')
	root["bg"] = "DarkGray"
	app = Main(root)
	app.pack()
	root.mainloop()
