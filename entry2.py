from tkinter import *
from quitter1 import Quitter 

fields = 'Name', 'Job', 'Pay'

def fetch(entries):
	for i in entries:
		print('Input => "%s"' % i.get())

def makeform(root, fields):
	entries = []
	for field in fields:
		row = Frame(root)
		lbl = Label(row, text=field, width=5)
		ent = Entry(row)
		row.pack(side=TOP,fill=X)
		lbl.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		entries.append(ent)
	return entries

if __name__ == '__main__':
	root = Tk()
	ents = makeform(root, fields)
	Button(root, text='Fetch', command=(lambda: fetch(ents))).pack(side=LEFT)   #command只需传入必要参数即可
	Quitter(root).pack()
	root.bind('<Return>', (lambda event: fetch(ents)))         #bind自动传递event参数
	root.mainloop()

