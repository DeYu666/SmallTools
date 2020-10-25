#coding:utf-8

"""
功能：
    对 易观千帆 中的 ios 移动 app 中的 1-9 月中的特定 app 竞品分析爬虫
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


import  os
def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')

def get_class():
    data_classes = {
        "通讯社交类":{
            "通讯": "易信；旺信；微话；有信（landray）；微微；来电；比邻；触宝电话；企业微信；TIM；WhatsApp；Skype",
            "社交": "微信；小红书；QQ；Soul；新浪微博；知乎；探探；陌陌；百度贴吧；美篇；LOFTER；QQ空间；连信；豆瓣； 脉脉；爱豆IDOL；派派；最右；伊对；陌生声",
        },
        "工具类":{
            "地图导航":"高德地图；百度地图；腾讯地图；北斗导航；奥维互动地图；搜狗地图；凯立德导航；途强在线；Google 地球；GPS工具箱；天下游；小猪导航",
            "拍照及图片处理":"美图秀秀；b612；BeautyCam美颜相机；轻颜相机；Faceu激萌；无他相机；黄油相机；水印相机；天天p图；一甜相机；玩图-全能美化；美妆相机；picsart；简拼；美人相机",
            "视频编辑":"剪映；快影；小影；彩视；录屏大师；剪影",
            "交通出行":"哈罗出行；摩拜单车；永安行；车来了；滴答出行；掌上出行；神州租车；滴滴出行；嘀嗒出行；亿通行；地铁通；首汽约车",
            "快递":"菜鸟裹裹；货拉拉；快递100；闪送；运满满司机；美团众包；运满满司机",
            "智能家居":"360智能摄像机；和家亲；小蚁摄像机；v380；华为智能家居；美的美居；海尔智家；和家亲；天猫精灵；米家；悟空遥控器；阿里Tv助手",
        },
        "视频流媒体类":{
            "综合视频":"爱奇艺；腾讯视频；芒果tv；优酷视频；搜狐视频；咪咕视频；pp视频；乐视视频； 风行视频；天翼超高清；看看视频； 哔哩哔哩",
            "短视频":"抖音短视频；快手；西瓜视频；火山视频；微视；美拍；秒拍；波波视频；VUE；快手极速版；好看视频；全民小视频；火山极速版；土豆视频；小影",
            "垂直在线视频":"韩剧tv（宝云网络）；爱奇艺奇巴布；福音TV；人人视频；小企鹅乐园；1905电影网；小蛙；戏曲多多；韩剧tv（乐酷网络）",
            "垂直直播视频":"斗鱼；虎牙直播；腾讯体育；企鹅电竞；yy；花椒直播；映客；PP体育；直播吧；秀色直播；红人直播；九秀直播；is语音",
        },
        "音乐电台":{
            "综合音乐平台":"qq音乐；网易云音乐；酷狗音乐；酷我音乐；虾米音乐；咪咕音乐；爱音乐；爱听4G；Y2002电音；多米音乐；VV音乐",
            "音乐娱乐": "全民K歌； 唱吧音视频；天籁K歌；K歌；酷我K歌；爱唱",
            "有声阅读": "喜马拉雅；蜻蜓FM；荔枝；懒人听书；得到；凯叔讲故事；氧气听书；企鹅FM；酷我畅听；听伴；凤凰FM；FM电台收音机；有声小说；阿基米德；清风DJ",
        },
        "在线购物":{
            "综合电商":"手机淘宝；京东；拼多多；苏宁易购；手机天猫；淘宝特价版；当当；微店；必要；蘑菇街；阿里巴巴；网易严选；国美；闲鱼",
            "旅游综合预定": "携程；去哪儿旅行；马蜂窝旅游；途牛旅游；同程旅行；艺龙旅行；驴妈妈旅游；出行365；无忧行",
        },
        "信息平台":{
            "职业招聘":"前程无忧51job；智联招聘；招财猫招聘；BOSS直聘；拉钩招聘；猎聘；大街；斗米；店长直聘；青团社兼职",
            "综合新闻资讯": "腾讯新闻；今日头条；网易新闻；新浪新闻；搜狐新闻；看点快报；人民日报；搜狐资讯；中青看点；一点咨询；趣头条；惠头条；东方头条；一点资讯；参考消息；中青看点；知乎日报",
            "房产信息": "安居客；贝克找房；我爱我家；链家；365淘房；巴乐兔租房；青客公寓",
        },
        "教育学习":{
            "中小学类教育":"作业帮；小猿搜题；快对作业；一起小学学生；学而思网校；学而思培优；纳米盒；爱作业",
            "教育平台": "学习强国；安全教育平台；腾讯课堂；网易公开课；中国大学mooc；嗨学；今日校园；网上优能；e学；小勾学习圈；优路学习；掌心宝贝园丁",
            "语言学习": "百词斩；流利说；叽里呱啦；英语趣配音；墨墨背单词；每日英语听力；知米背单词；可可英语；沪江开心词场；翼课学生；少儿趣配音；小站雅思；乐词-新东方背单词；英语魔方秀；TED英语演讲",
            "移动综合阅读": "掌阅；QQ阅读；咪咕阅读；书旗小说；小书亭；连尚读书；爱奇艺免费阅读；百度阅读；米读小说；追书神器免费版；熊猫看书；搜狗阅读；起点读书；微信读书；当当云读书",
        },
    }

    return data_classes


classes = get_class()

result_json = {}

for i in classes:
    t1 = {}
    for j in classes[i]:
        t2 = {}
        for k in classes[i][j].split("；"):
            t3 = {k: []}
            t2.update(t3)
        t4 = {j: t2}
        t1.update(t4)
    t5 = {i: t1}
    result_json.update(t5)

# print(result_json)




headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'referer': 'https://qianfan.analysys.cn/refine/view/pageApp/pageApp.html?pageType=categoryApp&cateId=119',
    # 'cookie': "",
    'cookie': "JSESSIONID=68C3E3701CA2CA677BD709AE25F7FBDE; LOCALE_LANG=zh-cn; i18n=zh; gdxidpyhxdE=X3M8rygGs83vow%2BZX6CS0YIGZSsInLnRuZX8xWBHCw8l%5C8tYfLXAZqSEyZeCQ3UnU8WK4i1AG47uc%5CINcAWH%2FgG61m262zsabfh%2BhBfpPgAxf%5CyU0LPLJrCpj62Z8kuudBRn4ElhdVyGMvbwaI0NAQJfzv67qWIgTgSCzxNg3fQHh6xe%3A1603370054328; _9755xjdesxxd_=32; echart-table-mode-type=1; ARK_ID=JS0468c485dc388a971c92b5e295ef63710468",
}



def scrapy(url):

    import requests
    import json
    import datetime

    url = url.replace("osTypeId=2","osTypeId=1")
    res = requests.get(url=url, headers=headers)
    res_datas1 = json.loads(res.content)
    # print(res_datas1)
    page = res_datas1['datas']['table']['totalPage']
    name_data = res_datas1['datas']['table']['heads']
    nonce = res_datas1['datas']['time']['statDate']
    time_all = datetime.datetime.fromtimestamp(nonce/1000)
    timeYMD = str(time_all).split(' ')[0]


    for i in range(1, page+1):
        # url2 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1577808000000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603462082625&appIds=&cateIds=&page=%s&pageSize=50&sortField=1&sort=desc"%(i)
        url2 = url.replace("page=1","page=" + str(i))

        url2 = url2.replace("osTypeId=2", "osTypeId=1")
        res = requests.get(url=url2, headers=headers)
        res_datas = json.loads(res.content)
        datas = res_datas['datas']['table']['bodys']
        # print(datas)
        for i in result_json:
            for j in result_json[i]:
                for k in result_json[i][j]:
                    for data in datas:
                        data_name = data['appName']
                        if str(data_name) == "None":
                            continue
                        if  str(data_name).replace(' ', '').upper() in  str(k).replace(' ', '').upper():
                            result_json[i][j][k] = data


    print(result_json)
    title = []


    # for data in datas:
    #     data_class = data['cateName']
    #     data_name = data['appName']
    #     for i in result_json:
    #          for j in result_json[i]:
    #              if j in data_class:
    #                  for k in result_json[i][j]:
    #                      if data_name in k:
    #                         result_json[i][j][k] = data



    # for i in result_json:
    #      for j in result_json[i]:
    #          for k in result_json[i][j]:
    #              for data in datas:
    #                  data_name = data['appName']
    #                  if str(data_name) == "None":
    #                      continue
    #                  if str(k).replace(' ', '').upper() in str(data_name).replace(' ', '').upper():
    #                     result_json[i][j][k] = data




    d_name = []
    for names in name_data:
        temp = {
            "name": names['label'],
            "key": names['prop']
        }

        d_name.append(temp)

    print(d_name)

    title = [
        {
            "name": "总类",
        },
        {
            "name": "分类",
        }
    ]
    title += d_name


    print(title)
    import xlwt


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




    # 设置单元格宽度
    for ii in range(0, len(title)):
        worksheet.col(ii).width = 5555

    # 写入标题
    for ii in range(0, len(title)):
        worksheet.write(0, ii, title[ii]['name'], style)


    # 写入数据
    line = 1
    for i in result_json:
        lie = 0
        worksheet.write(line, lie, i)
        lie += 1
        for j in result_json[i]:
            for k in result_json[i][j]:
                worksheet.write(line, lie, k)
                data_app = result_json[i][j][k]
                if len(data_app) == 0:
                    print(str(timeYMD) + str(k) + "  没有数据")
                    continue

                # print(data_app['24'])

                for l in range(0, len(d_name)):
                    worksheet.write(line, lie, j)
                    key = d_name[l]['key']
                    worksheet.write(line, l+2, data_app[key], style1)

                line += 1







    # 保存
    workbook.save('特定数据-安卓-易观千帆' + str(timeYMD) + '.xls')




    print("探探" in "探探")



url_1 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1577808000000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603462082625&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"
url_1 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1577808000000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603526752594&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"

url_2 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1580486400000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603466854934&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"
url_2 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1580486400000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603526853877&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"

url_3 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1582992000000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603526890783&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"

url_4 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1585670400000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603526931916&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"

url_5 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1588262400000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603528280899&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"

url_6 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1590940800000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603527046612&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"

url_7 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1593532800000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603527080288&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"

url_8 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1596211200000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603527110372&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"

url_9 = "https://qianfan.analysys.cn/refine/qianfan/appIndex/indexs?dateType=3&tabType=1&statDate=1598889600000&osTypeId=2&type=3&queryType=1&indexIds=1,2,3,4,5,6,24,25,7,8&timestamp=1603527142097&appIds=&cateIds=&page=1&pageSize=50&sortField=1&sort=desc"


url = [url_1, url_2, url_3, url_4, url_5, url_6, url_7, url_8, url_9]

for u in url:
    scrapy(u)


