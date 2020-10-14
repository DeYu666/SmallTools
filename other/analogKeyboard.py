'''
    模拟键盘敲击
'''

from pynput.keyboard import Key, Controller

keyboard = Controller()

# 模拟敲击键盘上的字母
def knock(zm):
    keyboard.press(zm)
    keyboard.release(zm)


# 参考链接
# https://www.jianshu.com/p/6c818ef1ef5e