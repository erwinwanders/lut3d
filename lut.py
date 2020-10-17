#Global imports
import time
import os
import telnetlib
import pandas as pd
import numpy as np


def getFileDT(inputFile:str) -> float:
    """Get latest filedate and time

    Args:
        inputFile (str): input file path and name

    Returns:
        float: system datetime
    """
    try:
        mtime = os.path.getmtime(inputFile)
    except OSError:
        mtime = 0
    return mtime


def calcLut(inputFile: str) -> str:
    """Convert input LUT file to required output format

    Args:
        inputFile (str): Filepath and name to input LUT file

    Returns:
        str: calculated string object whitespace-seperated
    """
    df = pd.read_csv(inputFile,delim_whitespace=True,header=0,names=['r','g','b'],skiprows=2)
    df = df.apply(lambda x: np.floor(1023 * x))
    df = df.astype('Int64')
    outputFile = df.to_csv (index = False,sep=' ' ,header=False)
    return outputFile


def sendLut(lutInpObj:str) -> str:
    """Open telnet session and send LUT object

    Args:
        lutInpObj (str): calculated LUT object

    Returns:
        str: message if session is closed
    """
    HOST = "192.168.10.150" #TODO: refactor to dynamic input
    PORT = "9995" #TODO: refactor to dynamic input
    
    telnetObj=telnetlib.Telnet(HOST,PORT,timeout=2)
  
    print("Send LUT")

    #TODO: Extract metadata from input file
    end = "LUT 0:\nLut Kind: 3Dx33x10b\nLut Name: superAwesome\n"
    
    lutobj = f"{lutInpObj}\n\n{end}\n\n"
    lutobj = bytes(lutobj.encode())
    print(type(lutobj)) 
    telnetObj.write(lutobj)
    telnetObj.read_until(b"ACK")
    telnetObj.close()
    return "Session closed"


def mainLoop():
    
    inputFile = '' #Path to cube file
    
    baseFileDT = getFileDT(inputFile)
    
    while(not time.sleep(5)):
        checkFileDT = getFileDT(inputFile)
        if checkFileDT > baseFileDT:
            start = time.time()
            print("New File Found")
            concLut = calcLut(inputFile)
            sendLut(concLut)
            baseFileDT = checkFileDT
            end = time.time()
            print(f"Lut successfully loaded in {round(end - start)} seconds")
        else:
            time.sleep(2)
    
  

if __name__ == "__main__":
	mainLoop()
    
