import pandas as pd
import uproot as ur
import matplotlib.pyplot as plt
import numpy as np
#import plotter
#import vecutils as vu
import awkward as ak


if __name__ == "__main__":
    root = '/scratch47/forAndres/tuples/simulation/2016/'
    f=ur.open(root +'11114077/StrippingB2KpiX2MuMuDarkBosonLine.root:B2KpiX2MuMuDarkBoson/DecayTree')
    print(f.keys())
    df=f.arrays(['piminus_P','Kplus_PE','Kplus_P','piminus_PE','Kplus_M', 'piminus_M','Kplus_PX','Kplus_PY','Kplus_PZ','piminus_PX','piminus_PY','piminus_PZ'],library='pd')
    df.eval('kstar_m = (Kplus_M**2 + piminus_M**2 + 2*(Kplus_PE*piminus_PE - (Kplus_PX*piminus_PX + Kplus_PY*piminus_PY + Kplus_PZ*piminus_PZ)))**(1/2)',inplace=True)
  

    print(df['kstar_m'])
    plt.hist(df['kstar_m'],bins=50)
    plt.savefig('kstar_M.png')
    
   
    

