"""
功能：
    对 易观千帆 中的 ios 移动 app 中的 1-9 月中的 app 竞品分析爬虫
    最终生成9个 excel 表格

涉及到的子功能有：
        通过url爬取数据(返回的是json数据，并部署html),(url 是在 network 中找到 ajax 请求的 url)
        读取 excle 表格数据
        查找 windows 的桌面路径
        新建 excle 表格，写入数据，并修改表格中数据样式

参数：
    函数 def_url 中的 url 数组是要爬取数据的地址。page 指的是第几页
    cookie : 爬取数据需要VIP用户的 cookie 值

调用方法：
    python yiguanqianfan.py
"""

import xlwt, requests, json, bs4
import os, sys
import datetime,time

cookie = ""
try:
    cookie = sys.argv[1]
except:
    pass


def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')




url_1 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1577808000000&osTypeId=0&type=3&queryType=1&indexIds=1,40,41,42,2,45,46,3,49,50,67,13,4,5,6,24,25,7,8,68,27,43,47,51,52,53,54,55,56&timestamp=1603532098618&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"
url_2 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1580486400000&osTypeId=0&type=3&queryType=1&indexIds=1,40,41,42,2,45,46,3,49,50,67,13,4,5,6,24,25,7,8,68,27,43,47,51,52,53,54,55,56&timestamp=1603532225363&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"
url_3 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1582992000000&osTypeId=0&type=3&queryType=1&indexIds=1,40,41,42,2,45,46,3,49,50,67,13,4,5,6,24,25,7,8,68,27,43,47,51,52,53,54,55,56&timestamp=1603532291927&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"
url_4 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1585670400000&osTypeId=0&type=3&queryType=1&indexIds=1,40,41,42,2,45,46,3,49,50,67,13,4,5,6,24,25,7,8,68,27,43,47,51,52,53,54,55,56&timestamp=1603532326621&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"
url_5 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1588262400000&osTypeId=0&type=3&queryType=1&indexIds=1,40,41,42,2,45,46,3,49,50,67,13,4,5,6,24,25,7,8,68,27,43,47,51,52,53,54,55,56&timestamp=1603532358347&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"
url_6 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1590940800000&osTypeId=0&type=3&queryType=1&indexIds=1,40,41,42,2,45,46,3,49,50,67,13,4,5,6,24,25,7,8,68,27,43,47,51,52,53,54,55,56&timestamp=1603532389934&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"
url_7 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1593532800000&osTypeId=0&type=3&queryType=1&indexIds=1,40,41,42,2,45,46,3,49,50,67,13,4,5,6,24,25,7,8,68,27,43,47,51,52,53,54,55,56&timestamp=1603532419912&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"
url_8 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1596211200000&osTypeId=0&type=3&queryType=1&indexIds=1,40,41,42,2,45,46,3,49,50,67,13,4,5,6,24,25,7,8,68,27,43,47,51,52,53,54,55,56&timestamp=1603532458525&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"
url_9 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1598889600000&osTypeId=0&type=3&queryType=1&indexIds=1,40,41,42,2,45,46,3,49,50,67,13,4,5,6,24,25,7,8,68,27,43,47,51,52,53,54,55,56&timestamp=1603532490823&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"


url = [url_1, url_2, url_3, url_4, url_5, url_6, url_7, url_8, url_9]



import time

ticks = time.time()
print('当前时间戳： ', ticks)

new_ticks = str(ticks).replace('.', '')[:-3]
print(new_ticks)

timestamp = new_ticks


a1 = "2020-4-1"
# 先转换为时间数组
timeArray = time.strptime(a1, "%Y-%m-%d")

# 转换为时间戳
statDate1 = int(time.mktime(timeArray))
statDate1 = str(statDate1) + "000"

print(statDate1)

url = []

statDate = int(statDate1)
timestamp = timestamp
for i in range(0, 183):
    # url.append("https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=1&tabType=1&statDate=1588176000000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,24,25&timestamp=1603628884434&appIds=&cateIds=&list=&page=1&pageSize=50&sortField=1&sort=desc")
    url.append("https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=1&tabType=1&statDate="+str(statDate)+"&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,24,25&timestamp="+str(timestamp)+"&appIds=&cateIds=&list=&page=1&pageSize=50&sortField=1&sort=desc")
    statDate += 86400000






def get_url(num, page):
    url = [
        "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1564588800000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1602568206580&appIds=&cateIds=&page=%s&pageSize=50&sortField=1&sort=desc"%(page),
        "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1567267200000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1602568206580&appIds=&cateIds=&page=%s&pageSize=50&sortField=1&sort=desc"%(page),
        "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1569859200000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1602568206580&appIds=&cateIds=&page=%s&pageSize=50&sortField=1&sort=desc"%(page),
        "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1572537600000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1602568206580&appIds=&cateIds=&page=%s&pageSize=50&sortField=1&sort=desc"%(page),
        "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1577808000000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603372282273&appIds=&cateIds=&cateList=%7B%22tradeIds%22:%221151137,1151138,1191167,1211192,1151142,1211193%22%7D&page=1&pageSize=50&sortField=1&sort=desc"
    ]
    return url[num], 9


headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'referer': 'https://qianfan.analysys.cn/refine/view/pageApp/pageApp.html?pageType=categoryApp&cateId=119',
    # 'cookie': "",
    'cookie': "JSESSIONID=6ED07AA5A18A18C35F77C185F7D358BD; LOCALE_LANG=zh-cn; i18n=zh; _9755xjdesxxd_=32; trialDetail=%E5%85%AC%E5%85%B1%E5%BA%95%E9%83%A8%E8%AF%95%E7%94%A8; ARK_STARTUP=eyJTVEFSVFVQIjp0cnVlLCJTVEFSVFVQVElNRSI6IjIwMjAtMTAtMDMgMTY6NDM6MTYuNjEyIn0%3D; Hm_lvt_d981851bd0d388f5b0fa75295b96745d=1601714599; Hm_lpvt_d981851bd0d388f5b0fa75295b96745d=1601714599; Hm_lvt_abe5c65ffb860ebf053a859d05bee0ea=1601711098,1602390103; Hm_lpvt_abe5c65ffb860ebf053a859d05bee0ea=1602390103; JSESSIONID=063D104D96DEF5A15813B07105A91768; gdxidpyhxdE=V262TnIENrODnTyaZMikQs%2BsD8hR3AvW8XOjXsX1jDE7vT2eb%5CMhzkh66yw5Sw9zQggwXgcp7tyzkjbPB3UDD6Z1fvBMZ8%5C1bnHHdjS%2BHHLmAnSYdwJHbNlzgrChw1%5CtbcL6KNDVCsOQZ%5C2VAj4Z0C8ywklNARK3j%2BCt0%2BYAqhMaP6oj%3A1602391854858; echart-table-mode-type=1; FZ_STROAGE.analysys.cn=eyJTRUVTSU9OSUQiOiJlZDhhOGFjMzMzNTJkMDA1IiwiU0VFU0lPTkRBVEUiOjE2MDM2MTI3MDY3NzIsIkFOU0FQUElEIjoiZmFiZTc5NGE3NDU1NDQzNSIsIkFOUyRERUJVRyI6MiwiQU5TVVBMT0FEVVJMIjoiaHR0cHM6Ly91YXQuYW5hbHlzeXMuY246NDA4OS8iLCJGUklTVERBWSI6IjIwMjAxMDAzIiwiRlJJU1RJTUUiOmZhbHNlLCJBUktfSUQiOiJKUzhlZWI3YjdhNGMyZTc3N2ZiNTQzNTIwM2ZmMmFjMTViOGVlYiIsIkFSS0ZSSVNUUFJPRklMRSI6IjIwMjAtMTAtMDMgMTY6NDM6MTYuNjM5IiwiQU5TU0VSVkVSVElNRSI6MH0%3D; ARK_ID=JSa377d2e643fbb10560c50c4a1c21f209a377",
}

if cookie != "":
    headers['cookie'] = cookie
    print(headers)


Null, length = get_url(0, 1)
print(length)

i = 0
for u in url:
    # u = u.replace("TypeId=2","TypeId=0")
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('Sheet1', cell_overwrite_ok=True)


    # 标题字体样式设置
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体

    font.name = '微软雅黑'
    font.height = 20 * 14  # 字体大小，11为字号，20为衡量单位
    style.font = font  # 设定样式
    style.alignment.horz = 2  # 水平居中 值为2
    # 内容字体样式设置
    style1 = xlwt.XFStyle()  # 初始化样式
    font1 = xlwt.Font()  # 为样式创建字体

    font1.name = '微软雅黑'
    font1.height = 20 * 10  # 字体大小，11为字号，20为衡量单位
    style1.font = font1  # 设定样式
    style1.alignment.wrap = 1  # 自动换行
    style1.alignment.horz = 2  # 水平居中 值为2


    line = 1

    res = requests.get(url=u, headers=headers)
    res_datas1 = json.loads(res.content)
    # print(res_datas1)
    page = res_datas1['datas']['table']['totalPage']


    for j in range(0, page):
        url_bak = u.replace("page=1","page=" + str(j+1))
        res = requests.get(url=url_bak, headers=headers)
        time.sleep(1)
        datas = json.loads(res.content)
        apps_data = datas['datas']['table']['bodys']
        names_data = datas['datas']['table']['heads']
        try:
            if apps_data[4]["25"] == -999999:
                print("cookie 过期")
                exit(1)
        except:
            pass

        d_name = []
        for names in names_data:
            temp = {
                "name": names['label'],
                "key": names['prop']
            }

            d_name.append(temp)

        # 设置单元格宽度
        for ii in range(0, len(d_name)):
            worksheet.col(ii).width = 3333

        result_data = []
        for app in apps_data:
            if app['appName'] == None:
                continue
            app_data = []
            for n in d_name:
                temp = {
                    "name": n['name'],
                    "data": app[n['key']]
                }
                app_data.append(temp)

            result_data.append(app_data)

        # 写入首行
        for ii in range(0, len(d_name)):
            worksheet.write(0, ii, d_name[ii]['name'], style)

        # 写入数据
        for ii in range(1, len(result_data)+1):
            for jj in range(0, len(d_name)):
                worksheet.write(line, jj, result_data[ii-1][jj]['data'], style1)
            line += 1

        nonce = datas['datas']['time']['statDate']

    time_all = datetime.datetime.fromtimestamp(nonce/1000)
    timeYMD = str(time_all).split(' ')[0]
    # 保存
    workbook.save(str(GetDesktopPath())+'\\ios-易观千帆' + str(timeYMD) + '.xls')
    time.sleep(10)
    print("已完成 "+ str(timeYMD) +" 的数据了")
