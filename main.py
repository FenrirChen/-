import random
import threading

import cv2
import numpy as np
import pyautogui
import win32gui
import win32con
import PIL.ImageGrab
from PIL import ImageGrab
from pyexpat import model
import time

'''

以下为测试学习用

ima=cv2.imread("C:\\Users\\18207\\Desktop\\demo\\py\\pythonProject\\mobile_background.jpg",1)
ima=np.zeros((512,512,3),dtype=np.uint8)
cv2.line(ima,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(ima,(0,0),(255,255),(0,255,0),5)
cv2.circle(ima,(100,100),100,(0,0,255),5)
cv2.ellipse(ima,(100,100),(20,50),180,180,360,(114,114,214))
cv2.putText(ima,"Hello World",(255,255),cv2.FONT_HERSHEY_SIMPLEX,1.2,(112,222,22),5,cv2.LINE_AA)
cv2.namedWindow("imgw")
cv2.imshow("imgw",ima)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''获取当前窗口句柄'''
chuangkou=win32gui.FindWindow(None,"MuMu模拟器12")


'''写日志文件'''
def file_write(file_name,thing):
    a=open(file_name,"a+")
    a.write(thing)
    a.close()


'''找到某个图像（model）在截图中的位置'''
def getxy(model):
    left, top, right, bottom = win32gui.GetWindowRect(chuangkou)
    pyautogui.screenshot().save("Screenshot/jietu.png")
    img=cv2.imread("Screenshot/jietu.png")
    moban=cv2.imread(model)
    height,width,channel = moban.shape
    result=cv2.matchTemplate(img,moban,cv2.TM_SQDIFF_NORMED)
    upleft=cv2.minMaxLoc(result)[2]
    lowright=(upleft[0]+width,upleft[1]+height)
    avg=((upleft[0]+lowright[0])/2,(upleft[1]+lowright[1])/2)
    return avg

'''随机小范围点击'''

def click_radonm(x,y,wucha,type):
    dx=random.randint(-wucha,wucha)
    dy=random.randint(-wucha,wucha)
    #print(f"原坐标为{x}，{y}")
    x+=dx
    y+=dy
    #print(f"修正坐标为{x}，{y}")
    pyautogui.click(x, y, button=type)

'''查找某个图像是否存在'''

def is_alive(model,wucha=0.01):
    pyautogui.screenshot().save("Screenshot/jietu.png")
    img = cv2.imread("Screenshot/jietu.png")
    moban = cv2.imread(model)
    height, width, channel = moban.shape
    result = cv2.matchTemplate(img, moban, cv2.TM_SQDIFF_NORMED)
    loc=np.where(result<=wucha)
    if len(loc[0])>0:
        return True
    else:
        return False

'''点击探索'''
def tansuo_takein():
    if is_alive("tep/tansuo.png",0.2):
        a = getxy("tep/tansuo.png")
        click_radonm(a[0],a[1],10,"left")
        time.sleep(2)
    print("点击探索")

'''点击御魂'''
def yuhun_takein():
    if is_alive("tep/yuhun.png",0.2):
        print("点击御魂")
        a = getxy("tep/yuhun.png")
        click_radonm(a[0],a[1],10,"left")
        time.sleep(1)
    #print("点击御魂")

'''点击八岐大蛇'''
def dashe_takein():
    if is_alive("tep/dashe.png",0.2):
        a = getxy("tep/dashe.png")
        click_radonm(a[0],a[1],10,"left")
    print("点击大蛇")

'''八岐大蛇战斗'''
def ttk_huntu(cishu):
    cishu=int(cishu)
    while True:
        if(is_alive("tep/tiaozhan.png")):
            print(f"即将开始挑战，剩余{cishu}次")
            file_write("log.txt", f"\n即将开始挑战，剩余{cishu}次")
            a = getxy("tep/tiaozhan.png")
            click_radonm(a[0],a[1],10,"left")
            time.sleep(1)
        if(is_alive("tep/tanchi.png")):
            cishu-=1
            print(f"挑战完成，剩余{cishu}次")
            file_write("log.txt", f"\n挑战完成，剩余{cishu}次")
            a = getxy("tep/tanchi.png")
            click_radonm(a[0],a[1],10,"left")
            if(cishu==0):
                print("战斗任务完成，自动结束")
                file_write("log.txt", "战斗任务完成，自动结束")
                break

