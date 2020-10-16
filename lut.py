def calcLut() -> str:

    import pandas as pd
    import numpy as np
    
    df = pd.read_csv(r'test.cube',delim_whitespace=True,header=0,names=['r','g','b'],skiprows=2)
    df = df.apply(lambda x: np.floor(1023 * x))
    df = df.astype('Int64')
    df.to_csv (r'testEW.cube', index = False,sep=' ' ,header=False)
    return print("File converted")



if __name__ == "__main__":
     calcLut()
