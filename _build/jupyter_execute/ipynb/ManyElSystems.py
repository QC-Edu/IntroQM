#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Many-Electron-Systems" data-toc-modified-id="Many-Electron-Systems-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Many-Electron Systems</a></span><ul class="toc-item"><li><span><a href="#Two-Electrons-in-a-Box" data-toc-modified-id="Two-Electrons-in-a-Box-8.1"><span class="toc-item-num">8.1&nbsp;&nbsp;</span>Two Electrons in a Box</a></span></li><li><span><a href="#Electron-Spin-and-the-Pauli-Principle" data-toc-modified-id="Electron-Spin-and-the-Pauli-Principle-8.2"><span class="toc-item-num">8.2&nbsp;&nbsp;</span>Electron Spin and the Pauli Principle</a></span><ul class="toc-item"><li><span><a href="#Two-Electrons-(with-Spin)-in-a-Box" data-toc-modified-id="Two-Electrons-(with-Spin)-in-a-Box-8.2.1"><span class="toc-item-num">8.2.1&nbsp;&nbsp;</span>Two Electrons (with Spin) in a Box</a></span></li><li><span><a href="#📝-Exercise:-Confirm-that-the-wavefunction-we-just-defined-$\psi_{n_1,m_{s,1},n_2,m_{s,2}}(x_1,\sigma_1;x_2,\sigma_2)-$-is-normalized-and-satisfies-the-Pauli-antisymmetry-relation-and-the-Pauli-exclusion-principle." data-toc-modified-id="📝-Exercise:-Confirm-that-the-wavefunction-we-just-defined-$\psi_{n_1,m_{s,1},n_2,m_{s,2}}(x_1,\sigma_1;x_2,\sigma_2)-$-is-normalized-and-satisfies-the-Pauli-antisymmetry-relation-and-the-Pauli-exclusion-principle.-8.2.2"><span class="toc-item-num">8.2.2&nbsp;&nbsp;</span>📝 Exercise: Confirm that the wavefunction we just defined $\psi_{n_1,m_{s,1},n_2,m_{s,2}}(x_1,\sigma_1;x_2,\sigma_2) $ is normalized and satisfies the Pauli antisymmetry relation and the Pauli exclusion principle.</a></span></li><li><span><a href="#Two-Electron-Atoms" data-toc-modified-id="Two-Electron-Atoms-8.2.3"><span class="toc-item-num">8.2.3&nbsp;&nbsp;</span>Two-Electron Atoms</a></span><ul class="toc-item"><li><span><a href="#Perturbative-Treatment-of-the-2-electron-atom" data-toc-modified-id="Perturbative-Treatment-of-the-2-electron-atom-8.2.3.1"><span class="toc-item-num">8.2.3.1&nbsp;&nbsp;</span>Perturbative Treatment of the 2-electron atom</a></span></li><li><span><a href="#Variational-Treatment-of-the-2-electron-atom" data-toc-modified-id="Variational-Treatment-of-the-2-electron-atom-8.2.3.2"><span class="toc-item-num">8.2.3.2&nbsp;&nbsp;</span>Variational Treatment of the 2-electron atom</a></span></li></ul></li></ul></li><li><span><a href="#Many-electron-wavefunctions:-the-Slater-Determinant" data-toc-modified-id="Many-electron-wavefunctions:-the-Slater-Determinant-8.3"><span class="toc-item-num">8.3&nbsp;&nbsp;</span>Many-electron wavefunctions: the Slater Determinant</a></span><ul class="toc-item"><li><span><a href="#📝-Exercise:-By-explicit-evaluation,-confirm-that-the-$2-\times-2$-and-$3-\times-3$-Slater-determinants-recover-the-result-that-would-be-obtained-by-explicit-antisymmetrization." data-toc-modified-id="📝-Exercise:-By-explicit-evaluation,-confirm-that-the-$2-\times-2$-and-$3-\times-3$-Slater-determinants-recover-the-result-that-would-be-obtained-by-explicit-antisymmetrization.-8.3.1"><span class="toc-item-num">8.3.1&nbsp;&nbsp;</span>📝 Exercise: By explicit evaluation, confirm that the $2 \times 2$ and $3 \times 3$ Slater determinants recover the result that would be obtained by explicit antisymmetrization.</a></span></li><li><span><a href="#📝-Exercise:-Write-a-Slater-determinant-for-the-lowest-energy-pentuplet-state-of-the-Carbon-atom,-with-electron-configuration-$\text{1s}^2-\text{2s}^1-\text{2p}_0^1-\text{2p}_{+1}^1-\text{2p}_{-1}^1$.-Assume-all-unpaired-electrons-have-$\alpha$-spin." data-toc-modified-id="📝-Exercise:-Write-a-Slater-determinant-for-the-lowest-energy-pentuplet-state-of-the-Carbon-atom,-with-electron-configuration-$\text{1s}^2-\text{2s}^1-\text{2p}_0^1-\text{2p}_{+1}^1-\text{2p}_{-1}^1$.-Assume-all-unpaired-electrons-have-$\alpha$-spin.-8.3.2"><span class="toc-item-num">8.3.2&nbsp;&nbsp;</span>📝 Exercise: Write a Slater determinant for the lowest-energy pentuplet state of the Carbon atom, with electron configuration $\text{1s}^2 \text{2s}^1 \text{2p}_0^1 \text{2p}_{+1}^1 \text{2p}_{-1}^1$. Assume all unpaired electrons have $\alpha$ spin.</a></span></li></ul></li><li><span><a href="#Example:-Many-electrons-in-a-Box" data-toc-modified-id="Example:-Many-electrons-in-a-Box-8.4"><span class="toc-item-num">8.4&nbsp;&nbsp;</span>Example: Many electrons in a Box</a></span><ul class="toc-item"><li><span><a href="#📝-Exercise:-Write-the-Slater-determinant-for,-and-an-approximate-energy-expression-for,-the-ground-state-and-first-excited-state-of-2-electrons-in-a-2-dimensional-square-box-and-2-electrons-in-a-3-dimension-square-box.-What-changes-when-you-repeat-the-exercise-for-3-electrons?" data-toc-modified-id="📝-Exercise:-Write-the-Slater-determinant-for,-and-an-approximate-energy-expression-for,-the-ground-state-and-first-excited-state-of-2-electrons-in-a-2-dimensional-square-box-and-2-electrons-in-a-3-dimension-square-box.-What-changes-when-you-repeat-the-exercise-for-3-electrons?-8.4.1"><span class="toc-item-num">8.4.1&nbsp;&nbsp;</span>📝 Exercise: Write the Slater determinant for, and an approximate energy expression for, the ground state and first excited state of 2 electrons in a 2-dimensional square box and 2 electrons in a 3-dimension square box. What changes when you repeat the exercise for 3 electrons?</a></span></li></ul></li><li><span><a href="#Example:-Spectroscopy-of-Cyanine-Dyes" data-toc-modified-id="Example:-Spectroscopy-of-Cyanine-Dyes-8.5"><span class="toc-item-num">8.5&nbsp;&nbsp;</span>Example: Spectroscopy of Cyanine Dyes</a></span></li><li><span><a href="#Many-Electron-Atoms-and-Molecules" data-toc-modified-id="Many-Electron-Atoms-and-Molecules-8.6"><span class="toc-item-num">8.6&nbsp;&nbsp;</span>Many-Electron Atoms and Molecules</a></span></li><li><span><a href="#🪞-Self-Reflection" data-toc-modified-id="🪞-Self-Reflection-8.7"><span class="toc-item-num">8.7&nbsp;&nbsp;</span>🪞 Self-Reflection</a></span></li><li><span><a href="#🤔-Thought-Provoking-Questions" data-toc-modified-id="🤔-Thought-Provoking-Questions-8.8"><span class="toc-item-num">8.8&nbsp;&nbsp;</span>🤔 Thought-Provoking Questions</a></span></li><li><span><a href="#🔁-Recapitulation" data-toc-modified-id="🔁-Recapitulation-8.9"><span class="toc-item-num">8.9&nbsp;&nbsp;</span>🔁 Recapitulation</a></span></li><li><span><a href="#🔮-Next-Up..." data-toc-modified-id="🔮-Next-Up...-8.10"><span class="toc-item-num">8.10&nbsp;&nbsp;</span>🔮 Next Up...</a></span></li><li><span><a href="#📚-References" data-toc-modified-id="📚-References-8.11"><span class="toc-item-num">8.11&nbsp;&nbsp;</span>📚 References</a></span></li></ul></li></ul></div>

