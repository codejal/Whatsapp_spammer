#WHATSAPP SPAMMER for multiple users at a time 

# author = Pranjal Gupta
# CSE,LNMIIT(2nd year)
# email : 19ucs162@lnmiit.ac.in

#firstly install pyautogui by command pip install pyautogui(windows) 
import pyautogui
import time

#------------------WORKING WITH COORDINATES (WILL WORK AFTER MODIFYING COORDINATES)------------------------
# cords=pyautogui.locateCenterOnScreen("start.png")
# print(cords)
# pyautogui.click(x=10,y=1080)
# time.sleep(1)
# pyautogui.click(x=440,y=520)
# time.sleep(15)
# pyautogui.click(x=200,y=200)
# time.sleep(1)
# pyautogui.click(x=1000,y=1000)
# x=range(100)
# for n in x:c
# pyautogui.typewrite('text here\n')


#-------------------WORKING WITH SEARCHES AND HOTKEYS-----------------------------------------------
#only for whatsapp desktop users

#OPENING WHATSAPP DESKTOP AND MAXIMISING THE WINDOW
names = [x for x in input("Enter multiple Preys: ").split()]
message=input("WHAT MESSAGE SHOULD BE SENT ? ")
repeat=int(input("HOW MANY TIMES SHOULD THE MESSEGE BE SENT ? "))
pyautogui.hotkey('Win', 's')
time.sleep(1)
pyautogui.typewrite('Whatsapp')
time.sleep(1)
pyautogui.typewrite('\n')
time.sleep(15)
pyautogui.hotkey('Win','Up')
time.sleep(1)


# pyautogui.typewrite(name)#NAME OF CONTACT
# pyautogui.typewrite('\n')
# time.sleep(2)
# pyautogui.typewrite(message)
# pyautogui.hotkey('Ctrl','a')
# pyautogui.hotkey('Ctrl','c')
# pyautogui.typewrite('\n')#MESSAGE
# for x in range(repeat):#REPITETION
#     pyautogui.hotkey('Ctrl','v')
#     pyautogui.typewrite('\n')#MESSAGE
for name in names:
    #CLICK ON COORDINATE AND SEND MESSEGE
    pyautogui.click(x=100,y=130)
    pyautogui.typewrite(name)#NAME OF CONTACT
    pyautogui.typewrite('\n')
    time.sleep(2)
    for x in range(repeat):#REPITETION
        pyautogui.typewrite(message)#MESSAGE
        pyautogui.typewrite('\n')#MESSAGE
        time.sleep(0)