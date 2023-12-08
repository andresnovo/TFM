import pandas as pd
import uproot as ur
import matplotlib.pyplot as plt
import numpy as np
#import plotter
#import vecutils as vu
import awkward as ak

if __name__ == "__main__":
    root = '/scratch47/forAndres/tuples/simulation/2016/'
    path_B0 = '11114066'; path_Bplus = '12113098'
    f0 = ur.open(root + path_B0 + '/StrippingB2KpiX2MuMuDarkBosonLine.root:B2KpiX2MuMuDarkBoson/DecayTree')
    f1 = ur.open(root + path_Bplus + '/StrippingB2KX2MuMuDarkBosonLine.root:B2KX2MuMuDarkBoson/DecayTree')
    print(f1.keys())
    #print(f.arrays(['muminus_PIDp'], cut = ['muminus_TRUTHID', 'muplus_TRUEID'], library = 'pd'))
    M_B0 = f0.arrays(['B_M'], library = 'pd')
    M_Bplus = f1.arrays(['B_M'], library = 'pd')

    plt.figure()
    plt.title('Masa do mesón $B^{0}$')
    plt.hist(M_B0, bins = 300)
    plt.xlabel('$m~(MeV)$')
    plt.ylabel('Probability')
    plt.minorticks_on()
    plt.savefig('/home3/andres.novo/TFM/first/B0_M.png')

    plt.figure()
    plt.title('Masa do mesón $B^{+}$')
    plt.hist(M_Bplus, bins = 300)
    plt.xlabel('$m~(MeV)$')
    plt.ylabel('Probability')
    plt.minorticks_on()
    plt.savefig('/home3/andres.novo/TFM/first/Bplus_M.png')