# ![Remdesivir](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/Remdesivir.png?raw=true "Molecular structure showing the electrostatic potential of Remdesivir, as evaluated using the GAMESS quantum chemistry program. Licensed as CC BY 2.0 by ChiralJon")

# # Many-Electron Systems
# In general, the Schr&ouml;dinger equation for many-electron systems cannot be solved exactly. For atoms and molecules, even accurate approximations are difficult, and finding more accurate ways to solve many-electron systems, at low enough computational cost to allow interesting and important molecules and their chemical phenomena to be modeled, is an extremely active area of scientific research.

# ## Two Electrons in a Box
# Arguably the simplest possible two-electron system is two electrons confined to a one-dimensional box of length $a$. The Hamiltonian contains terms for the kinetic energy of the two electrons, the potential that binds each electron, and the electron-electron repulsion between the electrons
# 
# $$
# \hat{H}_{\text{2 el. in 1 dim.}} = -\frac{\hbar^2}{2m}\frac{d^2}{dx_1^2} -\frac{\hbar^2}{2m}\frac{d^2}{dx_2^2} + V(x_1) + V(x_2) + \frac{e^2}{4 \pi \epsilon_0 |x_1 - x_2|}
# $$
# 
# where, as before,
# 
# $$
# V(x) = 
# \begin{cases}
#     +\infty & x\leq 0\\
#     0       & 0\lt x \lt a\\
#     +\infty & a \leq x
# \end{cases}
# $$
# 
# In atomic units, this is
# 
# $$
# \hat{H}_{\text{2 el. in 1 dim.}} = -\frac{1}{2}\frac{d^2}{dx_1^2} -\frac{1}{2}\frac{d^2}{dx_2^2} + V(x_1) + V(x_2) + \frac{1}{|x_1 - x_2|}
# $$
# 
# and the Schr&ouml;dinger equation is:
# 
# $$
# \hat{H}_{\text{2 el. in 1 dim.}} \psi_k(x_1,x_2) = E_k \psi_k(x_1,x_2)
# $$
# 
# To solve this equation, we need to make approximations. Note that the problem would be easy if the electron-electron repulsion were negligible. Were that the case, the Hamiltonian would be merely the sum of two particle-in-a-box Hamiltonians, one for each electron,
# 
# $$
# \hat{H}_{\text{2 noninteracting el. in 1 dim.}} = -\frac{1}{2}\frac{d^2}{dx_1^2} -\frac{1}{2}\frac{d^2}{dx_2^2} + V(x_1) + V(x_2) = \hat{H}_{\text{p-in-box}}(x_1) + \hat{H}_{\text{p-in-box}}(x_2) 
# $$
# 
# The Schr&ouml;dinger equation could then be solved by separation of variables, with the eigenfunctions and energies being:
# 
# $$
# \psi_{n_1,n_2}(x_1,x_2) = \psi_{n_1}(x_1)\psi_{n_2}(x_2) = \tfrac{2}{a} \sin\left(\tfrac{n_1 \pi x_1}{a} \right)\sin\left(\tfrac{n_2 \pi x_2}{a} \right)
# $$
# 
# $$
# E_{n_1,n_2} = E_{n_1}+E_{n_2} = \frac{h^2(n_1^2 + n_2^2)}{8ma^2}
# $$
# 
# This wavefunction is not quite right, however. Electrons are identical particles, so it is not allowable to label electron 1 with quantum number $n_1$ and electron 2 with quantum number $n_2$. Solving this problem, however, requires a consideration of electron spin.

