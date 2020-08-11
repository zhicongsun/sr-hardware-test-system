# SR 硬件测试系统开发手册


<br />项目开始日期：2020.07.17<br />文档更新日期：2020.08.10<br />更新人员：研发部硬件组SZC<br />注意：更新内容将标红示意
### 项目描述：

- 步骤一：登陆。测试人员输入账号密码。管理员直接操作数据库注册（后续可改进为其他方式）
- 步骤一：机器人控制板上贴有二维码，二维码记录了控制板的版本等信息，测试人员使用扫描枪读取信息（串口读取），GUI显示扫码枪连接状态和控制板版本信息
- 步骤二：测试人员手动烧录测试固件，烧录成功后控制板向PC端返回版本信息（串口）并GUI显示，随后控制板等待PC发送测试指令
- 步骤三：测试人员通过PC的GUI界面发送测试指令（串口），测试控制板外设等功能，统计丢包率等各项指标（详见控制板外设测试方案），最终得到控制板是否合格的结论，GUI显示合格结论和各项指标
- 步骤四：若合格，测试人员手动烧写功能固件，控制板返回功能固件版本信息，GUI显示信息，测试人员按GUI按钮打印SN码（或自动）；若不合格，测试人员按GUI按钮（或自动），生成不合格编号并打印不合格二维码
- 按GUI按钮生成测试报告，并将过程信息写入数据库。
<a name="55Dp5"></a>
### 数据库sr_test存放的数据：
<a name="JcOYc"></a>
#### 使用注意事项：

1. 数据库账号SR密码SR2020
1. 表内数据类型，没有特别标注的默认为VARCHAR(45)对应Python写入数据时应为string类型
1. 每个Table只能有16个变量，因此增加新的测试信息时，需要增加Tabel来容纳新的变量
1. 需要在Python上操作数据库时，对应的SQL语句建议使用SQL客户端生成，避免不了解MYSQL的开发者犯不小心的语法错误；
1. 在MySQL Workbench中修改Tabel的方法，右击Tabel选Alter Tabel选项，加入新的变量时，PK和NN需要打钩才可以支持数据的写入。创建Tabel的方法，在数据库下的Tabel上右击，点击Create Tabel设置名称等即可

