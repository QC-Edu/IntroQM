#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction-to-Quantum-Mechanics" data-toc-modified-id="Introduction-to-Quantum-Mechanics-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction to Quantum Mechanics</a></span><ul class="toc-item"><li><span><a href="#🎯-Objective¶" data-toc-modified-id="🎯-Objective¶-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>🎯 Objective¶</a></span></li><li><span><a href="#📜-Instructions" data-toc-modified-id="📜-Instructions-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>📜 Instructions</a></span></li><li><span><a href="#Wave-Particle-Duality" data-toc-modified-id="Wave-Particle-Duality-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Wave-Particle Duality</a></span><ul class="toc-item"><li><span><a href="#🎲-Particle-like-features-of-light." data-toc-modified-id="🎲-Particle-like-features-of-light.-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>🎲 Particle-like features of light.</a></span></li><li><span><a href="#🖩-Properties-of-photons" data-toc-modified-id="🖩-Properties-of-photons-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>🖩 Properties of photons</a></span></li><li><span><a href="#🪙-Properties-of-photons" data-toc-modified-id="🪙-Properties-of-photons-1.3.3"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span>🪙 Properties of photons</a></span></li><li><span><a href="#🪙-Properties-of-photons" data-toc-modified-id="🪙-Properties-of-photons-1.3.4"><span class="toc-item-num">1.3.4&nbsp;&nbsp;</span>🪙 Properties of photons</a></span></li><li><span><a href="#🖩-Properties-of-photons" data-toc-modified-id="🖩-Properties-of-photons-1.3.5"><span class="toc-item-num">1.3.5&nbsp;&nbsp;</span>🖩 Properties of photons</a></span></li><li><span><a href="#🎲-Properties-of-photons" data-toc-modified-id="🎲-Properties-of-photons-1.3.6"><span class="toc-item-num">1.3.6&nbsp;&nbsp;</span>🎲 Properties of photons</a></span></li><li><span><a href="#🖩-Momentum-from-a-green-laser-pointer" data-toc-modified-id="🖩-Momentum-from-a-green-laser-pointer-1.3.7"><span class="toc-item-num">1.3.7&nbsp;&nbsp;</span>🖩 Momentum from a green laser pointer</a></span></li><li><span><a href="#🖩-Wavelength-emitted-by-a-radiopharmaceutical" data-toc-modified-id="🖩-Wavelength-emitted-by-a-radiopharmaceutical-1.3.8"><span class="toc-item-num">1.3.8&nbsp;&nbsp;</span>🖩 Wavelength emitted by a radiopharmaceutical</a></span></li><li><span><a href="#🪙-Davisson-Germer-experiment" data-toc-modified-id="🪙-Davisson-Germer-experiment-1.3.9"><span class="toc-item-num">1.3.9&nbsp;&nbsp;</span>🪙 Davisson-Germer experiment</a></span></li><li><span><a href="#🎲-Davisson-Germer-experiment" data-toc-modified-id="🎲-Davisson-Germer-experiment-1.3.10"><span class="toc-item-num">1.3.10&nbsp;&nbsp;</span>🎲 Davisson-Germer experiment</a></span></li><li><span><a href="#🖩-Properties-of-photons" data-toc-modified-id="🖩-Properties-of-photons-1.3.11"><span class="toc-item-num">1.3.11&nbsp;&nbsp;</span>🖩 Properties of photons</a></span></li><li><span><a href="#🖩-Rydberg's-Law" data-toc-modified-id="🖩-Rydberg's-Law-1.3.12"><span class="toc-item-num">1.3.12&nbsp;&nbsp;</span>🖩 Rydberg's Law</a></span></li><li><span><a href="#🎲-Wave-properties-of-particles" data-toc-modified-id="🎲-Wave-properties-of-particles-1.3.13"><span class="toc-item-num">1.3.13&nbsp;&nbsp;</span>🎲 Wave properties of particles</a></span></li><li><span><a href="#🎲-Particle-properties-of-waves" data-toc-modified-id="🎲-Particle-properties-of-waves-1.3.14"><span class="toc-item-num">1.3.14&nbsp;&nbsp;</span>🎲 Particle properties of waves</a></span></li><li><span><a href="#🖩-Properties-of-photons" data-toc-modified-id="🖩-Properties-of-photons-1.3.15"><span class="toc-item-num">1.3.15&nbsp;&nbsp;</span>🖩 Properties of photons</a></span></li><li><span><a href="#🖩-Properties-of-photons" data-toc-modified-id="🖩-Properties-of-photons-1.3.16"><span class="toc-item-num">1.3.16&nbsp;&nbsp;</span>🖩 Properties of photons</a></span></li><li><span><a href="#🖩-De-Broglie-wavelength-of-a-baseball" data-toc-modified-id="🖩-De-Broglie-wavelength-of-a-baseball-1.3.17"><span class="toc-item-num">1.3.17&nbsp;&nbsp;</span>🖩 De Broglie wavelength of a baseball</a></span></li></ul></li><li><span><a href="#The-Schrödinger-Equation" data-toc-modified-id="The-Schrödinger-Equation-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>The Schrödinger Equation</a></span><ul class="toc-item"><li><span><a href="#✍️-Time-Dependent-Schrödinger-Equation" data-toc-modified-id="✍️-Time-Dependent-Schrödinger-Equation-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>✍️ Time-Dependent Schrödinger Equation</a></span></li><li><span><a href="#🎲-Hamiltonian-operator" data-toc-modified-id="🎲-Hamiltonian-operator-1.4.2"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>🎲 Hamiltonian operator</a></span></li></ul></li><li><span><a href="#Mathematics" data-toc-modified-id="Mathematics-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Mathematics</a></span><ul class="toc-item"><li><span><a href="#🪙-Mathematical-Properties-of-the-wavefunction" data-toc-modified-id="🪙-Mathematical-Properties-of-the-wavefunction-1.5.1"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>🪙 Mathematical Properties of the wavefunction</a></span></li><li><span><a href="#🎲-Complex-Conjugation" data-toc-modified-id="🎲-Complex-Conjugation-1.5.2"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>🎲 Complex Conjugation</a></span></li><li><span><a href="#✍️-Complex-Conjugation" data-toc-modified-id="✍️-Complex-Conjugation-1.5.3"><span class="toc-item-num">1.5.3&nbsp;&nbsp;</span>✍️ Complex Conjugation</a></span></li><li><span><a href="#🪙-Eigenfunctions-of-the-kinetic-energy-operator" data-toc-modified-id="🪙-Eigenfunctions-of-the-kinetic-energy-operator-1.5.4"><span class="toc-item-num">1.5.4&nbsp;&nbsp;</span>🪙 Eigenfunctions of the kinetic-energy operator</a></span></li></ul></li></ul></li></ul></div>

