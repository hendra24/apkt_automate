import pyautogui
import time
from threading import Thread
from pynput import keyboard
import keyboard

print("Masukan Jumlah Halaman : ")
max_page = int(input())

#configuration koordinate
origin_x, origin_y = 319,457
start_x, start_y = origin_x, origin_y
next_x, next_y = 395, 718
error_x, error_y = 713, 459
cari_x, cari_y = 265, 400

#calaculate program running time
start = time.time()

#print monitor size
mon_size = pyautogui.size()
print(f"Monitor {mon_size} ")

#counter biasa
page = 0
count = 0
    
while True and start_y < 692 :
    
    #check error connetion pop up
    pyautogui.click(error_x, error_y)
    
    pyautogui.click(start_x, start_y)
    time.sleep(0.8)
    pyautogui.press('enter')
    pyautogui.press('esc')

    start_y += 24
    print(start_x, start_y)
    time.sleep(1)
    count+=1
    
    if count == 10 :
        #check error connetion pop up
        pyautogui.click(error_x, error_y)

        count = 0
        #clean pop up 
        pyautogui.press('enter')
        pyautogui.press('esc')

        #klik next button
        pyautogui.click(next_x, next_y)
        time.sleep(0.5)
        start_x, start_y = origin_x,origin_y #back to origin
        print(page+1)
        page += 1
    
       

    if page > max_page:
        pyautogui.click(cari_x, cari_y)
        break

    try :
        if keyboard.is_pressed('q'):
            pyautogui.click(cari_x, cari_y)
            break
        else:
            pass
    finally:
        pass


durasi = time.time()-start
print(f"Job complete with duration : {durasi/60} minutes and {durasi%60} second.")

