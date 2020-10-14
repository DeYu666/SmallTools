"""
功能：
    对 易观千帆 中的 ios 移动 app 中的 8-11 月中的 app 竞品分析爬虫
    最终生成4个 excel 表格

涉及到的子功能有：
        通过url爬取数据(返回的是json数据，并部署html),(url 是在 network 中找到 ajax 请求的 url)
        读取 excle 表格数据
        查找 windows 的桌面路径
        新建 excle 表格，写入数据，并修改表格中数据样式

参数：
    函数 def_url 中的 url 数组是要爬取数据的地址。page 指的是第几页
    cookie : 爬取数据需要VIP用户的 cookie 值

调用方法：
    python yiguanqianfan.py "cookie值"
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


def get_url(num, page):
    url = [
        "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1564588800000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1602568206580&appIds=&cateIds=&page=%s&pageSize=50&sortField=1&sort=desc"%(page),
        "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1567267200000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1602568206580&appIds=&cateIds=&page=%s&pageSize=50&sortField=1&sort=desc"%(page),
        "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1569859200000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1602568206580&appIds=&cateIds=&page=%s&pageSize=50&sortField=1&sort=desc"%(page),
        "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1572537600000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1602568206580&appIds=&cateIds=&page=%s&pageSize=50&sortField=1&sort=desc"%(page),
    ]
    return url[num], len(url)


headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'referer': 'https://qianfan.analysys.cn/refine/view/pageApp/pageApp.html?pageType=categoryApp&cateId=119',
    # 'cookie': "",
    'cookie': "JSESSIONID=DA8B90022DB4EA16BBD45CA95C547E14; LOCALE_LANG=zh-cn; i18n=zh; Hm_lvt_abe5c65ffb860ebf053a859d05bee0ea=1602554206; trialDetail=v5%E5%BC%B9%E7%AA%97%E8%AF%95%E7%94%A8; _9755xjdesxxd_=32; JSESSIONID=AD45567699D9710D037071936DE3A2D3; openId=ofUeAs_BraBZIoIcDxJ2rVdy0JwU; Hm_lpvt_abe5c65ffb860ebf053a859d05bee0ea=1602556305; gdxidpyhxdE=AE53BuRx6LeWIgBvP8ZmMUgP4Er9y6JRB4QaTirMN4%2Fw95SYvH5ay7c7lfoXvemBScMrQLp1Hcgks4gbSxMbSPBtQpNryzrJp7t9w7UuIId%2F%2Fzq2wJH6UltMhScaunQbTYMmo7mqZEr%5C6VyLUS21Ls1NdJCy9JjKNf4LvoLC%2FYAyhV2n%3A1602557628865; echart-table-mode-type=2; ARK_ID=JSaf5e5b30a40fe7feab155bf3aead7a4eaf5e",
}

if cookie != "":
    headers['cookie'] = cookie
    print(headers)


Null, length = get_url(0, 1)
print(length)

for i in range(0, length):
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

    for j in range(0, 4):
        print(i, j+1)
        url, Null = get_url(i, j+1)
        res = requests.get(url=url, headers=headers)
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
    workbook.save(str(GetDesktopPath())+'\\易观千帆' + str(timeYMD) + '.xls')

