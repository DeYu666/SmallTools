# 自动化抓取优惠券

## 需要的插件
运行花生日记，需要一个模拟器 YunGameBox ，在其中下载花生日记，并打开花生日记应用。同时设置模拟按键，设置完后，最小化应用程序
运行淘宝联盟，需要 Chrome 驱动，并放到指定位置
需要一个QQ号，并打开将要发送的群，并在 setting 文件中设置相应信息

获取应用程序的标题和类需要下载 spyxx.exe,此应用可以查看某一应用程序的标题和类

## run.py 
启动程序
首先是一些全局变量，用于控制睡眠时间
alimama 获取淘宝联盟中商品的优惠券
huashengriji 获取花生日记中的优惠券


get_Goods_Juan 获取淘宝联盟中某一个商品的优惠券
get_one_Juan 获取花生日记中某一个商品的优惠劵

## setting.py 
存放一些配置文件，或者重要信息

## QQ.py
存放着通过QQ群名称打开QQ群，并将剪切板中的信息发送出去的 sendMsg 类
openApp 和 closeApp 两个函数通过 windows 中应用程序的标题和类打开应用程序和最小化应用程序

## browser_api.py
存放着操控浏览器工作的一些函数：
    create_browser 创建浏览器窗口，并通过url打开网页
    input_simulation 通过xpah路径定位元素，在元素中模拟输入text数据
    has_move 判断当前窗口是否有滑动，（特指淘宝联盟登录页面的窗口）
    move_simulation 模拟滑动，（特指淘宝联盟登录页面的窗口）
    entry_frame 通过xpah路径定位frame元素，进入frame 中
    click_element 通过xpah路径定位元素，并点击此元素
    click_element_byId 通过 id 属性路径定位元素，并点击此元素
    hover_mouse  通过xpah路径定位元素，模拟鼠标覆盖

    copy_yhj  没有用到
    scroll_element 没有用到

## Keyboard.py
存放模拟键盘按键的一些函数：
    knock 敲击键盘上某一个键
    openKnock 按压键盘上某一个键
    closeKnock 释放按压着的某一个键

## entity_api.py
存放着一些其他小工具：
    sleep 睡眠 sec 秒