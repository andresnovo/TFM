import pandas as pd
import uproot as ur
import matplotlib.pyplot as plt
import numpy as np
#import plotter
#import vecutils as vu
import awkward as ak


if __name__ == "__main__":

    def files(path,p,m,t):
        root = '/scratch47/forAndres/tuples/simulation/2016/'
        if p==path_B0:
            f=ur.open(root + path + '/StrippingB2KpiX2MuMuDarkBosonLine.root:B2KpiX2MuMuDarkBoson/DecayTree')
            data=f.arrays(['piminus_PT','Kplus_PT','muminus_PT','muplus_PT', 'piminus_P', 'Kplus_P', 'muminus_P', 'muplus_P'], cut = ['muplus_TRUEID' == -13, 'muminus_TRUEID' == +13], library='pd')
        else:
            f=ur.open(root + path + '/StrippingB2KX2MuMuDarkBosonLine.root:B2KX2MuMuDarkBoson/DecayTree')
            data=f.arrays(['Kplus_PT','muminus_PT','muplus_PT', 'Kplus_P', 'muminus_P', 'muplus_P'], cut = ['muplus_TRUEID' == -13, 'muminus_TRUEID' == +13], library='pd')
        return data

       
    
    path_B0=['11114066','11114074','11114077']; path_Bplus=['12113086','12113095','12113098']
    m=[2000,250,4000]
    t=[100,100,100]
    
    for i,j in enumerate(path_B0):
        df=files(j,path_B0,m[i],t[i])

        plt.figure()
        plt.suptitle('Comparativa dos momentos transversais das partículas do decaemento\n $B^{0} \longrightarrow (K^{*0}_{(892)} \longrightarrow K^{+}~\pi^{-}) (H^{0} \longrightarrow \mu^{+}~\mu^{-}) \quad m=%d~MeV \quad t=%d~ps$' %(m[i],t[i]))
        ax1=plt.subplot(1,2,1)
        ax1.hist(df['piminus_PT'], bins=50, color='blue', alpha=.7, label='$\pi^{-}_{PT}$')
        ax1.hist(df['Kplus_PT'], bins=50, color='red', alpha=.7, label='$K^{+}_{PT}$')
        ax1.legend(loc='best')
        ax1.set_xlabel('$Energy~(MeV)$')
        ax1.set_ylabel('$P_{T}~(MeV)$')
        ax1.minorticks_on()
        ax2=plt.subplot(1,2,2)
        ax2.hist(df['muplus_PT'], bins=50, color='blue', alpha=.7, label='$\mu^{+}_{PT}$')
        ax2.hist(df['muminus_PT'], bins=50, color='red', alpha=.7, label='$\mu^{-}_{PT}$')
        ax2.legend(loc='best')
        ax2.set_xlabel('$Energy~(MeV)$')
        ax2.set_ylabel('$P_{T}~(MeV)$')
        ax2.minorticks_on()
        plt.subplots_adjust(wspace=.5)
        plt.savefig('/home3/andres.novo/TFM/first/PT_plots/hist_PT_'+ j +'_cut.png')

        df.eval('pseudorapidity_1 = arccosh(piminus_P / piminus_PT)', inplace = True)
        df.eval('pseudorapidity_2 = arccosh(Kplus_P / Kplus_PT)', inplace = True)
        df.eval('pseudorapidity_3 = arccosh(muplus_P / muplus_PT)', inplace = True)
        df.eval('pseudorapidity_4 = arccosh(muminus_P / muminus_PT)', inplace = True)

        plt.figure()
        plt.suptitle('Comparativa dos momentos transversais das partículas do decaemento\n $B^{0} \longrightarrow (K^{*0}_{(892)} \longrightarrow K^{+}~\pi^{-}) (H^{0} \longrightarrow \mu^{+}~\mu^{-}) \quad m=%d~MeV \quad t=%d~ps$' %(m[i],t[i]))
        ax1=plt.subplot(1,2,1)
        ax1.hist(df['pseudorapidity_1'], bins=50, color='blue', alpha=.6, label='$\pi^{-}_{PT}$')
        ax1.hist(df['pseudorapidity_2'], bins=50, color='red', alpha=.6, label='$K^{+}_{PT}$')
        ax1.legend(loc='best')
        ax1.set_xlabel('$Energy~(MeV)$')
        ax1.set_ylabel('$Pseudorapidity$')
        ax1.minorticks_on()
        ax2=plt.subplot(1,2,2)
        ax2.hist(df['pseudorapidity_3'], bins=50, color='blue', alpha=.6, label='$\mu^{+}_{PT}$')
        ax2.hist(df['pseudorapidity_4'], bins=50, color='red', alpha=.6, label='$\mu^{-}_{PT}$')
        ax2.legend(loc='best')
        ax2.set_xlabel('$Energy~(MeV)$')
        ax2.set_ylabel('$Pseudorapidity$')
        ax2.minorticks_on()
        plt.subplots_adjust(wspace=.5)
        plt.savefig('/home3/andres.novo/TFM/first/PT_plots/hist_pseudor_'+ j +'_cut.png')

