import pandas as pd
import uproot as ur
import matplotlib.pyplot as plt
import numpy as np
#import plotter
#import vecutils as vu
import awkward as ak

def files(path,p,m,t):
    root = '/scratch47/forAndres/tuples/simulation/2016/'
    if p==path_B0:
        f    = ur.open(root + path + '/StrippingB2KpiX2MuMuDarkBosonLine.root:B2KpiX2MuMuDarkBoson/DecayTree')
        data = f.arrays(['piminus_PT','Kplus_PT','muminus_PT','muplus_PT', 'piminus_P', 'Kplus_P', 'muminus_P', 'muplus_P', 'piminus_TRUEID', 'Kplus_TRUEID', 'muminus_TRUEID', 'muplus_TRUEID'], library='pd')
        cuts = data.query('Kplus_TRUEID == 321' and 'piminus_TRUEID == -211' and 'muplus_TRUEID == -13' and 'muminus_TRUEID == +13')
    else:
        f    = ur.open(root + path + '/StrippingB2KX2MuMuDarkBosonLine.root:B2KX2MuMuDarkBoson/DecayTree')
        data = f.arrays(['Kplus_PT','muminus_PT','muplus_PT', 'Kplus_P', 'muminus_P', 'muplus_P', 'Kplus_TRUEID', 'muminus_TRUEID', 'muplus_TRUEID'], library='pd')
        cuts = data.query('Kplus_TRUEID == 321' and 'muplus_TRUEID == -13' and 'muminus_TRUEID == +13')
    return data, cuts
    
def plotter(path, path2, particles, particles_cut, representations, m, t):
    if path2 == path_B0:
        plt.figure(figsize = (12,7))
        plt.title('Comparativa da pseudorapidity das partículas do decaemento\n $B^{0} \longrightarrow (K^{*0}_{(892)} \longrightarrow K^{+}~\pi^{-}) (H^{0} \longrightarrow \mu^{+}~\mu^{-}) \quad m=%d~MeV \quad t=%d~ps$' %(m,t))
        plt.hist(df_data[particles], bins=50, color='darkblue', alpha=.7, label=representations)
        plt.legend(loc='best')
        plt.xlabel('$Energy~(MeV)$')
        plt.ylabel('$Pseudorapidity$')
        plt.minorticks_on()
        plt.savefig('/home3/andres.novo/TFM/first/cut_plots/hist_'+ path + '_' + particles + '.png')
        plt.close()

        plt.figure(figsize = (12,7))
        plt.title('Comparativa con "truth match cuts" da pseudorapidity das partículas do decaemento\n $B^{0} \longrightarrow (K^{*0}_{(892)} \longrightarrow K^{+}~\pi^{-}) (H^{0} \longrightarrow \mu^{+}~\mu^{-}) \quad m=%d~MeV \quad t=%d~ps$' %(m,t))
        plt.hist(df_cuts[particles_cut], bins=50, color='darkblue', alpha=.7, label=representations)
        plt.legend(loc='best')
        plt.xlabel('$Energy~(MeV)$')
        plt.ylabel('$Pseudorapidity$')
        plt.minorticks_on()
        plt.savefig('/home3/andres.novo/TFM/first/cut_plots/hist_' + path + '_' + particles_cut + '_cut.png')
        plt.close()

    else:
        plt.figure(figsize = (12,7))
        plt.title('Comparativa da pseudorapidity das partículas do decaemento\n$B^{+}~\longrightarrow~K^{+}~(H^{0}~\longrightarrow~\mu^{+}~ \mu{-}) \quad m=%d~MeV \quad t=%d~ps$' %(m,t))
        plt.hist(df_data[particles], bins=50, color='darkblue', alpha=.7, label=representations)
        plt.legend(loc='best')
        plt.xlabel('$Energy~(MeV)$')
        plt.ylabel('$Pseudorapidity$')
        plt.minorticks_on()
        plt.savefig('/home3/andres.novo/TFM/first/cut_plots/hist_' + path + '_' + particles + '.png')
        plt.close()

        plt.figure(figsize = (12,7))
        plt.title('Comparativa con "truth match cuts" da pseudorapidity das partículas do decaemento\n$B^{+}~\longrightarrow~K^{+}~(H^{0}~\longrightarrow~\mu^{+}~ \mu{-}) \quad m=%d~MeV \quad t=%d~ps$' %(m,t))
        plt.hist(df_cuts[particles_cut], bins=50, color='darkblue', alpha=.7, label=representations)
        plt.legend(loc='best')
        plt.xlabel('$Energy~(MeV)$')
        plt.ylabel('$Pseudorapidity$')
        plt.minorticks_on()
        plt.savefig('/home3/andres.novo/TFM/first/cut_plots/hist_' + path + '_' + particles_cut + '_cut.png')
        plt.close()
    return


