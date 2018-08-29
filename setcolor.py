from tkinter import *
from tkinter.colorchooser import askcolor

def changecolor():
	triple, hexstr = askcolor()			#最好不要直接使用索引，因为可能返回空值，会抛出异常
	if hexstr:				
		print(hexstr)
		btn.config(bg=hexstr)

root = Tk()
btn = Button(root, text='test change color', command=changecolor)
btn.pack()
root.mainloop()





