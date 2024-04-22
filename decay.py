from phasespace import GenParticle
import matplotlib.pyplot as plt
import numpy as np

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

##########################################################################################################################################

B_plus = GenParticle('B+', 5279.34).set_children(K_plus, J)
res = ['K+', 'J/psi(1S)', 'pi+', 'pi-', 'pi0', 'gamma_1', 'gamma_2']
weights, particles = B_plus.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^+ \longrightarrow K^+ + (J/\psi(1S) \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B+_K+_Jpsi(1S)_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^+ \longrightarrow K^+ + (J/\psi(1S) \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B+_K+_Jpsi(1S)_E.pdf')

##########################################################################################################################################

B_plus = GenParticle('B+', 5279.34).set_children(K_plus, eta_prime_3)
res = ['K+', 'eta_p', 'pi+', 'pi-', 'eta', 'gamma_1', 'gamma_2']
weights, particles = B_plus.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^+ \longrightarrow K^+ + (\eta^{\prime} \longrightarrow \pi^+ + \pi^- + (\eta \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B+_K+_etap_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^+ \longrightarrow K^+ + (\eta^{\prime} \longrightarrow \pi^+ + \pi^- + (\eta \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B+_K+_etap_E.pdf')

##########################################################################################################################################

B_plus = GenParticle('B+', 5279.34).set_children(K_plus, eta_2)
res = ['K+', 'eta', 'pi+', 'pi-', 'pi0', 'gamma_1', 'gamma_2']
weights, particles = B_plus.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^+ \longrightarrow K^+ + (\eta \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B+_K+_eta_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^+ \longrightarrow K^+ + (\eta \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B+_K+_eta_E.pdf')

##########################################################################################################################################

B_plus = GenParticle('B+', 5279.34).set_children(K_plus, omega)
res = ['K+', 'omega', 'pi+', 'pi-', 'pi0', 'gamma_1', 'gamma_2']
weights, particles = B_plus.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^+ \longrightarrow K^+ + (\omega \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B+_K+_omega_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^+ \longrightarrow K^+ + (\omega \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B+_K+_omega_E.pdf')

##########################################################################################################################################

B_plus = GenParticle('B+', 5279.34).set_children(K_plus, pion_plus, pion_minus)
res = ['K+', 'pi+', 'pi-']
weights, particles = B_plus.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^+ \longrightarrow K^+ + \pi^+ + \pi^-$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B+_K+_pi+pi-_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^+ \longrightarrow K^+ + \pi^+ + \pi^-$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B+_K+_pi+pi-_E.pdf')

##########################################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K0, J)
res = ['K0', 'J/psi(1S)', 'pi+', 'pi-', 'pi0', 'gamma_1', 'gamma_2']
weights, particles = B0.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^0 + (J/\psi (1S) \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K0_Jpsi(1S)_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^0 + (J/\psi (1S) \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K0_Jpsi(1S)_E.pdf')

##########################################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K0, eta_2)
res = ['K0', 'eta', 'pi+', 'pi-', 'pi0', 'gamma_1', 'gamma_2']
weights, particles = B0.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^0 + (\eta \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K0_eta_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^0 + (\eta \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K0_eta_E.pdf')

##########################################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K0, omega)
res = ['K0', 'omega', 'pi+', 'pi-', 'pi0', 'gamma_1', 'gamma_2']
weights, particles = B0.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^0 + (\omega \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K0_omega_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^0 + (\omega \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K0_omega_E.pdf')

##########################################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K_star, J)
res = ['K*', 'J/psi(1S)', 'pi+', 'pi-', 'pi0', 'gamma_1', 'gamma_2']
weights, particles = B0.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* + (J/\psi (1S) \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K*_Jpsi(1S)_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* + (J/\psi (1S) \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K*_Jpsi(1S)_E.pdf')

##########################################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K_star, eta_prime_3)
res = ['K*', 'eta_p', 'pi+', 'pi-', 'eta', 'gamma_1', 'gamma_2']
weights, particles = B0.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* + (\eta^{\prime} \longrightarrow \pi^+ + \pi^- + (\eta \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K*_etap_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* + (\eta^{\prime} \longrightarrow \pi^+ + \pi^- + (\eta \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K*_etap_E.pdf')

##########################################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K_star, eta_2)
res = ['K*', 'eta', 'pi+', 'pi-', 'pi0', 'gamma_1', 'gamma_2']
weights, particles = B0.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* + (\eta \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K*_eta_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* + (\eta \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K*_eta_E.pdf')

##########################################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K_star, omega)
res = ['K*', 'omega', 'pi+', 'pi-', 'pi0', 'gamma_1', 'gamma_2']
weights, particles = B0.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* + (\omega \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K*_omega_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* + (\omega \longrightarrow \pi^+ + \pi^- + (\pi^0 \longrightarrow \gamma + \gamma))$')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K*_omega_E.pdf')

##########################################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K0, pion_plus, pion_minus)
res = ['K0', 'pi+', 'pi-']
weights, particles = B0.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^0 +  \pi^+ + \pi^- $')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K0_pi+pi-_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^0 +  \pi^+ + \pi^- $')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K0_pi+pi-_E.pdf')

##########################################################################################################################################

B0 = GenParticle('B0', 5279.66).set_children(K_star, pion_plus, pion_minus)
res = ['K*', 'pi+', 'pi-']
weights, particles = B0.generate(n_events = int(10000))

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* +  \pi^+ + \pi^- $')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    momentum = np.sqrt(particles[j][:, 1]**2 + particles[j][:, 2]**2 + particles[j][:, 3]**2)
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$p~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K*_pi+pi-_p.pdf')

plt.figure(figsize = (12, 8))
plt.suptitle('$B^0 \longrightarrow K^* +  \pi^+ + \pi^- $')
for i, j in enumerate(res):
    plt.subplot(3, int(np.ceil(len(res)/3)), i + 1)
    energy = particles[j][:, 0]
    plt.title(j)
    plt.hist(momentum, bins = 50, color = 'darkgreen', edgecolor = 'greenyellow', density = True)
    plt.xlabel('$E~(MeV)$'); plt.ylabel('Probability')
    plt.minorticks_on()
plt.subplots_adjust(hspace = .5)
plt.subplots_adjust(wspace = .5)
plt.savefig('Decays_CM/B0_K*_pi+pi-_E.pdf')





















































