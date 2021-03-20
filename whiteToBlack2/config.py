# 参数


# 阿里妈妈优惠卷地址
# 获取一个商品信息  http://api.asa-zhang.top/alimama/getOneGoods/1/
url_coupons_alimama_get_one_goods = "http://api.asa-zhang.top/alimama/getOneGoods/"
# 使用淘口令查询优惠卷
url_coupons_alimama_parse_taokouling_get_goods = "http://api.asa-zhang.top/alimama/test"
# 循环发送优惠卷的时间 单位是 s
loop_coupons_alimama_time = 300

# 获取笑话的地址
url_tools_get_joke = "http://api.asa-zhang.top/tools/getJoke"

# 群组白名单
white_list = [809658371,]

# 循环发送消息的群号
LOOP_LIST = [809658371, ]

# VIP 用户
SUPERUSERS = [303205844]

# 昵称
NICKNAME = ["小羊", "小萌"]

# 使用手册
MANUAL = {
    "loop": [
        "开启循环",
        "关闭循环",
        "开启优惠卷发送",
        "关闭优惠卷发送",
        "查询当前状态",

    ],

    "private": [
        "发送笑话",
        "图灵机",
        "图片",
        ""
    ],

    "group": [
        "优惠卷查询",
        "商品查询",

    ],
}



# 以下全局变量
# 发送优惠卷
LOOP_COUPONS = False
# 开启循环
LOOP = False
