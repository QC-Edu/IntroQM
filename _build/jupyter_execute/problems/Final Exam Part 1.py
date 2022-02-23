#!/usr/bin/env python
# coding: utf-8

# <h1>Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Part-1;-Final-Exam-CHEM-3PA3;-Winter-2021" data-toc-modified-id="Part-1;-Final-Exam-CHEM-3PA3;-Winter-2021-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Part 1; Final Exam CHEM 3PA3; Winter 2021</a></span><ul class="toc-item"><li><span><a href="#✍️-Write-the-Time-Dependent-Schrödinger-equation-for-one-particle,-in-three-dimensions,-confined-by-the-time-dependent-potential-$V(x,y,z,t)$." data-toc-modified-id="✍️-Write-the-Time-Dependent-Schrödinger-equation-for-one-particle,-in-three-dimensions,-confined-by-the-time-dependent-potential-$V(x,y,z,t)$.-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>✍️ Write the Time-Dependent Schrödinger equation for one particle, in three dimensions, confined by the time-dependent potential $V(x,y,z,t)$.</a></span></li><li><span><a href="#✍️-Write-the-Time-Independent-Schrödinger-equation-for-a-one-electron-atom-with-atomic-number-$Z$-in-atomic-units." data-toc-modified-id="✍️-Write-the-Time-Independent-Schrödinger-equation-for-a-one-electron-atom-with-atomic-number-$Z$-in-atomic-units.-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>✍️ Write the Time-Independent Schrödinger equation for a one-electron atom with atomic number $Z$ in atomic units.</a></span></li><li><span><a href="#🖩-Compute-properties-of-a-photon-with-wavelength-486.1-nm." data-toc-modified-id="🖩-Compute-properties-of-a-photon-with-wavelength-486.1-nm.-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>🖩 Compute properties of a photon with wavelength 486.1 nm.</a></span></li><li><span><a href="#🧮-How-many-quantum-numbers-are-needed-to-label-the-eigenstates-of-the-following-Hamiltonian:" data-toc-modified-id="🧮-How-many-quantum-numbers-are-needed-to-label-the-eigenstates-of-the-following-Hamiltonian:-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>🧮 How many quantum numbers are needed to label the eigenstates of the following Hamiltonian:</a></span></li><li><span><a href="#🔀Below-is-a-list-of-terms-in-the-molecular-Hamiltonian,-together-with-their-mathematical-expressions." data-toc-modified-id="🔀Below-is-a-list-of-terms-in-the-molecular-Hamiltonian,-together-with-their-mathematical-expressions.-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>🔀Below is a list of terms in the molecular Hamiltonian, together with their mathematical expressions.</a></span></li><li><span><a href="#🔀Below-are-lists-of-different-Hamiltonians-we-considered-in-the-course,-together-with-the-names-of-functions-that-are-related-to-their-solutions." data-toc-modified-id="🔀Below-are-lists-of-different-Hamiltonians-we-considered-in-the-course,-together-with-the-names-of-functions-that-are-related-to-their-solutions.-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>🔀Below are lists of different Hamiltonians we considered in the course, together with the names of functions that are related to their solutions.</a></span></li><li><span><a href="#🖩-What-is-the-zero-point-energy-for-an-electron-confined-to-a-2-dimensional-circular-disk-of-radius-$4-\text{-a.u.}$:" data-toc-modified-id="🖩-What-is-the-zero-point-energy-for-an-electron-confined-to-a-2-dimensional-circular-disk-of-radius-$4-\text{-a.u.}$:-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>🖩 What is the zero-point energy for an electron confined to a 2-dimensional circular disk of radius $4 \text{ a.u.}$:</a></span></li><li><span><a href="#✍️-Write-a-Slater-determinant-for-the-excited-state,-$1\text{s}^2-2\text{s}^1-3\text{s}^1$-configuration-of-the-Beryllium-atom." data-toc-modified-id="✍️-Write-a-Slater-determinant-for-the-excited-state,-$1\text{s}^2-2\text{s}^1-3\text{s}^1$-configuration-of-the-Beryllium-atom.-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>✍️ Write a Slater determinant for the excited-state, $1\text{s}^2 2\text{s}^1 3\text{s}^1$ configuration of the Beryllium atom.</a></span></li><li><span><a href="#🧮-Compute-properties-of-a-${}^{7}\text{F}$-state." data-toc-modified-id="🧮-Compute-properties-of-a-${}^{7}\text{F}$-state.-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>🧮 Compute properties of a ${}^{7}\text{F}$ state.</a></span></li><li><span><a href="#✍️-Solve-the-Schrödinger-equation-for-a-muon,-$\mu^-$,-bound-to-Neon-nucleus." data-toc-modified-id="✍️-Solve-the-Schrödinger-equation-for-a-muon,-$\mu^-$,-bound-to-Neon-nucleus.-1.10"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>✍️ Solve the Schrödinger equation for a muon, $\mu^-$, bound to Neon nucleus.</a></span></li><li><span><a href="#✍️-Write-an-expression-for-the-lowest-energy-molecular-orbital-of-$\text{H}_3^{+2}$." data-toc-modified-id="✍️-Write-an-expression-for-the-lowest-energy-molecular-orbital-of-$\text{H}_3^{+2}$.-1.11"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>✍️ Write an expression for the lowest-energy molecular orbital of $\text{H}_3^{+2}$.</a></span></li><li><span><a href="#The-next-two-questions-refer-to-the-Laplacian-operator." data-toc-modified-id="The-next-two-questions-refer-to-the-Laplacian-operator.-1.12"><span class="toc-item-num">1.12&nbsp;&nbsp;</span>The next two questions refer to the Laplacian operator.</a></span><ul class="toc-item"><li><span><a href="#✍️-Show-that-$\nabla^2$-is-a-linear,-Hermitian-operator." data-toc-modified-id="✍️-Show-that-$\nabla^2$-is-a-linear,-Hermitian-operator.-1.12.1"><span class="toc-item-num">1.12.1&nbsp;&nbsp;</span>✍️ Show that $\nabla^2$ is a linear, Hermitian operator.</a></span></li><li><span><a href="#✍️-Show-that-$\nabla^2$-is-negative-definite." data-toc-modified-id="✍️-Show-that-$\nabla^2$-is-negative-definite.-1.12.2"><span class="toc-item-num">1.12.2&nbsp;&nbsp;</span>✍️ Show that $\nabla^2$ is negative definite.</a></span></li></ul></li><li><span><a href="#Expectation-values-of-$r^k$-and-related-properties-in-Hydrogenic-atoms." data-toc-modified-id="Expectation-values-of-$r^k$-and-related-properties-in-Hydrogenic-atoms.-1.13"><span class="toc-item-num">1.13&nbsp;&nbsp;</span>Expectation values of $r^k$ and related properties in Hydrogenic atoms.</a></span><ul class="toc-item"><li><span><a href="#✍️-Expectation-value-of-$r^{-1}$-for-Hydrogenic-Atoms." data-toc-modified-id="✍️-Expectation-value-of-$r^{-1}$-for-Hydrogenic-Atoms.-1.13.1"><span class="toc-item-num">1.13.1&nbsp;&nbsp;</span>✍️ Expectation value of $r^{-1}$ for Hydrogenic Atoms.</a></span></li><li><span><a href="#🖩-Expectation-value-of-$r^2$-for-a-4f-orbital-in-the-hydrogen-atom." data-toc-modified-id="🖩-Expectation-value-of-$r^2$-for-a-4f-orbital-in-the-hydrogen-atom.-1.13.2"><span class="toc-item-num">1.13.2&nbsp;&nbsp;</span>🖩 Expectation value of $r^2$ for a 4f orbital in the hydrogen atom.</a></span></li><li><span><a href="#🖩-What-is-the-most-probable-distance-to-find-an-electron-from-the-nucleus-in-the-4f-orbital-of-a-hydrogen-atom?" data-toc-modified-id="🖩-What-is-the-most-probable-distance-to-find-an-electron-from-the-nucleus-in-the-4f-orbital-of-a-hydrogen-atom?-1.13.3"><span class="toc-item-num">1.13.3&nbsp;&nbsp;</span>🖩 What is the most probable distance to find an electron from the nucleus in the 4f orbital of a hydrogen atom?</a></span></li><li><span><a href="#🖩-Heisenberg-Uncertainty-Principle" data-toc-modified-id="🖩-Heisenberg-Uncertainty-Principle-1.13.4"><span class="toc-item-num">1.13.4&nbsp;&nbsp;</span>🖩 Heisenberg Uncertainty Principle</a></span></li><li><span><a href="#💰-Bonus:-Derive-an-expression-for-$\sigma_r^2-\sigma_p^2$-for-any-state-of-a-Hydrogenic-atom-with-$l=n-1$." data-toc-modified-id="💰-Bonus:-Derive-an-expression-for-$\sigma_r^2-\sigma_p^2$-for-any-state-of-a-Hydrogenic-atom-with-$l=n-1$.-1.13.5"><span class="toc-item-num">1.13.5&nbsp;&nbsp;</span>💰 Bonus: Derive an expression for $\sigma_r^2 \sigma_p^2$ for <em>any</em> state of a Hydrogenic atom with $l=n-1$.</a></span></li></ul></li><li><span><a href="#Eigenfunctions-and-Eigenvalues-for-a-two-dimensional-Quantum-Dot." data-toc-modified-id="Eigenfunctions-and-Eigenvalues-for-a-two-dimensional-Quantum-Dot.-1.14"><span class="toc-item-num">1.14&nbsp;&nbsp;</span>Eigenfunctions and Eigenvalues for a two-dimensional Quantum Dot.</a></span><ul class="toc-item"><li><span><a href="#✍️-Write-expressions-for-the-eigenvalues-and-eigenfunctions-of-this-system." data-toc-modified-id="✍️-Write-expressions-for-the-eigenvalues-and-eigenfunctions-of-this-system.-1.14.1"><span class="toc-item-num">1.14.1&nbsp;&nbsp;</span>✍️ Write expressions for the eigenvalues and eigenfunctions of this system.</a></span></li><li><span><a href="#🖩-What-is-the-wavelength-that-corresponds-to-the-lowest-energy-excitation-when-$a_x-=-16$,-$a_y-=-9$,-and-$k_z-=-4$?" data-toc-modified-id="🖩-What-is-the-wavelength-that-corresponds-to-the-lowest-energy-excitation-when-$a_x-=-16$,-$a_y-=-9$,-and-$k_z-=-4$?-1.14.2"><span class="toc-item-num">1.14.2&nbsp;&nbsp;</span>🖩 What is the wavelength that corresponds to the lowest-energy excitation when $a_x = 16$, $a_y = 9$, and $k_z = 4$?</a></span></li></ul></li><li><span><a href="#✍️-What-is-the-form-of-the-eigenfunctions-for-the-Kratzer-Fues-Potential" data-toc-modified-id="✍️-What-is-the-form-of-the-eigenfunctions-for-the-Kratzer-Fues-Potential-1.15"><span class="toc-item-num">1.15&nbsp;&nbsp;</span>✍️ What is the form of the eigenfunctions for the Kratzer-Fues Potential</a></span><ul class="toc-item"><li><span><a href="#💰-Bonus:-Write-an-expression-for-the-energy-eigenvalues-and-the-radial-eigenfunctions-of-the-Kratzer-Fues-potential.-This-isn't-100%-trivial,-but-try-to-see-how-far-you-can-get." data-toc-modified-id="💰-Bonus:-Write-an-expression-for-the-energy-eigenvalues-and-the-radial-eigenfunctions-of-the-Kratzer-Fues-potential.-This-isn't-100%-trivial,-but-try-to-see-how-far-you-can-get.-1.15.1"><span class="toc-item-num">1.15.1&nbsp;&nbsp;</span>💰 Bonus: Write an expression for the energy eigenvalues and the radial eigenfunctions of the Kratzer-Fues potential. This isn't 100% trivial, but try to see how far you can get.</a></span></li></ul></li></ul></li></ul></div>