# ## Electron Spin and the Pauli Principle
# Consider a wavefunction for $N$ identical particles, $\Psi(\mathbf{r}_1, \mathbf{r}_2, \ldots, \mathbf{r}_N)$. We know that the particles are identical, so all observables cannot depend on the specific order in which the particle coordinates are listed. In particular, the probability of observing particles at specified positions cannot depend on *which* particle is at the specified positions. Ergo,
# 
# $$
# \left|\Psi(\mathbf{r}_1, \ldots, \mathbf{r}_j, \ldots, \mathbf{r}_k, \ldots, \mathbf{r}_N) \right|^2 
# =\left|\Psi(\mathbf{r}_1, \ldots, \mathbf{r}_k, \ldots, \mathbf{r}_j, \ldots, \mathbf{r}_N) \right|^2 
# $$
# 
# This means that for any real number $\eta$, 
# 
# $$
# \Psi(\mathbf{r}_1, \ldots, \mathbf{r}_j, \ldots, \mathbf{r}_k, \ldots, \mathbf{r}_N) 
# =e^{\pi i \eta} \Psi(\mathbf{r}_1, \ldots, \mathbf{r}_k, \ldots, \mathbf{r}_j, \ldots, \mathbf{r}_N) 
# $$
# 
# where $1^{1/2}=e^{\pi i \eta}$ denotes the [square root of unity](https://en.wikipedia.org/wiki/Root_of_unity). A [deep result](https://en.wikipedia.org/wiki/Spin%E2%80%93statistics_theorem) that can be derived from relativistic quantum mechanics but which is far beyond the scope of this course, is that particles have a property called *spin*, and that for particles with half-integer spin, $\eta = 1$ and the wavefunction is antisymmetric with respect to exchange of particles' spatial and spin coordinates, 
# 
# $$
# \Psi(\mathbf{r}_1, \sigma_1; \ldots; \mathbf{r}_j, \sigma_j; \ldots; \mathbf{r}_k, \sigma_k; \ldots; \mathbf{r}_N, \sigma_N) 
# =-1 \cdot \Psi(\mathbf{r}_1, \sigma_1; \ldots; \mathbf{r}_k, \sigma_k; \ldots; \mathbf{r}_j, \sigma_j; \ldots; \mathbf{r}_N, \sigma_N)
# $$
# 
# This equation is sometimes called the Pauli antisymmetry relation. Particles with half-integer spin are called [fermions](https://en.wikipedia.org/wiki/Fermion). Electrons, protons, and neutrons are fermions. 
# 
# Particles with integer spin are called [bosons](https://en.wikipedia.org/wiki/Boson). Photons are bosons. For bosons, the wavefunction is symmetric with respect to exchange of particles' positions and spin ($\eta = 0$),
# 
# $$
# \Psi(\mathbf{r}_1, \sigma_1; \ldots; \mathbf{r}_j, \sigma_j; \ldots; \mathbf{r}_k, \sigma_k; \ldots; \mathbf{r}_N, \sigma_N) 
# =+1 \cdot \Psi(\mathbf{r}_1, \sigma_1; \ldots; \mathbf{r}_k, \sigma_k; \ldots; \mathbf{r}_j, \sigma_j; \ldots; \mathbf{r}_N, \sigma_N)
# $$
# 
# Other values of $\eta$ do not occur for elementary particles, but can appear in some types of exotic physical phenomena. When $\eta \ne \{0,1 \}$, the particle is called an [anyon](https://en.wikipedia.org/wiki/Anyon).
# 
# The [Pauli exclusion principle](https://en.wikipedia.org/wiki/Pauli_exclusion_principle) states that fermions with the same spin can never be at the same location in space; it is a consequence of the Pauli antisymmetry relation. Suppose that $(\mathbf{r}_j,\sigma_j) = (\mathbf{r}_k,\sigma_k)$. Substituting this into the Pauli antisymmetry relation, we have that a wavefunction is equal to its negative,
# 
# $$
# \Psi(\mathbf{r}_1, \sigma_1; \ldots; \mathbf{r}_k, \sigma_k; \ldots; \mathbf{r}_k, \sigma_k; \ldots; \mathbf{r}_N, \sigma_N) 
# =-1 \cdot \Psi(\mathbf{r}_1, \sigma_1; \ldots; \mathbf{r}_k, \sigma_k; \ldots; \mathbf{r}_k, \sigma_k; \ldots; \mathbf{r}_N, \sigma_N)=0
# $$
# 
# The only number that is equal to its negative is zero, which indicates that the wavefunction (and ergo the wavefunction squared) is zero when two fermions with the same spin are at the same location. 
# 
# Electrons are fermions, and they have total spin of $\tfrac{1}{2}$. Recall the angular momentum operators and eigenfunctions we learned about with spherical systems. The spherical harmonics were eigenvalues of the total angular momentum squared and the angular momentum about a specified axis (usually chosen to be the $z$ axis), 
# 
# $$
# \begin{align}
# \hat{L}^2 Y_l^{m_l}(\theta,\phi) &= \hbar^2 l(l+1)  Y_l^{m_l}(\theta,\phi) \qquad \qquad l=0,1,2,\ldots \\
# \hat{L}_z Y_l^{m_l}(\theta,\phi) &= \hbar m_l  Y_l^{m_l}(\theta,\phi) \qquad \qquad \qquad m_l=0,\pm 1, \pm 2,\ldots, \pm l 
# \end{align}
# $$
# 
# Spin is also a type of angular momentum, and is governed by the same precepts. With some abuse of notation, we can denote spin eigenfunctions as if they were spherical harmonics,
# 
# $$
# \begin{align}
# \hat{S}^2 Y_s^{m_s} &= \hbar^2 s(s+1)  Y_s^{m_s} \qquad \qquad s \in \left\{0,\tfrac{1}{2},1,\tfrac{3}{2},2,\ldots \right\} \\
# \hat{S}_z Y_s^{m_s} &= \hbar m_s  Y_s^{m_s} \qquad \qquad \qquad m_l=\pm s, \pm (s-1), \ldots 
# \end{align}
# $$
# 
# For electrons, protons, and neutrons, the total spin quantum number is $s=\tfrac{1}{2}$, and the magnetic spin quantum number for the $z$ axis is $m_s \in \left\{-\tfrac{1}{2}, \tfrac{1}{2}\right\}$. For convenience, electrons with $m_s = \tfrac{1}{2}$ are usually said to be "up spin" or $\alpha$ spin electrons; electrons with $m_s = -\tfrac{1}{2}$ are usually said to be "down spin" or $\beta$ spin electrons. So: 
# 
# $$
# \begin{align}
# \hat{S}^2 |\alpha\rangle &= \tfrac{3}{4}\hbar^2   |\alpha\rangle \\
# \hat{S}^2 |\beta\rangle &= \tfrac{3}{4}\hbar^2   |\beta\rangle \\
# \hat{S}_z |\alpha\rangle &= \tfrac{1}{2}\hbar   |\alpha\rangle \\
# \hat{S}_z |\beta\rangle &= \tfrac{-1}{2}\hbar   |\beta\rangle \\
# \end{align}
# $$
# 
# In cases where no specific choice of spin is made, one usually uses the generic notation $\sigma \in \left\{\alpha,\beta \right\}$

# ### Two Electrons (with Spin) in a Box
# In order to describe two-electron systems, we need to embellish the electronic positions with spin coordinates. Going back to the wavefunction of two noninteracting electrons in a box, we have:
# 
# $$
# \psi_{n_1,m_{s,1},n_2,m_{s,2}}(x_1,\sigma_1;x_2,\sigma_2) = \psi_{n_1}(x_1)\psi_{n_2}(x_2)|\sigma_1(1) \sigma_2(2) \rangle = \tfrac{2}{a} \sin\left(\tfrac{n_1 \pi x_1}{a} \right)\sin\left(\tfrac{n_2 \pi x_2}{a} \right)|\sigma_1(1) \sigma_2(2) \rangle
# $$
# 
# Note that there are now *four* quantum numbers. As before, this reflects the dimensionality of the system, because there are two principle quantum numbers (corresponding to the spatial coordinates $x_1$ and $x_2$) and two spin quantum numbers (corresponding to the spin coordinates, $\sigma_1$ and $\sigma_2$). 
# 
# While this wavefunction solves the Schr&ouml;dinger equation, it does not satisfy the Pauli antisymmetry relation because it assigns electron one to a specific spin $\sigma_1$ and principle quantum number $n_1$. To fix this problem, we can explicitly antisymmetrize the wavefunction, 
# 
# $$
# \psi_{n_1,m_{s,1},n_2,m_{s,2}}(x_1,\sigma_1;x_2,\sigma_2) = \tfrac{1}{\sqrt{2}} \left(\psi_{n_1}(x_1)\psi_{n_2}(x_2)|\sigma_1(1) \sigma_2(2) \rangle - \psi_{n_1}(x_2)\psi_{n_2}(x_1)|\sigma_1(2) \sigma_2(1) \rangle \right)
# $$
# 
# The factor of $\tfrac{1}{\sqrt{2}}$ is a normalization constant. 

# ### &#x1f4dd; Exercise: Confirm that the wavefunction we just defined $\psi_{n_1,m_{s,1},n_2,m_{s,2}}(x_1,\sigma_1;x_2,\sigma_2) $ is normalized and satisfies the Pauli antisymmetry relation and the Pauli exclusion principle.

# ### Two-Electron Atoms
# In a two-electron atom, there are five times in the Hamiltonian: the kinetic energy of both electrons (2 terms), the potential of attraction between the electron and the nucleus (2 terms), and the electron-electron repulsion potential (1 term). 
# 
# $$
# \hat{H}_{\text{2 el. atom}} = -\frac{\hbar^2}{2m}\nabla_1^2 -\frac{\hbar^2}{2m}\nabla_2^2 - \frac{Ze^2}{4 \pi \epsilon_0 r_1} - \frac{Ze^2}{4 \pi \epsilon_0 r_2} + \frac{e^2}{4 \pi \epsilon_0 |\mathbf{r}_1 - \mathbf{r}_2|}
# $$
# 
# Here we introduce the notation
# 
# $$
# \nabla_k^2 = \frac{d^2}{dx_k^2}+ \frac{d^2}{dy_k^2}+\frac{d^2}{dz_k^2}
# $$
# 
# and
# 
# $$
# |\mathbf{r}_j - \mathbf{r}_k| = \sqrt{(x_j-x_k)^2+(y_j-y_k)^2+(z_j-z_k)^2}
# $$
# 
# As with other many-electron systems, solving the Schr&ouml;dinger equation exactly is impossible. However, if one neglects the electron-electron repulsion term, then the Schr&ouml;dinger equation reduces to 
# 
# $$
# \left(\hat{H}_{\text{1 el. atom}}(\mathbf{r}_1) + \hat{H}_{\text{1 el. atom}}(\mathbf{r}_2) \right) \Psi_k(\mathbf{r}_1,\mathbf{r}_2) = E_k \Psi_k(\mathbf{r}_1,\mathbf{r}_2)
# $$
# 
# Solving this equation by separation of variables gives:
# 
# $$
# \Psi_{n_1,l_1,m_{l,1},m_{s,1};n_2,l_2,m_{l,2},m_{s,2}}(\mathbf{r}_1,\sigma_1;\mathbf{r}_2,\sigma_2) 
# = \tfrac{1}{\sqrt{2}}\left( \phi_{n_1,l_1,m_{l,1}}(\mathbf{r}_1)|\sigma_{m_{s,2}}(1)\rangle \phi_{n_2,l_2,m_{l,2}}(\mathbf{r}_2)|\sigma_{m_{s,2}}(2)\rangle - \phi_{n_1,l_1,m_{l,1}}(\mathbf{r}_2)|\sigma_{m_{s,2}}(2)\rangle \phi_{n_2,l_2,m_{l,2}}(\mathbf{r}_1)|\sigma_{m_{s,2}}(1)\rangle \right)
# $$
# 
# $$
# E_{n_1,n_2} = -\frac{Z^2}{2n_1^2}-\frac{Z^2}{2n_2^2} = -\frac{Z^2}{2}\left(\frac{1}{n_1^2} + \frac{1}{n_2^2} \right)
# $$
# 

