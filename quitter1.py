from tkinter import *
# from sys import exit
from tkinter.messagebox import askokcancel

class Quitter(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		Button(parent, text='QUIT', command=self.quit).pack(side=LEFT, expand=YES, fill=BOTH)


	def quit(self):
		if askokcancel('verify', 'Do you want to quit?'):
			Frame.quit(self)
			# exit()

if __name__ == '__main__':
	Quitter().mainloop()


