"""
功能:
    对批量 excle 表格数据处理。整理原 excel 表格中星级的数量，分数，并计算平均分数。

涉及到的子功能有：
        读取 excle 表格数据
        查找 windows 的桌面路径
        新建 excle 表格，写入数据，并修改表格中数据样式

参数：
    需要一个文件夹，文件夹中是将要处理的数据

调用：
    python "文件夹绝对路径"
"""


import xlrd, re, xlwt
import sys
import os

class ReadExcel:

    def __init__(self, fileName, sheetName):
        """
        new_data是最后返回的值
        :param fileName: excel文件名，sheet名称
        :param sheetName:
        """
        self.fileName = fileName
        # self.sheetName = sheetName
        # 读取excel
        self.book = xlrd.open_workbook(self.fileName)
        # self.sheet0 = self.book.sheet_by_name(self.sheetName)
        self.sheet0 = self.book.sheet_by_index(sheetx=0)
        # 获取第一列数据
        self.col_value = self.sheet0.col_values(1)  # 第一列
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


def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')



def main(path, page_name):
    print("进入main")
    data_json = ReadExcel(path, page_name).read_excel()
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('Sheet1', cell_overwrite_ok=True)
    # 设置单元格宽度
    worksheet.col(0).width = 3333
    worksheet.col(1).width = 3333
    worksheet.col(2).width = 3333
    worksheet.col(3).width = 3333
    worksheet.col(4).width = 9999
    worksheet.col(5).width = 3333
    worksheet.col(6).width = 3333
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

    result = [0, 0, 0, 0, 0]
    score = [0, 0, 0, 0, 0]
    line = 0

    worksheet.write(line, 0, '发表时间', style)
    worksheet.write(line, 1, '作者', style)
    worksheet.write(line, 2, '评级', style)
    worksheet.write(line, 3, '标题', style)
    worksheet.write(line, 4, '内容', style)
    worksheet.write(line, 5, '评论总数', style)
    worksheet.write(line, 6, '评论总分', style)

    line += 1
    sum_count = 0
    sum_score = 0

    time_date = ""
    for i in range(0, 5):
        count = 0
        score = 0
        for data in data_json:
            level = data_json[data]['评级']
            if level == i+1:
                count += 1
                score += level
                # 数据写入excel,参数对应 行, 列, 值
                worksheet.write(line, 0, data_json[data]['发表时间'], style1)
                worksheet.write(line, 1, data_json[data]['作者'], style1)
                worksheet.write(line, 2, data_json[data]['评级'], style1)
                worksheet.write(line, 3, data_json[data]['标题'], style1)
                worksheet.write(line, 4, data_json[data]['内容'], style1)
                time_date = data_json[data]['发表时间']
                line += 1

        if score == 0:
            continue
        worksheet.write(line - 1, 5, count)
        worksheet.write(line - 1, 6, score)
        sum_count += count
        sum_score += score

    print(sum_score)
    print(sum_count)
    worksheet.write(line, 0, "总人数")
    worksheet.write(line, 1, sum_count)
    worksheet.write(line+1, 0, "总分数")
    worksheet.write(line+1, 1, sum_score)
    worksheet.write(line+2, 0, "总平均分")
    worksheet.write(line+2, 1, sum_score/sum_count)
    name = str(path).split('\\')[-1]
    name = name.split('/')[-1]
    name = name.split('.')[0]
    name = name.split('_')[0]
    name = name + time_date.split(" ")[0]
    workbook.save(str(GetDesktopPath())+'\\' + name + '.xls')




dir = sys.argv[1]

def file_name_walk(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:

            print(file)
            name = str(file)
            suffix = str(name).split('.')[-1]
            if suffix == "xls" or suffix == "xlsx":
                main(file_dir + "\\" + name, "")

file_name_walk(dir)


#
# print('参数列表:', str(sys.argv))
# name = sys.argv[1]
# suffix = str(name).split('.')[-1]
#
# page_name = sys.argv[2]
# if suffix == "xls" or suffix == "xlsx":
#     main(name, page_name)
#
#
#
#
