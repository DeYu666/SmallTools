'''
    需要安装 pyEmail
'''

import smtplib
import email.mime.multipart
import email.mime.text
import time
import xlrd

email_sender = "1684461397@qq.com"

email_sender_smtp_pass = "xyddimuhwkswfcad"
email_smtp_server = "smtp.qq.com"

title_1 = '3'
content_1 = '''
2
'''

title = '《帮你给焦虑症写的一份绝交书》'
content = '''
《帮你给焦虑症写的一份绝交书》
无聊的暑假马上就过完了，你肯定和我一样焦虑，大学生活是什么样的呀？能不能开学就找下对象呀？家里给的生活费够用吗…
同学，别慌，这有个！不是你想的那种身体力行！就是线上那种！群里还会每天发购物优惠券，赚生活费的同时还可以省钱，不做也没关系，进来看看又不花钱：515266016,点击下方链接也可加入：
https://jq.qq.com/?_wv=1027&k=jP8FlOYN
'''



def sendEmail(reciever_email, title, content):
    try:
        msg = email.mime.multipart.MIMEMultipart()
        msg['from'] = email_sender
        msg['to'] = reciever_email
        msg['subject'] = title

        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)

        smtp = smtplib.SMTP()
        smtp.connect(email_smtp_server)
        smtp.login(email_sender, email_sender_smtp_pass)
        smtp.sendmail(email_sender, reciever_email, str(msg))
        smtp.quit()
        print("Sending email success")
        return True
    except Exception as e:
        print("Sending email fail")
        return False





reciever_email = "575701035@qq.com"


sendEmail(reciever_email, title_1, content_1)
# time.sleep(5)
# sendEmail(reciever_email, title, content)
#



# workbook=xlrd.open_workbook("C:\\Users\\xd04\\Desktop\\lalala\\1.xlsx")  #文件路径
#
#
# # 获取所有sheet的名字
# names = workbook.sheet_names()
# print(names)
#
# # 通过sheet索引获得sheet对象
# worksheet = workbook.sheet_by_index(0)
# print(worksheet)
#
# col_data = worksheet.col_values(1)  # 获取第二列的内容
# print(col_data)
#
# for data in col_data:
#     # print(str(data).split('.')[0])
#     reciever_email = str(data).split('.')[0] + "@qq.com"
#
#     if (sendEmail(reciever_email, title, content)):
#         print("yes")
#     else:
#         print("no")