![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1597113484958-fd3943ee-6624-44a9-8c38-79b3cad7c960.png#align=left&display=inline&height=176&margin=%5Bobject%20Object%5D&name=image.png&originHeight=474&originWidth=1473&size=65237&status=done&style=none&width=546)

6. MySQL客户端版本：

![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1597026900214-cf5142e9-776f-4aa5-8d39-96bc23720c94.png#align=left&display=inline&height=322&margin=%5Bobject%20Object%5D&name=image.png&originHeight=322&originWidth=560&size=23687&status=done&style=none&width=560)
<a name="XiSH5"></a>
####  Tabel 1：adminstrators_data

- admin_name：账号
- adminstrators_password：密码
- admin_mac_address:：用于保存本地PC的MAC地址
- admin_remember：用于记录本次登录是否保存密码
<a name="Hh2Yu"></a>
#### Tabel 2: pcb_data

- admin_name：检测人员名称
- date_time：测试的时间信息
- pcb_version：PCB的扫描得到的控制板版本信息
- test_firmwave_version：测试固件的版本号
- is_qualified_or_not：是否合格（True or False）
- fucn_firmwave_version：功能固件版本，不合格产品无则为Null
- pcb_numb：测试编号，可以是合格编号或者不合格编号
- io_din：输入IO口是否运行良好
- io_dout：输出IO口是否运行良好
- uart115200_packet_loss_rate：UART波特率115200丢包率（INT）
- uart115200_error_rate：UART波特率115200的误码率（INT）
- uart115200_delay_time：UART波特率115200的传输延迟（INT）
- can50K_packet_loss_rate：CAN波特率50K丢包率（INT）
- can50K_error_rate：CAN波特率50K误码率（INT）
<a name="a8yF8"></a>
#### Tabel 3: peripeiral_data

- pcb_numb：测试编号，可以是合格编号或者不合格编号
- io_din：输入IO口是否运行良好
- io_dout：输出IO口是否运行良好
- uart115200_packet_loss_rate：UART波特率115200丢包率（INT）
- uart115200_error_rate：UART波特率115200的误码率（INT）
- uart115200_delay_time：UART波特率115200的传输延迟（INT）
- can50K_packet_loss_rate：CAN波特率50K丢包率（INT）
- can50K_error_rate：CAN波特率50K误码率（INT）
- uart9600_packet_loss_rate：UART波特率9600丢包率（INT）
- uart9600_error_rate：UART波特率9600的误码率（INT）
- uart9600_delay_time：UART波特率9600的传输延迟（INT）
- can100K_packet_loss_rate：CAN波特率100K丢包率（INT）
- can100K_error_rate：CAN波特率100K误码率（INT）
<a name="C7aM6"></a>
###  项目功能需求拆分以及完成情况：

- [x] 系统规划梳理：
      - 细化系统流程
      - 完整的测试人员操作步骤
      - EU200测试方案细化，通信方案与协议的确定
- [x] GUI交互界面：使用pyqt为GUI框架
      - 登陆界面：用户权限，需要账户密码登陆GUI交互界面，支持保存密码
      - 注册界面：已注册的管理人员可为新用户注册账号，也可以通过注册新账号来修改密码，账号信息会自动覆盖。有需要可将注册权限改为超级管理员。
      - 测试系统主界面：
         1. HELP菜单栏：可连接到软件在线帮助文档、显示软件版本界面、连接斯坦德机器人官网
         1. 硬件信息：显示扫码枪实时连接状态，控制器版本、测试固件版本，测试是否合格，功能固件版本。
         1. 外设信息：显示IO口、CAN、SPI、外设的测试数据，另外留了其他1和其他2接口，可补充数据。每一个接口的信息栏都有4个信息条，前3条显示数据，最后一条显示该接口的提示信息。（硬件信息、外设测试情况用于显示实时的数据，无数据状态时信息栏为默认的灰底黑色，有数据则为红底白色。）
         1. 当前状态与测试速度：显示实时的后台信息，以及本次测试的进度。蓝底红字部分显示操作提示信息，用户根据信息进行PCB测试即可。
         1. 选项：
            1. “生成PDF..。”按钮：
               1. 生成以“测试编号.pdf”命名的文件，保存在程序安装路径的pdfs文件夹中
               1. 打印标签，标签显示测试编号与测试的控制器版本，控制器测试通过打印SN码，不通过则打印二维码
               1. 写入数据库。将硬件信息和外设测试情况写入sr_test库中
               1. 生成以“测试编号.txt”命名的文档，保存在程序安装路径的txt文件夹下，方便开发人员检测故障。
            2. “取消本次测试”按钮：将除了扫码枪状态的信息都重置为默认值，相应的信息栏都会变成灰底黑字
      - 软件版本信息界面：显示软件版本号，公司标志，版权声明，技术支持联系方式；
- [x] 串口读取扫描枪数据：
      - 实现串口的热插拔，随时插入使用
      - 自动感知读取数据，提示下一步操作步骤和当前操作问题
- [x] PDF测试报告自动生成，可自定义PDF格式（PDF样式、表格、字体、图片）
- [x] 打印标签：读取Nicelabel dll，利用接口打印二维码和SN码

   （Nicelabel提供的接口不具有标签设计的功能，只能读取现成的模版，故换为以下方案）

- [x] 打印标签：python生成二维码和SN码，标签的编码为控制板的测试编码，以“年月+T/F+四位编号”命名，如“20200804T004”表示2020年8月4日第4个测试通过的控制器。标签可加入文字信息，利用打印机的dll接口打印
- [x] PCAN的集成和封装：实现继承PCANBasic类的DriveCAN，发送数据等帧类型可选，读取对应id的报文
- [x] USB2SPI的集成和封装：实现主机配置、读取功能、写入功能、写读功能
- [x] 系统稳定性的完善：

1.解决GUI结束后uart进程后台继续运行的问题<br />2.解决软件重运行崩溃的问题，原因是重新运行时未清除变量，可在spyder的预设中修改设置<br />3.解决软件重运行module 重载的问题，可在spyder的预设中修改设置为取消重载

- [x] USB转SPI测试集成
- [x] 打印的pdf中增加图表功能
- [ ] 通过CAN和控制板交互信息，测试EU200
- [ ] 将程序打包成exe文件
<a name="VYOhY"></a>
### 控制板外设测试方案：

- 硬件平台：EU200，具有一路UART，一路CAN，一路CAN和UART复用端口
- 测试指标：
   - 通信接口在**不同波特率下**的丢包率、误码率、传输延时（功能实现优先级：丢包率>误码率>传输时延）
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

具体通信指标的测试流程如下：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596417914475-ff257340-f1c9-4b88-8beb-5df979ff17fa.png#align=left&display=inline&height=606&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1211&originWidth=712&size=130747&status=done&style=none&width=356)<br />CAN的帧结构如图所示：  <br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596421268851-7385cd1b-054c-4652-ba26-6ccf88e97012.png#align=left&display=inline&height=60&margin=%5Bobject%20Object%5D&name=image.png&originHeight=61&originWidth=341&size=2146&status=done&style=none&width=334)

         - ID：1byte。
            - 测试UART：0xC1 表示开始帧；0xC2表示ACK开始帧；0xC3为结束帧；0xC4为ACK结束帧；0xC5消息帧；
            - 测试CAN：接着以上写
         - DATA[~]：消息内容
            - 开始帧：
               - DATA[0]是波特率位：0xB1——50K，9600

     0xB2——100k，115200

               - DATA[1]：状态，        0xA1——就绪

     0xA2——未就绪

               - DATA[2]~DATA[7]：默认数据位，为0xff
            - ACK开始帧：
               - DATA[0]是波特率位
               - DATA[1]：状态
               - DATA[2]~DATA[7]：默认数据位，为0xff
            - 消息帧：
               - DATA[0]是波特率位
               - DATA[1]是帧数：表示这是发送端发送/接收端接收到的第几个帧
               - DATA[2]~DATA[7]：默认数据位，为0xff，也是用来判断误码率的
            - 结束帧：
               - DATA[0]是波特率位
               - DATA[1]是帧数：表示一共发送了多少消息帧
               - DATA[2]~DATA[7]：默认数据位，为0xff
            - ACK结束帧：
               - DATA[0]是波特率位
               - DATA[1]是帧数位：表示一共接收了多少消息帧
               - DATA[2]：丢包率，x代表丢包率为x%
               - DATA[3]：误码率
               - DATA[4]~DATA[7]：默认数据位，为0xff

![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596417923314-a6c39b1a-777d-49ca-93e4-e73163c6d881.png#align=left&display=inline&height=326&margin=%5Bobject%20Object%5D&name=image.png&originHeight=651&originWidth=595&size=56396&status=done&style=none&width=297.5)<br />UART的帧结构如图所示：  (除了帧尾和校验位，其他与CAN帧相同)<br />             ![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596421292381-d167a091-5151-42cd-b8ba-030add0706b4.png#align=left&display=inline&height=63&margin=%5Bobject%20Object%5D&name=image.png&originHeight=64&originWidth=453&size=3292&status=done&style=none&width=447)

         - 帧头：1byte。0x5A
         - 命令：1byte。0xC1 表示开始帧；0xC2表示ACK开始帧；0xC3为结束帧；0xC4为ACK结束帧；0xC5消息帧；
         - DATA[~]：消息内容
            - 开始帧：
               - DATA[0]是波特率位：0xB1——9600

     0xB2——115200...

               - DATA[1]：串口状态，0xA1——就绪

     0xA2——未就绪

               - DATA[2]~DATA[7]：默认数据位，为0xff
            - ACK开始帧：
               - DATA[0]是波特率位
               - DATA[1]：串口状态
               - DATA[2]~DATA[7]：默认数据位，为0xff
            - 消息帧：
               - DATA[0]是波特率位
               - DATA[1]是帧数：表示这是发送端发送/接收端接收到的第几个帧
               - DATA[2]~DATA[3]是发送时间戳位（TX端发送的帧）/传输延迟位（RX端发送的帧）：DATA[2]为高位，DATA[3]为低位，以第一次消息帧发送为起始时间，单位为秒；传输延迟为接受到TX发送过来的帧与其时间戳的时间差。注意：只测试单向的传输延迟。
               - DATA[4]~DATA[7]：默认数据位，为0x00，也是用来判断误码率的
            - 结束帧：
               - DATA[0]是波特率位
               - DATA[1]是帧数：表示一共发送了多少消息帧
               - DATA[2]~DATA[7]：默认数据位，为0xff
            - ACK结束帧：
               - DATA[0]是波特率位
               - DATA[1]是帧数位：表示一共接收了多少消息帧
               - DATA[2]：丢包率，x代表丢包率为x%
               - DATA[3]：误码率
               - DATA[4]~DATA[5]：传输延迟（s）
               - DATA[6]~DATA[7]：默认数据位，为0xff
         - 校验位：1byte。CRC校验
         - 帧尾：2byte。0x0D 0x0A
<a name="7DCO2"></a>
### 程序流程示意图V0.1：
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596164065741-4f0828f1-9855-4121-87d4-20860a9177ca.png#align=left&display=inline&height=669&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1337&originWidth=709&size=96120&status=done&style=none&width=354.5)![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596163505782-196e3636-bd71-4ad4-87ac-6d2eb1f247b8.png#align=left&display=inline&height=13&margin=%5Bobject%20Object%5D&name=image.png&originHeight=25&originWidth=1&size=77&status=done&style=none&width=0.5)
<a name="ww5I9"></a>
### 数据流示意图V0.1：
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596421689746-e34862c4-450e-4be7-8f4b-f1c485865ca3.png#align=left&display=inline&height=215&margin=%5Bobject%20Object%5D&name=image.png&originHeight=430&originWidth=793&size=42246&status=done&style=none&width=396.5)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596421941240-e3a434bc-3ba8-45f4-bc53-87dd7744a199.png#align=left&display=inline&height=207&margin=%5Bobject%20Object%5D&name=image.png&originHeight=413&originWidth=556&size=58326&status=done&style=none&width=278)<br />

<a name="hgh9q"></a>
### UI模型V0.1：
测试界面如图，分为菜单栏、硬件信息、外设测试情况、当前状态与测试速度、选项五个部分，各个部分功能介绍如下：![测试界面2.PNG](https://cdn.nlark.com/yuque/0/2020/png/753325/1597021149915-caced51c-db6d-435d-95c3-5aa19958d847.png#align=left&display=inline&height=686&margin=%5Bobject%20Object%5D&name=%E6%B5%8B%E8%AF%95%E7%95%8C%E9%9D%A22.PNG&originHeight=686&originWidth=1555&size=79734&status=done&style=none&width=1555)<br />
<br />

<a name="aEiPk"></a>
### 项目开发环境：

- anaconda3+spyder4.01：环境管理与IDE，以下模块都通过conda安装
- python3.7.6：anaconda3自带的python版本
- tk8.6.8：GUI界面（老版本程序使用，现改为pyqt）
- pyqt5.9.2：GUI界面
- PCANBasic API V4.4.1.413：PCAN官方库
- reportlab3.5.26：生成PDF
- pymysql0.9.3：对MySql数据库操作
- ctype：python3.7.6自带版本，C语言的接口，带有指针等功能
- cyserial3.4：对串口操作
- uuid：获取唯一ID，获取本机MAC地址使用到
- re：自带版本，正则表达式匹配
- daetime：自带版本，获取当前时间信息
- webbrowser：自带版本，调取网页
- threading：自带版本，线程控制
<a name="Lphty"></a>
### 项目文件说明：
old_sr_hard_test.py：项目的功能实现代码，最终将作为一个module供调用，主函数也在该文件中<br />generate_pdf.py：包含新版pdf生成类和测试主函数<br />test_pdf.py：测试pdf生成的旧版类和测试主函数，弃用，存档<br />test_tkinter.py：包含gui的类和测试主函数<br />test_pymysql.py：包含测试mysql读取写入的函数<br />test_uart.py：包含封装的串口类，实现热插拔<br />test_global.py：测试global变量的文件<br />test_dll.py：测试读取dll并使用接口的函数，包含对nicelabel和打印机两个dll接口的使用
<a name="aFb76"></a>
### 数据处理
<a name="VCsUR"></a>
#### pcb_data和default_pcb_data：global变量
这两个list在mian函数里面初始化的。这里的pcb_data与数据库的pcb_data表不同，这里的pcb_data是list，每次控制器测试过程中，都用pcb_data来保存测试数据和状态数据，最后将需要的部分写入sr_test数据库的adminstrators_data、pcb_data和periphral_data三个表中。而dafault_pcb_data则是默认的初始数据，用于每次控制器测试完成后对pcb_data的值重置。<br />pcb_data的[0]位置是一个字典，这部分是给生成PDF封面时使用的，原因在于字典可以通过键名使用键值，程序一开始便如此书写，虽与list的其他部分（为list）不统一，但也无改变必要。
<a name="VNWyq"></a>
#### 二次开发注意事项

- 注意变量类型是string还是数值
- 注意pcb_data里许多string赋T/F值时候是"True"/"False"而不是bool型，这在条件判断的时候不注意容易出错，使用string的原因是方便与数据库统一，对应数据库中的VARCHAR(45)变量。
- 其他global型的变量的使用情况：

![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1597117258094-b8f862d2-5060-4351-8924-521b16bbc696.png#align=left&display=inline&height=362&margin=%5Bobject%20Object%5D&name=image.png&originHeight=724&originWidth=395&size=37724&status=done&style=none&width=197.5)

- 每次测试过程，pcb_data的数据只有一次赋值（不计最后测试结束时的重置），因此不存在抢占写入的问题，若以后开发过程对同一个数据有多处写入（赋值），则写数据时需要使用threading.lock模块，在全局变量的写入前后分别使用lock.acquire()和lock.release()的加锁解锁功能。
```python
pcb_data = [ # 测试的数据
        {'report_code': 'None', 
         'task_name':'None',
         'report_date':'None',
         'report_creator':'None'},
        ['admin_name','None'], # 在is_admin中赋值，登录时
        ['date_time','None'], # 在generate_pcb_nub中赋值，最后按下生成PDF按钮时
        ['pcb_version','None'], # 在runuart中赋值，扫码时
        ['test_firmwave_version','V0.0.1'],
        ['qualified_or_not','False'],
        ['func_firmwave_version','V0.0.1'],
        ['pcb_numb','None'], # 在generate_pcb_nub中赋值，最后按下生成PDF按钮时
        ['io_din','1101'],
        ['io_dout','0001'],
        ['uart115200_packet_loss_rate',10],
        ['uart115200_error_rate',20],
        ['uart115200_delay_time',100],
        ['can50k_packet_loss_rate',35],
        ['can50k_error_rate',45],
        ['uart9600_packet_loss_rate',20],
        ['uart9600_error_rate',10],
        ['uart9600_delay_time',200],
        ['can100k_packet_loss_rate',45],
        ['can100k_error_rate',35]
    ]
default_pcb_data = [ # 默认的数据，重置数据时候使用
        {'report_code': 'None', 
         'task_name':'None',
         'report_date':'None',
         'report_creator':'None'},
        ['admin_name','None'], # 在is_admin中赋值，登录时
        ['date_time','None'], # 在generate_pcb_nub中赋值，最后按下生成PDF按钮时
        ['pcb_version','None'], # 在runuart中赋值，扫码时
        ['test_firmwave_version','None'],
        ['qualified_or_not','None'],
        ['func_firmwave_version','None'],
        ['pcb_numb','None'], # 在generate_pcb_nub中赋值，最后按下生成PDF按钮时
        ['io_din','None'],
        ['io_dout','None'],
        ['uart115200_packet_loss_rate',-1],
        ['uart115200_error_rate',-1],
        ['uart115200_delay_time',-1],
        ['can50k_packet_loss_rate',-1],
        ['can50k_error_rate',-1],
        ['uart9600_packet_loss_rate',-1],
        ['uart9600_error_rate',-1],
        ['uart9600_delay_time',-1],
        ['can100k_packet_loss_rate',-1],
        ['can100k_error_rate',-1]
    ]
```
<a name="Ti3yB"></a>
### GUI
<a name="VxL1r"></a>
#### 各个界面
![注册界面.PNG](https://cdn.nlark.com/yuque/0/2020/png/753325/1597028299423-101a9e29-6e58-4589-b042-90330c058eb1.png#align=left&display=inline&height=337&margin=%5Bobject%20Object%5D&name=%E6%B3%A8%E5%86%8C%E7%95%8C%E9%9D%A2.PNG&originHeight=538&originWidth=329&size=11440&status=done&style=none&width=206)![登录界面.PNG](https://cdn.nlark.com/yuque/0/2020/png/753325/1596190823166-051f2c7a-e330-489b-961e-f0f8e950928f.png#align=left&display=inline&height=223&margin=%5Bobject%20Object%5D&name=%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2.PNG&originHeight=316&originWidth=337&size=8434&status=done&style=none&width=238)![版本界面.PNG](https://cdn.nlark.com/yuque/0/2020/png/753325/1596190821761-6cb2fbc7-184b-4054-afab-b25ce69706c0.png#align=left&display=inline&height=241&margin=%5Bobject%20Object%5D&name=%E7%89%88%E6%9C%AC%E7%95%8C%E9%9D%A2.PNG&originHeight=472&originWidth=575&size=52506&status=done&style=none&width=293)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1597028429832-8f31c009-08a1-4284-ba4f-0af27fd15b55.png#align=left&display=inline&height=84&margin=%5Bobject%20Object%5D&name=image.png&originHeight=120&originWidth=358&size=5568&status=done&style=none&width=252)![测试界面2.PNG](https://cdn.nlark.com/yuque/0/2020/png/753325/1597028322337-334ccf93-63d1-4cd7-a0f2-4c987ed159eb.png#align=left&display=inline&height=686&margin=%5Bobject%20Object%5D&name=%E6%B5%8B%E8%AF%95%E7%95%8C%E9%9D%A22.PNG&originHeight=686&originWidth=1555&size=79734&status=done&style=none&width=1555)
<a name="ptPpI"></a>
#### 各个类之间的继承关系UMI图
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1597114321852-50a02307-34c1-4fe3-80d3-5311a04503ca.png#align=left&display=inline&height=308&margin=%5Bobject%20Object%5D&name=image.png&originHeight=615&originWidth=1688&size=105166&status=done&style=none&width=844)<br />GUI界面采用PyQt5，其中Ui_MainWindow、Ui_Dialog、Ui_Register_Dialog和Ui_version_dialog是使用qtdesigner绘制.ui后生成的py类。
<a name="XqHWj"></a>
#### 二次开发注意事项

- **更改GUI界面的方法**

步骤一：在QtDesigner中绘制.ui文件，将.ui文件和所用到的资源文件.qrc转化为.py<br />pyqt5-tools工具包含了可将.ui转化为.py的模块**pyuic5**，而anaconda3自带pyqt5，就包含了pyqt5-tools，故无需下载，在conada界面输入以下命令：
```python
pyuic5 -o C:\Users\liuya\Desktop\SR_work\miangui.py C:\Users\liuya\Desktop\SR_work\miangui.ui
```
对于.ui中用到的资源文件.qrc，也需要通过**pyrcc5**转换为.py才可以import，命令如下：
```python
pyrcc5 -o C:\Users\liuya\Desktop\SR_work\sr_version_rc.py C:\Users\liuya\Desktop\SR_work\sr_version.qrc
```
步骤二：将.qrc生成的.py需要放置到工程文件夹中，才可import；.ui生成的.py文件不需要复制进工程文件夹，只需要复制生成的.py文件中的类，在sr_test_hd_system.py中替换对应的类，新import 资源文件的语句也需要复制，在生成的.py文件最底端，如下图所示。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1597029849962-03232b10-b226-433b-a056-e09f05ff3b61.png#align=left&display=inline&height=582&margin=%5Bobject%20Object%5D&name=image.png&originHeight=582&originWidth=1193&size=87097&status=done&style=none&width=1193)<br />若重置主测试界面的.ui，生成的类中需要将setupUi中setSizeGripEnabled置为False，否则报错，如下图所示。<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1597039526720-3d70c70a-fda3-48c1-b12f-aa43287d506b.png#align=left&display=inline&height=408&margin=%5Bobject%20Object%5D&name=image.png&originHeight=408&originWidth=1093&size=45202&status=done&style=none&width=1093)
<a name="t0lJW"></a>
### 注册功能
<a name="q1p87"></a>
#### 功能描述
可以通过已注册的账号信息来注册新的用户，也可以通过注册新用户来修改密码，账户会自动覆盖。已注册的账户名为SR，密码为SR2020。
<a name="01ZVT"></a>
#### 技术实现
注册功能对应的UI界面类是Ui_Register_Dialog和RegisterWin，其中Ui_Register_Dialog是.ui生成的类，RegisterWin则继承自Ui_Register_Dialog和QMainWindow，用于实现一些具体逻辑，方便.ui的二次开发。<br />RegisterWin的实例对象是在MainWindow类的构造函数中生成的，见以下代码块第15行。<br />
```python
class MainWindow(QMainWindow,Ui_MainWindow):
    """登录界面的类

    继承自Ui_MainWindow，实现用户权限功能，可调用测试界面、提示错误信息
    """
    exit_flag = "x" # 关闭事件的标识位，点击了取消或者x按钮置"x"，登录测试系统后自动关闭登录界面时置"onGloginClick"
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.mBtnLogin.clicked.connect(self.onLoginClick)
        self.mBtnCancel.clicked.connect(self.onCancelClick)
        # 要在主窗口类的初始化函数中对子窗口进行实例化，如果在其他函数中实例化子窗口
        # 可能会出现子窗口闪退的问题
        self.ChildDialog = ChildWin() # 测试界面的类
        self.RegisterDialog = RegisterWin() # 注册界面的类
        [is_mac_existence,admin_name,password] = self.is_remenbered_admin()
        if is_mac_existence == "True":
            self.mTextUserName.setText(admin_name)
            self.mTextPassword.setText(password)
```
当测试人员按下注册按钮，则调用类的onLoginClick方法，该方法的流程图如下左图：<br />该方法注册新的账户信息的函数为register_admin（独立的函数，非类方法），函数处理流程如下右图：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1597042968178-022db15b-c76d-486e-b55d-d5c5fe6a5770.png#align=left&display=inline&height=383&margin=%5Bobject%20Object%5D&name=image.png&originHeight=513&originWidth=367&size=16222&status=done&style=none&width=274)![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1597042985363-fedd4aa2-b5c7-4059-b146-5b5ef040adf3.png#align=left&display=inline&height=412&margin=%5Bobject%20Object%5D&name=image.png&originHeight=624&originWidth=335&size=18679&status=done&style=none&width=221)
<a name="NUXbJ"></a>
### 保持登录（保存密码）功能
<a name="piEse"></a>
#### 功能描述
在登录时候勾选保持登录，下次打开软件时候自动填充账号信息；登录时不勾选则需要手动输入；
<a name="PB6zJ"></a>
#### 技术实现
记录状态：在按下登录按钮时，触发了MainWindow类的onLoginClick函数，若勾选了保持登录选项，则调用get_mac_address()获取MAC地址，并将admin_remember置为"True"，接着调用register_admin将本次数据写入sr_test数据库的administrators_data表。见以下代码块的12~16行：
```python
def onLoginClick(self):
        """登录按钮的响应函数

        判断输入的账户信息是否存在数据库中，是则关闭登录界面、打开测试界面，否则提示原因
        """
        admin_name = self.mTextUserName.text()
        password = self.mTextPassword.text()
        is_admin_or_not = is_admin(admin_name,password)
        # 账户正确
        if is_admin_or_not[0] == True:
            self.exit_flag = "onLoginClick"
            # 如果选择保持登录状态，则把PC的MAC地址写入数据库，再次打开程序的时候会检测MAC地址是否匹配，匹配则自动显示账户密码
            if self.checkBox.isChecked():
                admin_mac_address = get_mac_address()
                admin_remember = "True"
                register_admin(admin_name,password,admin_mac_address,admin_remember)
            #不选择保持登录，则向MAC地址和是否保存写入"None"
            else:
                register_admin(admin_name,password,"None","None")
            self.close()
            self.ChildDialog.show()
        # 账户不正确
        else:
            self.exit_flag = "x"
            QMessageBox.information(None, "登录提示", is_admin_or_not[1], QMessageBox.Ok, QMessageBox.Ok)
```
读取状态：每次打开软件进入登录界面时，MainWindow类的构造函数会使用类的方法is_remembered_admin()去判断上次登录是否选择保持登录，是则调取保存的账户并自动填充。见以下代码10~13行：
```python
def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.mBtnLogin.clicked.connect(self.onLoginClick)
        self.mBtnCancel.clicked.connect(self.onCancelClick)
        # 要在主窗口类的初始化函数中对子窗口进行实例化，如果在其他函数中实例化子窗口
        # 可能会出现子窗口闪退的问题
        self.ChildDialog = ChildWin() # 测试界面的类
        self.RegisterDialog = RegisterWin() # 注册界面的类
        [is_mac_existence,admin_name,password] = self.is_remenbered_admin()
        if is_mac_existence == "True":
            self.mTextUserName.setText(admin_name)
            self.mTextPassword.setText(password)
```
其中MainWindow的方法is_remembered_admin通过读取本机PC的MAC地址，与数据库内的比对，如有选择保持登录，则会返回账号的信息。当数据库部署至服务器时，该功能可正常运行。
<a name="bxoTE"></a>
### UART驱动
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596422624173-a1ae58b0-0332-45ab-816e-b3dad3f380f0.png#align=left&display=inline&height=127&margin=%5Bobject%20Object%5D&name=image.png&originHeight=208&originWidth=311&size=7585&status=done&style=none&width=190)<br />实现了热插拔，详见源代码<br />接收线程uart_thread，注意使用到了global<br />UART热插拔待解决问题：重新将端口连上，需要大约3s重才能成功重连；有时候重连不成，显示连上但是断线，需要重新插拔。只要打开软件前连上端口，就不会出现以上问题。
```python
def runuart():
    global pcb_data
    global readpcbdata
    global uart_thread_destroy_flag
    while uart_thread_destroy_flag:
        recevied_data = readpcbdata.waitForPcbData()
        if recevied_data[0] is True:
            pcb_data[2][1] = recevied_data[1]
    try:
        readpcbdata.ser.close()#得到线程结束标识，则关闭串口
    except:
        print("串口还没打开，不用重复关闭")
```
<a name="3MiE4"></a>
### PCAN驱动
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596423630212-888680a0-5bf0-46a8-8328-864bdca4daf5.png#align=left&display=inline&height=262&margin=%5Bobject%20Object%5D&name=image.png&originHeight=348&originWidth=313&size=15359&status=done&style=none&width=236)<br />can线程，注意global
```python
def runcan():
    global objPCAN
    global can_thread_destroy_flag
    while can_thread_destroy_flag:
        objPCAN.can_read()
    try:
        objPCAN.Uninitialize(PCAN_NONEBUS)
    except:
        print("已经关闭can口，不用重新关闭")
```
<a name="YW2G6"></a>
### USB2SPI驱动
主要为主机的配置、写数据、读数据、写读数据，支持单SPI设备的驱动。self.DevIndex默认为0。<br />若要支持多设备，需要改变self.DevIndex的值，并调用SPI_Init初始化。
<a name="qLMol"></a>
### PyMySql操作
没有类，读写两个函数。写：<br />pymysql.connnect连接了数据库<br />sql对应的SQL语句操作对应的表
```python
def write_database(pcb_data):
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()
    
    sql = """INSERT INTO `sr_test`.`pcb_data` 
            (`user_name`, `pcb_version`, `qualified_or_not`, `firmware_version`, `pcb_numb`) 
             VALUES (%s, %s, %s, %s, %s)"""
    sr_user_name = pcb_data[1][1]
    sr_pcb_version = pcb_data[2][1]
    sr_qualified_or_not = pcb_data[3][1]
    sr_firmware_version = pcb_data[4][1]
    sr_pcb_numb = pcb_data[5][1]
    values = (sr_user_name,sr_pcb_version,sr_qualified_or_not,sr_firmware_version,sr_pcb_numb)
    try:
        cursor.execute(sql,values)
        db.commit()
        print("成功向表pcb_data中插入数据")
    except:
        db.rollback()
        print("向表pcb_data插入数据失败")
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")
```
读：
```python
def is_admin(admin_name,password):#通过数据库判断是否未管理员，是则返回True,否则返回False
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()
    search_cmd = """select * from sr_test.administrators_data"""
    cursor.execute(search_cmd)
    admin_data = cursor.fetchall()
    each_result = []*len(admin_data)
    allow_open  =  [None,"None"]    
    for i in range(len(admin_data)):
        each_result.append((admin_name in admin_data[i]))
    result = True in each_result
    print(each_result)
    
    if result == True:
        id_admin = each_result.index(True)#记录是哪个用户
        print("用户 %s 存在" %admin_name)
        if password == admin_data[id_admin][1]:#判断密码是否正确
            allow_open[0] = True
            print("用户 %s 密码正确" % admin_name)
            allow_open[1] = "你好管理员"
        else:
            allow_open[0] = False
            print("用户 %s 密码错误" % admin_name)
            allow_open[1]="用户存在，密码错误"
    else:
        print("用户不存在")
        allow_open[1] = "用户不存在"
    
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")
    return allow_open

```
<a name="EnlN7"></a>
### PDF生成
![image.png](https://cdn.nlark.com/yuque/0/2020/png/753325/1596422884062-6530a556-e683-4c46-8919-51d5d537ecde.png#align=left&display=inline&height=93&margin=%5Bobject%20Object%5D&name=image.png&originHeight=128&originWidth=311&size=4928&status=done&style=none&width=226)<br />读取pcb_data的数据接口，pcb_data是全局数据
```python
 def genTaskPDF(self,pcb_data):
        self.pcb_data=pcb_data
        # self.filename = self.pcb_data[0]['report_code']#编号
        print(self.pcb_data[2][1])
        self.filename = self.pcb_data[2][1] #二维码数据
 ...
```

<br />
<br />

