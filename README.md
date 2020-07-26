# SR PCB测试系统开发——项目记录文档

<a name="qFqzt"></a>
### 更新日期：2020.07.26
<a name="YZrnv"></a>
### 更新人员：研发部硬件组SZC
<a name="VSfA0"></a>
### 项目描述：

- 机器人控制板上贴有二维码，二维码记录了控制板的版本等信息，测试人员使用扫描枪读取其中的版本数据
- 之后进行控制板外设等功能等测试，读取测试固件版本和丢包率等数据，并得到控制板是否合格的结论，若合格则烧写功能固件并打印SN码，若不合格则打印不合格二维码
- 最后生成测试报告，并将过程信息写入数据库。
<a name="Efpmt"></a>
### 项目开发环境：

- anaconda3+spyder4.01：环境管理与IDE
- python3.7.6：anaconda3自带的python版本
- tk8.6.8：GUI界面（完成整体Demo后将改成PyQt5，tk设计的界面不美观）
- reportlab3.5.26：生成PDF
- pymysql0.9.3：对MySql数据库操作
- ctype：python3.7.6自带版本，C语言的接口，带有指针等功能
- cyserial3.4：对串口操作
<a name="a2TG1"></a>
### 项目功能需求拆分以及完成情况：

- [x] GUI交互界面：
      - 输入检测人员信息
      - 显示过程提示信息
      - 功能按钮：打印PDF并写入数据库的
- [x] 串口读取扫描枪数据
- [x] 自动生成测试报告PDF，自定义PDF格式（表格、字体、图片）
- [ ] 读取Nicelabel或者打印机的dll文件，利用接口自动打印二维码和SN码

（可读取Nicelabel接口并打印标签的nlbl模版，但Nicelabel提供的接口不具有标签设计的功能，只能读取现成的模版，故换方案为：使用python生成二维码的png，并通过打印机的dll提供的接口打印出。目前打印机dll的使用遇到了问题，读取不到USB）

- [ ] 通过串口和控制板交互信息
- [ ] 将程序打包成exe文件
<a name="VYOhY"></a>
### 程序流程示意图V0.0：
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1595390587286-25e52259-ebd7-4c72-b173-f43cba77b6e7.png#align=left&display=inline&height=453&margin=%5Bobject%20Object%5D&name=image.png&originHeight=905&originWidth=531&size=48333&status=done&style=none&width=265.5)
<a name="ww5I9"></a>
### 数据流示意图V0.0：
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1595399952494-b762ea7d-cf3a-474c-b6ba-87bdacf1a758.png#align=left&display=inline&height=215&margin=%5Bobject%20Object%5D&name=image.png&originHeight=430&originWidth=793&size=42405&status=done&style=none&width=396.5)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1595499705902-f3960cb2-35ad-4d93-8529-5a29f5cf6ec5.png#align=left&display=inline&height=207&margin=%5Bobject%20Object%5D&name=image.png&originHeight=413&originWidth=556&size=51405&status=done&style=none&width=278)
<a name="hgh9q"></a>
### 计划UI模型V0.0：
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1595401259181-358f21ee-7a05-4d9e-864b-60856d5def70.png#align=left&display=inline&height=311&margin=%5Bobject%20Object%5D&name=image.png&originHeight=621&originWidth=717&size=37119&status=done&style=none&width=358.5)
<a name="55Dp5"></a>
### 数据库存放的Tabel数据：

- 检测人员名称
- PCB的扫描得到的控制板基本信息
- 固件测试的版本号
- 是否合格（True or False）
- 功能固件版本，不合格产品无则为Null
- 合格编号或者不合格编号（存在同一个数据变量里）
- 其他信息


