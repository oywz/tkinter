from tkinter import *

def showPosEvent(event):
	print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

def showAllEvent(event):
	print(event)
	for attr in dir(event):
		if not attr.startswith('__'):
			print(attr, '=>', getattr(event, attr))

def onKeyPress(event):
	print('Got key press', event.char)

def onArrowKey(event):
	print('Got up arrow key press')

def onReturnKey(event):
	print('Got return key press')

def onLeftClick(event):
	print('Got left mouse button click:', end=' ')
	showPosEvent(event)

def onRightClick(event):
	print('Got right mouse button click', end=' ')
	showPosEvent(event)

def onMiddleClick(event):
	print('Got middle mouse button click', end=' ')
	showPosEvent(event)
	showAllEvent(event)

def onLeftDrag(event):
	print('Got left mouse button drag:', end=' ')
	showPosEvent(event)

def onDoubleLeftClick(event):
	print('Got double left mouse click', end=' ')
	showPosEvent(event)
	root.quit()

root = Tk()
labelfont = ('courier', 20, 'bold')
lbl = Label(root, text='Hello bind world')
lbl.config(bg='red', font=labelfont)
lbl.config(height=5, width=20)
lbl.pack(expand=YES, fill=BOTH)

lbl.bind('<Button-1>', onLeftClick)
lbl.bind('<Button-3>', onRightClick)
lbl.bind('<Button-2>', onMiddleClick)
lbl.bind('<Double-1>', onDoubleLeftClick)
lbl.bind('<B1-Motion>', onLeftDrag)

lbl.bind('<KeyPress>', onKeyPress)
lbl.bind('<Up>', onArrowKey)
lbl.bind('<Return>', onReturnKey)

lbl.focus()
root.title('click me')
root.mainloop()