# #### Perturbative Treatment of the 2-electron atom
# The energy and wavefunction obtained by totally neglecting the electron-electron repulsion are woefully inaccurate. (E.g., the ground-state energy of the Helium atom is too small by $\sim 3000 \text{kJ/mol}$ if you neglect the electron-electron repulsion. We can attempt to account for the effects of electron-electron correlation with perturbation theory. The Hamiltonian of interest, in atomic units, is
# 
# $$
# \hat{H}(\lambda) = -\frac{1}{2}\nabla_1^2 -\frac{1}{2}\nabla_2^2 - \frac{Z}{r_1} - \frac{Z}{r_2} + \frac{\lambda}{|\mathbf{r}_1 - \mathbf{r}_2|}
# $$
# 
# $\hat{H}(0)$ is the exactly solvable Hamiltonian we considered in the previous section. $\hat{H}(1)$ is the exact Hamiltonian of a 2-electron atom (with interacting electrons). The first-order correction to the ground-state energy can be evaluated from the Hellmann-Feynman theorem as:
# 
# $$
# \left[\frac{dE}{d\lambda} \right]_{\lambda = 0} = \langle \Psi(0) | \left[\tfrac{dH}{d\lambda} \right]_{\lambda = 0}| \Psi(0) \rangle = \iint \frac{ \left|\phi_{100}(\mathbf{r}_1)\phi_{100}(\mathbf{r}_2) \right|^2}{|\mathbf{r}_1 - \mathbf{r}_2|} d\mathbf{r}_1 d\mathbf{r}_2 = \frac{5Z}{8}
# $$
# 
# This evaluation of this integral is rather complicated, but detailed instructions are provided [here](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/atomsshort.pdf?raw=true).
# 
# To first order, then, the energy is:
# 
# $$
# E(1) = E(0) + (1) \left[\frac{dE}{d\lambda} \right]_{\lambda = 0} = -Z^2 + \tfrac{5z}{8}
# $$
# 
# For the Helium atom, this gives an energy
# 
# $$
# E_{\text{0th-order p.t.}} = -4 \text{ a.u.} \\
# E_{\text{1st-order p.t.}} = -2.75 \text{ a.u.} \\
# E_{\text{accurate}} = -2.9037 \text{ a.u.}
# $$
# 
# A more detailed derivations of this result is included in the [pdf](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/2elatom.pdf?raw=true). 

# #### Variational Treatment of the 2-electron atom
# The ground-state wavefunction for the 2-electron atom, with electron-electron repulsion excluded, is 
# 
# $$
# \Psi_{\text{non-interacting g.s.}} = \phi_{\text{1s}}(\mathbf{r}_1)\phi_{\text{1s}}(\mathbf{r}_2)\frac{\alpha(1)\beta(2) - \alpha(2)\beta(1)}{\sqrt{2}}
# $$
# 
# where
# 
# $$
# \phi_{\text{1s}}(r) = \sqrt{\frac{Z^3}{\pi}}e^{-Zr}
# $$
# 
# However, we know that one effect of the electron-electron repulsion is that the nucleus is screened. That is, electron 1 feels a reduced attraction to the nucleus because of its repulsion to electron 2. Obviously when the electron is very close to the nucleus, it feels the full nuclear charge ($Z_{eff}(0) = Z$) and when an electron is far from the nucleus, the nuclear charge is reduced one because of the other electron ($Z_{eff}(\infty) = Z-1$). This suggests using an orbital like:
# 
# $$
# \phi_{\text{1s}}(r) \propto e^{-\zeta(r)r}
# $$
# 
# where $\zeta(r)$ is chosen to minimize the energy. When this is done, and the variational principle is invoked to minimize $\zeta(r)$, one is doing a *Hartree-Fock* calculation on the two-electron atom. For the ground state of the Helium atom, this would give,
# 
# $$
# E_{\zeta = Z} = -2.75 \text{ a.u.} \\
# E_{\text{Hartree-Fock}} = -2.862 \text{ a.u.} \\
# E_{\text{accurate}} = -2.9037 \text{ a.u.}
# $$
# 
# Hartree-Fock is too difficult to solve by hand. Consider a very simple model, where the effective nuclear charge is chosen to be a constant, which "averages" somehow the values the effective nuclear charge should have near to, and far from, the nucleus. I.e., one picks a single value of $Z-1 \lt \zeta \lt Z$. The orbital is then
# 
# $$
# \phi_{\text{1s}}(r) = \sqrt{\frac{\zeta^3}{\pi}}e^{-\zeta r}
# $$
# 
# The integrals one needs can be evaluated relatively easily using the Hellmann-Feynman theorem, see the [detailed derivation](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/2elatom.pdf?raw=true). The final result is the energy expression,
# 
# $$
# E(\zeta) = \langle \Psi(\zeta) |\hat{H} | \Psi(\zeta) \rangle = -\zeta^2 -2\zeta Z + \tfrac{5}{8} \zeta
# $$
# 
# According to the variational principle, $E(\zeta) > E_{\text{Hartree-Fock}} > E_{\text{accurate}}$. The best result will be obtained by minimizing this expression with respect to $\zeta$. Setting
# 
# $$
# 0 = \frac{dE}{d\zeta} = 2\zeta - 2Z + \tfrac{5}{8}
# $$
# 
# So the optimal effective nuclear charge was
# 
# $$
# \zeta = Z - \tfrac{5}{16}
# $$
# 
# and substituting this back into the expression allows us to further augment our results for the ground state energy of the Helium atom:
# 
# $$
# E_{\zeta = Z} = -2.75 \text{ a.u.} \\
# E_{\zeta = Z - \tfrac{5}{16}} = -2.848 \text{ a.u.} \\
# E_{\text{Hartree-Fock}} = -2.862 \text{ a.u.} \\
# E_{\text{accurate}} = -2.9037 \text{ a.u.}
# $$
# 

