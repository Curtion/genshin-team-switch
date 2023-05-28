import os
import time
import pyautogui
import tkinter as tk

def checkGenshinMain():
    img_Q = os.path.join(os.path.dirname(__file__), '../icon/E.png')
    img_E = os.path.join(os.path.dirname(__file__), '../icon/Q.png')

    img_Q_O = pyautogui.locateOnScreen(img_Q, confidence=0.98)
    img_E_O = pyautogui.locateOnScreen(img_E, confidence=0.98)
    
    return img_Q_O != None and img_E_O != None

def checkGenshinTeam():
    img_left = os.path.join(os.path.dirname(__file__), '../icon/left.png')
    img_right = os.path.join(os.path.dirname(__file__), '../icon/right.png')

    img_left_Q = pyautogui.locateOnScreen(img_left, confidence=0.98)
    img_right_Q = pyautogui.locateOnScreen(img_right, confidence=0.98)
    
    return img_left_Q != None and img_right_Q != None

def teamList():
    list = []
    img_none = os.path.join(os.path.dirname(__file__), '../icon/none.png')
    img_none_Os = pyautogui.locateAllOnScreen(img_none, confidence=0.98)
    for img_none_O in img_none_Os:
        list.append(img_none_O)
    img_active = os.path.join(os.path.dirname(__file__), '../icon/active.png')
    img_active_Os = pyautogui.locateOnScreen(img_active, confidence=0.98)
    if img_active_Os != None:
        list.append(img_active_Os)
    img_old_active = os.path.join(os.path.dirname(__file__), '../icon/old_active.png')
    img_old_active_Os = pyautogui.locateOnScreen(img_old_active, confidence=0.98)
    if img_old_active_Os != None:
        list.append(img_old_active_Os)
    list.sort(key=lambda x: x.left)
    active_index = 0
    for i in range(len(list)):
        if list[i].left == img_active_Os.left:
            active_index = i
            break
    return list, active_index

def next():
    img_right = os.path.join(os.path.dirname(__file__), '../icon/right.png')
    img_right_Os = pyautogui.locateOnScreen(img_right, confidence=0.98)
    if img_right_Os != None:
        pyautogui.click(img_right_Os)
        return True
    return False

def prev():
    img_left = os.path.join(os.path.dirname(__file__), '../icon/left.png')
    img_left_Os = pyautogui.locateOnScreen(img_left, confidence=0.98)
    if img_left_Os != None:
        pyautogui.click(img_left_Os)
        return True
    return False

def ok():
    img_ok = os.path.join(os.path.dirname(__file__), '../icon/ok.png')
    img_ok_Os = pyautogui.locateOnScreen(img_ok, confidence=0.98)
    if img_ok_Os != None:
        pyautogui.click(img_ok_Os)
    time.sleep(0.2)
    pyautogui.press("esc")
    return True

def checkSuccess(taregt):
    _, index = teamList()
    return index + 1 == taregt

def setTarget(target):
    list, index = teamList()
    current = index + 1

    if target > len(list):
        msg("目标位置超出范围!")
        pyautogui.press("esc")
        time.sleep(0.2)
        return

    count = 0
    direction = ''

    if current > target:
        a = current - target
        b = len(list) - abs(current - target)
        if a < b:
            count = a
            direction = 'prev'
        else:
            count = b
            direction = 'next'
    else:
        a = target - current
        b = len(list) - abs(target - current)
        if a < b:
            count = a
            direction = 'next'
        else:
            count = b
            direction = 'prev'

    for _ in range(count):
        time.sleep(0.1)
        if direction == 'next':
            next()
        else:
            prev()

    time.sleep(0.1)
    
def msg(msg):
    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry("800x55+560+915")
    root.attributes("-alpha", 0.6)
    root.wm_attributes('-topmost', 1)
    root.resizable(False, False)
    label = tk.Label(root, text=msg, font=("Arial", 28), justify="center")
    label.pack()
    root.after(500, lambda: root.destroy())
    root.mainloop()