# # Part 1; Final Exam CHEM 3PA3; Winter 2021
# 
# &#x1f468;&#x200d;&#x1f3eb; **Overview:**
# This is Part 1 of 3 Parts of your Final Exam/Project. 
# - Part 1. Questions on the Course Material. (40%)
# - Part 2. Applying the Course material. (40%)
# - Part 3. Discussing your exam and the Course Material. (20%) 
# 
# **You must submit your Jupyter notebooks for Part 1 and Part 2 at least 48 hours prior to your appointment for Part 3.** You will be given your grade on Part 1 and Part 2 before the oral exam, so that you know what your status is. *For late submission of Part 1 and/or Part 2, I will deduct 2 points per hour.
# 
# 
# &#x1f4dc; **Instructions:**
# Answer the following questions. These are worth 40% of your exam, and each question is worth 2 points. (Some questions have multiple parts.) There is also a bonus problem.
# - You can upload files for mathematical answers or type them in Markdown.
# - You can use the notebook as a calculator for numerical problems; but you can also just type in your answer computed offline.
# - You may find these [sheets containing reference data and mathematical formulas/identities](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/ReferenceConstantsConversionsMath.pdf?raw=true) useful.
# - You may also find it useful to know that the [speed of light, in atomic units](https://en.wikipedia.org/wiki/Hartree_atomic_units), is 137.036 a.u..
# 
# 
# &#x1f4d6; **Rules for "Open Book" Exam:**
# **Like all other portions of this exam, this part of the exam is open notes and open library. It is "open internet search" but you (obviously!) can't post questions on an internet discussion board or homework/problem/exam help site. You are not allowed to communicate with your classmates or any other human being (except me) about these questions or your responses, and this includes human beings (singular or plural, known or anonymous) online.**
# 
# 
# &#x2611;&#xfe0f; **Checklist Before Submission:**
# - Make sure you fill in any place that says YOUR CODE HERE or "YOUR ANSWER HERE". 
# - Remove "Not Implemented Error" where appropriate. 
# - **Please put your name, username (the prefix to your @mcmaster.ca e-mail), and student ID number in the cell below.**
# - Before you turn these problems in, make sure everything runs as expected. 
#   - First, restart the kernel (in the menubar, select Kernel → Restart). 
#   - Then run all cells (in the menubar, select Cell → Run All). 
# - Turn in your exam as a Jupyter notebook.
# 
# 

# In[1]:


Name = "First M. Last"
email_user_name = "username"
ID_number = 1234567

# It's useful to import these libraries. 
# You can import others or not even use these, though.
import numpy as np
import scipy
from scipy import constants


# ## &#x270d;&#xfe0f; Write the Time-Dependent Schr&ouml;dinger equation for one particle, in three dimensions, confined by the time-dependent potential $V(x,y,z,t)$. 
# **Note:** Write out the specific Hamiltonian; do not just write $\hat{H}$. Report your answer in the below markdown cell. You can drag-and-drop a photo/screenshot/image of your answer to the cell, but before submitting please confirm that the image is appropriately embedded.

# === BEGIN MARK SCHEME ===
# 
# The time-dependent Schr&ouml;dinger equation is:
# $$
# \hat{H} \Psi(x,y,z,t) = i \hbar \frac{d \Psi(x,y,z,t)}{dt}
# $$
# Substituting in the specific value of the Hamiltonian,
# $$
# \left(-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}-\frac{\hbar^2}{2m}\frac{d^2}{dy^2}-\frac{\hbar^2}{2m}\frac{d^2}{dz^2} + V(x,y,z,t) \right) \Psi(x,y,z,t) = i \hbar \frac{d \Psi(x,y,z,t)}{dt}
# $$
# 
# === END MARK SCHEME ===

# ## &#x270d;&#xfe0f; Write the Time-Independent Schr&ouml;dinger equation for a one-electron atom with atomic number $Z$ in atomic units.
# **Note:** Report your answer in the below Markdown Cell.

# === BEGIN MARK SCHEME ===
# 
# $$
# \left(-\tfrac{1}{2} \nabla^2 - \tfrac{Z}{r} \right)\Psi(r,\theta,\phi) = \Psi(r,\theta,\phi)
# $$
# There are several other ways you could have written this. For example, you could have written out the Laplacian in spherical coordinates or in Cartesian coordinates. For example, 
# $$
# \left(-\frac{1}{2}\frac{d^2}{dx^2} -\frac{1}{2}\frac{d^2}{dy^2}-\frac{1}{2}\frac{d^2}{dz^2}- \frac{Z}{\sqrt{x^2+y^2+z^2}} \right) \Psi(x,y,z) = \Psi(x,y,z)
# $$
# 
# === END MARK SCHEME ===

# ## &#x1F5A9; Compute properties of a photon with wavelength 486.1 nm.
# The photon emitted when a 4p electron in the Hydrogen atom deexcites into a 2s orbital has wavelength 486.1 nm. Compute its
# - frequency in Hz
# - angular frequency in Hz
# - wavenumber, $\bar{\nu}$, in $\text{cm}^{-1}$.
# - angular wavenumber, $k$, in $\text{m}^{-1}$.
# - period in s.
# - momentum in m kg/s
# - energy in Joules.

