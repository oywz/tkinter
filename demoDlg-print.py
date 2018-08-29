from tkinter import *
from dialogTable import demos 
from quitter1 import Quitter 

class Demo(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		Label(self, text='Basic demos').pack()
		for key in demos:
			func = lambda key=key: self.printit(key)
			Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
		Quitter(self).pack(side=TOP, fill=BOTH)

	def printit(self, name):
		print(name, 'returns => ', demos[name]())	  #在print函数中调用其他函数

if __name__ == '__main__':
	Demo().mainloop()