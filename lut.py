import tkinter as tk
import pandas as pd
import numpy as np
import sys
from tkinter import messagebox 
import telnetlib
import time

def mainLoop():
    start = time.time()
    inputFile = '' #Path to cube file
    concLut = calcLut(inputFile)
    sendLut(concLut)
    
    end = time.time()
    print(end - start)

def calcLut(inputFile):
    df = pd.read_csv(inputFile,delim_whitespace=True,header=0,names=['r','g','b'],skiprows=2)
    df = df.apply(lambda x: np.floor(1023 * x))
    df = df.astype('Int64')
    outputFile = df.to_csv (index = False,sep=' ' ,header=False)
    return outputFile

#def loadFile():
#        f = open("lut1.cube","r")
#        return f.read()


def sendLut(lutInpObj):
    HOST = "192.168.10.150"
    PORT = "9995"
    
    telnetObj=telnetlib.Telnet(HOST,PORT,timeout=2)
  
    print("Send LUT")

    end = "LUT 0:\nLut Kind: 3Dx33x10b\nLut Name: superAwesome\n"
    
    lutobj = f"{lutInpObj}\n\n{end}\n\n"
    lutobj = bytes(lutobj.encode())
    print(type(lutobj)) 
    telnetObj.write(lutobj)
    telnetObj.read_until(b"ACK")
    telnetObj.close()

if __name__ == "__main__":
	mainLoop()
    
