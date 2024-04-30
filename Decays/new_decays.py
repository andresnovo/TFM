from phasespace import GenParticle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

B_momenta = pd.read_csv('B_P.csv')
B_momentum = np.array([B_momenta['B_PX'], B_momenta['B_PY'], B_momenta['B_PZ'], B_momenta['B_PE']]).T

photon_1 = GenParticle('gamma_1', 0)
photon_2 = GenParticle('gamma_2', 0)
pion_plus = GenParticle('pi+', 139.57039)
pion_minus = GenParticle('pi-', 139.57039)
pion_0 = GenParticle('pi0', 134.9768).set_children(photon_1, photon_2)
eta_1 = GenParticle('eta', 547.862).set_children(photon_1, photon_2)
eta_2 = GenParticle('eta', 547.862).set_children(pion_plus, pion_minus, pion_0)
omega = GenParticle('omega', 782.66).set_children(pion_plus, pion_minus, pion_0)
eta_prime_1 = GenParticle('eta_p', 957.78).set_children(photon_1, photon_2)
eta_prime_2 = GenParticle('eta_p', 957.78).set_children(pion_plus, pion_minus, pion_0)
eta_prime_3 = GenParticle('eta_p', 957.78).set_children(pion_plus, pion_minus, eta_1)
J = GenParticle('J/psi(1S)', 3096.900).set_children(pion_plus, pion_minus, pion_0)
K_plus = GenParticle('K+', 493.677)
K0 = GenParticle('K0', 497.611)
K_star = GenParticle('K*', 895.55)
ALP_1 = GenParticle('X', 1000).set_children(pion_plus, pion_minus, eta_1)
ALP_2 = GenParticle('X', 3000).set_children(pion_plus, pion_minus, eta_1)

