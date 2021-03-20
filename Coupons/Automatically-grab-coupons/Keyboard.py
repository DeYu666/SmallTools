from pynput.keyboard import Key, Controller

keyboard = Controller()


def knock(zm):
    keyboard.press(zm)
    keyboard.release(zm)

def openKnock(zm):
    keyboard.press(zm)

def closeKnock(zm):
    keyboard.release(zm)

# https://www.jianshu.com/p/6c818ef1ef5e