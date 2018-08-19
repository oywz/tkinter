from tkinter import *
from random import randint

def randquest(ops):
	if ops == '+':
		a, b = randint(1, 10), randint(1, 10)
	elif ops == '-':
		a, b = randint(10, 20), randint(1, 10)
	elif ops == 'x':
		a, b = randint(1, 10), randint(1, 10)
	return "{} {} {} = ".format(a, ops, b), a+b

def ask():
	msg.config(text=randquest('+'))

def check():
	ans = var.get()
	if ans == int(randquest('+')[1]):
		count += 1
		var.set('')
		msg.config(text=randquest('+'))
	else:
		var.set('')


count = 0
var = IntVar()

root = Tk()
frame = Frame(root) 
frame.pack()
msg = Message(frame, text=randquest('+'))
msg.pack(side=LEFT)
ent = Entry(frame).pack(side=RIGHT)
ent.config(textvariable=var)
Button(root, text='出题', command=ask).pack()

root.mainloop()

