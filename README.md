# SR 硬件测试系统开发文档

![sr_new.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/753325/1596187871902-9ed71732-9edd-4cdf-9af6-4c0644b5dd89.jpeg#align=left&display=inline&height=73&margin=%5Bobject%20Object%5D&name=sr_new.jpg&originHeight=339&originWidth=1280&size=114217&status=done&style=none&width=276)<br />项目开始日期：2020.07.17<br />文档更新日期：2020.07.26<br />更新人员：研发部硬件组SZC<br />注意：更新内容将标红示意
<a name="L5YGG"></a>
### [项目GitHub](https://github.com/RadarSun/SR_work)
<a name="VSfA0"></a>
### 项目描述：

- 步骤一：登陆。测试人员输入账号密码。管理员直接操作数据库注册（后续可改进为其他方式）
- 步骤一：机器人控制板上贴有二维码，二维码记录了控制板的版本等信息，测试人员使用扫描枪读取信息（串口读取），GUI显示扫码枪连接状态和控制板版本信息
- 步骤二：测试人员手动烧录测试固件，烧录成功后控制板向PC端返回版本信息（串口）并GUI显示，随后控制板等待PC发送测试指令
- 步骤三：测试人员通过PC的GUI界面发送测试指令（串口），测试控制板外设等功能，统计丢包率等各项指标（详见控制板外设测试方案），最终得到控制板是否合格的结论，GUI显示合格结论和各项指标
- 步骤四：若合格，测试人员手动烧写功能固件，控制板返回功能固件版本信息，GUI显示信息，测试人员按GUI按钮打印SN码（或自动）；若不合格，测试人员按GUI按钮（或自动），生成不合格编号并打印不合格二维码
- 按GUI按钮生成测试报告，并将过程信息写入数据库。
<a name="55Dp5"></a>
### 数据库存放的数据：
<a name="JcOYc"></a>
#### 1. Tabel 1：admin_data

- user_name：账号
- password：密码
<a name="Hh2Yu"></a>
#### 2. Tabel 2: pcb_data

- admin_name：检测人员名称
- pcb_version：PCB的扫描得到的控制板版本信息
- test_firmwave_version：测试固件的版本号
- is_qualified_or_not：是否合格（True or False）
- fucn_firmwave_version：功能固件版本，不合格产品无则为Null
- pcb_numb：合格编号或者不合格编号（存在同一个数据变量里）
- uart_packet_loss_rate：UART丢包率
- can_packet_loss_rate：CAN丢包率
- io_in_on：输入IO口是否运行良好
- io_out_on：输出IO口是否运行良好
<a name="a2TG1"></a>
###  项目功能需求拆分以及完成情况：

- [x] GUI交互界面：使用pyqt为GUI框架
      - 登陆界面：用户权限，需要账户密码登陆GUI交互界面
      - 测试系统主界面：
         1. 控制板信息：控制板版本；测试固件版本；各指标测试结果；是否合格；功能固件版本；编号；
         1. 操作提示信息：“请连接扫码机”等；
         1. 功能按钮：“打印标签 生成PDF 写入数据库”按钮；“自动运行”按钮；（待开发）
         1. 过程日志：Text滚动显示，软件关闭后写入本地txt文件，以查询软件故障原因；（待开发）
      - 软件版本信息界面：显示软件版本号，公司标志，版权声明，技术支持联系方式；
- [x] 串口读取扫描枪数据：
      - 实现串口的热插拔，随时插入使用
      - 自动感知读取数据，提示下一步操作步骤和当前操作问题
- [x] PDF测试报告自动生成，可自定义PDF格式（PDF样式、表格、字体、图片）
- [x] 打印标签：读取Nicelabel dll，利用接口打印二维码和SN码

   （Nicelabel提供的接口不具有标签设计的功能，只能读取现成的模版，故换为以下方案）

- [x] 打印标签：python生成二维码和SN码，利用打印机的dll接口打印
- [x] PCAN的集成和封装：发送数据等帧类型可选，读取对应id的报文
- [ ] 通过串口和控制板交互信息，测试EU200
- [ ] 将程序打包成exe文件
<a name="VYOhY"></a>
### 控制板外设测试方案：

- 硬件平台：EU200，具有一路UART，一路CAN，一路CAN和UART复用端口
- 测试指标：
   - 通信接口在**不同波特率下**的丢包率、误码率、传输延时
   - 输入输出IO的功能是否完整，读取、输出高低电平
- 测试方案：
   - IO口：
      - 非严密测试：（可能采取其他方案）
         - 硬件：控制板的输出输入IO口互连
         - 过程：PC端发送测试IO命令帧，控制板收到命令帧后，先将输出置高，输入读取电平，记录电平数据is_high[x]（1）；后将输出置低，输入读取电平，记录电平数据is_low[x]（0有效）；最后判断高低电平测试是否符合结果，符合则对应的一组IO运行良好，否则单独人工测试（还没确定怎么处理）。
   - 通信接口：根据实际需求，确定固定的发送频率，同时收发1024帧。通信接口硬件连接如图所示：

![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596182642976-705b2197-8e15-45e2-8aad-aa7e828b797e.png#align=left&display=inline&height=135&margin=%5Bobject%20Object%5D&name=image.png&originHeight=199&originWidth=347&size=7521&status=done&style=none&width=236)

      - **丢包率**：
         - CAN：控制板与PC交互。
               - 规定PC端发送的帧数量，PC端发送开始帧后，控制器端每收到一个信息帧计数加一，待PC发送结束帧后（结束帧不计数），控制器端比较接收到的帧数量与规定数量，得到丢包率
         - UART：控制板自发自收，最终指标结果发送给PC端。
            - 硬件：控制板两个通信接口互连。复用引脚设置为UART，与PC串口相连
            - 过程：PC端发送开始帧，控制板端开始自发自收信息帧。每收到一个信息帧计数加一，待PC发送结束帧后（结束帧不计数），控制器端比较接收到的帧数量与规定数量，得到丢包率
      - **误码率**：每收到信息帧，对比数据与规定数据，得到每一帧的误码率标志位并缓存，待消息帧结束后统计误码率
      - **传输延时**：只测试串口，CAN暂不测试。控制板的两个串口互连接，嵌入式系统有一个一直在运行的定时器，每一发送的信息帧都携带当时的时间戳，每次收到数据进入回调后读取实时时间戳，最后得到的时间差保存为当前帧的传输延时。信息帧结束后，统计平均传输时延。

具体通信指标的测试流程如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596189286417-3c79a637-4e5b-40f9-8db4-69e5f41b61df.png#align=left&display=inline&height=597&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1193&originWidth=712&size=123564&status=done&style=none&width=356)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596189320485-0af21f18-b672-44f4-981d-cdaa799b2ea8.png#align=left&display=inline&height=308&margin=%5Bobject%20Object%5D&name=image.png&originHeight=616&originWidth=595&size=52344&status=done&style=none&width=297.5)<br />UART的帧结构如图所示：  <br />             ![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596178733425-a56cb4ae-9f31-44f6-9e8c-9e3676c578b9.png#align=left&display=inline&height=64&margin=%5Bobject%20Object%5D&name=image.png&originHeight=64&originWidth=453&size=3184&status=done&style=none&width=453)

         - 帧头：1byte。0x5A
         - 命令：1byte。0x01 表示开始帧；0x02表示信息帧；0x03表示结束帧；
         - DATA[~]：1byte。开始结束帧的DATA[0]用来表示TX/RX，对应1/0；
         - 校验位：1byte。CRC校验
         - 帧尾：2byte。0x0D 0x0A
<a name="7DCO2"></a>
### 程序流程示意图V0.1：
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596164065741-4f0828f1-9855-4121-87d4-20860a9177ca.png#align=left&display=inline&height=669&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1337&originWidth=709&size=96120&status=done&style=none&width=354.5)![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596163505782-196e3636-bd71-4ad4-87ac-6d2eb1f247b8.png#align=left&display=inline&height=13&margin=%5Bobject%20Object%5D&name=image.png&originHeight=25&originWidth=1&size=77&status=done&style=none&width=0.5)
<a name="ww5I9"></a>
### 数据流示意图V0.0：
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1595399952494-b762ea7d-cf3a-474c-b6ba-87bdacf1a758.png#align=left&display=inline&height=215&margin=%5Bobject%20Object%5D&name=image.png&originHeight=430&originWidth=793&size=42405&status=done&style=none&width=396.5)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1595499705902-f3960cb2-35ad-4d93-8529-5a29f5cf6ec5.png#align=left&display=inline&height=207&margin=%5Bobject%20Object%5D&name=image.png&originHeight=413&originWidth=556&size=51405&status=done&style=none&width=278)
<a name="hgh9q"></a>
### 计划UI模型V0.0：
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1595401259181-358f21ee-7a05-4d9e-864b-60856d5def70.png#align=left&display=inline&height=311&margin=%5Bobject%20Object%5D&name=image.png&originHeight=621&originWidth=717&size=37119&status=done&style=none&width=358.5)<br />

<a name="aEiPk"></a>
### 项目开发环境：

- anaconda3+spyder4.01：环境管理与IDE，以下模块都通过conda安装
- python3.7.6：anaconda3自带的python版本
- tk8.6.8：GUI界面（老版本程序使用，现改为pyqt）
- pyqt5.9.2：GUI界面
- reportlab3.5.26：生成PDF
- pymysql0.9.3：对MySql数据库操作
- ctype：python3.7.6自带版本，C语言的接口，带有指针等功能
- cyserial3.4：对串口操作
<a name="Lphty"></a>
### 项目文件说明：
old_sr_hard_test.py：项目的功能实现代码，最终将作为一个module供调用，主函数也在该文件中<br />generate_pdf.py：包含新版pdf生成类和测试主函数<br />test_pdf.py：测试pdf生成的旧版类和测试主函数，弃用，存档<br />test_tkinter.py：包含gui的类和测试主函数<br />test_pymysql.py：包含测试mysql读取写入的函数<br />test_uart.py：包含封装的串口类，实现热插拔<br />test_global.py：测试global变量的文件<br />test_dll.py：测试读取dll并使用接口的函数，包含对nicelabel和打印机两个dll接口的使用
<a name="aFb76"></a>
### PyQt5 GUI
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596161733431-15b90dbd-744d-4141-8c44-c614c6de5009.png#align=left&display=inline&height=307&margin=%5Bobject%20Object%5D&name=image.png&originHeight=613&originWidth=1303&size=79194&status=done&style=none&width=651.5)<br />GUI界面采用PyQt5，其中Ui_MainWindow、Ui_Dialog和Ui_version_dialog是使用qtdesigner绘制.ui后通过**pyuic5**生成的类文件，将.ui转换为.py需要pyqt5-tools工具，anaconda3自带pyqt5，就包含了该功能包，故无需下载，在conada界面输入以下命令：
```python
pyuic5 -o C:\Users\liuya\Desktop\SR_work\miangui.py C:\Users\liuya\Desktop\SR_work\miangui.ui
```
对于.ui中用到的资源文件.qrc，也需要通过**pyrcc5**转换为.py才可以import，命令如下：
```python
pyrcc5 -o C:\Users\liuya\Desktop\SR_work\sr_version_rc.py C:\Users\liuya\Desktop\SR_work\sr_version.qrc
```


<a name="t0lJW"></a>
### UART
<a name="qLMol"></a>
### PyMySql
<a name="EnlN7"></a>
### PDF
<a name="3MiE4"></a>
### PCAN

<br />
<br />
<br />

