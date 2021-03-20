import requests, json

from config import MANUAL, SUPERUSERS
import config, glo


def is_manual(content):
    key_words = ['使用手册', '你能做什么', '帮助']
    for k in key_words:
        if k in content:
            return k
    return False


def is_command(content):
    for key in MANUAL.keys():
        if content in MANUAL[key]:
            return True
    return False


def current_state():

    result_state = ""

    if glo.get_value("LOOP"):
        result_state += "   循环发送已开启 \n"
    else:
        result_state += "   循环发送已关闭 \n"

    if glo.get_value("LOOP_COUPONS"):
        result_state += "   优惠卷发送已开启"
    else:
        result_state += "   优惠卷发送已关闭"

    return result_state


async def private_manual(bot, event):
    message_manual = ""
    for key in MANUAL.keys():
        if key == "loop" and event.user_id in SUPERUSERS:
            message_manual += "循环指令: \n    "
            message_manual += "\n    ".join(MANUAL[key])
            message_manual += "\n\n"
        if key == "private":
            message_manual += "私聊指令: \n    "
            message_manual += "\n    ".join(MANUAL[key])

    await bot.send(event, message_manual)


async def private_command(bot, event, command):
    print("--- private_command ---  " + str(command) + "  ---")

    message = ""
    # 普通命令
    if command == "发送笑话":
        message = get_joke()
    elif command == "图片":
        message = "图片生产中...."
    elif command == "":
        message = ""

    # 超级用户命令
    elif event.user_id in SUPERUSERS:
        if command == "开启优惠卷发送":
            message = "优惠卷发送已开启"
            glo.set_value("LOOP_COUPONS", True)
        elif command == "关闭优惠卷发送":
            message = "优惠卷发送已关闭"
            glo.set_value("LOOP_COUPONS", False)
        elif command == "查询当前状态":
            message = "当前状态为 \n\n"
            message += current_state()
    else:
        message = "你说的是人话么？"

    await bot.send(event, message)


def get_joke():
    url = config.url_tools_get_joke
    res = requests.get(url=url)
    joke = json.loads(res.content)
    return joke['content']
