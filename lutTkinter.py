import tkinter as tk
from tkinter import messagebox 
import telnetlib

def calcLut(inputFile,outputFile):

    import pandas as pd
    import numpy as np
    
    df = pd.read_csv(inputFile,delim_whitespace=True,header=0,names=['r','g','b'],skiprows=2)
    df = df.apply(lambda x: np.floor(1023 * x))
    df = df.astype('Int64')
    df.to_csv (outputFile, index = False,sep=' ' ,header=False)
    return messagebox.showwarning("Status","File converted")

def show_entry_fields():
    print(f"Input {e1.get()}, Ouput {e2.get()}")
    calcLut(e1.get(),e2.get())
       
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

def pingTel():
    HOST = "192.168.10.150 9995"
    tn = telnetlib.Telnet(HOST)
    tn.write(b"P\n\n")
    return messagebox.showwarning(print(tn.read_all().decode('ascii')))
    

master = tk.Tk()
tk.Label(master, text="Input File path").grid(row=0)
tk.Label(master, text="Output File path").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, text='Convert', command=show_entry_fields).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)


tk.Button(master, text='Ping', command=pingTel).grid(row=3, 
                                                               column=2, 
                                                               sticky=tk.W, 
                                                               pady=4)

master.mainloop()

tk.mainloop()