import pyautogui
import time
import random
import os
import subprocess


DELAY_BETWEEN_COMMANDS = 2
STARTUP_DELAY_PROGRAM = 20

def main():
    # INIT
    pyautogui.FAILSAFE = True

    os.startfile (r'C:\Users\Joris\Desktop\PyThon\Art of War.lnk')
    #subprocess.Popen('Art of War')
    #subprocess.Popen('C:\Program Files\BlueStacks\HD-RunApp.exe')

    # countdown timer
    print("starting")
    for i in range(0, STARTUP_DELAY_PROGRAM):
        print(STARTUP_DELAY_PROGRAM-i)
        time.sleep(1)
    print("Go")

    #ReportMousePosition()

    for seq in range(0, 10):
        DoBattle()

    #DoHeadHunt()
    
    # Done
    print("Done")


def DoBattle():
    for seq in range(1, 11):
        #Select Battle
        pyautogui.click(480, 1422,duration=0.25)
        time.sleep(DELAY_BETWEEN_COMMANDS)
        print("starting attack" , seq)
        #Start Attack
        pyautogui.click(480, 1426,duration=0.25)
        time.sleep(25 + random.randint(0, 10))
        #Watch video for extra gold
        if seq == 5:
            WatchVideo()
        elif seq == 10:
            WatchVideo()
        else:
            pyautogui.click(656, 1145,duration=0.25)
            time.sleep(5+ random.randint(0, 5))
        print("finished attacking", seq)


def WatchVideo():
    pyautogui.click(331, 1171,duration=0.25)
    time.sleep(35+ random.randint(0, 5))
    #Back to the screen 
    pyautogui.hotkey('ctrl', 'shift', '2')
    time.sleep(3+ random.randint(0, 5))

def DoHeadHunt():
    #Go to Territory
    pyautogui.click(660, 1643, duration=0.25)
    print("Go to territory")
    time.sleep(DELAY_BETWEEN_COMMANDS)
    #Go to HeadHunt
    pyautogui.click(736, 961,duration=0.25)
    print("Go to HeadHunt")
    time.sleep(DELAY_BETWEEN_COMMANDS)
    #Dessert Treasure
    DesertTreasureHunt()
    #Winter is Coming
    WinterIsComing()

    #Back to the screen 
    pyautogui.hotkey('ctrl', 'shift', '2')
    time.sleep(3+ random.randint(0, 5))
    #Go to Home
    pyautogui.click(455, 1639, duration=0.25)

    print("DoHeadHunt Done")


def DesertTreasureHunt():
     for seq in range(1, 11):
            #Select Easy mode
            pyautogui.click(731, 601,duration=0.25)
            time.sleep(DELAY_BETWEEN_COMMANDS)
            #Start Attack
            pyautogui.click(473, 1426,duration=0.25)
            time.sleep(10 + random.randint(0, 5))
            #Watch video for extra gold
            if seq > 6:
                WatchVideo()
            else:
                pyautogui.click(656, 1145,duration=0.25)
                time.sleep(5+ random.randint(0, 5))
            print("easy mode", seq)

def WinterIsComing():
    for seq in range(1, 11):
            #Select Hard mode
            pyautogui.click(826, 1003,duration=0.25)
            time.sleep(DELAY_BETWEEN_COMMANDS)
            #Start Attack
            pyautogui.click(473, 1426,duration=0.25)
            time.sleep(15 + random.randint(0, 5))
            #Watch video for extra gold
            if seq > 6:
                WatchVideo()
            else:
                pyautogui.click(656, 1145,duration=0.25)
                time.sleep(5+ random.randint(0, 5))
            print("Hard mode", seq)

def ReportMousePosition(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        time.sleep(1)

if __name__ == "__main__":
    main()