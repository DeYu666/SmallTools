import json,time,urllib,requests
import my_request
import write_excel


COOKIES = 'sajssdk_2015_cross_new_user=1; AG_Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ImIyZjBjNjNlLTJlZTYtM2I4NS04ZDlmLTUzZGQ1NmU5NzVkYiIsImFjYyI6MzY2OTY0LCJleHAiOjE2MDkxNDUwODQsImlhdCI6MTYwNjU1MzA4NX0.5ue38Uh7p-am-rUTlwadCFP0_5dKCLUuHongDrvabLw; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22366964%22%2C%22first_id%22%3A%221760dece82fc04-0103da4d68076c-c791e37-2073600-1760dece830cbf%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fyoucloud.com%2F%22%7D%2C%22%24device_id%22%3A%221760dece82fc04-0103da4d68076c-c791e37-2073600-1760dece830cbf%22%7D'
headers = my_request.get_header(COOKIES)


def search_id(name:str):
    result_id = []
    name = urllib.parse.quote(name)
    res = requests.get(url=f"https://data.appgrowing.cn/api/leaflet/brand?query={name}&sort=-adverts&startDate=2020-11-01&endDate=2020-11-30&timeType=month&limit=20&page=1&brandType=401"
                        , headers=headers)
    datas = json.loads(res.content)
    for d in datas["data"]:
        temp = {
            "id" : d["brandInfo"]["id"],
            "name": d["brandInfo"]["name"]["raw"]
        }
        result_id.append(temp)

    return result_id


def get_sum_ios(id:str):
    res = requests.get(
        url=f"https://data.appgrowing.cn/api/brand/leaflet/count?platform=iOS&brandType=401&startDate=2020-07-01&endDate=2020-09-30&page=1&id={id}"
        , headers=headers)
    datas = json.loads(res.content)
    return datas["data"][id]["total"] # 26445


def get_sum_all(id:str):
    res = requests.get(
        url=f"https://data.appgrowing.cn/api/brand/leaflet/count?platform=iOS,Android&brandType=401&startDate=2020-07-01&endDate=2020-09-30&page=1&id={id}"
        , headers=headers)
    datas = json.loads(res.content)
    return datas["data"][id]["total"]  # 26445

# search_id("陌陌")
print(get_sum_ios("71"))


title = ["名称","全部设备","ios"]
file_name = "appgrowing广告总量"

myExcel = write_excel.Excel()
myExcel.write_title(title)


with open('百度指数app名字.txt',"r",encoding='UTF-8') as lines:  # 一次性读入txt文件，并把内容放在变量lines中
    array = lines.readlines()  # 返回的是一个列表，该列表每一个元素是txt文件的每一行
    for name in array:
        name = name.split(" ")[1].replace("\n","")
        id_name_arr = search_id(name)
        try:
            for single in id_name_arr:
                temp = []
                temp.append(single["name"])
                temp.append(get_sum_all(single["id"]))
                time.sleep(1)
                temp.append(get_sum_ios(single["id"]))
                time.sleep(1)
                myExcel.write_content_line(temp)

        except Exception as e :
            print(str(name)+"---------------"+str(e))



myExcel.save_excel(file_name)
