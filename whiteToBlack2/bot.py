from aiocqhttp import CQHttp, Event

from src.coupons import coupons, coupons_group, is_coupons, coupons_send_one_goods
from src.common import is_manual,is_command, private_manual,private_command
import glo

bot = CQHttp()
glo._init()


# 发送优惠卷
glo.set_value("LOOP_COUPONS", False)
# 开启循环
glo.set_value("LOOP", False)


# 私聊
@bot.on_message('private')
async def _(event: Event):
    global LOOP_COUPONS, LOOP

    if is_manual(event.message):
        await private_manual(bot, event)
    elif is_command(event.message):
        await private_command(bot, event, event.message)
    else:
        await bot.send(event, '你发了：')
        return {'reply': event.message}


# 群聊
@bot.on_message('group')
async def handle_msg(event):
    # print(event)
    if is_coupons(event.message):
        await coupons_group(bot, event)


# 循环事件
@bot.on_message
def sync_handle_msg(event):
    # print(event)
    LOOP = glo.get_value("LOOP")
    if event.user_id == 303205844 and event.message_type == "private" and event.message == "开启循环" and not LOOP:
        bot.sync.send_private_msg(user_id=event.user_id, message='我已经开启了循环模式')
        # 设置开始循环
        glo.set_value("LOOP", True)

        i = 1
        while glo.get_value("LOOP", False):
            if glo.get_value("LOOP_COUPONS", False):
                coupons_send_one_goods(bot, i)

            # 如果没有循环任务，则关闭循环
            else:
                glo.set_value("LOOP", False)
                break
            i += 1 if i < 100 else 1
            print(glo.get_value("LOOP"), i)

    if event.user_id == 303205844 and event.message_type == "private" and event.message == "关闭循环" and LOOP:
        bot.sync.send_private_msg(user_id=event.user_id, message='我已经关闭了循环模式')
        # 设置关闭循环
        glo.set_value("LOOP", False)


bot.run(host='127.0.0.1', port=8080)

