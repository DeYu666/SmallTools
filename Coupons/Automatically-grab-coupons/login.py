from selenium import webdriver
import os, time, json, random
from selenium.webdriver.common.action_chains import ActionChains



DEBUG = True
COOKIE_FILE = './conf/cookie.txt'
COOKIE_TIME_FILE = './conf/cookie_time.txt'
# 登陆地址
login_url = 'http://pub.alimama.com/'



# 模拟输入
def _input_simulation(e, text):
    for i in range(len(text)):
        sleep_time = random.randint(8, 30)
        time.sleep(int(sleep_time / 10))
        e.send_keys(text[i])

# 判断是否有滑动
def _has_move(device):
    yanzhen = device.find_element_by_id('nocaptcha-password')
    style = yanzhen.get_attribute('style')
    if style == 'display: block;':
        return True
    return False


# 模拟滑动
def _move_simulation(device, e):
    try:
        action = ActionChains(device)
        action.click_and_hold(e).perform()
        print('2')
        offset = 40
        for i in range(int(320 / offset)):
            ActionChains(device).move_by_offset(xoffset=offset, yoffset=0).perform()
            time.sleep(int((offset - i) / 50))
        action.release().perform()
        action.reset_actions()
    except Exception as e:
        if DEBUG: print(e)



browser = webdriver.Chrome()
browser.maximize_window()
browser.get(login_url)

time.sleep(5)
print("1")

# 阿里妈妈登录
# static_button = browser.find_element_by_id('mx_114_alimama')
# static_button.click()
# time.sleep(random.uniform(2, 5))
# browser.switch_to.frame(browser.find_element_by_xpath("//*[@id='mx_109']/iframe"))
# _input_simulation(browser.find_element_by_xpath('//*[@id="J_logname"]'), '17635158631')

# 淘宝账户登录
browser.switch_to.frame(browser.find_element_by_xpath("//*[@id='mx_109']/iframe"))
_input_simulation(browser.find_element_by_xpath('//*[@id="fm-login-id"]'), '17635158631')
time.sleep(random.uniform(0.2, 2))
_input_simulation(browser.find_element_by_xpath('//*[@id="fm-login-password"]'), 'zdy1314')
time.sleep(random.uniform(0.2, 2))

# 检查滑动验证 display: block;
while True:
    if _has_move(browser):
        print('有滑动验证 ================ ')
        _move_simulation(browser, browser.find_element_by_id('nc_1_n1z'))
        time.sleep(2)

        try:
            browser.find_element_by_xpath('//*[@id="nocaptcha-password"]/div/span/a').click()
        except Exception as e:
            break
    print("循环第几遍")

browser.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

print(browser.get_cookies())
cookies = {item["name"]: item["value"] for item in browser.get_cookies()}

try:
    with open(COOKIE_FILE, 'w') as f:
        f.write(json.dumps(cookies))
    with open(COOKIE_TIME_FILE, 'w') as f:
        f.write(str(int(time.time())))
except Exception as e:
    print("file error", e)


temp_cookies = browser.get_cookies()



def copy_yhj(browser,xpath_url):
    try:
        browser.find_element_by_xpath(xpath_url).click()
        time.sleep(1)
        print("3")
        # browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="_oid_ifr_"]'))
        browser.find_element_by_xpath('//*[@id="J_copy_all"]').click()
        time.sleep(1)
    except Exception as e:
        if DEBUG: print(e)
    


browser.switch_to.window(browser.window_handles[-1])
# 优惠券地址
yhj_gao_url = 'https://pub.alimama.com/promo/search/index.htm?fn=gao'



try:
    browser.add_cookie(temp_cookies)
    browser.get(yhj_gao_url)

    # for i in range(100, 500):
    #     xpath = "//*[@id=mx_"+str(i)+"]/a"
    #     copy_yhj(browser,xpath)

    xpath = '//*[@id="mx_174"]/a'
    copy_yhj(browser,xpath)

except  Exception as e:
    print("cookies add error" , e)

    while True:
        try:
            time.sleep(3)        
            browser.find_element_by_xpath('//*[@id="mx_109"]/div/div[2]/div[2]/a').click()
            time.sleep(3)
            browser.find_element_by_xpath('//*[@id="magix_vf_header"]/div/div[2]/div[1]/ul/li[3]/a').click()
            time.sleep(3)
            browser.find_element_by_xpath('//*[@id="_magix_router_view_uid_4"]/div/div[2]/div[3]/div').click()
            time.sleep(3)
            ActionChains(browser).move_to_element(browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div[3]/div/div[2]/div/div[1]/div/span[2]')).perform()
            browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div/div/div[3]/div/div[2]/div/div[1]/div/span[2]/div/div/div[1]/div/span/a').click()
            browser.find_element_by_xpath('//*[@id="J_copy_all"]').click()
            pass
        except  Exception as e:
            print("222 error" , e)


