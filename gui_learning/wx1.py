"""
    Learning about how construct a simple GUI with wxpython
"""
import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, id, title, size, style):
        super(MainWindow, self).__init__(parent=parent, id=id, title=title, size=size, style=style)
        self.Centre()
        self.run()

    def run(self):
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    main_window = MainWindow(None, 999, 'Example GUI', (800, 600), wx.DEFAULT_FRAME_STYLE)
    app.MainLoop()
