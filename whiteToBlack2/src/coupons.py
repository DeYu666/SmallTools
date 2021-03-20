import config, requests, json, re, time
from aiocqhttp import MessageSegment


def is_coupons(content):
    # 优惠卷链接命令
    pattern = "￥؋‎฿₿¢₡₵$₫֏€₲₾₴₭₺₼₥₦₱£﷼‎៛₽₨௹₹৲৳૱₪₸₮₩¥₳₠₢₯₣₤₶₧₰₷"
    pattern = "([" + pattern + "])" + "(\\w+)\\1"
    result = re.compile(pattern).findall(content)
    if len(result) > 0:
        return True
    else:
        return False


def print_goods(goods_info):
    result = ""
    for key in goods_info.keys():
        result += goods_info[key] + "\n " if key == "dtitle" and goods_info[key] else ""
        result += "【推荐理由】: " + goods_info[key] + "\n " if key == "desc" and goods_info[key] else ""
        result += "【原价】: " + goods_info[key] + "\n " if key == "originalPrice" and goods_info[key] else ""
        result += "【卷后价】: " + goods_info[key] + "\n " if key == "actualPrice" and goods_info[key] else ""
        result += "【优惠卷数量】: " + goods_info[key] + "\n " if key == "couponReceiveNum" and goods_info[key] else ""
        result += "【日销售量】: " + goods_info[key] + "\n " if key == "dailySales" and goods_info[key] else ""
        result += "【优惠卷链接】: " + goods_info[key] + "\n " if key == "couponLink" and goods_info[key] else ""
        result += "【淘口令】: " + goods_info[key] + "\n" if key == "tpwd" and goods_info[key] else ""
        result += "【优惠卷信息】: " + goods_info[key] + "" if key == "couponInfo" and goods_info[key] else ""
    return result


async def coupons(bot, event):
    print("群组id: " + str(event.group_id))
    if event.group_id in config.white_list:  # 群组白名单
        await bot.send(event, "您配吗？")


async def coupons_group(bot, event):
    if event.group_id in config.white_list:  # 群组白名单
        url = config.url_coupons_alimama_parse_taokouling_get_goods
        params = {"content": event.message}

        res = requests.get(url=url, params=params)
        goods = json.loads(res.content)
        await bot.send(event, print_goods(goods), at_sender=True)


def coupons_send_one_goods(bot, order):
    url = config.url_coupons_alimama_get_one_goods + str(order) + "/"
    res = requests.get(url=url)
    goods = json.loads(res.content)

    # 获取商品图片链接
    url_pic = ""
    if goods['marketingMainPic']:
        url_pic = goods['marketingMainPic']
    elif goods['mainPic']:
        url_pic = goods['mainPic']

    message = print_goods(goods)
    for q in config.LOOP_LIST:
        if url_pic:
            img = MessageSegment.image(url_pic)
            bot.sync.send_group_msg(group_id=q, message=img + "\n" + message)
        else:
            bot.sync.send_group_msg(group_id=q, message=message)

    time.sleep(config.loop_coupons_alimama_time)
    pass