'''返回主界面'''

def zhujiemian_back():
    while True:
        if(is_alive("tep/fanhui.png",0.1)):
            a = getxy("tep/fanhui.png")
            click_radonm(a[0], a[1], 10, "left")
        else:
            if(is_alive("tep/fanhui2.png",0.1)):
                a = getxy("tep/fanhui2.png")
                click_radonm(a[0], a[1], 10, "left")
            else:
                break
        time.sleep(2)
    print("已返回主界面")


'''活动内容'''

'''源赖光活动'''
def ttk_yuanlaiguang():
    tim=1
    time_start=time.time()
    while True:
        if is_alive("tep/tiaozhan_yuanlaiguang.png",0.1):
            a = getxy("tep/tiaozhan_yuanlaiguang.png")
            click_radonm(a[0], a[1], 10, "left")
            time_start=time.time()
        if is_alive("tep/jieshu_yuanlaiguang.png",0.1):
            a = getxy("tep/jieshu_yuanlaiguang.png")
            click_radonm(a[0], a[1], 10, "left")
            time_start = time.time()
            file_write("log.txt", f"\n挑战完成{tim}次")
            tim += 1
        time_end=time.time()
        if time_end-time_start>=30:
            click_radonm(2146, 788, 10, "left")
            time.sleep(3)



'''周年庆活动'''

def zhounian_999():
    tim = 1
    time_start = time.time()
    while True:
        if is_alive("tep/zhounian_999.png", 0.1):
            a = getxy("tep/zhounian_999.png")
            click_radonm(a[0], a[1], 10, "left")
            time_start = time.time()
        if is_alive("tep/jieshu_yuanlaiguang.png", 0.1):
            a = getxy("tep/jieshu_yuanlaiguang.png")
            click_radonm(a[0], a[1], 10, "left")
            time_start = time.time()
            file_write("log.txt", f"\n挑战完成{tim}次")
            tim += 1
        time_end = time.time()
        if time_end - time_start >= 30:
            click_radonm(2146, 788, 10, "left")
            time.sleep(3)


'''活动内容到此为止'''


'''进入突破'''
def tupo_takein():
    if is_alive("tep/tupo.png",0.2):
        a = getxy("tep/tupo.png")
        click_radonm(a[0],a[1],10,"left")

zuobiao=[[1920,604],[2146,604],[2355,604],[1920,696],[2146,696],[2355,696],[1920,788],[2146,788],[2355,788]]

'''清突破'''
def ttk_tupo():
    for i in range(8):
        click_radonm(zuobiao[i][0],zuobiao[i][1],5,"left")
        time.sleep(1)
        if is_alive("tep/tupo_jingong.png",0.1):
            a=getxy("tep/tupo_jingong.png")
            click_radonm(a[0],a[1],10,"left")
            while True:
                if is_alive("tep/huizhang.png"):
                    click_radonm(zuobiao[7][0], zuobiao[7][1], 5, "left")
                    break
    for i in range(3):
        click_radonm(zuobiao[8][0], zuobiao[8][1], 5, "left")
        time.sleep(1)
        a = getxy("tep/tupo_jingong.png")
        click_radonm(a[0], a[1], 10, "left")
        a=getxy("tep/fanhui.png")
        click_radonm(a[0], a[1], 10, "left")
        time.sleep(1)
        click_radonm(a[0], a[1], 10, "left")

'''模式选择'''
def method_choice():
    clear=open("log.txt","w")
    clear.truncate(0)
    clear.close()
    file_write("log.txt", "开始运行")
    print("请选择模式:")
    print("1.魂土")
    print("2.绘卷")
    method=int(input())
    if method not in (1,2):
        print("输入错误，请重新输入")
        method_choice()
    else:
        if(method==1):
            print("请输入战斗次数:")
            cishu=input()
            zhujiemian_back()
            tansuo_takein()
            yuhun_takein()
            dashe_takein()
            ttk_huntu(cishu)


ttk_yuanlaiguang()
#zhounian_999()