# # Introduction to Quantum Mechanics
# 
# ##  &#x1f3af; Objective¶
# To review basic aspects of quantum mechanics.
# 
# ## &#x1f4dc; Instructions
# Before you turn this problem in, make sure everything runs as expected. First, restart the kernel (in the menubar, select Kernel → Restart) and then run all cells (in the menubar, select Cell → Run All).
# 
# Make sure you fill in any place that says YOUR CODE HERE or "YOUR ANSWER HERE", as well as your name, username (the prefix to your @university.ext e-mail), and student ID number in the cell below

# In[1]:


Name = "First M. Last"
email_user_name = "username"
ID_number = 1234567

# It's useful to import these libraries. 
# You can import others or not even use these, though.
import numpy as np
import scipy
from scipy import constants


# ## Wave-Particle Duality

# ### &#x1f3b2; Particle-like features of light.
# Which of the following phenomena are strongly associated with the particle-like nature of light. <br>
# **A**. Blackbody radiation <br>
# **B**. Compton Scattering  <br>
# **C**. Electron Diffraction <br>
# **D**. Stern-Gerlach Experiment <br>
# **E**. Photoelectric effect 

# In[2]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then ad1 = ["A", "C"]. 
# I've initialized the answer to the empty list.
ad1 = []

### BEGIN SOLUTION
ad1 = ["A", "B", "E"]
### END SOLUTION


