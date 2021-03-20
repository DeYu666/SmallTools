from selenium import webdriver
import os, time, json, random
from selenium.webdriver.common.action_chains import ActionChains


# 创建浏览器窗口，并通过url打开网页
def create_browser(url):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)
    return browser




# 模拟输入
def input_simulation(browser, xpath, text):
    e = browser.find_element_by_xpath(xpath)
    for i in range(len(text)):
        sleep_time = random.randint(8, 30)
        time.sleep(int(sleep_time / 10))
        e.send_keys(text[i])


# 判断是否有滑动
def has_move(browser):
    yanzhen = browser.find_element_by_id('nocaptcha-password')
    style = yanzhen.get_attribute('style')
    if style == 'display: block;':
        return True
    return False


# 模拟滑动
def move_simulation(browser, id,isKuai = 0, DEBUG = True):

    e = browser.find_element_by_id(id)
    try:
        action = ActionChains(browser)
        action.click_and_hold(e).perform()
        print('2')
        offset = 40
        for i in range(int(330 / offset)):
            ActionChains(browser).move_by_offset(xoffset=offset, yoffset=0).perform()
            if isKuai:
                pass
            else:
                time.sleep(int((offset - i) / 50))
        action.release().perform()
        action.reset_actions()
    except Exception as e:
        if DEBUG: print(e)



def entry_frame(browser,xpath):
    browser.switch_to.frame(browser.find_element_by_xpath(xpath))
    return browser


def click_element(browser,xpath):
    browser.find_element_by_xpath(xpath).click()
    return browser


def click_element_byId(browser,id):
    browser.find_element_by_id(id).click()
    return browser


def hover_mouse(browser,xpath):
    ActionChains(browser).move_to_element(browser.find_element_by_xpath(xpath)).perform()
    


def copy_yhj(browser,xpath_url, DEBUG = True):
    try:
        browser.find_element_by_xpath(xpath_url).click()
        time.sleep(1)
        print("3")
        # browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="_oid_ifr_"]'))
        browser.find_element_by_xpath('//*[@id="J_copy_all"]').click()
        time.sleep(1)
    except Exception as e:
        if DEBUG: print(e)



def scroll_element(browser,xpath):
    target = browser.find_element_by_xpath(xpath)
    browser.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
    return browser