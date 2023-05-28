
import threading
import time
from utils.mod import *
import keyboard
import pyautogui
import pystray
from PIL import Image
from pystray import MenuItem

def on_hotkey(key):
    on_hotkey_run(key)

def on_hotkey_run(key):
    target = 0
    if key == 0:
        target = 10
    else:
        target = key
    msg("开始切换至队伍:{}".format(target))
    genshins = pyautogui.getWindowsWithTitle('原神')
    if len(genshins) == 0:
        msg("原神没有运行!")
        return

    genshin = genshins[0]
    try:
        genshin.activate()
    except:
        genshin.minimize()
        genshin.maximize()
        genshin.restore()
    time.sleep(0.5)
    
    if checkGenshinTeam() == False:
        for i in range(4):
            main = checkGenshinMain()
            if main == False:
                msg("原神不处于主页,尝试ESC第{}次".format(i+1))
                pyautogui.press("esc")
                time.sleep(1)
                if i == 3:
                    msg("请进入原神主页!")
                    return
            else:
                pyautogui.press("l")
                time.sleep(4)
                break
    
    setTarget(target)
    if checkSuccess(target) == False:
        for i in range(3):
            msg("切换至队伍:{}失败,重试中...".format(target))
            setTarget(target)
            if checkSuccess(target) == True:
                break
            else:
                msg("切换失败,重试第{}次".format(i+1))
    ok()
    time.sleep(1)
    msg("成功切换至队伍:{}".format(target))

def listener():
    for i in range(10):
        keyboard.add_hotkey('alt+' + str(i), on_hotkey, args=(i,))
    keyboard.wait()

t = threading.Thread(target=listener)
t.daemon = True
t.start()

def on_exit(icon, item):
    icon.stop()

def on_about(icon, item):
    msg("Alt+数字键切换队伍", time=3000)

menu = (MenuItem('帮助', action=on_about),MenuItem('退出', action=on_exit))
icon = os.path.join(os.path.dirname(__file__), './icon/right.png')
image = Image.open(icon)
icon = pystray.Icon("name", image, "原神队伍切换工具", menu)
icon.run()
