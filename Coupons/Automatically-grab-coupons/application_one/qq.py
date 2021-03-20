"""
    自动发送QQ消息

    环境： windows7
    软件： python3 、QQ

    条件：1、登录 QQ
          2、打开将要发送消息的群.(必须要将窗口依次排列，请勿多窗口放在一起)
          3、运行此 python 文件
"""

import win32gui
import win32con
import win32clipboard as w
import win32com.client



def openApp(class_name,name):
    hwnd = win32gui.FindWindow(class_name,name)
    win32gui.ShowWindow(hwnd,win32con.SW_SHOWNORMAL)


def closeApp(class_name,name):
    hwnd = win32gui.FindWindow(class_name,name)
    win32gui.ShowWindow(hwnd,win32con.SW_MINIMIZE)


# 将内容放到剪贴版
def setText(text):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, text)
    w.CloseClipboard()


class sendMsg():
    def __init__(self,receiver):
        self.receiver=receiver
        

    #发送消息
    def sendmsg(self):
        qq=win32gui.FindWindow(None,self.receiver)
        win32gui.SendMessage(qq,win32con.WM_PASTE , 0, 0)
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

