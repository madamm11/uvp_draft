import pyautogui
import time
import subprocess
import os


# def test_delete_settings():
#     try:
#         os.remove('C:\\ProgramData\\VisionWorks\\ApplicationSettings.dat')
#         print('settings removed')
#     except Exception as e
#         print(str(e))


def test_open1():
    try:

        subprocess.Popen(r'C:\\Program Files (x86)\\Analytik Jena\\VisionWorks\\VisionWorks.exe', cwd=r'C:\\Program Files (x86)\\Analytik Jena\\VisionWorks')

    except Exception as e:
        print(str(e))

def test_update_check():
    try:
        time.sleep(10)
        pyautogui.click(247, 508)
        pyautogui.click(588, 924)
       #checkbox: never ask again, maybe better leave it unchecked for consistency
        pyautogui.click(1026, 814)
        pyautogui.click(1184, 617)
    except Exception as e:
        print(str(e))
def test_close():
    try:
        os.system('TASKKILL /F /IM VisionWorks.exe')

    except Exception as e:
        print(str(e))



# pyautogui.doubleClick(49, 412)
# time.sleep(10)
# pyautogui.click(208, 516)