# In[2]:


# Give your answers as Floats. I have initialized the variables to None.
frequency = None         #Frequency in Hz.
wavenumber = None        #Wavenumber, nu-bar, in cm^-1
momentum = None          #Momentum in SI units.
energy = None            #Energy in SI units.

### BEGIN SOLUTION
# It is helpful to first convert the wavelength into m (SI units)
wavelength_m = 486.1e-9 
#wavelength * frequency = speed of light. So:
frequency = constants.c/wavelength_m

#wavenumber is either 1/wavelength or 2pi/wavelength. In this context we are using nu-bar, which is the former. 
#However, we want it in cm^-1. So
wavelength_cm = 485.1e-7      #Wavelength in cm
wavenumber = (wavelength_cm)**-1

#momentum = h/lambda, where h is Planck's constant. So
momentum = constants.h/wavelength_m

#Energy is h * frequency or h * c / lambda or momentum times c. Using the former,
energy = constants.h * frequency

### END SOLUTION


# In[3]:


print(f"The frequency of a photon with wavelength 486.1 nm is {frequency:.3e} Hz.")
print(f"The wavenumber, nu-bar, of a photon with wavelength  486.1 nm is {wavenumber:.3e} cm^-1.")
print(f"The momentum of a photon with wavelength  486.1 nm is {momentum:.3e} kg m/s.")
print(f"The energy of a photon with wavelength  486.1 nm is {energy:.3e} Joules.")

assert(isinstance(frequency,float)), "Type Error: The frequency should be a float."
assert(isinstance(wavenumber,float)), "Type Error: The wavenumber should be a float."
assert(isinstance(momentum,float)), "Type Error: The momentum should be a float."
assert(isinstance(energy,float)), "Type Error: The energy should be a float."

### BEGIN HIDDEN TESTS
assert(np.isclose(frequency,6.167e14,rtol=1e-3))
assert(np.isclose(wavenumber,2.061e4,rtol=1e-3))
assert(np.isclose(momentum,1.363e-27,rtol=1e-3))
assert(np.isclose(energy,4.086e-19,rtol=1e-3))
### END HIDDEN TESTS


# ## &#x1f9ee; How many quantum numbers are needed to label the eigenstates of the following Hamiltonian:
# $$
# \hat{H} =  -\frac{\hbar^2}{2m}\frac{d^2}{dx_1^2} -\frac{\hbar^2}{2m}\frac{d^2}{dy_1^2}
# -\frac{\hbar^2}{2m}\frac{d^2}{dx_2^2}-\frac{\hbar^2}{2m}\frac{d^2}{dy_2^2}
# + x_1^2 + y_1^2 + x_2^2 + y_2^2
# + e^{-2\left(x_1^2 + y_1^2\right)} + e^{-2\left(x_2^2 + y_2^2\right)} 
# $$

# In[4]:


# Give your answer as an integer. I have initialized the variable to None
number_of_quantum_nos = None

### BEGIN SOLUTION
# There are two uncoupled particles. Each particle has two quantum numbers. This is not clear at first, 
#    perhaps, since it seems like maybe the x and y coordinates are coupled in the last term. However, the 
#    Hamiltonian has the form H(r1,r2,theta1,theta2), because the potential doesn't depend on the angle. So
#    it has circular symmetry and there will be an l (angular momentum) and n (principle) quantum number
#    for each of the two particles. Ergo
number_of_quantum_nos = 4

# I would also accept 6, as there are also spin quantum numbers for each particle.
### END SOLUTION


# In[5]:


print(f'The states of this Hamiltonian are labelled with {number_of_quantum_nos} quantum numbers.')

assert isinstance(number_of_quantum_nos,int), "Type error: The answer should be an integer."

### BEGIN HIDDEN TESTS
assert(number_of_quantum_nos == 4 or number_of_quantum_nos == 6)
### END HIDDEN TESTS


# ## &#x1f500;Below is a list of terms in the molecular Hamiltonian, together with their mathematical expressions. 
# Match the verbal description of the term to its mathematical expression; the mathematical expressions are written in atomic units. Report your answer as a dictionary. The keys and values are:
# 
# **Keys:**
# `electronic kinetic energy`, `nuclear kinetic energy`, `electron-electron repulsion potential`, `nucleus-nucleus repulsion potential`, `electron-nuclear attraction potential`
# 
# **Values**:
# "eq1", "eq2", "eq3", "eq4", and "eq5", where
# 
# `eq1`:  $ \sum_{a=1}^{A-1} \sum_{b=a+1}^A \frac{Z_a Z_b}{\left| \mathbf{x}_a - \mathbf{x}_b \right|} $
# 
# `eq2`:  $\sum_{a=1}^A -\tfrac{1}{2m_a} \nabla^2_{\mathbf{x}_a} $
# 
# `eq3`:  $ \sum_{i=1}^N \sum_{a=1}^A -\frac{Z_a}{\left| \mathbf{r}_i - \mathbf{x}_a \right|} $
# 
# `eq4`:  $\sum_{i=1}^N -\tfrac{1}{2} \nabla^2_{\mathbf{r}_i} $
# 
# `eq5`:  $ \sum_{i=1}^{N-1} \sum_{j=i+1}^N \frac{1}{\left| \mathbf{r}_i - \mathbf{r}_j \right|} $
# 
# 
# For example, the following is an example of an *incorrect* answer with the correct format:
# ```
# hamiltonian_terms = {'electronic kinetic energy':'eq1', 'nuclear kinetic energy':'eq2', 'electron-electron repulsion potential':'eq3', 'nucleus-nucleus repulsion potential':'eq4', 'electron-nuclear attraction potential':'eq5'}
# ```

# In[6]:


# Enter your answer as a dictionary called hamiltonian_terms. 
# The below dictionary has the keys typed in already for you; you need to type in the values eq1, eq2, eq3, eq4, eq5 
#      instead of the place-holder values listed here.
hamiltonian_terms = {'electronic kinetic energy':'eq#', 
                     'nuclear kinetic energy':'eq#', 
                     'electron-electron repulsion potential':'eq#', 
                     'nucleus-nucleus repulsion potential':'eq#', 
                     'electron-nuclear attraction potential':'eq#'}
### BEGIN SOLUTION
hamiltonian_terms = {'electronic kinetic energy':'eq4', 
                     'nuclear kinetic energy':'eq2', 
                     'electron-electron repulsion potential':'eq5', 
                     'nucleus-nucleus repulsion potential':'eq1', 
                     'electron-nuclear attraction potential':'eq3'}
### END SOLUTION


# In[7]:


print(hamiltonian_terms)

assert len(hamiltonian_terms) == 5, "There should be 5 key:value pairs in the hamiltonian_terms dictionary!"

k = ['electron-electron repulsion potential', 'electron-nuclear attraction potential', 
     'electronic kinetic energy', 'nuclear kinetic energy', 'nucleus-nucleus repulsion potential']
v = ['eq1', 'eq2', 'eq3', 'eq4', 'eq5']
assert sorted(hamiltonian_terms.keys()) == k, "At least one key does not match the original dictionary"
assert sorted(hamiltonian_terms.values()) == v, "At least one value does not match the equation labels"

### BEGIN HIDDEN TESTS
hamiltonian_terms_answer = {'electronic kinetic energy': 'eq4', 'nuclear kinetic energy': 'eq2', 
                'electron-electron repulsion potential': 'eq5', 'nucleus-nucleus repulsion potential': 'eq1', 
                'electron-nuclear attraction potential': 'eq3'}
assert(hamiltonian_terms == hamiltonian_terms_answer)
### END HIDDEN TESTS


# ## &#x1f500;Below are lists of different Hamiltonians we considered in the course, together with the names of functions that are related to their solutions. 
# Match each operator with the type of (special) functions that are its eigenfunctions. Report your answer as a dictionary. The keys and values are:
# 
# **Keys:**
# 
# `Ham1`:  $ -\frac{\hbar^2}{2m} \left(\frac{1}{r^2} \frac{d^2}{dr^2} + \frac{1}{r} \frac{d}{dr} - \frac{l^2}{r^2} \right) $
# 
# `Ham2`:  $ - \hbar^2 \left[\frac{1}{\sin \theta}\frac{d}{d\theta}\sin\theta\frac{d}{d\theta} 
# + \frac{1}{\sin^2 \theta} \frac{d^2}{d\phi^2}\right] $
# 
# `Ham3`:  $ -\frac{1}{2} \left( \frac{d^2}{dr^2} + \frac{2}{r} \frac{d}{dr}\right) + \frac{l(l+1)}{2r^2} - \frac{Z}{r} $
# 
# `Ham4`:  $ \frac{d^2}{dx^2} $
# 
# **Values**:
# `associated Laguerre polynomials`, `sines and cosines`, `Bessel functions`, `spherical harmonics`
# 
# For example, the following is an example of an *incorrect* answer with the correct format:
# ```
# eigenfunctions = {'Ham1':'associated Laguerre Polynomials', 'Ham2':'sines and cosines', 'Ham3':'spherical harmonics', 'Ham4':'Bessel functions'}
# ```

