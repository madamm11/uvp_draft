import pyautogui
import time
import subprocess
import cv2
import numpy as np
import os


def test_open1():
    try:

        subprocess.Popen(r'C:\\Program Files (x86)\\Analytik Jena\\VisionWorks\\VisionWorks.exe', cwd=r'C:\\Program Files (x86)\\Analytik Jena\\VisionWorks')

    except Exception as e:
        print(str(e))

def test_update_check():
    try:
        time.sleep(10)
        #click Protein Gel Electrophoresis
        pyautogui.click(247, 508)
        #click Not Now (subscription dialog)
        pyautogui.click(1026, 814)

    except Exception as e:
        print(str(e))


def test_open_demo_img():
    try:
        time.sleep(2)
        #click demo
        pyautogui.click(35, 196)
        #input file name
        pyautogui.typewrite('Colony Sample.tif\n')


    except Exception as e:
        print(str(e))


def test_apply_CC():
    try:
        #collapse actions panel
        pyautogui.click(1890, 560)
        time.sleep(2)
        #click analysis
        pyautogui.click(1850, 90)
        #click CC
        pyautogui.click(1850, 170)
        #click auto
        pyautogui.click(1650, 580)
        time.sleep(40)      #time for analysis

    except Exception as e:
        print(str(e))

def test_flatten():
    try:
        pyautogui.click(275,1005)
        pyautogui.click(1100,600)


    except Exception as e:
        print(str(e))

def test_save_flatten_analyzed():

    try:
        #click Save As
        time.sleep(5)
        pyautogui.click(113,272)
        time.sleep(1)
        #input file name
        pyautogui.typewrite('C:\\Users\\madamie\\PycharmProjects\\Draft\\Colony Sample_a.jpg\n')
        #click confirmation button for jpg saving
        time.sleep(2)
        pyautogui.click(1190,730)

    except Exception as e:
        print(str(e))

def test_image_comparison():
    try:
        time.sleep(5)
        image1 = cv2.imread("C:\\Users\\madamie\\PycharmProjects\\Draft\\Colony Sample_4test.jpg")
        image2 = cv2.imread("C:\\Users\\madamie\\PycharmProjects\\Draft\\Colony Sample_a.jpg")

        difference = cv2.subtract(image1, image2)

        result = not np.any(difference)  #true if there are no differences

        if result is True:
            print("ANALYSIS SUCCESSFUL")
        else:
            if os.path.exists("C:\\Users\\madamie\\PycharmProjects\\Draft\\result.jpg"):
                os.remove("C:\\Users\\madamie\\PycharmProjects\\Draft\\result.jpg")
            cv2.imwrite("result.jpg", difference)
            print("THE ANALYSIS CHANGED")



    except Exception as e:
        print(str(e))

def test_clean_files():
    try:
        os.remove('C:\\Users\\madamie\\PycharmProjects\\Draft\\Colony Sample_a.jpg')
        print('file removed')


    except Exception as e:
        print(str(e))

def test_close():
    try:
        os.system('TASKKILL /F /IM VisionWorks.exe')

    except Exception as e:
        print(str(e))