# In[3]:


print("The following phenomena are associated with the particle-like nature of light:", ad1)
assert(isinstance(ad1,set) or isinstance(ad1,list) or isinstance(ad1,tuple))
assert(len(ad1) > 0)
### BEGIN HIDDEN TESTS
assert(set(map(str.casefold,ad1)) == {"a","b","e"})
### END HIDDEN TESTS


# === BEGIN MARK SCHEME ===
# 
# More information about this question can be found in section 3 of the notes [From Newton to Schrodinger](https://paulwayers.github.io/IntroQChem/notes/html/History.html "See especially section 3").
# 
# === END MARK SCHEME ===

# ### &#x1F5A9; Properties of photons
# What is the frequency of light in Hz ($s^{-1}$) of light with wavelength 500 nm?

# In[4]:


# Use the code box as a calculator, but report your answer as a float. 
# ansDuality2 = float. I've initialized the answer to None.
ad2 = None

### BEGIN SOLUTION
# wavelength * frequency = speed of light
ad2 = constants.c/500e-9
print("the frequency of light with wavelength 500 nm is {0:.3e} Hz".format(ad2))
### END SOLUTION


# In[5]:


assert(isinstance(ad2,float))

### BEGIN HIDDEN TESTS
assert(np.isclose(ad2,constants.c/500e-9,rtol=1e-3))
### END HIDDEN TESTS


# === BEGIN MARK SCHEME ===
# 
# The key equations for this problem are:
# 
# $$\lambda \nu = c$$
# 
# so
# 
# $$\nu = \frac{c}{\lambda}$$
# 
# === END MARK SCHEME ===

# ### &#x1fa99; Properties of photons
# 
# Doubling the wavelength of radiation doubles its frequency. (True/False)
# 

# In[6]:


# Report your answer as a Boolean, so freq_double = True or freq_double = False
freq_double = None

### BEGIN SOLUTION
freq_double = False
### END SOLUTION


# In[7]:


assert(isinstance(freq_double,bool))
print("It is", freq_double, "that when the wavelength of radiation doubles its frequency does also.")
### BEGIN HIDDEN TESTS
assert(freq_double == False)
# The frequency halves, because frequency = c/wavelength
### END HIDDEN TESTS


# ### &#x1fa99; Properties of photons
# 
# Doubling the wavelength of radiation halves its speed. (True/False)

# In[8]:


# Report your answer as a Boolean, so speed_halves = True or speed_halves = False
speed_halves = None

### BEGIN SOLUTION
speed_halves = False
### END SOLUTION


# In[9]:


assert(isinstance(speed_halves,bool))
print("It is", speed_halves, "that when the wavelength of radiation doubles its speed halves.")
### BEGIN HIDDEN TESTS
assert(speed_halves == False)
# The speed of light is a constant and does not depend on its wavelength.
### END HIDDEN TESTS


# ### &#x1F5A9; Properties of photons
# A helium-neon laser emits light at 632.8 nm.  What is the energy of the photons generated by this laser, in Joules?

# In[10]:


# Use the code box as a calculator, but report your answer as a float. 
# E_HeNe = float. I've initialized the answer to None.
E_HeNe = None

### BEGIN SOLUTION
# E = h * frequency = h * c/wavelength
E_HeNe = constants.h * constants.c/632.8e-9
print("the energy of light with wavelength 632.8 nm is {0:.3e} J".format(E_HeNe))
### END SOLUTION


# In[11]:


assert(isinstance(E_HeNe,float))

### BEGIN HIDDEN TESTS
assert(np.isclose(E_HeNe,3.1391e-19,rtol=1e-3))
### END HIDDEN TESTS


# ### &#x1f3b2; Properties of photons
# 
# Which of the following changes would double the energy of a photon: <br>
# **A**. Doubling its frequency <br>
# **B**. Doubling its wavelength <br>
# **C**. Doubling its momentum <br>
# **D**. Doubling its speed <br>
# **E**. Doubling its effective (relativistic) mass <br>
# **F**. Doubling its wavenumber. 

