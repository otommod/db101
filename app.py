import wx


class Window(wx.Frame):
    def __init__(self, foo):
        self.foo = foo

    def on_click(self, event):
        self.foo.show_gif(event)
