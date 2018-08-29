from tkinter import *

def dialog():
	win = Toplevel()
	Label(win, text='Hard drive reformatted').pack()
	Button(win, text='OK', command=win.quit).pack()
	win.protocol('WM_DELETE_WINDOW', win.quit)

	win.focus_set()
	win.grab_set()
	win.mainloop()			#quit跳出此mainloop
	win.destroy()			#跳出mainloop后应该把窗口销毁，不然窗口依然存在！
	print('dialog exit!')

root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()