# In[12]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then e_doubles = ["A", "C"]. 
# I've initialized the answer to the empty list.
e_doubles = []

### BEGIN SOLUTION
e_doubles = ["A","C","E","F"]
### END SOLUTION


# In[13]:


print("Ways you can double the energy of a photon include", e_doubles)
assert(isinstance(e_doubles,set) or isinstance(e_doubles,list) or isinstance(e_doubles,tuple))
assert(len(e_doubles) > 0)
### BEGIN HIDDEN TESTS
assert(set(map(str.casefold,e_doubles)) == {"a","c","e","f"})
### END HIDDEN TESTS


# ### &#x1F5A9; Momentum from a green laser pointer
# I have a high-powered green laser pointer (532 nm wavelength, 100 mW power) that I use for astronomical starspotting. If I shine this laser pointer on you, how much momentum, per second, will be transferred to you? Report your answer in SI units of kg m/s.

# In[14]:


# Use the code box as a calculator, but report your answer as a float. 
# p_greenlaser = float. I've initialized the answer to None.
p_greenlaser = None

### BEGIN SOLUTION
# The energy and momentum of a single green photon is 
p_greenphoton = constants.h/532e-9  #in kg m/s
E_greenphoton = constants.h*constants.c/532e-9 #in Joules
# Based on the power, which is 100 mW = .1 J/s, we can deduce
# power = (energy of a single photon)(number of photons per second)
n_greenphotons_persecond = .1/E_greenphoton
p_greenlaser = p_greenphoton * n_greenphotons_persecond
### END SOLUTION


# In[15]:


assert(isinstance(p_greenlaser,float))
print("the momentum transfered per second is {0:.3e} kg m/s".format(p_greenlaser))

### BEGIN HIDDEN TESTS
assert(np.isclose(p_greenlaser,3.336e-10,rtol=1e-3))
### END HIDDEN TESTS


# ### &#x1F5A9; Wavelength emitted by a radiopharmaceutical
# The radioactive isotope Cobalt-60 is used in nuclear medicine to treat cancer. The energy emitted by Cobalt-60 is 1.29 x 10^11 J/mol. What is the wavelength of the emitted $\gamma$ rays?

# In[16]:


# Use the code box as a calculator, but report your answer as a float. 
# wlength_Co60 = float. I've initialized the answer to None.
wlength_Co60 = None

### BEGIN SOLUTION
# The energy is given in Joules per mole, so let's first compute the energy of a single photon,
E_photonCo60 = 1.29e11/constants.N_A
# The wavelength is then determined form E = h*frequency = hc/wavelength
wlength_C60 = constants.h * constants.c/E_photonCo60
print("the wavelength emitted by the radioactive isotope Co60 is {0:.3e} m".format(wlength_C60))
### END SOLUTION


# In[17]:


assert(isinstance(wlength_C60,float))

### BEGIN HIDDEN TESTS
assert(np.isclose(wlength_C60,9.273e-13,rtol=1e-3))
### END HIDDEN TESTS


# ### &#x1fa99; Davisson-Germer experiment
# The Davisson-Germer experiment was among the first explicit verifications of the wave-like nature of electrons, and was foundational for modern electron diffraction methods. (True/False)

# In[18]:


# Report your answer as a Boolean, so ad3 = True or ad3 = False
ad3 = None

### BEGIN SOLUTION
ad3 = True
### END SOLUTION


# In[19]:


assert(isinstance(ad3,bool))
print("The answer is:", ad3)
### BEGIN HIDDEN TESTS
assert(ad3 == True)
### END HIDDEN TESTS


# === BEGIN MARK SCHEME ===
# 
# You can find more details about the Davisson-Germer experiment in section 3.3 of the [notes on the Introduction to Quantum Mechanics](https://paulwayers.github.io/IntroQChem/notes/html/History.html).
# 
# === END MARK SCHEME ===

# ### &#x1f3b2; Davisson-Germer experiment
# The Davisson-Germer experiment demonstrated that if you shine a beam of electrons on a metal crystal, the result is <br>
# **A**. the electrons are absorbed at “critical energies” similar to the optical (light) absorption spectrum. <br>
# **B**. the electrons scatter according to the Bragg law for X-ray scattering. <br>
# **C**. the electrons go right through the metal. <br>
# **D**. the metal gets very hot and becomes a dull red color (stimulated blackbody emission of radiation). <br>