# In[8]:


# Enter your answer as a dictionary called hamiltonian_terms. 
# The below dictionary has the values typed in already for you; you need to type in the keys Ham1, Ham2, Ham3, Ham4 
#      instead of the place-holder values listed here.
# eigenfunctions = {'Ham#':'associated Laguerre Polynomials', 
#                   'Ham#':'sines and cosines', 0
#                   'Ham#':'spherical harmonics', 
#                   'Ham#':'Bessel functions'}
### BEGIN SOLUTION
eigenfunctions = {'Ham3':'associated Laguerre Polynomials', 
                  'Ham4':'sines and cosines', 
                  'Ham2':'spherical harmonics', 
                  'Ham1':'Bessel functions'}
### END SOLUTION


# In[9]:


print(eigenfunctions)

assert len(eigenfunctions) == 4, "There should be 4 key:value pairs in the eigenfunctions dictionary!"

v = ['Bessel functions', 'associated Laguerre Polynomials', 'sines and cosines', 'spherical harmonics'] 
k = ['Ham1', 'Ham2', 'Ham3', 'Ham4']
assert sorted(eigenfunctions.keys()) == k, "At least one Hamiltonian label does not match the original dictionary"
assert sorted(eigenfunctions.values()) == v, "At least one special function name does not match the original dictionary"

### BEGIN HIDDEN TESTS
eigenfunctions_answer = {'Ham3':'associated Laguerre Polynomials', 'Ham4':'sines and cosines', 
                         'Ham2':'spherical harmonics', 'Ham1':'Bessel functions'}
assert(eigenfunctions == eigenfunctions_answer)
### END HIDDEN TESTS


# ## &#x1F5A9; What is the zero-point energy for an electron confined to a 2-dimensional circular disk of radius $4 \text{ a.u.}$:
# - in Hartree atomic units? 
# - in kJ/mol (kiloJoules per mole)?

# In[10]:


# You can use the code box as a calculator if you like; either way, report your answer as float(s). 
# I've initialized the answers to None.
zero_pt_E_au = None                  #Energy in Hartree (atomic units)
zero_pt_E_kJperMol = None            #Energy in kJ/mol (SI units)

### BEGIN SOLUTION
# The answer in atomic units can be evaluated directly from the notebook for particles in multi-dimensional systems
# using the widget. After you click the widget, your cursor keys can be used to make fine adjustments to its value.
zero_pt_E_au = .181

# The conversion factor to kJ/mol is 2625.5 kJ/mol per Hartree. So:
zero_pt_E_kJperMol = .181 * 2625.5 
### END SOLUTION


# In[11]:


print(f'The zero-point energy of a electron confined to a disk of radius 4 Bohr is {zero_pt_E_au:.3f} Hartree.')
print(f'The zero-point energy of a electron confined to a disk of radius 4 Bohr is {zero_pt_E_kJperMol:.3f} kJ/mol.')

# basic tests:
assert(isinstance(zero_pt_E_au,float)), "The answer should be an float"
assert(isinstance(zero_pt_E_kJperMol,float)), "The answer should be an integer"

### BEGIN HIDDEN TESTS
assert(np.isclose(zero_pt_E_au,0.181,rtol=1e-2))
assert(np.isclose(zero_pt_E_kJperMol,474.215,rtol=1e-2))
### END HIDDEN TESTS


# ## &#x270d;&#xfe0f; Write a Slater determinant for the excited-state, $1\text{s}^2 2\text{s}^1 3\text{s}^1$ configuration of the Beryllium atom. 
# Assume that the unpaired electrons have the same spin. You may denote the spatial orbitals as $\phi_{1s}(\mathbf{r})$, $\phi_{2s}(\mathbf{r})$ and $\phi_{3s}(\mathbf{r})$.

# === BEGIN MARK SCHEME ===
# 
# $$
# \Psi(\mathbf{r}_1,\mathbf{r}_2,\mathbf{r}_3,\mathbf{r}_4) = \frac{1}{\sqrt{4!}}
# \begin{vmatrix} 
# \phi_{1s}(\mathbf{r}_1)|\alpha(1)\rangle &\phi_{1s}(\mathbf{r}_1)|\beta(1)\rangle & \phi_{2s}(\mathbf{r}_1)|\alpha(1)\rangle & \phi_{3s}(\mathbf{r}_1)|\alpha(1)\rangle \\ 
# \phi_{1s}(\mathbf{r}_2)|\alpha(2)\rangle &\phi_{1s}(\mathbf{r}_2)|\beta(2)\rangle & \phi_{2s}(\mathbf{r}_2)|\alpha(2)\rangle & \phi_{3s}(\mathbf{r}_2)|\alpha(2)\rangle \\ 
# \phi_{1s}(\mathbf{r}_3)|\alpha(3)\rangle &\phi_{1s}(\mathbf{r}_3)|\beta(3)\rangle & \phi_{2s}(\mathbf{r}_3)|\alpha(3)\rangle & \phi_{3s}(\mathbf{r}_3)|\alpha(3)\rangle \\ 
# \phi_{1s}(\mathbf{r}_4)|\alpha(4)\rangle &\phi_{1s}(\mathbf{r}_4)|\beta(4)\rangle & \phi_{2s}(\mathbf{r}_4)|\alpha(4)\rangle & \phi_{3s}(\mathbf{r}_4)|\alpha(4)\rangle 
# \end{vmatrix} 
# $$
# 
# You could also choose the 2s and 3s electrons to have $\beta$ spin.
# 
# === END MARK SCHEME ===

# ## &#x1f9ee; Compute properties of a ${}^{7}\text{F}$ state.
# The ground-state term symbol for Samarium (Sm, atomic number 62) is ${}^{7}\text{F}_0$.
# - How many nominally spatial and spin states are associated with the ${}^{7}\text{F}$ term symbol? Answer with an integer.
# - In addition to J=0, what other J values are possible for the ${}^7{\text{F}}$ term symbol? Answer with a set or list of integers.
# 
# For example, for a triplet P state, we would have 
# ```
# multiplicity_3P = 9
# Jvalues_3P = [0,1,2]
# ```

# In[12]:


# Multiplicity of septuplet F state of Samarium (integer)
multiplity_7F = None   

# J values associated with septuplet F state of Samarium (set or list of integers)
Jvalues_7F = None

### BEGIN SOLUTION
# There are 7 spin states. An F-term corresponds to L=3, with 7 orbital antular momentum states (M_L=-3,-2,-1,0,1,2,3).
multiplicity_7F = 7*7

# Since S = 3 and L = 3, the J values are |L-S|=0, |L-S|+1=1, ..., L+S = 6
Jvalues_7F = [0,1,2,3,4,5,6]
### END SOLUTION


# In[13]:


print(f'A septuplet-F term is {multiplicity_7F}-fold degenerate and has J values {Jvalues_7F}.')
      
assert(isinstance(multiplicity_7F,int)), "The multiplicity should be an integer"
assert(isinstance(Jvalues_7F,set) or isinstance(Jvalues_7F,list) or isinstance(Jvalues_7F,tuple)), "The list of J values should be a list of integers."
assert(len(Jvalues_7F) >= 1)
      
### BEGIN HIDDEN TESTS
assert(multiplicity_7F == 49)
assert(set(Jvalues_7F) == {0,1,2,3,4,5,6})
### END HIDDEN TESTS


# ## &#x270d;&#xfe0f; Solve the Schr&ouml;dinger equation for a muon, $\mu^-$, bound to Neon nucleus.
# In [muonic atoms](https://en.wikipedia.org/wiki/Exotic_atom), a muon replaces an electron. The muon and the electron are both fermions, and they have the same charge. However, the mass of the muon is $207$ times the mass of the electron, $m_\mu = 206.8 m_e$. 
# 
# Assuming the Born-Oppenheimer approximation is valid and that relativistic effects can be neglected, **what are the energy eigenfunctions and eigenvalues for a system composed of one $\mu^-$ bound to a Neon nucleus.** 

