
from win32api import *
from win32gui import *
import win32con
import os
import struct
import time
from datetime import datetime,timedelta
from threading import Thread

class WindowsBalloonTip:
    def __init__(self):
        message_map = { win32con.WM_DESTROY: self.OnDestroy,}
        wc = WNDCLASS()
        self.hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = 'PythonTaskbar'
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        self.classAtom = RegisterClass(wc)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)

    def balloon_tip(self,title, msg,icon=None):
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        hwnd = CreateWindow(self.classAtom, "Taskbar",style, 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0, 0, self.hinst, None)
        UpdateWindow(hwnd)

        flags =NIF_ICON | NIF_MESSAGE | NIF_TIP
        iconPathName = os.path.abspath(icon)
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE

        if icon and os.path.exists(iconPathName) :
            hicon = LoadImage(self.hinst, iconPathName,win32con.IMAGE_ICON, 0, 0, icon_flags)
            Shell_NotifyIcon(NIM_ADD, (hwnd, 0, flags, win32con.WM_USER+20, hicon, 'Tooltip'))
            Shell_NotifyIcon(NIM_MODIFY, (hwnd, 0, NIF_INFO, win32con.WM_USER+20, hicon, 'Balloon Tooltip', msg, 200, title))
        else:
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)
            Shell_NotifyIcon(NIM_ADD, (hwnd, 0, flags, win32con.WM_USER+20, hicon, 'Tooltip'))
            Shell_NotifyIcon(NIM_MODIFY, (hwnd, 0, NIF_INFO, win32con.WM_USER+20, hicon, 'Balloon Tooltip', msg, 200, title,NIIF_INFO))




w=WindowsBalloonTip()
w.balloon_tip('Go & Study', ' minutes passed')
current= lambda : datetime.now().replace(second=0,microsecond=0)
start_time=current()
end_time=start_time+timedelta(minutes=1)

def fire_up():
    i=0
    while True:
        if current()==end_time :
                i+=1
                print i
                secc=(datetime.now()-start_time).seconds
                w.balloon_tip('Go & Study', '{}{:^.3f} minutes passed'.format(i,secc/60.0))
                time.sleep(4)
        else:
            time.sleep(1)
# fire_up()