import time
import requests
import urllib.parse
import datetime
import xlwt
import write_excel


def decrypt(t: str, e: str) -> str:
    n, i, a, result = list(t), list(e), {}, []
    ln = int(len(n)/2)
    start, end = n[ln:], n[:ln]
    a = dict(zip(end, start))
    return ''.join([a[j] for j in e])

COOKIES = 'BAIDUID=8759768F974CE3E6C2884260097331A4:FG=1; PSTM=1574683224; H_PS_PSSID=1445_21116_29567_29220; BIDUPSID=43233656E2011B10D268D7B02D7A956A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=2; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1574939615; BDUSS=hWWDJ0Z01VOWZINGdPaWRkTUotYmR4WlRhcEhJNTVDQzA3SUpDNzBSWHRPQWRlRVFBQUFBJCQAAAAAAAAAAAEAAAA3VXuxu6rPxNPQxMzGpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO2r313tq99daE; CHKFORREG=f47c79690c889b9fe3bb335ced026f76; bdindexid=j4g6p93elqe6o7phocmmfn53o2; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1574940479'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Cookie': COOKIES,
    'DNT': '1',
    'Host': 'zhishu.baidu.com',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'zhishu.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
session = requests.Session()
session.headers.update(headers)


def get_ptbk(uniqid: str) -> str:
    with session.get(
        url=f"http://index.baidu.com/Interface/ptbk?uniqid={uniqid}"
    ) as response:
        ptbk = response.json()["data"]
        return ptbk


def get_index_data(keyword: str, start: str, end: str) -> str:
    keyword = urllib.parse.quote(keyword)
    with session.get(
        url=f"http://index.baidu.com/api/SearchApi/index?area=0&word=[[%7B%22name%22:%22{keyword}%22,%22wordType%22:1%7D]]&startDate={start}&endDate={end}"
    ) as response:
        data = response.json()["data"]
        all_data = data["userIndexes"][0]["all"]["data"]

        uniqid = data["uniqid"]
        ptbk = get_ptbk(uniqid)
        result = decrypt(ptbk, all_data).split(',')
        return result


def GetDesktopPath():
    import os
    return os.path.join(os.path.expanduser("~"), 'Desktop')

# 获取从开始日期 start 到截止日期 end 中的所有日期
def get_date_list(start:str, end: str):
    # 也可以是%Y%m%d
    datestart = datetime.datetime.strptime(start,'%Y-%m-%d')
    dateend = datetime.datetime.strptime(end,'%Y-%m-%d')

    data_list = []
    while datestart<dateend:
        datestart+=datetime.timedelta(days=1)
        data_list.append(datestart.strftime('%Y-%m-%d'))
    return data_list



start = "2020-7-01"
end = "2020-9-30"

d_name = []
d_name.append("名称")
d_name += get_date_list(start, end)



myExcel = write_excel.Excel()

myExcel.write_title(d_name)



line = 1
with open('./百度指数修改名单.txt',"r",encoding='UTF-8') as lines:  # 一次性读入txt文件，并把内容放在变量lines中
    array = lines.readlines()  # 返回的是一个列表，该列表每一个元素是txt文件的每一行
    for name in array:
        temp = []
        arr_name = name.split(" ")
        if len(arr_name) == 2:
            name = arr_name[1].replace("\n","")
        else:
            name = arr_name[0].replace("\n","")
        try:
            data = get_index_data(
                keyword=name,
                start=start,
                end=end
            )
            temp.append(name)
            temp += data
            time.sleep(1)

            myExcel.write_content_line(temp)


            break
        except Exception as e:
            print(name)
            continue
myExcel.save_excel("123")