# ![2 electron Slater determinant](https://upload.wikimedia.org/wikipedia/commons/d/da/Slater-Determinant.png "Slater determinant wavefunction for 2 electrons in 1 dimension, appropriate for 2 electrons in a particle-in-a-box. CC by attribution 3 by Lpd-Lbr")
# ## Many-electron wavefunctions: the Slater Determinant
# For more than two electrons, explicitly antisymmetrizing the wavefunction becomes extremely tedious. For example, for a 3-electron system, with electrons in the spatial orbitals $\phi_1(\mathbf{r})$, $\phi_2(\mathbf{r})$, and $\phi_3(\mathbf{r})$, the antisymmetrized wavefunction is:
# 
# $$
# \begin{align}
# \Psi(\mathbf{r}_1,\sigma_1;\mathbf{r}_2,\sigma_2;\mathbf{r}_3,\sigma_3) = \tfrac{1}{\sqrt{3!}}(&\phi_1(\mathbf{r}_1)|\sigma_1(1)\rangle  \phi_2(\mathbf{r}_2)|\sigma_2(2)\rangle  \phi_3(\mathbf{r}_3)|\sigma_3(3)\rangle \\
#  &- \phi_1(\mathbf{r}_1)|\sigma_1(1)\rangle  \phi_2(\mathbf{r}_3)|\sigma_2(3)\rangle  \phi_3(\mathbf{r}_2)|\sigma_3(2)\rangle \\
#  &- \phi_1(\mathbf{r}_2)|\sigma_1(2)\rangle  \phi_2(\mathbf{r}_1)|\sigma_2(1)\rangle  \phi_3(\mathbf{r}_3)|\sigma_3(3)\rangle \\
#  &+ \phi_1(\mathbf{r}_2)|\sigma_1(2)\rangle  \phi_2(\mathbf{r}_3)|\sigma_2(3)\rangle  \phi_3(\mathbf{r}_1)|\sigma_3(1)\rangle \\
#  &-\phi_1(\mathbf{r}_3)|\sigma_1(3)\rangle  \phi_2(\mathbf{r}_2)|\sigma_2(2)\rangle  \phi_3(\mathbf{r}_1)|\sigma_3(1)\rangle \\
#  &+ \phi_1(\mathbf{r}_3)|\sigma_1(3)\rangle  \phi_2(\mathbf{r}_1)|\sigma_2(1)\rangle  \phi_3(\mathbf{r}_2)|\sigma_3(2)\rangle )
# \end{align}
# $$
# 
# In general, for an $N$ electron wavefunction, there are $N!$ terms in the antisymmetrized product. 
# 
# It is helpful to introduce a more compact notation. The product of a spatial orbital and a spin eigenfunction is called a spin-orbital, and denoted
# 
# $$
# \phi_n(\mathbf{r_k},s_k) = \phi_n(k) = \phi_n(\mathbf{r}_k)\sigma_n(k)
# $$
# 
# For example, we can then rewrite the 3-electron antisymmetrized product as:
# 
# $$
# \begin{align}
# \Psi(\mathbf{r}_1,\sigma_1;\mathbf{r}_2,\sigma_2;\mathbf{r}_3,\sigma_3) = &\tfrac{1}{\sqrt{3!}}(\phi_1(1)\phi_2(2)\phi_3(3) - \phi_1(1)\phi_2(3)\phi_3(2)  \\
# &-\phi_1(3)\phi_2(2)\phi_3(1) + \phi_1(3)\phi_2(1)\phi_3(2) \\
# &-\phi_1(2)\phi_2(1)\phi_3(3) + \phi_1(2)\phi_2(3)\phi_3(1))
# \end{align}
# $$
# 
# or as a [Slater determinant](https://en.wikipedia.org/wiki/Slater_determinant)
# 
# $$
# \Psi(1,2,3) = \frac{1}{\sqrt{3!}}
# \begin{vmatrix} 
# \phi_1(1) & \phi_2(1) & \phi_3(1) \\ 
# \phi_1(2) & \phi_2(2) & \phi_3(2) \\ 
# \phi_1(3) & \phi_2(3) & \phi_3(3) 
# \end{vmatrix} 
# $$
# 
# To exemplify the notation, let's write a Slater determinant for the ground-state electron configuration of the Beryllium atom, $\text{1s}^2\text{2s}^2$. 
# 
# $$
# \Psi(\mathbf{r}_1,\mathbf{r}_2,\mathbf{r}_3,\mathbf{r}_4) = \frac{1}{\sqrt{4!}}
# \begin{vmatrix} 
# \phi_{1s}(\mathbf{r}_1)|\alpha(1)\rangle &\phi_{1s}(\mathbf{r}_1)|\beta(1)\rangle & \phi_{2s}(\mathbf{r}_1)|\alpha(1)\rangle & \phi_{2s}(\mathbf{r}_1)|\beta(1)\rangle \\ 
# \phi_{1s}(\mathbf{r}_2)|\alpha(2)\rangle &\phi_{1s}(\mathbf{r}_2)|\beta(2)\rangle & \phi_{2s}(\mathbf{r}_2)|\alpha(2)\rangle & \phi_{2s}(\mathbf{r}_2)|\beta(2)\rangle \\ 
# \phi_{1s}(\mathbf{r}_3)|\alpha(3)\rangle &\phi_{1s}(\mathbf{r}_3)|\beta(3)\rangle & \phi_{2s}(\mathbf{r}_3)|\alpha(3)\rangle & \phi_{2s}(\mathbf{r}_3)|\beta(3)\rangle \\ 
# \phi_{1s}(\mathbf{r}_4)|\alpha(4)\rangle &\phi_{1s}(\mathbf{r}_4)|\beta(4)\rangle & \phi_{2s}(\mathbf{r}_4)|\alpha(4)\rangle & \phi_{2s}(\mathbf{r}_4)|\beta(4)\rangle 
# \end{vmatrix} 
# $$
# 
# The first row of this determinant indicates that the first electron can be in the 1s or 2s orbital, with spin up or spin down. Similarly, the second row of the determinant indicates which orbitals/spins the second electron can have. The first column of the determinant indicates that the up-spin 1s orbital can be occupied by the first, second, third, or fourth electron. Similarly, the last column indicates that the down-spin 2s orbital can be occupied by the first, second, third, or fourth electron.
# 
# In general, for an $N$-electron system with occupied spin-orbitals $\phi_1, \phi_2, \ldots \phi_N$, the Slater determinant is:
# 
# $$
# \Psi(1,2,\ldots,N) = \frac{1}{\sqrt{N!}}
# \begin{vmatrix} 
# \phi_1(1) & \phi_2(1) & \cdots & \phi_N(1) \\ 
# \phi_1(2) & \phi_2(2) & \cdots & \phi_N(2) \\
# \vdots & \vdots & \ddots & \vdots \\ 
# \phi_1(N) & \phi_2(N) & \cdots & \phi_N(N) \\ 
# \end{vmatrix} 
# $$
# 
# Because all the key information in the determinant can be inferred from the first row, we often abbreviate the Slater determinant with 
# 
# $$
# \Psi(1,2,\ldots,N) = \tfrac{1}{\sqrt{N!}}
# \begin{vmatrix} 
# \phi_1 & \phi_2 & \cdots & \phi_N  
# \end{vmatrix} 
# $$
# 
# The Slater determinant captures the Pauli antisymmetry relation because when you interchange two rows of a determinant (corresponding to interchanging the coordinates of two electrons) the determinant changes by a multiplicative factor of -1. Similarly, the Pauli exclusions principle is satisfied because when two electrons are at the same location, two rows of the determinant are equal, and the determinant is zero. In addition to the (spatial) Pauli principles, the Slater determinant indicates that you cannot put two electrons in the same spin-orbital (because the determinant is zero if two columns are the same). The ability to satisfy these key mathematical properties of fermions with a compact wavefunction form is why the Slater determinant is certral to practical quantum chemistry.
# 
# Incidentally, [for bosons the situation is similar](https://en.wikipedia.org/wiki/Fock_space), but instead of a Slater determinant one has a Slater [permanent](https://en.wikipedia.org/wiki/Permanent_(mathematics)). A permanent is similar to a determinant, but when rows (or columns) are interchanged, the permanent of a matrix does not change. Unfortunately, permanents are much more difficult to evaluate, computationally, than determinants.
# 