if __name__ == "__main__":
    path_B0    = ['11114066','11114074','11114077']
    path_Bplus = ['12113086','12113095','12113098']
    m = [2000,250,4000]
    t = [100,100,100]

    for i,j in enumerate(path_B0):
        df_data, df_cuts = files(j,path_B0,m[i],t[i])

        df_data.eval('eta_piminus = arccosh(piminus_P / piminus_PT)', inplace = True)
        df_data.eval('eta_Kplus = arccosh(Kplus_P / Kplus_PT)', inplace = True)
        df_data.eval('eta_muplus = arccosh(muplus_P / muplus_PT)', inplace = True)
        df_data.eval('eta_muminus = arccosh(muminus_P / muminus_PT)', inplace = True)

        df_cuts.eval('eta_piminus_cut = arccosh(piminus_P / piminus_PT)', inplace = True)
        df_cuts.eval('eta_Kplus_cut = arccosh(Kplus_P / Kplus_PT)', inplace = True)
        df_cuts.eval('eta_muplus_cut = arccosh(muplus_P / muplus_PT)', inplace = True)
        df_cuts.eval('eta_muminus_cut = arccosh(muminus_P / muminus_PT)', inplace = True)

        particles       = ['eta_piminus', 'eta_Kplus', 'eta_muplus', 'eta_muminus']
        particles_cut   = ['eta_piminus_cut', 'eta_Kplus_cut', 'eta_muplus_cut', 'eta_muminus_cut']
        representations = ['$\eta(\pi^{-})$', '$\eta(K^{+})$', '$\eta(\mu^{+})$', '$\eta(\mu^{-})$']

        [plotter(j, path_B0, k, l, n, m[i], t[i]) for k, l, n in zip(particles, particles_cut, representations)]
    

    for i,j in enumerate(path_Bplus):
        df_data, df_cuts = files(j,path_Bplus,m[i],t[i])

        df_data.eval('eta_Kplus = arccosh(Kplus_P / Kplus_PT)', inplace = True)
        df_data.eval('eta_muplus = arccosh(muplus_P / muplus_PT)', inplace = True)
        df_data.eval('eta_muminus = arccosh(muminus_P / muminus_PT)', inplace = True)

        df_cuts.eval('eta_Kplus_cut = arccosh(Kplus_P / Kplus_PT)', inplace = True)
        df_cuts.eval('eta_muplus_cut = arccosh(muplus_P / muplus_PT)', inplace = True)
        df_cuts.eval('eta_muminus_cut = arccosh(muminus_P / muminus_PT)', inplace = True)

        particles       = ['eta_Kplus', 'eta_muplus', 'eta_muminus']
        particles_cut   = ['eta_Kplus_cut', 'eta_muplus_cut', 'eta_muminus_cut']
        representations = ['$\eta(K^{+})$', '$\eta(\mu^{+})$', '$\eta(\mu^{-})$']

        [plotter(j, path_Bplus, k, l, n, m[i], t[i]) for k, l, n in zip(particles, particles_cut, representations)]

    