import time, datetime
from skimage import io



def sleep(sec):
    time.sleep(sec)


def isInThisInterval(start_time,end_time):
    now = datetime.datetime.now().strftime("%H:%M")
    print("当前时间:" + now)
    if start_time < now < end_time:
        print("在此区间中")
        return True
    else:
        print('不在此区间中')
        return False


# 初始化二维数组
# m是行, n是列
def initArray(m, n):
    Array = [[0 for i in range(n)] for i in range(m)]
    return Array


def saveImgByURL(url, savePath):
    image = io.imread(url)
    io.imsave(savePath, image)  # 保存图片
    # io.imshow(image)  # 显示图片



