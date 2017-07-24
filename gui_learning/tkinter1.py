"""
    Learning about how construct a simple GUI in tkinter/Tkinter (py3.x, p2.x)
"""
try:
    from Tkinter import *
except ImportError:
    from tkinter import *


class MainWindow(Frame):
    def __init__(self, parent):
        Frame().__init__(master=parent)

if __name__ == '__main__':
    root = Tk()
    root.wm_title('Example GUI')
    main_window = MainWindow(root)
    root.mainloop()
