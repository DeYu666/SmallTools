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
    'cookie': "JSESSIONID=741E41315B301D660278392E58313721; LOCALE_LANG=zh-cn; i18n=zh; gdxidpyhxdE=X3M8rygGs83vow%2BZX6CS0YIGZSsInLnRuZX8xWBHCw8l%5C8tYfLXAZqSEyZeCQ3UnU8WK4i1AG47uc%5CINcAWH%2FgG61m262zsabfh%2BhBfpPgAxf%5CyU0LPLJrCpj62Z8kuudBRn4ElhdVyGMvbwaI0NAQJfzv67qWIgTgSCzxNg3fQHh6xe%3A1603370054328; _9755xjdesxxd_=32; echart-table-mode-type=1; ARK_ID=JS080c8dce99d5d7f35844cf267e5e4d04080c",
}

if cookie != "":
    headers['cookie'] = cookie
    print(headers)


Null, length = get_url(0, 1)
print(length)

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
    workbook.save('全网-易观千帆' + str(timeYMD) + '.xls')

