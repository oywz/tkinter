from tkinter import *
import sys

def quit():
	print("Bye...")
	sys.exit()

root = Tk()
Button(root, text='Exit', command=quit).pack(expand=YES)
root.mainloop()