# In[20]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then ad3b = ["A", "C"]. 
# I've initialized the answer to the empty list.
ad3b = []

### BEGIN SOLUTION
ad3b = ["B"]
### END SOLUTION


# In[21]:


print("In the Davisson-Germer experiment", ad3b)
assert(isinstance(ad3b,set) or isinstance(ad3b,list) or isinstance(ad3b,tuple))
assert(len(ad3b) == 1)
### BEGIN HIDDEN TESTS
assert(set(map(str.casefold,ad3b)) == {"b"})
### END HIDDEN TESTS


# ### &#x1F5A9; Properties of photons
# What is the momentum of a $\gamma$-ray photon with a wavelength of $10^{-13}$ m in SI units of ${\frac{\text{m} \cdot \text{kg}}{\text{s}}}$?

# In[22]:


# Use the code box as a calculator, but report your answer as a float. 
# ad4 = float. I've initialized the answer to None.
ad4 = None

### BEGIN SOLUTION
# momentum = h/wavelength
ad4 = constants.h/1e-13
print("the momentum of a photon with a wavelength of 1e-13 m is {0:.3e} m kg/s".format(ad4))
### END SOLUTION


# In[23]:


assert(isinstance(ad4,float))

### BEGIN HIDDEN TESTS
assert(np.isclose(ad4,constants.h/1e-13,rtol=1e-3))
### END HIDDEN TESTS


# === BEGIN MARK SCHEME ===
# The momentum of a photon can be computed from the De Broglie relation (here, better credited to Compton):
# 
# $$ p = \frac{h}{\lambda} $$
# 
# === END MARK SCHEME ===

# ### &#x1F5A9; Rydberg's Law
# Rydberg's law says that the wavenumber for the absorptions for a one-electron atom/ion with atomic number Z is given by the expression
# 
# $$ \tilde{\nu} = \left( 1.0974 \cdot 10^7 m^{-1}\right) Z^2 
# \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right) $$
# 
# where $1 < n_1 < n_2 < \inf$. Suppose you are given the Hydrogen atom in its ground state, $n_1=1$. What is the lowest absorption frequency?

# In[24]:


# Use the code box as a calculator, but report your answer as a float. 
# ad5 = float. I've initialized the answer to None.
ad5 = None

### BEGIN SOLUTION
wavenumber = 1.0974e7 * 1 * (1 - 1./4) #from the Rydberg formula
# frequency is speed of light times wavenumber, where wavenumber = 1/wavelength
ad5 = constants.c*wavenumber
print("the lowest absorption frequency for the hydrogen atom is {0:.3e} Hz".format(ad5))
### END SOLUTION


# In[25]:


assert(isinstance(ad5,float))

### BEGIN HIDDEN TESTS
assert(np.isclose(ad5,2.467e15,rtol=1e-3))
### END HIDDEN TESTS


# === BEGIN MARK SCHEME ===
# 
# The lowest absorption frequency will correspond to exciting from the ground state to the lowest excited state, so $n_2 = 2$. Using this, we can compute the wavelength from:
# 
# $$\tilde{\nu} = (1.0974\cdot 10^7)(1^2)\left(\frac{1}{1^2} - \frac{1}{2^2} \right) $$
# 
# and then convert the wavelength to frequency using
# 
# $$ \nu = c\tilde{\nu} $$
# 
# === END MARK SCHEME ===

# ### &#x1f3b2; Wave properties of particles
# Which of the following experimental results are often cited as examples of the wave-likeness of particles like electrons?  
# **A**. blackbody radiation  
# **B**. discrete emission lines in the hydrogen spectrum  
# **C**. photoelectric effect  
# **D**. Compton scattering of light by a particle  
# **E**. Electron scattering from a crystal

# In[26]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then ad6 = ["A", "C"]. 
# I've initialized the answer to the empty list.
ad6 = []

