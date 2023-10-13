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
    df=f.arrays(['Kplus_PX','piminus_PX'],library='pd')
    df.eval('kstar_PX = Kplus_PX + piminus_PX',inplace=True)    
    plt.hist(df['kstar_PX'],bins=50)
    plt.savefig('kstar.png')
    

