import pyautogui
import time
import random
import os
import subprocess


DELAY_BETWEEN_COMMANDS = 2
STARTUP_DELAY_PROGRAM = 5

def main():
    # INIT
    pyautogui.FAILSAFE = True
    # Start Bluestack & Art of War
    #os.startfile (r'C:\Users\Joris\Desktop\PyThon\ArtOfWar\Art of War.lnk')

    # countdown timer
    print("starting")
    for i in range(0, STARTUP_DELAY_PROGRAM):
        print(STARTUP_DELAY_PROGRAM-i)
        time.sleep(1)
    print("Go")

    #ReportMousePosition()

    #DoBattle(AmmountOfAtacks=5)

    DoHeadHunt()
    DoHeadHunt()
    #DoHeadHunt()
    #DoBattle()

    #for seq in range(0, 10):
    #    DoBattle()

    #DoHeadHunt()
    
    # Done
    print("Done")


def DoBattle(AmmountOfAtacks=10):
    for seq in range(1, AmmountOfAtacks + 1 ):
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
            print("Start easy mode", seq )
            pyautogui.click(731, 601,duration=0.25)
            time.sleep(DELAY_BETWEEN_COMMANDS)
            #Start Attack
            pyautogui.click(473, 1426,duration=0.25)
            time.sleep(10 + random.randint(0, 5))
            #Watch video for extra gold
            if seq > 4:
                WatchVideo()
            else:
                pyautogui.click(656, 1145,duration=0.25)
                time.sleep(5+ random.randint(0, 5))
            print("Finish easy mode", seq)

def WinterIsComing():
    for seq in range(1, 11):
            #Select Hard mode
            print("Start Hard mode", seq )
            pyautogui.click(826, 1003,duration=0.25)
            time.sleep(DELAY_BETWEEN_COMMANDS)
            #Start Attack
            pyautogui.click(473, 1426,duration=0.25)
            time.sleep(15 + random.randint(0, 5))
            #Watch video for extra gold
            if seq > 4:
                WatchVideo()
            else:
                pyautogui.click(656, 1145,duration=0.25)
                time.sleep(5+ random.randint(0, 5))
            print("Finish Hard mode", seq )

def ReportMousePosition(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        time.sleep(1)

if __name__ == "__main__":
    main()