### BEGIN SOLUTION
ad6 = ["E"]
### END SOLUTION


# In[27]:


print("The following phenomena are associated with the wave-like nature of electrons:", ad6)
assert(isinstance(ad6,set) or isinstance(ad6,list) or isinstance(ad6,tuple))
assert(len(ad6) > 0)
### BEGIN HIDDEN TESTS
assert(set(map(str.casefold,ad6)) == {"e"} or set(map(str.casefold,ad6)) == {"b","e"})
### END HIDDEN TESTS
# B is a reasonable answer from the viewpoint of the Bohr model of the Hydrogen atom, but is less obvious than
# E (electron scattering).


# ###  &#x1f3b2; Particle properties of waves
# Which of the following experimental results are often cited as examples of the particle-likeness of radiation (light)?   
# **A**. blackbody radiation <br>
# **B**. discrete emission lines in the hydrogen spectrum <br>
# **C**. photoelectric effect <br>
# **D**. Compton scattering of light by a particle <br>
# **E**. Electron scattering from a crystal <br>

# In[28]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then ad7 = ["A", "C"]. 
# I've initialized the answer to the empty list.
ad7 = []

### BEGIN SOLUTION
ad7 = ["A","C","D"]
### END SOLUTION


# In[29]:


print("The following phenomena are associated with the particle-like nature of light:", ad7)
assert(isinstance(ad7,set) or isinstance(ad7,list) or isinstance(ad7,tuple))
assert(len(ad7) > 0)
### BEGIN HIDDEN TESTS
assert(set(map(str.casefold,ad7)) == {"a","c","d"})
### END HIDDEN TESTS


# ### &#x1F5A9; Properties of photons
# Suppose you are given a photon with an energy of 2 eV. What is its momentum in 
# $\frac{\text{m} \cdot \text{kg}}{\text{s}}$? What is its frequency in Hz?

# In[30]:


# Use the code box as a calculator, but report your answer as float(s). 
# I've initialized the answers to None.
momentum_d9 = None
frequency_d9 = None

### BEGIN SOLUTION
# frequency = E/h
# get Planck's constant in useful units.
h_in_eVs = scipy.constants.value("Planck constant in eV/Hz")
frequency_d9 = 2.0/h_in_eVs
#Now useful to use Planck's constant in nice units.
momentum_d9 = constants.h*frequency_d9/constants.c

print("the frequency of a photon with an energy of 2 eV is {0:.3e} Hz".format(frequency_d9))
print("the momentum of a photon with an energy of 2 eV is {0:.3e} m kg/s".format(momentum_d9))
### END SOLUTION


# In[31]:


assert(isinstance(momentum_d9,float))
assert(isinstance(frequency_d9,float))

### BEGIN HIDDEN TESTS
assert(np.isclose(momentum_d9,1.069e-27,rtol=1e-3))
assert(np.isclose(frequency_d9,4.836e+14,rtol=1e-3))
### END HIDDEN TESTS


# === BEGIN MARK SCHEME ===
# 
# First we can compute the frequency of the photon as:
# 
# $$ \nu = \frac{E}{h} $$
# 
# but there is the slight complication that the energy was given in electron-volts. Fortunately we have this constant built into to scipy.constants. 
# 
# The momentum of the photon can be computed from the De Broglie relation,
# 
# $$ p = \frac{h}{\lambda} = \frac{h}{\tfrac{c}{\nu}} = \frac{h \nu}{c} = \frac{E}{c} $$
# 
# Where the last formula, which was proposed long ago by Einstein and Compton and appeared in the notes, could have been used directly had you remembered it. However, because our energy is in electron-volts, it's a bit easier to use the next-to-last formula.
# 
# === END MARK SCHEME ===

# ### &#x1F5A9; Properties of photons
# What is the momentum and energy of a photon with angular wavenumber $k=10^7 \text{m}^{-1}$?

# In[32]:


# Use the code box as a calculator, but report your answer as float(s). 
# I've initialized the answers to None.
p_from_k = None   #momentum of the photon
E_from_k = None   #Energy of the photon

### BEGIN SOLUTION
# p = h-bar * k
p_from_k = constants.hbar * 1e7
E_from_k = constants.c * p_from_k

