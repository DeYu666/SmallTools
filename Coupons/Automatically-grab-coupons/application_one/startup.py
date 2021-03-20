from qq import *
from ReadExcel import ReadExcel
from entity import *
from alimamaByExcel import *
from setting import *
from copyImg import copyImg
from sendEmail import sendEmail









if __name__ == '__main__':
    qq=sendMsg(qq_receiver)
    while True:
        try:
            if isInThisInterval(start_time, end_time):
                # data_json = ReadExcel(r".\***.xls", "Page1").read_excel()
                data_json = ReadExcel(Excle_path, "Page1").read_excel()
                info = ["商品主图", "商品名称", "商品价格(单位：元)", "优惠券面额", "优惠券短链接(300天内有效)", "优惠券淘口令(30天内有效)"]
                datas = getGoodsInfo(data_json, info)


                for data in datas:
                    if data[3] == None or data[1] == 0:
                        continue
                    saveImgByURL(data[0], Img_path)
                    # 这里缺复制图片并发送到群中
                    copyImg(Img_path)
                    qq.sendmsg()
                    
                    sleep(3)
                    goods_detail = printGoodsInfo(data)
                    # 这里缺复制文字并发送到群中
                    setText(goods_detail)
                    qq.sendmsg()
                    sleep(send_time)

            title = '加工邮件——赶紧重置 Excel'
            content = '''
            赶紧重置 Excel
            '''
            sendEmail(reciever_email, title, content)
        except Exception as e:
            # 发送邮件通知
            title = '紧急邮件——自动化工具貌似挂了'
            content = '''
            紧急邮件——自动化工具貌似挂了
            '''
            sendEmail(reciever_email, title, content)
