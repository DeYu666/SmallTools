# Tools

这个文件夹中将会存放一些零碎的代码，每个文件都是一个小功能。供以后参考。

## excle 文件夹存放着对 excel 表格操作的一些代码

- excel_clearUp.py   
  - 对表格中的数据进行处理，并将结果保存到一个新的 excel 表格中
- yiguanqianfan.py  
  - 通过分析易观千帆的 network ，找出调用数据的 api 接口，然后通过 python 爬取数据，并保存到 excle  表格中
- ReadExcel.py  
  - 单纯的一个读取 excle 表格数据的一个代码。
- write_excel.py
  - 对数据写入到excel的代码做了一层包装，用起来更加的方便了。
  - 有三个方法，为excel写入首行 title; 为excel写入内容，一行一行写入；生成 excel 表格并保存。
- baiduzhishu.py
  - 通过分析百度指数的 network , 找出调用数据的 api 接口，然后通过 python 爬取数据，并保存到 excel 表格中
- appgrowing.py
  - 通过分析 appgrowing 的 network , 找出调用数据的 api 接口，然后通过 python 爬取数据，并保存到 excel 表格中
- 。。。。
  - 。。。。

## other 文件存放着没有汇总的一些代码片段

- analogKeyboard.py   
  - 这是python 模拟键盘敲击的程序。内部有一个参考链接，十分详细，有时间转载到我自己的博客。
- sendEmail.py    
  - 使用 python 发送邮件的程序。这次使用的是qq邮箱。
  - 开启pop3/smtp服务有一个参考链接：https://www.jianshu.com/p/cf7241166e33
- setting.py 
  - setting.py 中的 email_sender_smtp_pass 字段需要到QQ邮箱中开启pop3/smtp服务，会自动生成一个授权码。这个字段就是授权码

- 。。。。。。



## website 文件夹中存放着搭建博客的 React 静态代码

- my-blog-static-0   这是搭建完纯静态的博客网站时的代码。各个组件并没有互相连接。