print("the momentum of a photon with an angular wavenumber of 1e7 1/m is {0:.3e} m kg/s.".format(p_from_k))
print("the energy of a photon with an angular wavenumber of 1e7 1/m is {0:.3e} J.".format(E_from_k))
### END SOLUTION


# In[33]:


assert(isinstance(p_from_k,float))
assert(isinstance(E_from_k,float))

### BEGIN HIDDEN TESTS
assert(np.isclose(p_from_k,1.055e-27,rtol=1e-3))
assert(np.isclose(E_from_k,3.162e-19,rtol=1e-3))
### END HIDDEN TESTS


# === BEGIN MARK SCHEME ===
# 
# We can start with the equation for the momentum, which is easy:
# 
# $$ p = \hbar k $$
# 
# 
# The equation for the energy can deduced directly as $E = pc$, but if you forgot this, then,
# 
# $$ E = h \nu = \frac{hc}{\lambda} = p c $$
# 
# using the Planck relation (first equality) and the De Broglie relation (last equality).
# 
# === END MARK SCHEME ===

# ### &#x1F5A9; De Broglie wavelength of a baseball
# During departmental baseball games, your instructor insists that the only reason he strikes out is because of the De Broglie wavelength of the baseball means that even though he swings in the correct location, he still misses. Suppose that the opposing major-league-quality hurler throws the baseball (mass = 145 g) at 100 miles-per-hour (45 m/s). What is the De Broglie wavelength of the baseball?

# In[34]:


# Use the code box as a calculator, but report your answer as float(s). 
# I've initialized the answer to None.
wl_baseball = None   #wavelength of the baseball.

### BEGIN SOLUTION
# wavelength = h/momentum = h/(mass * velocity) = h/(.145 kg * 45 m/s)
wl_baseball = constants.h/(.145*45)

print("the wavelength of the baseball is {0:.3e} m!".format(wl_baseball))
### END SOLUTION


# In[35]:


assert(isinstance(wl_baseball,float))

### BEGIN HIDDEN TESTS
assert(np.isclose(wl_baseball,1.e-34,rtol=1e-2))
### END HIDDEN TESTS


# ## The Schr&ouml;dinger Equation

# ### &#x270d;&#xfe0f; Time-Dependent Schr&ouml;dinger Equation
# What is the time-dependent Schr&ouml;dinger equation for the complex conjugate of the wavefunction, $\Psi^*$?
# Put your answer in the markdown cell below. You can drag and drop an attachment (of most types) to this cell also. 

# === BEGIN MARK SCHEME ===
# 
# Taking the complex-conjugate of the time-dependent Schr&ouml;dinger equation gives:
# 
# $$ -i \hbar \frac{d \Psi^*(x,t)}{dt} = - \frac{\hbar}{2m} \frac{d^2 \Psi^*(x,t)}{dx^2} + V(x,t)\Psi^*(x,t) $$
# 
# === END MARK SCHEME ===

# ### &#x1f3b2; Hamiltonian operator
# The Hamiltonian operator corresponds to which observable property of a quantum system? <br>
# **A**. Action <br>
# **B**. Momentum <br>
# **C**. Kinetic Energy <br>
# **D**. De Broglie Wavelength <br>
# **E**. Total Energy <br>
# **F**. Angular Momentum <br>
# **G**. Entropy  
# **H**. Planck Mass

# In[36]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then ansSE2 = ["A", "C"]. 
# I've initialized the answer to the empty list.
ansSE2 = []

### BEGIN SOLUTION
ansSE2 = ["E"]
### END SOLUTION


# In[37]:


print("The Hamiltonian is the quantum-mechanical operator for:", ansSE2)
assert(isinstance(ansSE2,set) or isinstance(ansSE2,list) or isinstance(ansSE2,tuple))
assert(len(ansSE2) == 1)
### BEGIN HIDDEN TESTS
assert(set(map(str.casefold,ansSE2)) == {"e"})
### END HIDDEN TESTS


# ## Mathematics

# ###  &#x1fa99; Mathematical Properties of the wavefunction
# A probability density can be negative. (True/False)