#######################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K_star, eta_prime_3)
res = ['gamma_1', 'gamma_2', 'gamma_1', 'gamma_2']
weights, particles = B0.generate(n_events = int(len(B_momentum)), boost_to = B_momentum)

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* + (\eta^{\prime} \longrightarrow \pi^+ + \pi^- + (\eta \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    if i in [0, 1]:
        plt.subplot(2, int(np.ceil(len(res)/2)), i + 1)
        momentum = np.sqrt(particles[j][:, 0]**2 + particles[j][:, 1]**2 + particles[j][:, 2]**2)
        plt.title(j)
        plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
        plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
        plt.xticks(rotation=90)
        plt.minorticks_on()
    else:
        plt.subplot(2, int(np.ceil(len(res)/2)), i + 1)
        momentum_T = np.sqrt(particles[j][:, 0]**2 + particles[j][:, 1]**2)
        plt.title(j)
        plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
        plt.xticks(rotation=90)
        plt.xlabel('$p_T~(MeV)$'); plt.ylabel('Probability')
        plt.minorticks_on()        

plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_etap_P&PT.pdf')

#######################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K_star, ALP_1)
res = ['gamma_1', 'gamma_2', 'gamma_1', 'gamma_2']
weights, particles = B0.generate(n_events = int(len(B_momentum)), boost_to = B_momentum)

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* + (X(1000) \longrightarrow \pi^+ + \pi^- + (\eta \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    if i in [0, 1]:
        plt.subplot(2, int(np.ceil(len(res)/2)), i + 1)
        momentum = np.sqrt(particles[j][:, 0]**2 + particles[j][:, 1]**2 + particles[j][:, 2]**2)
        plt.title(j)
        plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
        plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
        plt.xticks(rotation=90)
        plt.minorticks_on()
    else:
        plt.subplot(2, int(np.ceil(len(res)/2)), i + 1)
        momentum_T = np.sqrt(particles[j][:, 0]**2 + particles[j][:, 1]**2)
        plt.title(j)
        plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
        plt.xticks(rotation=90)
        plt.xlabel('$p_T~(MeV)$'); plt.ylabel('Probability')
        plt.minorticks_on()        

plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_ALP1000_P&PT.pdf')

#######################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K_star, ALP_2)
res = ['gamma_1', 'gamma_2', 'gamma_1', 'gamma_2']
weights, particles = B0.generate(n_events = int(len(B_momentum)), boost_to = B_momentum)

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* + (X(3000) \longrightarrow \pi^+ + \pi^- + (\eta \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    if i in [0, 1]:
        plt.subplot(2, int(np.ceil(len(res)/2)), i + 1)
        momentum = np.sqrt(particles[j][:, 0]**2 + particles[j][:, 1]**2 + particles[j][:, 2]**2)
        plt.title(j)
        plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
        plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
        plt.xticks(rotation=90)
        plt.minorticks_on()
    else:
        plt.subplot(2, int(np.ceil(len(res)/2)), i + 1)
        momentum_T = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2)
        plt.title(j)
        plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
        plt.xticks(rotation=90)
        plt.xlabel('$p_T~(MeV)$'); plt.ylabel('Probability')
        plt.minorticks_on()        

plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_ALP3000_P&PT.pdf')

#######################################################################################################################

B0_1 = GenParticle('B0', 5279.66).set_children(K_star, eta_prime_3)
B0_2 = GenParticle('B0', 5279.66).set_children(K_star, ALP_1)
B0_3 = GenParticle('B0', 5279.66).set_children(K_star, ALP_2)
res = ['gamma_1', 'gamma_2', 'gamma_1', 'gamma_2']
_, particles_1 = B0_1.generate(n_events = int(len(B_momentum)), boost_to = B_momentum)
_, particles_2 = B0_2.generate(n_events = int(len(B_momentum)), boost_to = B_momentum)
_, particles_3 = B0_3.generate(n_events = int(len(B_momentum)), boost_to = B_momentum)

plt.figure(figsize = (12, 8))
plt.suptitle('Comparativa de momentos')
for i, j in enumerate(res):
    if i in [0, 1]:
        plt.subplot(2, int(np.ceil(len(res)/2)), i + 1)
        momentum_1 = np.sqrt(particles_1[j][:, 0]**2 + particles_1[j][:, 1]**2 + particles_1[j][:, 2]**2)
        momentum_2 = np.sqrt(particles_2[j][:, 0]**2 + particles_2[j][:, 1]**2 + particles_2[j][:, 2]**2)
        momentum_3 = np.sqrt(particles_3[j][:, 0]**2 + particles_3[j][:, 1]**2 + particles_3[j][:, 2]**2)
        plt.title(j)
        plt.hist(momentum_3, bins = 50, color = 'blue', alpha = .3, density = True, label = '$X(3000)$')
        plt.hist(momentum_1, bins = 50, color = 'red', alpha = .3, density = True, label = '$\eta^{\prime}$')
        plt.hist(momentum_2, bins = 50, color = 'green', alpha = .3, density = True, label = '$X(1000)$')
        plt.legend()
        plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
        plt.xticks(rotation=90)
        plt.xlim([0, 75000])
        plt.minorticks_on()
    else:
        plt.subplot(2, int(np.ceil(len(res)/2)), i + 1)
        momentum_1 = np.sqrt(particles_1[j][:, 0]**2 + particles_1[j][:, 0]**2)
        momentum_2 = np.sqrt(particles_2[j][:, 0]**2 + particles_2[j][:, 0]**2)
        momentum_3 = np.sqrt(particles_3[j][:, 0]**2 + particles_3[j][:, 0]**2)
        plt.title(j)
        plt.hist(momentum_3, bins = 50, color = 'blue', alpha = .3, density = True, label = '$X(3000)$')
        plt.hist(momentum_1, bins = 50, color = 'red', alpha = .3, density = True, label = '$\eta^{\prime}$')
        plt.hist(momentum_2, bins = 50, color = 'green', alpha = .3, density = True, label = '$X(1000)$')
        plt.legend()
        plt.xlabel('$p_T~(MeV)$'); plt.ylabel('Probability')
        plt.xticks(rotation=90)
        plt.xlim([0, 5500])
        plt.minorticks_on()        

plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/comparativa_P&PT.pdf')