# === BEGIN MARK SCHEME ===
# 
# For convenience, I will work in atomic units. The time-independent Schr&ouml;dinger equation, assuming the Born-Oppenheimer approximation, is then:
# $$
# \left(-\frac{1}{2 m_\mu} \nabla^2 - \frac{Z}{r} \right) \Psi(\mathbf{r}) = E\Psi(\mathbf{r})
# $$
# This is very close to the hydrogenic atom. Multiply both sides of the equation by $m_\mu$ to obtain a hydrogenic system,
# 
# $$
# \left(-\frac{1}{2} \nabla^2 -\frac{Z m_\mu}{r} \right) \Psi(\mathbf{r}) = Em_\mu \Psi(\mathbf{r})
# $$
# This is just the Hydrogenic atom, but with the atomic charge replaced by $Z m_\mu$. 
# 
# **Eigenvalues:**
# This means that 
# $$
# E m_\mu = -\frac{(Z m_\mu)^2}{2n^2}
# $$
# and so:
# $$
# E_n = -m_\mu \frac{Z^2}{2n^2} = - \frac{20700}{2n^2} = -\frac{10350}{n^2}
# $$
# In the last line, the atomic number of Neon ($Z=10$) and the mass of the muon ($m_\mu = 207$) were used.
# 
# **Eigenvectors:**
# The eigenvectors are similar; one notices that they should be the same as the normal Hydrogenic eigenvectors, but with $Z$ replaced by $Z m_\mu$. So:
# $$
# \psi_{nlm}(r,\theta,\phi) \propto \left(\frac{2Z m_\mu r}{n}\right)^l L_{n-1-l}^{2l+1}\left(\frac{2Z m_\mu r}{n}\right) e^{-{Z m_\mu r}/{n}}  Y_l^{m} (\theta, \phi)
# $$
# 
# === END MARK SCHEME ===

# ## &#x270d;&#xfe0f; Write an expression for the lowest-energy molecular orbital of $\text{H}_3^{+2}$. 
# You may assume that the system is well-described by the separated-atom limit, and that the Hydrogen atoms are arranged as an equilateral triangle ($\text{D}_{3h}$ symmetry). You do not need to normalize the molecular orbital.

# === BEGIN MARK SCHEME ===
# 
# Because we are near the separated atom limit, the linear combination of atomic orbitals (LCAO) approach
# should be acceptable. So, labeling the Hydrogen atoms as $a$, $b$, and $c$, we have
# $$
# \psi_{\text{H}_3^{+2}}(\mathbf{r}) = c_a \phi_{\text{1s}}^{(a)}(\mathbf{r}) 
# + c_b \phi_{\text{1s}}^{(b)}(\mathbf{r}) 
# + c_c \phi_{\text{1s}}^{(c)}(\mathbf{r})  
# $$
# Because we are in the ground state, there are no nodes. That means that $c_a$, $c_b$, and $c_c$ all have the same sign (they are all positive or all negative. Because we are in a $\text{D}_3h$ geometry, all the hydrogen atoms are equivalent, which means that $c_a = c_b = c_c$. So
# $$
# \psi_{\text{H}_3^{+2}}(\mathbf{r}) = c \phi_{\text{1s}}^{(a)}(\mathbf{r}) 
# + c \phi_{\text{1s}}^{(b)}(\mathbf{r}) 
# + c \phi_{\text{1s}}^{(c)}(\mathbf{r})  
# $$
# 
# === END MARK SCHEME ===

# ## The next two questions refer to the Laplacian operator.
# In this question you will show, mathematically, that two properties of the Laplacian operator are true. It is OK (but not essential) to assume that you are interested in the Laplacian operator in 1 dimension, $\nabla^2 = \frac{d^2}{dx^2}$. 
# Note: You may assume that the wavefunction, and its first first and second derivatives, vanish at the ends of the region of integration. However, there are also ways to answer these questions without explicitly invoking those assumptions.
# 
# ### &#x270d;&#xfe0f; Show that $\nabla^2$ is a linear, Hermitian operator.

# === BEGIN MARK SCHEME ===
# 
# Both parts of this question were taken from an old exam.
# 
# To show that $\nabla^2$ is linear, we need only recall that it is the second derivative operator. We know that differentiation is a linear operator. I.e., differentiation of a constant times a function is equal to a constant, times the value obtained by differentiating the function. Similarly, differentiation of a sum of functions is equal to summing the derivatives of the functions. Mathematically,
# $$
# \frac{d^k}{dx^k} \text{constant} \cdot f(x) = \text{constant} \cdot\frac{d^kf}{dx^k} 
# $$
# and
# $$
# \frac{d^k\left(f(x) + g(x) \right)}{dx^k} = \frac{d^kf(x)}{dx^k} + \frac{d^kg(x)}{dx^k}
# $$
# So $\nabla^2$ is linear.
# 
# One can show that $\nabla^2$ is Hermitian using integration by parts, similar to how we did in the course notes. You can also recognize that the Hermitian property follows directly from [Green's second identity](https://en.wikipedia.org/wiki/Green%27s_identities#Green's_second_identity) . (In both cases you use the fact that the wavefunction and its derivatives vanish at the end of the interval of integration.)
# 
# However, we also know that $\nabla^2$ is closely related to the momentum operator. 
# $$
# \hat{p}^2 = -i \hbar \nabla \cdot -i \hbar \nabla = - \hbar^2 \nabla^2
# $$
# In atomic units, then, $\nabla^2 = - \hat{p}^2$. The following math uses the fact that the momentum operator is Hermitian. 
# 
# We need to show that 
# $$
# \int \Phi(x)^* \nabla^2 \Psi(x) dx = \int \left( \nabla^2 \Phi(x) \right)^* \Psi(x) dx 
# $$
# To this end, we start with the relationship between the Laplacian and the momentum operator, then (repeatedly) invoke the fact the momentum operator is Hermitian. So:
# \begin{align}
# \int \Phi(x)^* \nabla^2 \Psi(x) dx &=\int \Phi(x)^* -\hat{p}^2 \Psi(x) dx \\
# &=-\int \Phi(x)^* \hat{p}\hat{p} \Psi(x) dx \\
# &=-\int \left(\hat{p}\Phi(x)\right)^* \hat{p} \Psi(x) dx \\
# &=-\int \left(\hat{p}\hat{p}\Phi(x)\right)^* \Psi(x) dx \\
# &=\int \left(-\hat{p}^2\Phi(x)\right)^* \Psi(x) dx \\
# &=\int \left(\nabla^2\Phi(x)\right)^* \Psi(x) dx
# \end{align}
# === END MARK SCHEME ===

# ### &#x270d;&#xfe0f; Show that $\nabla^2$ is negative definite. 
# That is, show that for *any* $\Psi(\mathbf{r})$, it is *always* true that 
# $$
# \langle \Psi | \nabla^2 | \Psi \rangle < 0
# $$

# === BEGIN MARK SCHEME ===
# 
# One can show that $\nabla^2$ is negative-definite using [Green's first identity](https://en.wikipedia.org/wiki/Green%27s_identities#Green's_first_identity) or integration by parts. However, as with the first part of this problem, one can also directly invoke the connection to the momentum operator, $\nabla^2 = - \hat{p}^2$. Since the square of an operator is positive definite, it's clear that the negative of the operator is negative definite. However, more explicitly, one can write:
# \begin{align}
# \int \Psi(x)^* \nabla^2 \Psi(x) dx &=\int \Psi(x)^* -\hat{p}^2 \Psi(x) dx \\
# &=-\int \Psi(x)^* \hat{p}\hat{p} \Psi(x) dx \\
# &=-\int \left(\hat{p}\Psi(x)\right)^* \hat{p} \Psi(x) dx \\
# &=-\int \left|\hat{p}\Psi(x)\right|^2 dx \\
# &<0
# \end{align}
# 
# 
# 
# 
# === END MARK SCHEME ===

# ## Expectation values of $r^k$ and related properties in Hydrogenic atoms.
# The goal of this problem is to explore the radial distribution function and its expectation values for hydrogenic atoms. A key integral that will be useful is
# $$
# \int_0^{\infty} r^n e^{-\beta r} dr = \frac{n!}{\beta^{n+1}}
# $$
# 
# It is also useful to know [Kramer's recursion relation](https://phlconnect.ched.gov.ph/admin/uploads/81dc9bdb52d04dc20036dbd8313ed055/53-hydrogen-4.pdf) for radial expectation values. If $\psi_{nlm}(r,\theta,\phi)$ denotes a normalized hydrogenic wavefunction, then Kramer's recursion states that:
# $$
# \langle \psi_{nlm} | r^k | \psi_{nlm} \rangle = a_{n}(k,Z) \langle \psi_{nlm} | r^{k-1} | \psi_{nlm} \rangle + b_{nl}(k,Z) \langle \psi_{nlm} | r^{k-2} | \psi_{nlm} \rangle
# $$
# where
# 
# \begin{align}
# a_{n}(k,Z) &=  \frac{n^2(2k+1)}{(k+1)Z}\\
# b_{nl}(k,Z) &= \frac{n^2 k \left(k^2 - (2l+1)^2\right)}{4Z^2(k+1)}
# \end{align}
# A detailed derivation of this relation can be found [here](http://www.blazartheory.com/files/notes/qmnotes/Kramers__Relation.pdf). You will not *need* to use this relation in this problem; it's a matter of preference whether you use this relation or perform integrals.
# 
# Throughout this problem you may use atomic units.