# In[38]:


prob_canbe_negative = None

### BEGIN SOLUTION
prob_canbe_negative = False
### END SOLUTION


# In[39]:


assert(isinstance(prob_canbe_negative,bool))
print("It is", prob_canbe_negative, "that a probability density can be negative.")
### BEGIN HIDDEN TESTS
assert(prob_canbe_negative == False)
### END HIDDEN TESTS


# ### &#x1f3b2; Complex Conjugation
# Let $z$ be a complex number. If $w$ is the product of $z$ and its complex 
# conjugate, $w = z z^*$, which of the following is **always** true about $w$: <br>
# **A**. w is an imaginary number. <br>
# **B**. w is a complex number. <br>
# **C**. w is nonzero real number. <br>
# **D**. w is a nonnegative real number. <br>
# **E**. w is a nonzero complex number. <br>
# **F**. None of the above

# In[40]:


# Report your answer as a list, tuple, or set containing the correct answers. 
# For example, if the answers are A and C, then zzstar = ["A", "C"]. 
# I've initialized the answer to the empty list.
zzstar = []

### BEGIN SOLUTION
zzstar = ["B","D"]
### END SOLUTION


# In[41]:


print("The product of a number and its complex conjugate is always", zzstar)
assert(isinstance(zzstar,set) or isinstance(zzstar,list) or isinstance(zzstar,tuple))
assert(len(zzstar) > 0)
### BEGIN HIDDEN TESTS
assert(set(map(str.casefold,zzstar)) == {"b","d"})
### END HIDDEN TESTS


# ### &#x270d;&#xfe0f; Complex Conjugation
# What is the complex conjugate of 
# 
# $$ \Psi(x,t) = A e^{(a+bi)(kx - \omega t)} $$
# 

# === BEGIN MARK SCHEME ===
# The complex conjugate is obtained by replacing $i$ with $-i$. So
# 
# $$ \Psi^*(x,t) = A e^{(a-bi)(kx - \omega t)} $$
# 
# I would accept an answer where it was not assumed that the constants in the expression were real, e.g.,
# 
# $$ \Psi^*(x,t) = A^* e^{(a^*-b^*i)(k^*x - \omega^* t)} $$
# 
# === END MARK SCHEME ===

# ### &#x1fa99; Eigenfunctions of the kinetic-energy operator
# *Every* eigenfunction of the momentum operator is also an eigenfunction of the kinetic-energy operator. (True/False)

# In[42]:


# Report your answer as a Boolean, so is_also_eigenfunction = True or = False
is_also_eigenfunction = None

### BEGIN SOLUTION
is_also_eigenfunction = True
### END SOLUTION


# In[43]:


assert(isinstance(is_also_eigenfunction,bool))
print("The answer is:", is_also_eigenfunction)
### BEGIN HIDDEN TESTS
assert(is_also_eigenfunction == True)
### END HIDDEN TESTS


# 
# $$\hat{p} \psi(x) = \lambda \psi(x) $$
# 
# $$ \hat{T} = \frac{\hat{p}^2}{2m} $$
# 
# $$ \hat{T} \psi(x) = \tfrac{1}{2m} \hat{p} \hat{p} \psi(x) =  \tfrac{1}{2m} \hat{p} \lambda \psi(x) =  \tfrac{1}{2m} \lambda^2 \psi(x) $$
# 
# The reverse is also true, but it's more subtle. You can use the fact that $\hat{p} = 2m \sqrt{\hat{T}}$, but this is not quite true; $\cos a x$ and $sin a x$ are eigenfunctions of the kinetic energy but not the momentum. The general result is that, given an operator, $\hat{Q}$, with has eigenfunctions
# 
# $$ \hat{Q} \psi_k(x) = \theta_k \psi_k(x) $$
# 
# then any (analytic) function of $\hat{Q}$, has the same eigenfunctions, and the values are:
# 
# $$ f(\hat{Q}) \psi_k(x) = f(\theta_k) \psi_k(x) $$
# 

# &#x1f4dd; 
# &#x1f500;

# In[ ]:




