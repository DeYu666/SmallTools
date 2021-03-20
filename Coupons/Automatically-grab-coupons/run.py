from setting import *
from browser_api import *
from entity_api import *
from QQ import *
from Keyboard import *

LONG_SLEEP = 10000

PAGE_SLEEP = 8

GOODS_SLEEP = 8

SEND_SLEEP = 300

OTHER_SLEEP = 1

def sendQQ():
    qq=sendMsg(qq_receiver)
    qq.sendmsg()


def goods_error(browser):

    for i in range(1, 10):
        try:
            browser = entry_frame(browser,'/html/body/div['+ str(i) +']/div[2]/iframe')
            move_simulation(browser,'nc_1_n1z', 1)
            sleep(PAGE_SLEEP)
            break
        except Exception as e:
            pass



def get_Goods_Juan(browser, tittle_xpath, goods_xpath):
    print("1")
    # 点击“高佣大额券”
    browser = click_element(browser, tittle_xpath)
    sleep(PAGE_SLEEP)
    print("2")
    # 移动到商品位置
    browser = scroll_element(browser, goods_xpath + '/a/img')
    sleep(OTHER_SLEEP)
    print("3")

    # 悬停在图片上
    hover_mouse(browser, goods_xpath + '/a/img')
    sleep(OTHER_SLEEP)
    print("4")

    # 点击“我要推广”
    browser = click_element(browser, goods_xpath + '/div/span/a')
    sleep(GOODS_SLEEP)
    print("5")

    # 点击“一键复制”
    browser = click_element_byId(browser, 'J_copy_all')
    sleep(GOODS_SLEEP)
    print("6")

    
    # # 后退
    # browser.back()
    # sleep(GOODS_SLEEP)

    # 返回
    
    for i in range(0, 10):
        try:   
            browser = click_element(browser, "/html/body/div["+ str(i) +"]/div/a")
            sleep(GOODS_SLEEP)
            try:
                browser = click_element(browser,'//*[@id="nocaptcha"]/div/span/a')
                sleep(LONG_SLEEP)
                print("一点取消")
                break
            except Exception as e:
                # 求救
                pass
        except Exception as e:
            pass    

    return browser










def alimama():
    # 打开阿里妈妈
    browser = create_browser(login_url)

    sleep(PAGE_SLEEP)

    # 进入输入账户和密码的框
    browser = entry_frame(browser,'/html/body/div/div/div[2]/div/div/div[2]/div/iframe')

    # 输入用户名 和 密码
    input_simulation(browser,'/html/body/div[1]/div/div[2]/div/form/div[1]/div[2]/input', username)
    sleep(OTHER_SLEEP)
    input_simulation(browser,'/html/body/div[1]/div/div[2]/div/form/div[2]/div[2]/input', passwd)
    sleep(OTHER_SLEEP)

    while True:
        # 检查滑动验证
        if has_move(browser):
            move_simulation(browser,'nc_1_n1z')
        try:
            # 查看滑动是否失败，若失败，则重新滑动
            browser = click_element(browser,'//*[@id="nocaptcha-password"]/div/span/a')
        except Exception as e:
            break
        sleep(PAGE_SLEEP)



    # 点击登录
    browser = click_element(browser,'/html/body/div[1]/div/div[2]/div/form/div[4]/button')
    sleep(PAGE_SLEEP)

    # 进入后台
    browser = click_element(browser,'/html/body/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/a')
    sleep(PAGE_SLEEP)


    # 点击“我要推广”
    browser = click_element(browser,'/html/body/div[2]/div[4]/div/div[2]/div[1]/ul/li[3]/a')
    sleep(PAGE_SLEEP)


    while True:
        # “高佣大额券” 的xpath
        tittle_xpath = '/html/body/div[1]/div/div[4]/div[1]/div/div/div[2]/div[3]/div'

        for i in range(1,61):
            try:
                print("进入选择商品")
                goods_xpath =  '/html/body/div[1]/div/div[4]/div[1]/div/div/div[3]/div/div[2]/div/div[1]/div/span['+ str(i) +']/div/div/div[1]'
                
                browser = get_Goods_Juan(browser, tittle_xpath, goods_xpath)
                qq=sendMsg(qq_receiver)
                qq.sendmsg()
            except Exception as e:
                try:
                    # 间隙滑动验证
                    goods_error(browser)

                except Exception as e:
                    # 报错
                    pass
        try:
            browser = click_element(browser,'/html/body/div[1]/div/div[4]/div[1]/div/div/div[3]/div/div[2]/div/div[2]/div/div/ul/li[6]/a')
        except Exception as e:
            # 求救
            pass






def get_one_Juan():
    knock("w")
    sleep(GOODS_SLEEP)
    knock("e")
    sleep(GOODS_SLEEP)
    knock("r")
    sleep(GOODS_SLEEP)
    knock("m")
    sleep(GOODS_SLEEP)
    knock("n")
    sleep(GOODS_SLEEP)
    knock("b")
    sleep(GOODS_SLEEP)
    knock(Key.f2)
    sleep(GOODS_SLEEP)
    knock("v")
    sleep(GOODS_SLEEP)
    knock("c")
    sleep(GOODS_SLEEP)
    knock("q")
    sleep(OTHER_SLEEP)
    knock("q")
    sleep(OTHER_SLEEP)


def get_many_Juan():
    openApp('LDPlayerMainFrame', "云即玩雷电摸拟器")
    knock("1")
    sleep(GOODS_SLEEP)
    get_one_Juan()
    closeApp('LDPlayerMainFrame', "云即玩雷电摸拟器")
    sendQQ()
    sleep(SEND_SLEEP)
    openApp('LDPlayerMainFrame', "云即玩雷电摸拟器")
    knock("2")
    sleep(GOODS_SLEEP)
    get_one_Juan()
    closeApp('LDPlayerMainFrame', "云即玩雷电摸拟器")
    sendQQ()
    sleep(SEND_SLEEP)
    openApp('LDPlayerMainFrame', "云即玩雷电摸拟器")
    knock("3")
    sleep(GOODS_SLEEP)
    get_one_Juan()
    closeApp('LDPlayerMainFrame', "云即玩雷电摸拟器")
    sendQQ()
    sleep(SEND_SLEEP)
    openApp('LDPlayerMainFrame', "云即玩雷电摸拟器")
    knock("4")
    sleep(GOODS_SLEEP)
    get_one_Juan()
    closeApp('LDPlayerMainFrame', "云即玩雷电摸拟器")
    sendQQ()
    sleep(SEND_SLEEP)


def huashengriji():
    get_many_Juan()
    openApp('LDPlayerMainFrame', "云即玩雷电摸拟器")
    openKnock("0")
    sleep(4)
    closeKnock("0")
    closeApp('LDPlayerMainFrame', "云即玩雷电摸拟器")




if __name__ == "__main__":
    try:
        while True:
            huashengriji()  
    except Exception as e:
        print(e)