# ### &#x270d;&#xfe0f; Expectation value of $r^{-1}$ for Hydrogenic Atoms.
# What is the expectation value of $r^{-1}$ for a Hydrogenic atom. That is, what is the expectation value of 
# $$
# \langle \psi_{nlm} | r^{-1} | \psi_{nlm} \rangle
# $$
# for an electron bound to a nuclear of charge Z. *Report your answer as a float, in atomic units.*

# === BEGIN MARK SCHEME ===
# 
# The problems in this question are (at most) small revisions to problems from old exams posted on the web site. 
# 
# This first question is most easily solved using the Hellmann-Feynman theorem. Note that for a Hydrogenic atom,
# $$
# \frac{d\hat{H}}{dZ} = -\frac{1}{r}
# $$
# Furthermore,
# $$
# \frac{dE}{dZ} = \frac{d}{dZ} \frac{-Z^2}{2n^2} = -\frac{Z}{n^2}
# $$
# So, 
# $$
# \int \psi_{nlm}(\mathbf{r})^* \left[ \frac{1}{r}\right] \psi_{nlm}(\mathbf{r}) d \mathbf{r} = \int \psi_{nlm}(\mathbf{r})^* \left[-\frac{dH}{dZ} \right]\psi_{nlm}(\mathbf{r}) d \mathbf{r} = - \frac{dE}{dZ} = \frac{Z}{n^2}
# $$
# In the next-to-last equality we used the Hellmann-Feynman theorem.
# 
# === END MARK SCHEME ===

# ### &#x1F5A9; Expectation value of $r^2$ for a 4f orbital in the hydrogen atom.
# What is the expectation value of $r^2$ for the 4f orbital in the hydrogen atom (Z=1). That is, what is the expectation value of 
# $$
# \langle \psi_{43m} | r^2 | \psi_{43m} \rangle
# $$
# in the Hydrogen atom? *Report your answer as a float, in atomic units.*
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[14]:


# Expectation value of r^2 for a 4f orbital in the hydrogen atom (Z=1) in atomic units (Bohr^2). 
# I have initialized the variable to None. Give your answer in atomic units (Bohr).
avg_r2 = None    

### BEGIN SOLUTION
avg_r2 = 360   #See below for explanation.    
### END SOLUTION


# In[15]:


print(f'The expectation value of r^2 for an electron in the 4f orbital of the hydrogen atom is {avg_r2:.2f} Bohr^2.')

### BEGIN HIDDEN TESTS
assert(np.isclose(avg_r2,360.,rtol=1e-2))
### END HIDDEN TESTS


# You can use this markdown cell to (optionally) describe how you obtained your answer.
# 
# === BEGIN MARK SCHEME ===
# This problem could be done numerically, or using the Kramer's recursion, or by explicit integration. The key step to doing it with Kramer's relation is to note that because the hydrogenic wavefunctions are normalized,
# $$
# \langle \psi_{nlm} |r^0| \psi_{nlm} \rangle = \langle \psi_{nlm} | \psi_{nlm} \rangle = 1
# $$
# This means that you have the results for $k=-1$ (from the previous part of this problem) and $k=0$ (from normalization). So you can deduce expressions for k=1 
# \begin{align}
# \langle \psi_{nlm} |r| \psi_{nlm} \rangle &= \frac{3\cdot4^2}{2} \langle r^0 \rangle + \frac{4^2(1-7^2)}{8} \langle r^{-1} \rangle \\
# &= 24 - 6 = 18 \text{ Bohr}
# \end{align}
# \begin{align}
# \langle \psi_{nlm} |r^2| \psi_{nlm} \rangle &= \frac{5\cdot4^2}{3} \langle r^1 \rangle + \frac{32(4-7^2)}{12} \langle r^{0} \rangle \\
# &= 360 \text{ Bohr}^2
# \end{align}
# 
# I will show how to do it with explicit integration. The key is to remember that the spherical harmonics are orthonormal,
# $$
# \int_0^\pi \int_0^{2 \pi} Y_l^m(\theta,\phi)^* Y_{l'}^{m'}(\theta,\phi) \sin \theta d\phi d\theta = \delta_{l l'} \delta_{m m'}
# $$
# We also need to remember that for $l=n-1$, the radial wavefunction is proportional to $r^l e^{-Zr/n}$. So for these cases, we have:
# \begin{align}
# \langle \psi_{n,n-1,m} | r^k | \psi_{n,n-1,m} \rangle 
# &= \frac{\int_0^{\infty} \int_0^\pi \int_0^{2 \pi} r^{n-1} e^{-Zr/n} Y_{n-1}^m(\theta,\phi)^*\left[r^k \right] r^{n-1} e^{-Zr/n}Y_{n-1}^{m}(\theta,\phi) r^2\sin \theta d\phi d\theta dr}{\int_0^{\infty} \int_0^\pi \int_0^{2 \pi} r^{n-1} e^{-Zr/n} Y_{n-1}^m(\theta,\phi)^* r^{n-1} e^{-Zr/n}Y_{n-1}^{m}(\theta,\phi) r^2\sin \theta d\phi d\theta dr} \\
# &= \frac{\int_0^{\infty} r^{2n+k}e^{-2Zr/n} dr}{\int_0^{\infty} r^{2n}e^{-2Zr/n}dr} \\
# &= \frac{(2n+k)!\left(\tfrac{2Z}{n}\right)^{2n+1}}{(2n)!\left(\tfrac{2Z}{n}\right)^{2n+k+1}} \\
# &= \frac{n^k(2n+k)(2n+k-1)\cdots(2n+1)}{2^kZ^k}
# \end{align}
# Therefore we have that
# $$
# \langle \psi_{4,3,m} | r | \psi_{4,3,m} \rangle = 18 \text{ Bohr}
# $$
# $$
# \langle \psi_{4,3,m} | r^2 | \psi_{4,3,m} \rangle = 360 \text{ Bohr}^2
# $$
# 
# === END MARK SCHEME ===

# ### &#x1F5A9; What is the most probable distance to find an electron from the nucleus in the 4f orbital of a hydrogen atom?
# Report your answer in Bohr (atomic units).
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[16]:


# Most probable distance at which to observe an electron in the 4f orbital from the nucleus of the hydrogen atom.
# I have initialized the variable to None. Give your answer in atomic units (Bohr).
dist_mostprob = None    

### BEGIN SOLUTION
dist_mostprob = 16   #See below for explanation.    
### END SOLUTION


# In[17]:


print(f'The most probable value of the distance from the nucleus for a 4f electron in Hydrogen is {dist_mostprob:.2f} Bohr.')

### BEGIN HIDDEN TESTS
assert(np.isclose(dist_mostprob,16,rtol=1e-2))
### END HIDDEN TESTS


# You can use this markdown cell to (optionally) describe how you obtained your answer.
# 
# === BEGIN MARK SCHEME ===
# This problem could be done numerically, but I'll show the analytic solution. The key is to understand that the eigenfunction of the 4f orbital, and any orbital that has $l=n-1$, is simply
# $$
# psi_{n,n-1,m}(r, \theta, \phi) \propto r^{n-1} e^{-Zr/n} Y_{n-1}^{m}(\theta,\phi)
# $$
# and the probability of observing a particle at r units from the nucleus at *some* value of $(\theta,\phi)$ requires integration over $d\theta d\phi$. So, using $p(r_0)$ to denote the probability of observing a particle $r_0$ units from the nucleus,
# $$
# p(r_0) \propto \int_0^{\infty} \int_0^\pi \int_0^{2 \pi} r^{n-1} e^{-Zr/n} Y_{n-1}^m(\theta,\phi)^*\left[\delta(r-r_0) \right] r^{n-1} e^{-Zr/n}Y_{n-1}^{m}(\theta,\phi) r^2\sin \theta d\phi d\theta dr
# $$
# or simply
# $$
# p(r) \propto r^{2n} e^{-2Zr/n}
# $$
# We could have inferred this without all the mathematics by merely noting that the surface area of a sphere is proportional to $r^2$, so the probability of observing an electron on a spherical shell of radius $r$ is r^2 times the radial wavefuncton squared.
# 
# To find the most-probable distance, we need to differentiate this equation and set the derivative equal to zero. So
# $$
# 0 = \frac{dp}{dr} = (2n)r^{2n-1}e^{-2Zr/n} + r^{2n} \left( \tfrac{-2Z}{n} \right) e^{-2Zr/n} = \left(2n - \tfrac{-2Z}{n}r \right)r^{2n-1} e^{-2Zr/n}
# $$
# So,
# $$
# r_{\text{most probable}} = \frac{n^2}{Z}
# $$
# For the 4f (n=4) orbital of Hydrogen (Z=1), this is just 16.
# 
# === END MARK SCHEME ===

