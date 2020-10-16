import tkinter as tk
import sys
from tkinter import messagebox 
import telnetlib
import time

def mainLoop():
    start = time.time()
    
    pingTel()
    
    end = time.time()
    print(end - start)

def loadFile():
        f = open("lut1.cube","r")
        return f.read()

def pingTel():
    HOST = "192.168.10.150"
    #HOST = "towel.blinkenlights.nl"
    PORT = "9995"
    
    print("start")
    telnetObj=telnetlib.Telnet(HOST,PORT,timeout=2)
  
    print("Send LUT")

    #end = "LUT 0:\nLut Kind: 3Dx33x10b\nLut Name: superAwesome"

    lutobj = f"{loadFile()}\n\n"
    lutobj = bytes(lutobj.encode())
    print(type(lutobj)) 
    telnetObj.write(lutobj)
   
    telnetObj.interact()    
    telnetObj.close()

if __name__ == "__main__":
	mainLoop()
    
