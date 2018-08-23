import sys
from tkinter import *

def hello(event):
	print('hello, please press twice to exit!')

def quit(event):
	print("Hello, I'm going...")
	sys.exit()
	
btn = Button(None, text='Hello event world')
btn.pack()
btn.bind('<Button-1>', hello)
btn.bind('<Double-1>', quit)
mainloop()
