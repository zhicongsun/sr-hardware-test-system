import matplotlib.pyplot as plt
import os

def draw_line_chart(pcb_numb,peripheral_type,loss_rate,error_rate,delay_time = None):

    # 定义自己的字体，微软雅黑，否则中文显示不出来,这边不用了
    # myfont = fm.FontProperties(fname=r'.\msyh.ttf') # 设置字体,配合，需要fontproperties = myfont，import matplotlib.font_manager as fm

    plt.rcParams['font.sans-serif'] = ['SimHei'] # 支持中文
    # 定义显示的数据
    
    # 根据检测id速度的类型显示Label
    if len(loss_rate)==1:
        x = range(1,2)
        x_label = ["50K_9600"]
    elif len(loss_rate)==2:
        x = range(1,3)
        x_label = ["50K_9600","100K_115200"]
    elif len(loss_rate)==3:
        x = range(1,4)
        x_label = ["50K_9600","100K_115200","200K_150000"]
    else:
        print("输入列表参数包含超过3个元素，有问题")
        pass

    # 创建画布
    plt.figure()
    #绘图
    plt.plot(x, loss_rate, marker='o', color='r', label='丢包率')
    plt.plot(x, error_rate, marker='*', color='b', label='误码率')
    if peripheral_type == "UART": # CAN没有延迟参数
        plt.plot(x,delay_time,marker='o', color='y', label='传输延迟')
    elif peripheral_type == "CAN":
        pass

    # 显示图例（使绘制生效）
    plt.legend()
    # 横坐标名称
    plt.xlabel('波特率')
    # 横坐标刻度转换为文字
    plt.xticks([1,2],x_label)
    # 纵坐标名称
    plt.ylabel('% / ms')
    # 标题
    if peripheral_type == "UART":
        plt.title("UART通信数据统计")
    elif peripheral_type == "CAN":
        plt.title("CAN通信数据统计")
    else:
        pass
    # 保存图片到本地，命名格式：pcb_numb + 外设类型
    img_path = os.getcwd() + "/matplot_images/" + pcb_numb + peripheral_type + ".png"
    plt.savefig(img_path,dpi=500,bbox_inches = 'tight')
    
if __name__ == '__main__':
    pcb_numb = "20200803T0001"
    # peripheral_type = "CAN"
    # loss_rate = [2,10,11]
    # error_rate = [3,7,2]
    # draw_line_chart(pcb_numb,peripheral_type,loss_rate,error_rate)
    
    # peripheral_type = "UART"
    # delay_time = [100,70,222]
    # draw_line_chart(pcb_numb,peripheral_type,loss_rate,error_rate,delay_time)
    peripheral_type = "UART"
    loss_rate = [2]
    error_rate = [3]
    delay_time = [100]
    draw_line_chart(pcb_numb,peripheral_type,loss_rate,error_rate,delay_time)
