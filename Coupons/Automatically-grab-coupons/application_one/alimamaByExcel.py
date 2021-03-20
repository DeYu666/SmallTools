from entity import *


def getGoodsInfo(data_json, info):
    datas = initArray(200, 6)
    i = 0
    for key in data_json:
        for j in range(0, len(info)):
            datas[i][j] = data_json[key][info[j]]
        i += 1
    return datas


def printGoodsInfo(data):
    goods_detail = str(data[1]) + "\n " + \
                    "【在售价】：￥" + data[2] + "\n " + \
                    "【券后价】：" + str(float(data[2]) - float(data[3])) + "\n " + \
                    "【推荐理由】 领" + str(data[3]) + "元独家券，包邮秒杀！\n " + \
                    "【下单口令】" + str(data[5]) + "\n " + \
                    "【下单链接】" + str(data[4]) + "\n "
    return goods_detail