"""GUI的基本框架——module1"""

import wx
import PyQt5


# noinspection PyPep8Naming
from wx import Frame


class c_Frame( wx.Frame ):
    """docstring"""

    def __init__( self, parent, title ):
        wx.Frame.__init__( self,
                           parent,
                           title = title,
                           pos = (500, 200),
                           size = (400, 200)
                           )
        self = wx.Frame( parent,
                         title = title,
                         pos = (500, 200),
                         size = (400, 200)
                         )
        panel = wx.Panel( self, pos = (50, 20), size = (400, 100) )
        text1 = wx.TextCtrl( panel, value = "Hello, \\nWorld!", size = (200, 100) )
        self.Show( True )


if __name__ == '__main__':
    app = wx.App( )
    frame = c_Frame( None, "Example" )
    app.MainLoop( )

# app = wx.App()
# frame = wx.Frame(None,title='helloworld')
# frame.Show(True)
# app.MainLoop()