for i,j in enumerate(path_Bplus):
        df=files(j,path_Bplus,m[i],t[i])

        plt.figure()
        plt.suptitle('Comparativa dos momentos transversais das partículas do decaemento\n$B^{+}~\longrightarrow~K^{+}~(H^{0}~\longrightarrow~\mu^{+}~ \mu{-}) \quad m=%d~MeV \quad t=%d~ps$' %(m[i],t[i]))
        ax1=plt.subplot(1,2,1)
        ax1.hist(df['Kplus_PT'], bins=50, color='blue', alpha=.7, label='$K^{+}_{PT}$')
        ax1.legend(loc='best')
        ax1.set_xlabel('$Energy~(MeV)$')
        ax1.set_ylabel('$P_{T}~(MeV)$')
        ax1.minorticks_on()
        ax2=plt.subplot(1,2,2)
        ax2.hist(df['muplus_PT'], bins=50, color='blue', alpha=.7, label='$\mu^{+}_{PT}$')
        ax2.hist(df['muminus_PT'], bins=50, color='red', alpha=.7, label='$\mu^{-}_{PT}$')
        ax2.legend(loc='best')
        ax2.set_xlabel('$Energy~(MeV)$')
        ax2.set_ylabel('$P_{T}~(MeV)$')
        ax2.minorticks_on()
        plt.subplots_adjust(wspace=.5)
        plt.savefig('/home3/andres.novo/TFM/first/PT_plots/hist_PT_'+ j +'_cut.png')

        df.eval('pseudorapidity_1 = arccosh(Kplus_P / Kplus_PT)', inplace = True)
        df.eval('pseudorapidity_2 = arccosh(muplus_P / muplus_PT)', inplace = True)
        df.eval('pseudorapidity_3 = arccosh(muminus_P / muminus_PT)', inplace = True)

        plt.figure()
        plt.suptitle('Comparativa dos momentos transversais das partículas do decaemento\n$B^{+}~\longrightarrow~K^{+}~(H^{0}~\longrightarrow~\mu^{+}~ \mu{-}) \quad m=%d~MeV \quad t=%d~ps$' %(m[i],t[i]))
        ax1=plt.subplot(1,2,1)
        ax1.hist(df['pseudorapidity_1'], bins=50, color='blue', alpha=.6, label='$K^{+}_{PT}$')
        ax1.legend(loc='best')
        ax1.set_xlabel('$Energy~(MeV)$')
        ax1.set_ylabel('$Pseudorapidity$')
        ax1.minorticks_on()
        ax2=plt.subplot(1,2,2)
        ax2.hist(df['pseudorapidity_2'], bins=50, color='blue', alpha=.6, label='$\mu^{+}_{PT}$')
        ax2.hist(df['pseudorapidity_3'], bins=50, color='red', alpha=.6, label='$\mu^{-}_{PT}$')
        ax2.legend(loc='best')
        ax2.set_xlabel('$Energy~(MeV)$')
        ax2.set_ylabel('$Pseudorapidity$')
        ax2.minorticks_on()
        plt.subplots_adjust(wspace=.5)
        plt.savefig('/home3/andres.novo/TFM/first/PT_plots/hist_pseudor_'+ j +'_cut.png')

    