# ### &#x1F5A9; Heisenberg Uncertainty Principle 
# The Heisenberg Uncertainty Principle between momentum and position in 3 dimensions states that 
# $$
# \sigma_r^2 \sigma_p^2 \ge  \tfrac{3}{4} \hbar^2
# $$
# where
# $$
# \sigma_r^2 = \langle \psi_{n,n-1,m} | r^2 | \psi_{n,n-1,m} \rangle - \langle \psi_{n,n-1,m} | r | \psi_{n,n-1,m} \rangle^2 \\
# \sigma_p^2 = \langle \psi_{n,n-1,m} | \hat{p}^2 | \psi_{n,n-1,m} \rangle - \langle \psi_{n,n-1,m} | \hat{p} | \psi_{n,n-1,m} \rangle^2
# $$
# To reassure yourself that this is true, compute $\sigma_r^2 \sigma_p^2$ for the 4f state of the hydrogen atom. *Report your answer as a float, in atomic units.*
# 
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[18]:


# Write the left-hand-side of the Heisenberg Uncertainty relation, which should be bigger than 3/2 hbar.
# Give your answer in atomic units.
test_Heisenberg = None    

### BEGIN SOLUTION
test_Heisenberg = 2.25   #See below for explanation.    
### END SOLUTION


# In[19]:


print(f'The product of the variance in position and momentum for an electron in the 4f orbital of Hydrogen is {test_Heisenberg:.2f} times hbar.')
assert(test_Heisenberg >= 0.75), "The Heisenberg Uncertainty Principle has been violated!"

### BEGIN HIDDEN TESTS
assert(np.isclose(test_Heisenberg,2.25,rtol=1e-2))
### END HIDDEN TESTS


# You can use this markdown cell to (optionally) explain how you obtained your answer.
# 
# === BEGIN MARK SCHEME
# 
# Like the previous questions in this problem, this question was taken off a recent exam. We have already computed the first part of what we need, which is (see the question before last)
# $$
# \sigma_r^2 = 360 - 18^2 = 36 \text{ Bohr}^2
# $$
# We also know that because the hydrogen atom is in its 4f stationary state, there is no *net* motion of the electrons, so $\langle \hat{p} \rangle = 0$. We realize that the kinetic energy of the Hydrogen atom, in atomic units, is $\langle \hat{p}^2/2 \rangle$, so 
# $$
# \sigma_p^2 = \langle \hat{p}^2 \rangle = 2 [\text{kinetic energy}]
# $$
# The kinetic energy can be inferred in several different ways. For example, we could deduce it from the Hellmann-Feynman theorem, by differentiated the energy with respect to $\hbar$. However, in the first part of this question, we learned that 
# $\langle r^{-1} \rangle = \tfrac{Z}{n^2}$, which implies that the potential energy for the Hydrogen atom is $\langle -Zr^{-1} \rangle = -\tfrac{Z^2}{n^2}$. Now
# $$
# E = \text{kinetic energy + potential energy}
# $$
# and we know now that 
# $$
# -\frac{Z^2}{2n^2} = \langle \hat{T} \rangle + -\frac{Z^2}{n^2}
# $$
# So
# $$
# \langle \hat{T} \rangle = \frac{Z^2}{2n^2}
# $$
# and
# $$
# \sigma_p^2 = \langle \hat{p}^2 \rangle = 2\langle \hat{T} \rangle = \frac{Z^2}{n^2}
# $$
# So, for an electron in the 4f (n=4) orbital of Hydrogen (Z=1), 
# $$
# \sigma_r^2 \sigma_p^2 = 36 \cdot \tfrac{1}{16} = \tfrac{9}{4} = 2.25 > \frac{3}{4}
# $$
# 
# === END MARK SCHEME
# 

# ### &#x1f4b0; Bonus: Derive an expression for $\sigma_r^2 \sigma_p^2$ for *any* state of a Hydrogenic atom with $l=n-1$. 

# === BEGIN MARK SCHEME ===
# 
# Almost everything you need to do for this problem is already done. From three problems ago,
# $$
# \langle \psi_{n,n-1,m} | r^k | \psi_{n,n-1,m} \rangle = \frac{n^k(2n+k)(2n+k-1)\cdots(2n+1)}{2^kZ^k}
# $$
# and specifically, 
# $$
# \langle \psi_{n,n-1,m} | r^2 | \psi_{n,n-1,m} \rangle = \frac{n^2(2n+2)(2n+1)}{4Z^2}
# \langle \psi_{n,n-1,m} | r | \psi_{n,n-1,m} \rangle = \frac{n(2n+1)}{2Z}
# $$
# So
# $$
# \sigma_r^2 = \frac{n^2(2n+2)(2n+1)}{4Z^2} -  \frac{n^2(2n+1)^2}{4Z^2} = \frac{n^2(2n+1)}{4Z^2}
# $$
# From the previous problem
# $$
# \sigma_p^2 = \frac{Z^2}{n^2}
# $$
# So
# $$
# \sigma_r^2 \sigma_p^2 = \frac{2n+1}{4} \ge \frac{3}{4}
# $$
# In the ground state ($n=1$), one is just at the threshhold of violating the uncertainty principle; as $n$ increases the mutual uncertainty in momentum and position increases.
# 
# === END MARK SCHEME ===

# ## Eigenfunctions and Eigenvalues for a two-dimensional Quantum Dot.
# Modern displays often use quantum dot technology, where one (or more) electrons are confined to a region within a material. For an electron confined to a rectangular region in two dimensions, it is reasonable to approximate its motion perpendicular to the rectangle with harmonic confinement. The time-independent Schr&ouml;dinger equation, eigenfunctions, and eigenvalues for a harmonically confined electron are, in atomic units:
# $$
# \left(-\tfrac{1}{2}\tfrac{d^2}{dz^2} + \tfrac{1}{2}\kappa z^2\right) \psi_k(z) = E_k \psi_k(z)
# $$
# where the eigenenergies are
# $$
# E_k = \sqrt{\kappa}\left(k+\tfrac{1}{2}\right) \qquad \qquad k=0,1,2,\ldots
# $$
# and the eigenfunctions are given in terms of the [Hermite polynomials](https://en.wikipedia.org/wiki/Hermite_polynomials), $H_k(z)$, as:
# $$
# \psi_k^{(\text{harm. osc.})}(z) =\frac{1}{2^k k!}\sqrt[4]{\frac{\kappa}{\pi}}
# e^{-\sqrt{\kappa}z^2/2}H_k\left(\sqrt[4]{\kappa}z\right)
# $$
# The Hamiltonian for an electron confined to a rectangular region, in atomic units, is then:
# $$
# \hat{H} = -\frac{1}{2} \frac{d^2}{dx^2} -\frac{1}{2} \frac{d^2}{dy^2} -\frac{1}{2} \frac{d^2}{dz^2} 
#  + V_{a_x}(x) + V_{a_y}(y) + \frac{1}{2} \kappa z^2
# $$
# where
# $$
# V_a(x) = 
# \begin{cases}
#     +\infty & x\leq 0\\
#     0       & 0\lt x \lt a\\
#     +\infty & a \leq x
# \end{cases}
# $$
# 
# ### &#x270d;&#xfe0f; Write expressions for the eigenvalues and eigenfunctions of this system.
# 

