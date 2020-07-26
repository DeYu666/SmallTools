# import json  
# import xmltodict
import win32gui
import win32con
import win32clipboard as w

from skimage import io
from QQ import *
# def xmlToJson(xml):
#     try:
#         convertJson = xmltodict.parse(xml,encoding="utf-8")
#         jsonStr = json.dumps(convertJson,indent=4)
#         return jsonStr
#     except Exception as e:
#         print(e)
#         return 0



# if __name__ == "__main__":
#     jsonStr = xmlToJson(students.xls)
#     print(jsonStr)


import xlrd, re

class ReadExcel:

    def __init__(self, fileName, sheetName):
        """
        new_data是最后返回的值
        :param fileName: excel文件名，sheet名称
        :param sheetName:
        """
        self.fileName = fileName
        self.sheetName = sheetName
        # 读取excel
        self.book = xlrd.open_workbook(self.fileName)
        self.sheet0 = self.book.sheet_by_name(self.sheetName)
        # 获取第一列数据
        self.col_value = self.sheet0.col_values(0)  # 第一列
        self.new_data = {}

    def data_type(self, test_type, test_value):
        """
        判断从excel单元格中获取的数据类型
        1 string（text）, 2 number, 3 date, 4 boolean
        :param test_type: 类型
        :param test_value: 值
        :return:
        """
        if test_type == 1:
            """字符串"""
            return test_value

        elif test_type == 2:
            if '.0' in str(test_value):
                """整数"""
                return int(test_value)
            else:
                """浮点"""
                return test_value

        elif test_type == 3:
            """日期"""
            date = xlrd.xldate_as_datetime(test_value, 0).strftime('%Y-%m-%d')
            return date

        elif test_type == 4:
            """布尔类型"""
            if test_value == 1:
                return True
            elif test_value == 0:
                return False

    def write_list(self, value):
        """
        取出某一行的值，将其写入一个新的字典
        :param value:   self.col_value.index 是一个列表（第一列的值），self.col_value.index(value)是判断value这个值是在列表中的第几位
        :return: 新建的字典
        """
        test_data = {}
        for j in range(1, self.sheet0.ncols):
            test_type = self.sheet0.cell_type(self.col_value.index(value), j)  # 单元格数据类型
            test_value = self.sheet0.cell_value(self.col_value.index(value), j)  # 单元格数据值
            result = self.data_type(test_type, test_value)
            test_data[self.sheet0.row_values(0)[j]] = result
        return test_data

    def read_excel(self):
        """
        读取excel表中数据
        :return: 字典格式
        """
        # 遍历将相同类型的用例分在一起
        for i in self.col_value[1:]:
            m = re.findall("_\d+_", i)  # 按照固定格式匹配，用于判断用例是否是相同的类型
            if len(m) == 0:
                test_data = self.write_list(i)
                self.new_data[i] = test_data
            else:
                n = re.findall("(.+_\d+?)_\d+", i)[-1]  # 按照固定格式匹配，提取相同的字符
                if n not in self.new_data.keys():
                    test_data = self.write_list(i)
                    self.new_data[n] = [test_data]
                else:
                    test_data = self.write_list(i)
                    self.new_data[n].append(test_data)
        return self.new_data



def sendQQ():
    qq=sendMsg("暑期实践活动")
    qq.sendmsg()


if __name__ == '__main__':
    data_json = ReadExcel(r"C:\\Users\Administrator\Desktop\\教链项目\silei-2020-07-26.xls", "Page1").read_excel()

    datas = [ [ 0 for i in range(6)] for i in range(200)] # n是列，m是行
    i = 0

    for key in data_json:
        datas[i][0] = data_json[key]["商品主图"]
        datas[i][1] = data_json[key]["商品名称"]
        datas[i][2] = data_json[key]["商品价格(单位：元)"]
        datas[i][3] = data_json[key]["优惠券面额"]
        datas[i][4] = data_json[key]["优惠券短链接(300天内有效)"]
        datas[i][5] = data_json[key]["优惠券淘口令(30天内有效)"]
        i += 1

    print(datas[0])





    image = io.imread(datas[1][0])
    # io.imshow(image) # 显示图片
    io.imsave('d:/newface.jpg', image) # 保存图片


    for data in datas:
        if data[3] == None or data[1] == 0:
            continue
        
        goods_detail = str(data[1]) + "\n " + \
                        "【在售价】：￥" + data[2] + "\n " + \
                        "【券后价】：" +  str(float(data[2]) - float(data[3])) + "\n " + \
                        "【推荐理由】 领" + str(data[3]) + "元独家券，券后【"+ str(float(data[2]) - float(data[3])) +"】包邮秒杀！\n " + \
                        "【下单口令】" + data[5] + "\n " + \
                        "【下单链接】" + data[4] + "\n "

        print(goods_detail)
    


    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, goods_detail)
    w.CloseClipboard()

    sendQQ()