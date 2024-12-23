import time
# 模拟输入字符串
import pyautogui
from PIL import Image, ImageChops
import pyautogui
import numpy as np
from pynput.keyboard import Key, Controller

import cv2

def response_xb():
    keyboard = Controller()
    pyautogui.moveTo(415,820) 
    pyautogui.click() 
    time.sleep(0.3)
    keyboard.type("@") 
    # pyautogui.moveTo(574,666) #540，708
    pyautogui.moveTo(574,666) #540，708
    pyautogui.scroll(-8000
                     )
    time.sleep(1)
    pyautogui.click() 

def output(stri,t):
    keyboard = Controller()
    # response_xb()
    time.sleep(0.3)
    while(t>0):
        
  
        pyautogui.moveTo(1100,900)
        pyautogui.click() 
        time.sleep(0.3)
        keyboard.type("")
        keyboard.type(stri)
        t-=1
    time.sleep(0.3)
    pyautogui.press("enter")

import pyautogui
import pytesseract
from PIL import Image
import os
import pygetwindow as gw
# 设置Tesseract的路径，如果你已经将其添加到系统路径中，可以不需要设置
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def screenshot_and_ocr(x=400, y=500, width=1500, height=300 ,save_path='C:\\Users\\af\\Desktop\\OCR\\screenshot.png', ):
    # 截图
    
    
    # 截图指定区域
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    # 保存截图到指定路径
    # 保存截图到当前工作目录
    screenshot.save(save_path)
    # 使用Tesseract进行文字识别，指定中文简体语言包
    text = pytesseract.image_to_string(Image.open(save_path), lang='chi_sim')
    return text

from zhipuai import ZhipuAI

conversation_history = []

def query_large_model(text, history):
    try:
        # 初始化ZhipuAI客户端
        client = ZhipuAI(api_key="187d5d14120f1e6522bd2aba6d0b395d.sc1XZaysPXyHSq4y")
        
        # 构建请求消息，包括历史消息
        messages = [
            {"role": "system", "content": "你是一个乐于解答各种问题的助手。"}
        ]
        messages.extend(history)  # 添加历史消息
        messages.append({"role": "user", "content": text})  # 添加当前用户输入
        
        # 同步调用大模型API
        response = client.chat.completions.create(
            model="glm-4-flash",  # 填写需要调用的模型名称
            messages=messages,
            stream=False,
        )
        
        # 获取模型的回复并更新历史
        reply = response.choices[0].message.content
        conversation_history.append({"role": "user", "content": text})
        conversation_history.append({"role": "assistant", "content": reply})
        
        # 返回模型的回复
        return reply
    except Exception as e:
        # 如果发生错误，返回错误信息
        return f"出错了：{str(e)}"


# 使用函数

# text = "哈哈"  # 这里是你想要查询的文本


# sk-wExgY92cMC8UTyXPrj1wlkti1C6zZtXfu2LXJmqyQRrS756m
# 调用函数，保存到当前工作目录
# time.sleep(1)


import matplotlib.pyplot as plt
def find_pure_white_contour():
    # 截取屏幕的特定区域
    x, y, width, height = 400, 300, 1500, 500  # 请根据实际情况修改这些值
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    frame = np.array(screenshot)
    
    # 转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 定义纯白色的RGB值
    pure_white = np.array([255, 255, 255], dtype=np.uint8)
    
    # 创建一个掩码，其中接近纯白色的像素为255，其他为0
    lower_white = np.array([255, 255, 255])
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(frame, lower_white, upper_white)
    
    # 形态学操作，填补空洞
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)
    mask = cv2.erode(mask, kernel, iterations=1)
    
    # 寻找掩码中的轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 在原始图像上绘制轮廓
    轮廓图像 = frame.copy()
    cv2.drawContours(轮廓图像, contours, -1, (0, 255, 0), 2)  # 使用绿色绘制轮廓

    # 显示绘制轮廓的图像
    # plt.imshow(cv2.cvtColor(轮廓图像, cv2.COLOR_BGR2RGB))
    # plt.title("Contours on Original Screenshot")
    # plt.axis('off')
    # plt.show()
    
    # 遍历轮廓，找到具有纯白外延的轮廓
    for contour in contours:
        # 计算轮廓的边界框
        x1, y1, w1, h1 = cv2.boundingRect(contour)
        area = w1 * h1  # 计算面积
        
        # 打印轮廓的边界框坐标和面积
        print(f"Contour with bounding box: ({x1}, {y1}, {x1+w1}, {y1+h1}) and area: {area} pixels")
        if  area > 800:
            return x1+x, y1+y, w1, h1
    
    return None



def check_for_changes(new_coords, old_coords):
    # 检查新坐标与旧坐标是否有变化
    return new_coords != old_coords
# 调用函数
old_coords=(0,0,0,0)
import re
def main():
    while True:
        time.sleep(1)  # 每秒检查一次
        coords = (0,0,0,0)
        old_coords = coords  # 初始化旧坐标为当前坐标
        coords = find_pure_white_contour()  # 假设这是你之前定义的函数
        if coords:
            print(f"白色对话框坐标: {coords}")
            if check_for_changes(coords, old_coords):
                # 如果坐标有变化，执行识别和查询
                print("开始识别")
                
                recognized_text = screenshot_and_ocr(coords[0], coords[1], coords[2], coords[3])
                
                if(recognized_text):    
                    print("识别结果：")
                    print(recognized_text)
                    if True:
                    # if '@e' in recognized_text:
                        print("找到 '@e'，继续执行操作。")
                        output("afbot:  ",1)
                        recognized_text = recognized_text.replace('@e', '')  # 去除text中所有的'@'符号
                        recognized_text = recognized_text.replace('@', '')  # 去除text中所有的'@'符号
                        # recognized_text = re.sub(r'[a-zA-Z]', '*', recognized_text)
                        result = query_large_model(recognized_text,conversation_history )
                        output(result, 1)
                        old_coords = coords  # 更新旧坐标为当前坐标
                else:
                    # output("识别失败", 1)
                    continue
            else:
                print("坐标未变化，等待...")
        else:
            print("未检测到白色对话框")

if __name__ == "__main__":
    main()
    # time.sleep(2)
    # response_xb()
















































