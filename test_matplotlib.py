
import matplotlib.pyplot as plt
import os

def draw_line_chart(imgname):
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_1 = [i * 2 for i in x]
    y_2 = [i * 4 for i in x]
    
    # 创建画布
    plt.figure()
    
    '''绘制第一条数据线
    1、节点为圆圈
    2、线颜色为红色
    3、标签名字为y1-data
    '''
    plt.plot(x, y_1, marker='o', color='r', label='y1-data')
    
    '''绘制第二条数据线
    1、节点为五角星
    2、线颜色为蓝色
    3、标签名字为y2-data
    '''
    plt.plot(x, y_2, marker='*', color='b', label='y2-data')
    
    # 显示图例（使绘制生效）
    plt.legend()
    
    # 横坐标名称
    plt.xlabel('baudrate')
    
    # 纵坐标名称
    plt.ylabel('error_rate')
    
    img_path = os.getcwd() + "/matplot_images/" + imgname + ".png"
    # 保存图片到本地
    plt.savefig(img_path,dpi=500,bbox_inches = 'tight')
    
if __name__ == '__main__':
    imgname = "20200803001"
    draw_line_chart()


