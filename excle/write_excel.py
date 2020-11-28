import xlwt


class Excel:
    def __init__(self):
        # 创建一个workbook 设置编码
        self.workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        self.worksheet = self.workbook.add_sheet('Sheet1', cell_overwrite_ok=True)
        # 标题字体样式设置
        self.style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = '微软雅黑'
        font.height = 20 * 14  # 字体大小，11为字号，20为衡量单位
        self.style.font = font  # 设定样式
        self.style.alignment.horz = 2  # 水平居中 值为2

        # 内容字体样式设置
        self.style1 = xlwt.XFStyle()  # 初始化样式
        font1 = xlwt.Font()  # 为样式创建字体
        font1.name = '微软雅黑'
        font1.height = 20 * 10  # 字体大小，11为字号，20为衡量单位
        self.style1.font = font1  # 设定样式
        self.style1.alignment.wrap = 1  # 自动换行
        self.style1.alignment.horz = 2  # 水平居中 值为2

        # 写入的行数  正文从第二行写入
        self.line = 1

    # 写入 Excel 首行标题
    def write_title(self,title_arr):
        # 设置单元格宽度
        for ii in range(0, len(title_arr)):
            self.worksheet.col(ii).width = 3333

        # 写入首行
        for ii in range(0, len(title_arr)):
            self.worksheet.write(0, ii, title_arr[ii], self.style)


    # 写入 Execl 正文信息， 一次只写入一行
    def write_content_line(self, content_arr):
        # 写入数据
        for jj in range(0, len(content_arr)):
            self.worksheet.write(self.line, jj, content_arr[jj], self.style1)
        self.line += 1


    # 保存 excel 表格
    def save_excel(self, file_name:str):
        self.workbook.save(file_name + '.xls')


"""
用法：

import write_excel

myExcel = write_excel.Excel() #  初始化

myExcel.write_title(d_name) #  写入标题 d_name 是一个一维数组

myExcel.write_content_line(temp) #  写入内容 temp 是一个一维数组
"""