# ### &#x1f4dd; Exercise: By explicit evaluation, confirm that the $2 \times 2$ and $3 \times 3$ Slater determinants recover the result that would be obtained by explicit antisymmetrization.
# 
# ### &#x1f4dd; Exercise: Write a Slater determinant for the lowest-energy pentuplet state of the Carbon atom, with electron configuration $\text{1s}^2 \text{2s}^1 \text{2p}_0^1 \text{2p}_{+1}^1 \text{2p}_{-1}^1$. Assume all unpaired electrons have $\alpha$ spin.

# ![Cyanine Dyes](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/CyanineDyes.svg?raw=true? "Resonance structures of two different types of cyanine dye")
# ## Example: Many electrons in a Box
# The Hamiltonian for $N$ electrons confined to a box is, in atomic units,
# 
# $$
# \hat{H}_{\text{N el. in 1 dim.}} = \sum_{n=1}^{N} \left(-\frac{1}{2}\frac{d^2}{dx_n^2} + V(x_n)\right)  \sum_{m=1}^{N-1}\sum_{n=m+1}^{N} \frac{1}{|x_m - x_n|}
# $$
# 
# where, as usual,
# 
# $$
# V(x) = 
# \begin{cases}
#     +\infty & x\leq 0\\
#     0       & 0\lt x \lt a\\
#     +\infty & a \leq x
# \end{cases}
# $$
# 
# To solve the Schr&ouml;dinger equation, we neglect the electron-electron repulsion energy. The resulting Hamiltonian is:
# 
# $$
# \hat{H}_{\text{N el. in 1 dim.}} = \sum_{n=1}^{N} \left(-\frac{1}{2}\frac{d^2}{dx_n^2} + V(x_n)\right)  
# = \sum_{n=1}^{N} \hat{H}_{\text{p-in-box}}(x_n)
# $$
# 
# The ground-state energy and wavefunction is obtained by occupying the lowest-energy one-electron states. If the system is closed-shell, then $N$ is even, and the ground-state wavefunction and energy are estimated to be merely,
# 
# $$
# \Psi_{\text{g.s.; no e-e repulsion}}(x_1,x_2,\ldots,x_N) = 
# \frac{1}{\sqrt{N!}} \begin{vmatrix} 
# \phi_1(x_1)\alpha(1) & \phi_1(x_1)\beta(1) & \cdots & \phi_{N/2}(x_1)\alpha(1) &\phi_{N/2}(x_1)\beta(1) \\ 
# \phi_1(x_2)\alpha(2) & \phi_1(x_2)\beta(2) & \cdots & \phi_{N/2}(x_2)\alpha(2) & \phi_{N/2}(x_2)\beta(2) \\ 
# \vdots & \vdots & \; & \vdots & \vdots \\ 
# \phi_1(x_N)\alpha(N) & \phi_1(x_N)\beta(N) & \cdots & \phi_{N/2}(x_N)\alpha(N) & \phi_{N/2}(x_N)\beta(N) 
# \end{vmatrix} 
# $$
# 
# $$
# E_{\text{g.s.; no e-e repulsion}} = \sum_{n=1}^{N/2} 2\epsilon_n
# $$
# 
# where
# 
# $$
# \phi_n(x) = \sqrt{\tfrac{2}{a}} \sin\left(\tfrac{n \pi x}{a}\right) 
# $$
# 
# $$
# \epsilon_n = \frac{(\pi n)^2}{2a^2}
# $$
# 
# The lowest-energy excitation energy of a particle-in-a-box is obtained by exciting an electron from the highest-occupied orbital,
# 
# $$
# \phi_{\text{highest occ.}}(x) = \phi_{N/2}(x) 
# $$
# 
# $$
# \epsilon_{\text{highest occ.}} = \epsilon_{N/2}
# $$
# 
# to the lowest unoccupied orbital, 
# 
# $$
# \phi_{\text{lowest unocc.}}(x) = \phi_{N/2+1}(x) 
# $$
# 
# $$
# \epsilon_{\text{lowest unocc.}} = \epsilon_{N/2+1}
# $$
# 
# The Slater determinant and energy of the lowest-energy excited state is then:
# 
# $$
# \Psi_{\text{e.s.; no e-e repulsion}}(x_1,x_2,\ldots,x_N) = 
# \frac{1}{\sqrt{N!}} \begin{vmatrix} 
# \phi_1(x_1)\alpha(1) & \phi_1(x_1)\beta(1) & \cdots & \phi_{N/2}(x_1)\alpha(1) &\phi_{N/2+1}(x_1)\beta(1) \\ 
# \phi_1(x_2)\alpha(2) & \phi_1(x_2)\beta(2) & \cdots & \phi_{N/2}(x_2)\alpha(2) & \phi_{N/2+1}(x_2)\beta(2) \\ 
# \vdots & \vdots & \; & \vdots & \vdots \\ 
# \phi_1(x_N)\alpha(N) & \phi_1(x_N)\beta(N) & \cdots & \phi_{N/2}(x_N)\alpha(N) & \phi_{N/2+1}(x_N)\beta(N) 
# \end{vmatrix} 
# $$
# 
# $$
# E_{\text{e.s.; no e-e repulsion}} = \sum_{n=1}^{N/2-1} 2\epsilon_n + \epsilon_{N/2} + \epsilon_{N/2+1}
# $$
# 
# where, as before, we've assumed that electron-electron repulsion is negligible. This is reasonable for a sufficiently large box, where electrons can space themselves far away from each other. 
# 
# There are seemingly two equivalent excited states, depending on whether the $\alpha$ or $\beta$ electron is excited. In practice, however, this state is not a singlet. To form a singlet state, one takes a linear combination of these two choices:
# 
# $$
# \Psi_{\text{singlet}}(x_1,x_2,\ldots,x_N) = 
# \frac{1}{\sqrt{2N!}} \left(\begin{vmatrix} 
# \cdots & \phi_{N/2}(x_1)\alpha(1) &\phi_{N/2+1}(x_1)\beta(1) \\ 
# \cdots & \phi_{N/2}(x_2)\alpha(2) & \phi_{N/2+1}(x_2)\beta(2) \\ 
# \cdots & \vdots & \vdots \\ 
# \cdots & \phi_{N/2}(x_N)\alpha(N) & \phi_{N/2+1}(x_N)\beta(N) 
# \end{vmatrix} + \begin{vmatrix} 
# \cdots & \phi_{N/2+1}(x_1)\alpha(1) &\phi_{N/2}(x_1)\beta(1) \\ 
# \cdots & \phi_{N/2+1}(x_2)\alpha(2) & \phi_{N/2}(x_2)\beta(2) \\ 
# \cdots & \vdots & \vdots \\ 
# \cdots & \phi_{N/2+1}(x_N)\alpha(N) & \phi_{N/2}(x_N)\beta(N) 
# \end{vmatrix} \right)
# $$
# 
# Notice that for an arbitrary state, the (noninteracting) energy is just the sum of the occupied orbital energies. If $n_k$ denotes the number of electrons in a spatial orbital, then
# 
# $$
# E_{\text{no e-e repulsion}} = \sum_{k=1}^{\infty} n_k \epsilon_k 
# $$
# 

# ### &#x1f4dd; Exercise: Write the Slater determinant for, and an approximate energy expression for, the ground state and first excited state of 2 electrons in a 2-dimensional square box and 2 electrons in a 3-dimension square box. What changes when you repeat the exercise for 3 electrons?