# === BEGIN MARK SCHEME
# 
# This system is a sum of three Hamiltonians, two of which are 1-dimensional particles-in-a-box and one of which is a 1-dimensional Harmonic Oscillator. 
# $$
# \hat{H} = \hat{H}_x + \hat{H}_y + \hat{H}_z
# $$
# with
# $$
# \hat{H}_x = -\frac{1}{2} \frac{d^2}{dx^2} + V_{a_x}(x) \\
# \hat{H}_y = -\frac{1}{2} \frac{d^2}{dy^2} + V_{a_y}(y) \\
# \hat{H}_z = -\frac{1}{2} \frac{d^2}{dz^2} + \frac{1}{2} \kappa z^2
# $$
# By separation of variables, the eigenenergies are the sums of the eigenenergies of the components' energies which, using the formula for the energies of the particle-in-a-box in atomic units, gives
# $$
# E_{n_x,n_y,k} = \frac{n_x^2 \pi^2}{2a_x^2} + \frac{n_y^2 \pi^2}{2a_y^2} + \sqrt{\kappa}\left(k+\tfrac{1}{2}\right) \qquad n_x,n_y = 1,2,\ldots \quad k=0,1,\ldots
# $$
# and the eigenfunctions are the products of the individual components' eigenfunctions
# $$
# \psi_{n_x,n_y,k}(x,y,z) = \frac{2}{\sqrt{a_x a_y}} \sin\left(\frac{n_x \pi x}{a_x}\right) \sin\left(\frac{n_y \pi y} {a_y}\right) \cdot\frac{1}{2^k k!}\sqrt[4]{\frac{\kappa}{\pi}}
# e^{-\sqrt{\kappa}z^2/2}H_k\left(\sqrt[4]{\kappa}z\right)
# $$
# 
# === END MARK SCHEME

# ###  &#x1F5A9; What is the wavelength that corresponds to the lowest-energy excitation when $a_x = 16$, $a_y = 9$, and $k_z = 4$?
# Report your answer in nm. 
# 
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[20]:


# Report the wavelength of the lowest-energy excitation in nm. I have initialized the variable to None.
wavelength_qdot_nm = None

### BEGIN SOLUTION
# The energy of excitation is
excitation_energy = (4 - 1) * np.pi**2 / (2 * 16**2) 
# The wavelength in atomic units is thus
wavelength_qdot_au = 2 * np.pi * 137.036 / excitation_energy
# The wavelength in nanometers is, finally
wavelength_qdot_nm = wavelength_qdot_au * 0.0529177 
### END SOLUTION


# In[21]:


print(f'The wavelength associated with the lowest-energy excitation of the specified quantum dot is {wavelength_qdot_nm:.1f} nm.')

### BEGIN HIDDEN TESTS
assert(np.isclose(wavelength_qdot_nm,787.9,rtol=1e-3))
### END HIDDEN TESTS


# You can use this markdown cell to (optionally) explain your answer
# 
# === BEGIN MARK SCHEME
# 
# The ground state energy is easily determined for this system. The question is what the lowest excited state will be. It will correspond to an excitation in the $x$, $y$, or $z$ direction. The box in the $x$ direction is larger, which means its energy levels are more closely spaced. So the excitation will be in either the $x$ or $z$ direction. We should check. The excitations corresponding to the possibilities are
# $$
# E_x^{(1\rightarrow2)} = \frac{(4-1)\pi^2}{512} = .0578 \\
# E_y^{(1\rightarrow2)} = \frac{(4-1)\pi^2}{162} = .1828 \\
# E_z^{0\rightarrow1} = (1-0)\sqrt{4} = 2
# $$
# So the lowest-energy excitation occurs in the $x$ direction, which is intuitive given the nature of the system being described. 
# 
# The excitation energy of 0.0578 can be converged into wavelength in several different ways. The easiest is to recall that the speed of light in atomic units is 137.036. So from
# $$
# E = \frac{hc}{\lambda} = \frac{2 \pi \hbar c}{\lambda} 
# $$
# we have, in atomic units, that
# $$
# \lambda = \frac{2 \pi 137.036}{E} = \frac{2\cdot512 \pi 137.036}{3 \pi^2} = \frac{1024 \cdot 137.036}{3 \pi} = 14889 a.u.
# $$
# To convert this from Bohr to nanometers, we use the fact that 1 Bohr = 0.0529177 nm. So 
# $$
# \lambda = 787.9 nm
# $$
# 
# === END MARK SCHEME

# ## &#x270d;&#xfe0f; What is the form of the eigenfunctions for the Kratzer-Fues Potential
# The Kratzer-Fues potential is a reasonable model for a diatomic molecule rotating and vibrating in 3 dimensions, or even a ion-pair complex (e.g., an single ion pair from an ionic solvent in the gas phase). It has the form
# $$
# V_{\text{Kratzer-Fues}}(r) = \frac{a}{r^2} - \frac{b}{r} \qquad \qquad a>0 \text{ and } b>0
# $$
# and so the Schr&ouml;dinger equation has the form:
# $$
# \left(-\frac{\hbar^2}{2m}\nabla^2 +\frac{a}{r^2} - \frac{b}{r} \right) \psi(\mathbf{r}) = E\psi(\mathbf{r}) 
# $$
# Using separation of variables, write the *form* of the solutions for the Kratzer-Fues potential. What is the radial Schr&ouml;dinger equation for this system?

# === BEGIN MARK SCHEME ===
# 
# This is a spherically-symmetric Schr&ouml;dinger equation in 3 dimensions. This means that the solution is  the product of a radial part and a spherical harmonic,
# $$
# \psi_{nlm_l}(r,\theta,\phi) = R_{nl}(r) Y_l^{m_l} (\theta,\phi)
# $$
# and the radial wavefunction, $R_{nl}(r)$ satisfies the radial Schr&ouml;dinger equation for a 3-dimensional system,
# $$
# \left(-\frac{\hbar^2}{2m} \left( \frac{d^2}{dr^2}
# + \frac{2}{r} \frac{d}{dr}\right) 
#       + \frac{\hbar^2 l(l+1)}{2mr^2} + \frac{a}{r^2} - \frac{b}{r} \right)
#       R_{n,l}(r) 
# = E_{n,l}R_{n,l}(r)
# $$
# or, simplifying slightly,
# $$
# \left(-\frac{\hbar^2}{2m} \left( \frac{d^2}{dr^2}
# + \frac{2}{r} \frac{d}{dr}\right) 
#       + \frac{\hbar^2 l(l+1) + 2ma}{2mr^2} - \frac{b}{r} \right)
#       R_{n,l}(r) 
# = E_{n,l}R_{n,l}(r)
# $$
# 
# === END MARK SCHEME ===

# ### &#x1f4b0; Bonus: Write an expression for the energy eigenvalues and the radial eigenfunctions of the Kratzer-Fues potential. This isn't 100% trivial, but try to see how far you can get.
# 

# === BEGIN MARK SCHEME
# 
# Notice that the radial Hamiltonian for the Kratzer-Fues potential looks *a lot* like the Hydrogenic atom, which has the Hamiltonian,
# $$
# \left(-\frac{1}{2} \left( \frac{d^2}{dr^2}
# + \frac{2}{r} \frac{d}{dr}\right) 
#       + \frac{l(l+1)}{2r^2} - \frac{Z}{r} \right)
#       R_{n,l}(r) 
# = E_{n,l}R_{n,l}(r)
# $$
# Returning to the Kratzer-Fues case, if one uses atomic units multiplies both sides of the equation by $m$, then
# $$
# \left(-\frac{1}{2} \left( \frac{d^2}{dr^2}
# + \frac{2}{r} \frac{d}{dr}\right) 
#       + \frac{l(l+1) + 2ma}{2r^2} - \frac{bm}{r} \right)
#       R_{n,l}(r) 
# = \left(mE_{n,l}\right)R_{n,l}(r)
# $$
# If you then defined a value, $l'$, such that
# $$
# l'(l'+1) = l(l+1) + 2ma
# $$
# the solutions would be Hydrogenic, 
# $$
# E_{\text{Kratzer-Fues},n} = -\frac{mb^2}{2n^2}
# $$
# and
# $$
# R_{n,l}(r) \propto \left( \frac{2mbr}{n} \right)^{l'} L_{n-1-l'}^{2l'+1}\left(\frac{2mbr}{n}\right) e^{-\frac{mbr}{n}}
# $$
# This treatment is a bit naive, insofar as there is no guarantee that l' is an integer, so defining the associated Laguerre polynomial of a non-integer degree may be required. Such a polynomial can be defined by generalizing the associated Laguerre functions to noninteger degree using hypergeometric functions. However, that's further than I wished to go.
# 
# In practice, this solution is not quite right except for the exceptional cases where $l'$ is an integer less than $n$. But this is the *idea* of the solution, which is all that is really important for this bonus. The exact solution can be found various places, see, [for example](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.741.7716&rep=rep1&type=pdf). The detailed solution can be found at in 
# > S. Flügge *Practical Quantum Mechanics* (Berlin:Springer, 1957)
# 
# === END MARK SCHEME
