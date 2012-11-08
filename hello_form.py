#-*- coding: cp950 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'My Test Frame Fro Python',size=(1000,600))
        panel = wx.Panel(self,-1)
        button = wx.Button(panel,label="壽敕",pos=(125,10),size=(50,30))
        self.lbl = wx.StaticText(panel,-1,"Pos:",pos=(125,60))
        self.posCtrl = wx.TextCtrl(panel,-1,"",pos=(160,60))
        self.btnTest = wx.Button(panel,-1,"萸僻",pos=(125,100),size=(50,20))
        self.txtTest = wx.TextCtrl(panel,-1,"",(123,130))
        self.spin = wx.SpinCtrl(panel,-1,"",(125,170))
        self.spin.SetRange(1,100)
        self.spin.SetValue(1)


        self.Bind(wx.EVT_BUTTON,self.OnCloseMe,button)
        self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
        panel.Bind(wx.EVT_MOTION,self.OnMove,panel)
        self.Bind(wx.EVT_BUTTON,self.OnBtnClick,self.btnTest)
        
    def OnCloseMe(self,event):
        self.Close(True)
    def OnCloseWindow(self,event):
        self.Destroy()
    def OnMove(self,event):
        pos = event.GetPosition()        
        self.posCtrl.SetValue(str(pos.x)+','+ str(pos.y))
    def OnBtnClick(self,event):
        wx.Execute('notepad')
        wx.MessageBox("context","title")

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()