# ![Spectroscopy](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/Spectroscopy.jpg?raw=true "light on stones, CC SA licensed")
# ## Example: Spectroscopy of Cyanine Dyes
# We are now, finally, in position to revisit the spectrum of the cynanine dyes we began our treatment of quantum mechanics with. Recall that for the cyanine dyes, we can approximate the length of the box with 
# 
# $$
# a = \left(5.67 + 2.49 (k + 1)\right) \cdot 10^{-10} \text{ m} = \left(10.71 + 4.71 (k + 1)\right)\text{ a.u.}
# $$
# 
# and the number of conjugated $\pi$-electrons is:
# 
# $$
# N = 2k + 6
# $$
# 
# The excitation energy is then:
# 
# $$
# \begin{align}
# \Delta E(k) &= E_{\text{e.s.; no e-e repulsion}} - E_{\text{g.s.; no e-e repulsion}} \\
# &= \sum_{n=1}^{k+2} 2\epsilon_n + \epsilon_{k+3} + \epsilon_{k+4} - \sum_{n=1}^{k+3} 2\epsilon_n \\
# &= \epsilon_{k+4} - \epsilon_{k+3} \\
# &= \frac{\pi^2 (k+4)^2}{2a^2} - \frac{\pi^2 (k+3)^2}{2a^2} \\
# &= \frac{\pi^2 \left[(k+4)^2 - (k+3)^2\right]}{2\left(10.71 + 4.71 (k + 1)\right)^2} \\
# &= \frac{\pi^2 (2k+7)}{2\left(10.71 + 4.71 (k + 1)\right)^2}
# \end{align}
# $$
# 
# The wavelength of the transition is given by finding the frequency of the transition. Because we are working in atomic units, it's easier to first compute the angular frequency, which is just equal to the energy difference (in atomic units),
# 
# $$
# \Delta E(k) = \hbar \omega
# $$
# 
# Then from
# 
# $$
# \omega \lambda = 2\pi c
# $$
# 
# we have
# 
# $$
# \lambda = \frac{2 \pi c}{\omega}
# $$
# 
# where the speed of light, in atomic units, is 137.036. 
# 
# The following code block computes the excitation energies for cyanine dyes of a given length, $k$.

# In[1]:


import ipywidgets as widgets
import math

# set up the slider for the size of the dye.
k = widgets.IntSlider(
    value=0,
    min=-2,
    max=10,
    step=1,
    description='k for dye:',
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='d')
    
# Define a function for the wavelength associated with the
# lowest-frequency excitation of a cyanine dye with 
# specified value of k
def compute_wavelength(k):
    "Compute absorption wavelength of a cyanine dye with 2k+6 pi electrons in nm."
    # length of box:
    a = 10.71 + 4.71 * (k + 1)
    # angular frequency of absorption and excitation energy are the same in a.u.
    omega = math.pi**2 * (2 * k + 7) / (2 * a**2)
    # compute absorption wavelength in Bohr (a.u.)
    lambda_au = (2 * math.pi * 137.036)/omega
    # convert Bohr to nanometers
    lambda_nm = lambda_au * 0.0529177
    return lambda_nm

print("For a cyanine dye, there are 2k+6 conjugated pi electrons in the box.")
print("For reference, the experimental absorption wavelengths for various k are:")
print("k = 0 (6 pi electrons):  313 nm")
print("k = 1 (8 pi electrons):  416 nm")
print("k = 2 (10 pi electrons): 519 nm")
print("k = 3 (12 pi electrons): 625 nm")

def print_wavelength(k):
    print(f'The experimental absorption wavelength for k={k} is {compute_wavelength(k):.0f} nm')

out = widgets.interactive_output(print_wavelength, {'k': k})

widgets.VBox([widgets.VBox([k]),out]) 


# ![Molecular Magnet](https://upload.wikimedia.org/wikipedia/commons/e/e7/Struktur_SMM-Mn12.png "Structure of the Mn12 molecular magnet, licensed CCSA3 by Orci")
# ## Many-Electron Atoms and Molecules
# Detailed notes on [many-electron atoms](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/atomsshort.pdf?raw=true) and [molecules](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/molecules.pdf?raw=true) are available as PDFs.
# 
# For a molecule in the [Born-Oppenheimer approximation](https://en.wikipedia.org/wiki/Born%E2%80%93Oppenheimer_approximation), the [electronic Hamiltonian](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/Chpt%201.pdf?raw=true) for $N$ electrons at positions $\mathbf{r}_1, \mathbf{r}_2, \ldots \mathbf{r}_N$ and $P_{\text{atoms}}$ nuclei at positions $\mathbf{R}_1, \mathbf{R}_2, \ldots \mathbf{R}_P$ is, in atomic units,
# 
# $$
# \hat{H}_{\text{molecule}} = \sum_{n=1}^{N} -\frac{\nabla_n^2}{2} -\sum_{n=1}^{N}\sum_{p=1}^{P_{\text{atoms}}}\frac{Z_p}{|\mathbf{r}_n - \mathbf{R}_P|} + \sum_{m=1}^{N-1}\sum_{n=m+1}^{N} \frac{1}{|\mathbf{r}_m - \mathbf{r}_n|}
# $$
# 
# The electron-nuclear potential binds the electrons to the system, and is augmented by additional terms when the molecule is contained in an external field, which can be provided by an experimental apparatus or even surrounding solvent molecules. For this reason, it is common to replace the electron nuclear potential with a more general *external potential*, 
# 
# $$
# v(\mathbf{r}) = -\sum_{p=1}^{P_{\text{atoms}}}\frac{Z_p}{|\mathbf{r} - \mathbf{R}_P|} + \text{possible additional terms}
# $$
# 
# The external potential contains all the potentials acting on the electrons that are *not* due to the other electrons. The Hamiltonian for *any* $N$-electron system is thus:
# 
# $$
# \hat{H}_{\text{el}} = \sum_{n=1}^{N} -\frac{\nabla_n^2}{2} +\sum_{n=1}^{N}v(\mathbf{r}_n) + \sum_{m=1}^{N-1}\sum_{n=m+1}^{N} \frac{1}{|\mathbf{r}_m - \mathbf{r}_n|}
# $$
# 
# The Schr&ouml;dinger equation for $\hat{H}_{\text{el}}$ is not solvable because of the electron-electron coupling terms. As we saw for many-electron atoms, neglecting the electron-electron terms entirely is a poor approximation. Recall that the idea of the Hartree-Fock approximation is that electrons are screened; we can therefore replace the detailed pairwise electron-electron repulsion term with an effective *internal potential* that represents the interactions of the electrons with the cloud of other electrons, 
# 
# $$
# w(\mathbf{r}) = \text{effective potential that an electron at }\mathbf{r}\text{ feels from the cloud of other electrons}
# $$
# 
# This leads to a decoupled electronic Hamiltonian in which the individual electronic coordinates act (quasi)independently,
# 
# $$
# \hat{H}_{\text{ind. el}} = \sum_{n=1}^{N} \left(-\frac{\nabla_n^2}{2} +v(\mathbf{r}_n) +w(\mathbf{r}_n)\right)
# $$
# 
# The eigenfunctions of this Hamiltonian are Slater determinants of the orbitals that solve the one-electron Schr&ouml;dinger equation,
# 
# $$
# \left[-\tfrac{1}{2} \nabla^2 + v(\mathbf{r}) + w(\mathbf{r}) \right] \phi_k(\mathbf{r}) = \epsilon_k \phi_k(\mathbf{r})
# $$
# 
# $$
# \Psi_{\text{ind. el}}(\mathbf{r}_1, \mathbf{r}_2, \ldots \mathbf{r}_N) 
# =\frac{1}{\sqrt{N!}} \begin{vmatrix} 
# \phi_1(1) & \phi_2(1) & \cdots & \phi_N(1) \\ 
# \phi_1(2) & \phi_2(2) & \cdots & \phi_N(2) \\
# \vdots & \vdots & \ddots & \vdots \\ 
# \phi_1(N) & \phi_2(N) & \cdots & \phi_N(N) \\ 
# \end{vmatrix} 
# $$
# 
# and the eigenenergy is the sum of the energy of the orbitals that are occupied in the determinant,
# 
# $$
# E_{\text{ind. el}} = \epsilon_1 + \epsilon_2 + \cdots + \epsilon_N
# $$
# 
# 
# There are many different ways to choose $w(\mathbf{r})$.
# - choose $w(\mathbf{r})$ so that the resulting Slater determinant is as close as possible to the true ground-state wavefunction. (Bruckner)
# - choose $w(\mathbf{r})$ so that the resulting determinant has the lowest possible energy. (Hartree-Fock)
# - choose $w(\mathbf{r})$ as a local operator so that the determinant has the lowest possible energy. (Optimized Effective Potential)
# - choose $w(\mathbf{r})$ so that the electron density and related properties (like the electrostatic potential) are exact. (Kohn-Sham Density Functional Theory)
# - choose $w(\mathbf{r})$ so that the orbital energies, $\epsilon_k$, correspond exactly to the energies required to add (unoccupied orbitals) or remove (occupied orbitals) electrons from the system. (Green's Function methods).
# 
# In practice, most quantum chemistry calculations start from a Slater determinant wavefunction, which was induced by a specific choice of $w(\mathbf{r})$, typically Hartree-Fock. Sometimes further corrections (using variational methods or perturbation theory) are added to the underlying approach.
# 
# ![H2 orbitals](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/H2OrbitalsAnimation.gif?raw=true "H2 orbital animation")

