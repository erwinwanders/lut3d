#Global imports
import time
import os
import telnetlib
import pandas as pd
import numpy as np

def loadFile(filePathName):
        f = open(filePathName,"r")
        return f.read()

def sendLut(lutInpObj:str) -> str:
    """Open telnet session and send LUT object
    Args:
        lutInpObj (str): calculated LUT object
    Returns:
        str: message if session is closed
    """
    HOST = "192.168.10.150" #TODO: refactor to dynamic input
    PORT = "9995" #TODO: refactor to dynamic input
    
    print("Send LUT")

    telnetObj=telnetlib.Telnet(HOST,PORT,timeout=2)
    #telnetObj.interact()
    telnetObj.read_until(b"END PRELUDE:")
    
    #TODO: Extract metadata from input file
    #start = "LUT DATA 0:"
    #end = "LUT 0:\nLut Kind: 3Dx33x10b\nLut Name: superAwesome\n"
    #lutobj = f"{start}\n{lutInpObj}\n\n{end}\n\n"
    
    lutobj = lutInpObj
    print(len(lutobj))
    lutobj = bytes(lutobj.encode())
    print("Start write")
    telnetObj.write(lutobj)
    print("End write")
    telnetObj.read_until(b"ACK")
    telnetObj.close()
    return "Session closed"


def mainLoop():
    print("Welcome to LUT Convert and Send")
    inputFile = '/Users/lennertprins/Desktop/testEW.cube' #Path to cube file
    
    inp = loadFile(inputFile)
    sendLut(inp)
    return print("done")

  
if __name__ == "__main__":
	mainLoop()