# ## &#x1fa9e; Self-Reflection
# - When will the orbital approximation be most accurate? Least accurate?
# - Explain what the Hartree-Fock approximation has to do with the concept of effective nuclear charge.
# - Can you think of a system where a single Slater determinant would be an extremely poor approximation?
# 
# ## &#x1f914; Thought-Provoking Questions
# - When will the orbital approximation be most accurate? Least accurate?
# - Show that the spin-angular-momentum operators commute with the molecular Hamiltonian? What is the implication of that in terms of the observability of a molecule's spin.
# - Derive the Rydberg formula.
#    - An [advanced](https://www.weimer.itp.uni-hannover.de/fileadmin/weimer-group/qdt.pdf) (and approximate) version of the [Rydberg formula](https://en.wikipedia.org/wiki/Rydberg_state) holds for highly-excited states of most atoms and molecules, and is particularly accurate for excitations from the highest occupied ($ns$ orbital) of [alkali metal atoms](https://en.wikipedia.org/wiki/Rydberg_atom). The basic idea is that the excitation energy can be expressed as a formula like the below, where the [quantum defect](https://en.wikipedia.org/wiki/Quantum_defect), $\delta_{l}$, [depends on the orbital angular momentum of the state](https://www.weimer.itp.uni-hannover.de/fileadmin/weimer-group/qdt.pdf). Can you understand where the below formula for the excitation energy comes from? Why does the quantum defect depend on angular momentum? Why does the quantum defect decrease as the angular momentum of the state? (For example, for Rubidium, $\delta_0 = 3.13$ but $\delta_2 = 1.35$.) Why does the quantum defect increase for heavier alkali metal atoms? (For example, for Li, $\delta_0 = 0.41$ but for Cs, $\delta_0 = 4.13$.)
#    
# $$
# \Delta E_{ns \rightarrow n'l'} \approx \frac{1}{2}\left(\frac{1}{(n-\delta_0)^2}-\frac{1}{(n'-\delta_{l'})^2}\right)
# $$
# 
#    - Can you derive a Rydberg-like formula for the wavenumber of excitations for a particle-in-a-box? How would this formula become more complicated for particles-in-a-box in higher dimensions?
# - For conjugated linear molecules like the cyanine dyes, the $\pi$-electrons are really confined to a 3-dimensional region, but the size of the region that is perpendicular to the conjugation is much smaller. For example, one could consider a 3-dimensional box or a 3-dimension cylinder:
# 
# $$
# \hat{H}_{\text{p-in-3d-box}} = - \frac{\hbar^2}{2m} \nabla^2 + V_{a_x}(x) + V_{a_y}(y) + V_{a_z}(z)
# $$
# 
# $$
# \hat{H}_{\text{p-in-cylinder}} = - \frac{\hbar^2}{2m} \nabla^2 + V_{a_z}(z) + V_{a_r}(r)
# $$
# 
# $$
# V_a(x) = 
# \begin{cases}
#     +\infty & x\leq 0\\
#     0       & 0\lt x \lt a\\
#     +\infty & a \leq x
# \end{cases}
# $$
# 
#   - What are the eigenfunctions and eigenenergies for these systems? 
#   - Why is the one-dimensional particle-in-a-box model sufficient for describing the *spectroscopy* of cyanine dyes? How long does the chain need to be (e.g., for what value of $k$) before the non-one-dimensionality of the box becomes important? You can assume the following (reasonable-ish) values for the parameters:
# 
# $$
# \begin{align}
# a_x &= a_y = 2 \cdot 10^{-10} \text{ m} \\
# a_r &= 1 \cdot 10^{-10} \text{ m} \\
# a_z &= \left(5.67 + 2.49 (k + 1)\right) \cdot 10^{-10} \text{ m} = \left(10.71 + 4.71 (k + 1)\right)\text{ a.u.}
# \end{align}
# $$
# 
# - The Coulomb potential governing interparticle attraction/repulsion between two particles, with charges $q_m$ and $q_n$ and positions $\mathbf{r}_m$ and $\mathbf{r}_n$ in a d-dimensional system is given below. Note that these expressions are *not* the usual inverse power of the distance. Nonetheless, when considering systems like the cyanine dyes or 2-dimensional quantum dots, we usually use the 3-dimensional Coulomb potential. Why? 
# 
# $$
# V_{\text{Coulomb}} = 
# \begin{cases}
# (q_m q_n) \left|\mathbf{r}_m - \mathbf{r}_n \right|^{2-d} & d> 0 \text{ and } d \ne 2 \\
# (q_m q_n)\ln\left|\mathbf{r}_m - \mathbf{r}_n \right|  & d = 2
# \end{cases}
# $$
# 
# 
# 
# ## &#x1f501; Recapitulation
# - What are bosons? What are fermions? How do the wavefunctions differ? 
# - Write the Schr&ouml;dinger equation for a many-electron molecule in the Born-Oppenheimer approximation.
# - What is the fundamental assumption that underlies the orbital approximation?
# - What is a Slater determinant?
# - What is the fundamental idea behind Hartree-Fock theory?
# - How does one use the secular equation to approximate the wavefunction for a many-electron system?
# - Why are Gaussian basis functions used in quantum chemistry?
# - How does one compute an excitation energy? 
# 
# ## &#x1f52e; Next Up...
# - H&uuml;ckel Theory and Its Extensions
# 
# ## &#x1f4da; References
# My favorite sources for this material are:
# - [Randy's book](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/DumontBook.pdf?raw=true)
# - D. A. MacQuarrie, Quantum Chemistry (University Science Books, Mill Valley California, 1983)
# 
# There are also some excellent wikipedia articles:
# - [Slater determinant](https://en.wikipedia.org/wiki/Slater_determinant)
# - [Hartree-Fock](https://en.wikipedia.org/wiki/Hartree%E2%80%93Fock_method)

# In[ ]:




