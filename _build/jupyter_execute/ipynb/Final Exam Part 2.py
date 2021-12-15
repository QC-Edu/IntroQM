#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Part-2:-Final-Exam-3PA3;-Winter-2021:-The-Harmonic-Oscillator" data-toc-modified-id="Part-2:-Final-Exam-3PA3;-Winter-2021:-The-Harmonic-Oscillator-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Part 2: Final Exam 3PA3; Winter 2021: The Harmonic Oscillator</a></span><ul class="toc-item"><li><span><a href="#The-1-dimensional-Harmonic-Oscillator" data-toc-modified-id="The-1-dimensional-Harmonic-Oscillator-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>The 1-dimensional Harmonic Oscillator</a></span><ul class="toc-item"><li><span><a href="#Motivation:-Nuclear-Schrödinger-Equation-for-a-Diatomic-Molecule" data-toc-modified-id="Motivation:-Nuclear-Schrödinger-Equation-for-a-Diatomic-Molecule-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Motivation: Nuclear Schrödinger Equation for a Diatomic Molecule</a></span></li><li><span><a href="#Quadratic-Approximation-to-the-Potential-Energy-Curve-and-the-Rigid-Rotor-Approximation" data-toc-modified-id="Quadratic-Approximation-to-the-Potential-Energy-Curve-and-the-Rigid-Rotor-Approximation-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Quadratic Approximation to the Potential Energy Curve and the Rigid Rotor Approximation</a></span></li><li><span><a href="#🖩-Exercise:-Isotope-Effects-in-Rotational-Spectroscopy-(8-pts.)" data-toc-modified-id="🖩-Exercise:-Isotope-Effects-in-Rotational-Spectroscopy-(8-pts.)-2.1.3"><span class="toc-item-num">2.1.3&nbsp;&nbsp;</span>🖩 Exercise: Isotope Effects in Rotational Spectroscopy (8 pts.)</a></span></li><li><span><a href="#The-Harmonic-Oscillator-Hamiltonian" data-toc-modified-id="The-Harmonic-Oscillator-Hamiltonian-2.1.4"><span class="toc-item-num">2.1.4&nbsp;&nbsp;</span>The Harmonic Oscillator Hamiltonian</a></span></li><li><span><a href="#Solutions-to-the-Harmonic-Oscillator-Hamiltonian" data-toc-modified-id="Solutions-to-the-Harmonic-Oscillator-Hamiltonian-2.1.5"><span class="toc-item-num">2.1.5&nbsp;&nbsp;</span>Solutions to the Harmonic Oscillator Hamiltonian</a></span></li><li><span><a href="#🖩-Isotope-Effects-in-Vibrational-Spectroscopy-(8-pts)" data-toc-modified-id="🖩-Isotope-Effects-in-Vibrational-Spectroscopy-(8-pts)-2.1.6"><span class="toc-item-num">2.1.6&nbsp;&nbsp;</span>🖩 Isotope Effects in Vibrational Spectroscopy (8 pts)</a></span></li></ul></li><li><span><a href="#The-Morse-Oscillator" data-toc-modified-id="The-Morse-Oscillator-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>The Morse Oscillator</a></span><ul class="toc-item"><li><span><a href="#Motivation" data-toc-modified-id="Motivation-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Motivation</a></span></li><li><span><a href="#Solution" data-toc-modified-id="Solution-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Solution</a></span></li><li><span><a href="#🖩-Compare-the-Morse-and-Harmonic-Oscillators-(8-pts)" data-toc-modified-id="🖩-Compare-the-Morse-and-Harmonic-Oscillators-(8-pts)-2.2.3"><span class="toc-item-num">2.2.3&nbsp;&nbsp;</span>🖩 Compare the Morse and Harmonic Oscillators (8 pts)</a></span></li></ul></li><li><span><a href="#Vibrating-Diatomic-Molecules--in-an-External-Field" data-toc-modified-id="Vibrating-Diatomic-Molecules--in-an-External-Field-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Vibrating Diatomic Molecules  in an External Field</a></span><ul class="toc-item"><li><span><a href="#Motivation" data-toc-modified-id="Motivation-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Motivation</a></span></li><li><span><a href="#Hamiltonian-for-a-Polar-Diatomic-Molecule-in-an-External-Uniform-Electric-Field" data-toc-modified-id="Hamiltonian-for-a-Polar-Diatomic-Molecule-in-an-External-Uniform-Electric-Field-2.3.2"><span class="toc-item-num">2.3.2&nbsp;&nbsp;</span>Hamiltonian for a Polar Diatomic Molecule in an External Uniform Electric Field</a></span></li><li><span><a href="#The-Harmonic-Oscillator-in-a-Uniform-External-Electric-Field" data-toc-modified-id="The-Harmonic-Oscillator-in-a-Uniform-External-Electric-Field-2.3.3"><span class="toc-item-num">2.3.3&nbsp;&nbsp;</span>The Harmonic Oscillator in a Uniform External Electric Field</a></span><ul class="toc-item"><li><span><a href="#Sketch-of-Perturbative-Approach" data-toc-modified-id="Sketch-of-Perturbative-Approach-2.3.3.1"><span class="toc-item-num">2.3.3.1&nbsp;&nbsp;</span>Sketch of Perturbative Approach</a></span></li><li><span><a href="#Exact-Solution-by-Completing-the-Square" data-toc-modified-id="Exact-Solution-by-Completing-the-Square-2.3.3.2"><span class="toc-item-num">2.3.3.2&nbsp;&nbsp;</span>Exact Solution by Completing the Square</a></span></li></ul></li><li><span><a href="#🖩-Model-the-HF-molecule-in-a-uniform-electric-field-in-the-Harmonic-Oscillator-Approximation.-(8-pts)" data-toc-modified-id="🖩-Model-the-HF-molecule-in-a-uniform-electric-field-in-the-Harmonic-Oscillator-Approximation.-(8-pts)-2.3.4"><span class="toc-item-num">2.3.4&nbsp;&nbsp;</span>🖩 Model the HF molecule in a uniform electric field in the Harmonic Oscillator Approximation. (8 pts)</a></span></li><li><span><a href="#The-Morse-Oscillator-in-an-External-Electric-Field" data-toc-modified-id="The-Morse-Oscillator-in-an-External-Electric-Field-2.3.5"><span class="toc-item-num">2.3.5&nbsp;&nbsp;</span>The Morse Oscillator in an External Electric Field</a></span></li><li><span><a href="#👩🏽‍💻-Model-the-HF-molecule-in-a-uniform-electric-field-using-the-Morse-potential.--(8-pts)" data-toc-modified-id="👩🏽‍💻-Model-the-HF-molecule-in-a-uniform-electric-field-using-the-Morse-potential.--(8-pts)-2.3.6"><span class="toc-item-num">2.3.6&nbsp;&nbsp;</span>👩🏽‍💻 Model the HF molecule in a uniform electric field using the Morse potential.  (8 pts)</a></span></li><li><span><a href="#💰-Bonus.-Use-the-other-approach.-(8-pts)" data-toc-modified-id="💰-Bonus.-Use-the-other-approach.-(8-pts)-2.3.7"><span class="toc-item-num">2.3.7&nbsp;&nbsp;</span>💰 Bonus. Use the other approach. (8 pts)</a></span></li></ul></li><li><span><a href="#📚-References" data-toc-modified-id="📚-References-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>📚 References</a></span></li></ul></li></ul></div>

# 
# # Part 2: Final Exam 3PA3; Winter 2021: The Harmonic Oscillator
# 
# &#x1f468;&#x200d;&#x1f3eb; **Overview:**
# This is Part 2 of 3 Parts of your Final Exam/Project. 
# - **Part 1.** Questions on the Course Material. (40%)
# - **Part 2.** Applying the Course material. (40%)
# - **Part 3.** Discussing your exam and the Course Material. (20%) 
# 
# **You must submit your Jupyter notebooks for Part 1 and Part 2 at least 48 hours prior to your appointment for Part 3.** You will be given your grade on Part 1 and Part 2 before the oral exam, so that you know what your status is. *For late submission of Part 1 and/or Part 2, I will deduct 2 points per hour.
# 
# 
# &#x1f4dc; **Instructions:**
# Answer the following questions. These are worth 40% of your exam, and each question is worth 5 points. There is also a bonus problem.
# - You can upload files for mathematical answers or type them in Markdown.
# - You can use the notebook as a calculator for numerical problems; but you can also just type in your answer computed offline.
# - You may find these [sheets containing reference data and mathematical formulas/identities](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/ReferenceConstantsConversionsMath.pdf?raw=true) useful.
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
# **Instructions**: Read this set of notes. There are a few exercises and problems sprinkled throughout for you to answer. 
# 
# Submit your exam online as a Jupyter notebook.
# 

# In[1]:


# It's useful to import these libraries. 
# You can import others or not even use these, though.
import numpy as np
import scipy
from scipy import constants


# 
# ![Harmonic Oscillator](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/QuantumHarmonicOscillatorAnimation.gif?raw=true "Visualization of the Harmonic Oscillator and its Eigenfunctions. CC1 licensed")
# 
# ## The 1-dimensional Harmonic Oscillator
# ### Motivation: Nuclear Schr&ouml;dinger Equation for a Diatomic Molecule
# The nuclear Schr&ouml;dinger equation for a diatomic molecule is
# 
# $$
# \left(-\frac{\hbar^2}{2M_1}\nabla^2_1 -\frac{\hbar^2}{2M_2}\nabla^2_2 + E_{\text{electronic}}(\mathbf{R}_1,\mathbf{R}_2)\right) \chi(\mathbf{R}_1,\mathbf{R}_2) = E_{\text{total}}\chi(\mathbf{R}_1,\mathbf{R}_2)
# $$
# 
# The potential energy surface on which the nuclei move, $E_{\text{electronic}}\left(\mathbf{R}_1,\mathbf{R}_2\right)$, depends only on the separation between the molecules, 
# 
# $$
# E_{\text{electronic}}\left(\mathbf{R}_1,\mathbf{R}_2\right) = V\left( \left|\mathbf{R}_1 - \mathbf{R}_2 \right| \right)
# $$
# 
# This suggests changing coordinates using the [center of mass](https://en.wikipedia.org/wiki/Center_of_mass). Specifically, we define a coordinate that describes the position of the center of mass
# 
# $$
# \mathbf{R} = \frac{M_1 \mathbf{R}_1 + M_2\mathbf{R}_2}{M_1 + M_2}
# $$
# 
# and a coordinate that describes the internuclear position
# 
# $$
# \mathbf{u} = \mathbf{R}_2 - \mathbf{R}_1
# $$
# 
# To rewrite the Hamiltonian in this new coordinate system, we need to rewrite the kinetic energy in the new coordinates. To do this, notice that differentiation with respect to the old (Cartesian) coordinates of the nuclei can be re-expressed in the new coordinates as:
# 
# $$
# \begin{align}
# \frac{df}{dX_1} &= \frac{df}{du_x}\frac{du_x}{dX_1} + \frac{df}{dR_x}\frac{dR_x}{dX_1} \\
# &= -\frac{df}{du_x} + \frac{M_1}{M_1+M_2}\frac{df}{dR_x} \\
# \frac{df}{dX_2} &= \frac{df}{du_x}\frac{du_x}{dX_2} + \frac{df}{dR_x}\frac{dR_x}{dX_2} \\
# &= \frac{df}{du_x} + \frac{M_2}{M_1+M_2}\frac{df}{dR_x}
# \end{align}
# $$
# 
# So the momentum operators for the nuclei can be written as:
# 
# $$
# \hat{\mathbf{p}}_1 = -\hat{\mathbf{p}}_u + \frac{M_1}{M_1+M_2}\hat{\mathbf{p}}_R \\
# \hat{\mathbf{p}}_2 = \hat{\mathbf{p}}_u + \frac{M_2}{M_1+M_2}\hat{\mathbf{p}}_R
# $$
# 
# and the kinetic energy operators are
# 
# $$
# \frac{\hat{\mathbf{p}}_1^2}{2M_1} = \frac{\hat{\mathbf{p}}_u^2}{2M_1} + \frac{M_1\hat{\mathbf{p}}_R^2}{2(M_1+M_2)^2} \\
# \frac{\hat{\mathbf{p}}_2^2}{2M_1} = \frac{\hat{\mathbf{p}}_u^2}{2M_2} + \frac{M_2\hat{\mathbf{p}}_R^2}{2(M_1+M_2)^2}
# $$
# 
# Adding together these expressions gives the Schr&ouml;dinger equation in the new coordinate system,
# 
# $$
# \left(-\frac{\hbar^2}{2} \left(\frac{1}{M_1} + \frac{1}{M_2} \right) \nabla^2_u 
#       -\frac{\hbar^2}{2} \left(\frac{1}{M_1 + M_2} \right)\nabla^2_R 
#       + V(u) \right) \chi(\mathbf{R},\mathbf{u}) = E_{\text{total}}\chi(\mathbf{R},\mathbf{u})
# $$
# 
# or, introducing the reduced mass 
# 
# $$
# \mu = \frac{M_1 M_2}{M_1 + M_2} = \left(\frac{1}{M_1} + \frac{1}{M_2} \right)^{-1} \\
# $$
# 
# and total mass
# 
# $$
# M = M_1 + M_2
# $$
# 
# 
# $$
# \left(-\frac{\hbar^2}{2 \mu}-\frac{\hbar^2}{2M}\nabla^2_R + V(u) \right) \chi(\mathbf{R},\mathbf{u}) = E_{\text{total}}\chi(\mathbf{R},\mathbf{u})
# $$
# 
# This Schr&ouml;dinger equation can be solved by separation of variables. The Schr&ouml;dinger equation for the center of mass represents the translational motion of the molecule; in the absence of a potential confining the molecule, this is just the Schr&ouml;dinger equation for a free particle,
# 
# $$
# -\frac{\hbar^2}{2M}\nabla^2_R \eta(\mathbf{R}) = E \eta(\mathbf{R}) 
# $$
# 
# This contributes nothing to the energy if we assume the molecule is not moving (so that it's kinetic energy is zero). If the molecule were confined, that confining potential would be inserted here. 
# 
# The Schr&ouml;dinger equation for the internuclear coordinate represents the rotations and vibrations of the molecule:
# 
# $$
# \left(-\frac{\hbar^2}{2 \mu} + V(u) \right) \varphi(\mathbf{u}) = E_{\text{rovib}}\varphi(\mathbf{u})
# $$
# 
# The Hamiltonian in this equation is typically called the rovibrational Hamiltonian; its energy is the rovibrational energy. Because the potential energy depends only on the internuclear distance, the system is spherically symmetric. Separating out the angular dependence in the usual way,
# 
# $$
# \left(-\frac{\hbar^2}{2\mu} \left( \frac{d^2}{du^2}
# + \frac{2}{u} \frac{d}{du}\right) 
#       + \frac{\hat{L}^2(\theta_u,\phi_u)}{2\mu u^2} + V(u) \right)
#       \varphi_{k,J,M_J}(u,\theta_u,\phi_u) 
# = E_{k,J,M_J}\varphi_{k,J,M_J}(u,\theta_u,\phi_u)
# $$
# 
# Recall that $\hat{L}^2$ is the angular momentum squared, and its eigenfunctions are the spherical harmonics, which we have chosen to denote with a different quantum number to avoid confusion with the electronic problem,
# 
# 
# $$
# \begin{align}
# \hat{L}^2 Y_J^{M_J}(\theta_u,\phi_u) = \hbar^2 J(J+1) Y_J^{M_J}(\theta_u,\phi_u) \qquad \qquad J&=0,1,2,\ldots \\ M_J &= 0,\pm 1,\ldots\,\pm J
# \end{align}
# $$
# The exact wavefunction is therefore the product of a radial wavefunction and a spherical harmonic, 
# 
# $$
# \varphi_{k,J,M_J}(u,\theta_u,\phi_u) = R_k(u)  Y_J^{M_J}(\theta_u,\phi_u)
# $$
# 
# where the radial wavefunction and the rovibrational energy are obtained by solving
# 
# $$
# \left(-\frac{\hbar^2}{2\mu} \left( \frac{d^2}{du^2}
# + \frac{2}{u} \frac{d}{du}\right) 
#       + \frac{\hbar^2 J(J+1)}{2\mu u^2} + V(u) \right)
#       R_{k}(u) = E_{k,J}R_{k}(u)
# $$
# 

# ### Quadratic Approximation to the Potential Energy Curve and the Rigid Rotor Approximation
# The potential energy of a diatomic molecule goes to infinity at short internuclear separation ($u \rightarrow 0$) because of the nuclear-nuclear repulsion and approaches a constant (which we typically define to be zero) at infinite internuclear distance. In between these limits, there is typically a minimum at $r_e$, which represents the equilibrium bond length for the molecule (in the absence of quantum effects). If we assume that the atomic nuclei, which are much more massive than electrons, have relatively small De Broglie wavelength and do not deviate far from $u = r_e$, it is reasonable to expand the potential energy in a Taylor series about that point,
# $$
# V(u) = V(r_e) + V'(r_e)(u-r_e) + \tfrac{1}{2!}V''(r_e)(u - r_e)^2 + \cdots
# $$
# Because we are expanding around the minimum, $V'(r_e) = 0$. The term $V(r_e)$ only shifts the total energy of the system up or down by a constant, so we can *choose* to set the zero of the energy scale so that $V(r_e) = 0$. Neglecting higher-order terms in the expansion, which we hope will be small, we can then write
# $$
# \left(-\frac{\hbar^2}{2\mu} \left( \frac{d^2}{du^2}
# + \frac{2}{u} \frac{d}{du}\right) 
#       + \frac{\hbar^2 J(J+1)}{2\mu u^2} + \tfrac{1}{2}V''(r_e)(u-r_e)^2 \right)
#       R_{k}(u) = E_{k,J}R_{k}(u)
# $$
# The rotational contribution can also be simplified by taking a Taylor series:
# $$
# \frac{\hbar^2}{2\mu u^2}u^-2 = \frac{\hbar^2}{2\mu r_e^2} - \frac{2\hbar^2}{2\mu r_e^3}(u - r_e) + \cdots  
# $$
# The first and higher-order terms in the series represent centrifugal distortion, which indicates that a molecule rotates faster and faster, larger bond lengths are favored. Such effects are usually small for low-energy vibrational states of strong bonds, where it is reasonable to make a [*rigid rotor approximation*](https://en.wikipedia.org/wiki/Rigid_rotor#Quantum_mechanical_rigid_rotor) and truncate the Taylor series after the zeroth order term. The rotational and vibrational problems then decouple, with the rotational wavefunctions and energies being given by:
# $$
# \frac{\hat{L}^2}{2\mu r_e^2} Y_J^{M_J}(\theta_u,\phi_u) = \frac{\hbar^2 J(J+1)}{2 \mu r_e^2}      Y_J^{M_J}(\theta_u,\phi_u)
# $$
# and the vibrational Hamiltonian is then approximated as a [quantum mechanical harmonic oscillator](https://en.wikipedia.org/wiki/Quantum_harmonic_oscillator):
# $$
# \left(-\frac{\hbar^2}{2\mu} \left( \frac{d^2}{du^2}
# + \frac{2}{u} \frac{d}{du}\right) + \tfrac{1}{2}V''(r_e)(u-r_e)^2 \right)
#       R_{k}(u) = E_{k}R_{k}(u)
# $$

# ### &#x1F5A9; Exercise: Isotope Effects in Rotational Spectroscopy (8 pts.)
# For a diatomic molecule that has a permanent dipole moment, allowed rotational transitions correspond to $\Delta J = \pm 1$. 
# 
# - A measurement informs you that the transition associated with the $J=0$ to $J=1$ transition in ${}^1\text{H}{}^{35}\text{Cl}$ (note the isotope labels) is characterized by $\tilde{\nu} = \tfrac{1}{\lambda} = 20.9 \text{ cm}^{-1}$. **What is the equilibrium bond length of HCl in picometers?** 
# - Assume that $\text{T}{}^{37}\text{Cl}$ (i.e., ${}^3\text{H}{}^{37}\text{Cl}$) molecule has the same bond length. **What is the wavenumber of the $J=0$ to $J=1$ transition for $\text{T}{}^{37}\text{Cl}$ in $\text{ cm}^{-1}$?**
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[2]:


# Report your answers in this cell. I have initialize the variables to None.
re_HCl = None
wavenumber_T37Cl = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(f"The equilibrium bond length of HCl is {re_HCl:.1f} pm.")
print(f"The wavenumber of the J=0 -> 1 transition in TCl(37) {wavenumber_T37Cl:.3f} cm-1.")


# YOUR ANSWER HERE

# ### The Harmonic Oscillator Hamiltonian
# ![harmonic oscillator wf](https://upload.wikimedia.org/wikipedia/commons/9/9e/HarmOsziFunktionen.png "The Harmonic Oscillator wavefunctions and energy levels. CC-SA3 by AllenMcC")
# 
# It is convenient to change the coordinates in this problem, so that the dependence on $r_e$ is not explicit. Defining 
# $$
# x = u - r_e \\
# \kappa_e = V''(r_e)
# $$
# the harmonic-oscillator Hamiltonian becomes:
# $$
# \left(-\frac{\hbar^2}{2\mu} \left( \frac{d^2}{dx^2}
# + \frac{2}{u} \frac{d}{dx}\right) + \tfrac{1}{2}\kappa_e x^2 \right)
#       R_{k}(x) = E_{k,J}R_{k}(x)
# $$
# In the picture of a diatomic molecule where the atoms are connected to each other with a harmonic spring $x$ is the deviation of the spring from its equilibrium length and $\kappa_e$ is the force constant for the spring. The angular frequency for the spring is
# $$
# \omega = \sqrt{\frac{\kappa_e}{\mu}}
# $$
# and the reduced mass is defined as previously,
# $$
# \mu = \frac{M_1 M_2}{M_1 + M_2}
# $$

# ### Solutions to the Harmonic Oscillator Hamiltonian
# We will not attempt to solve the harmonic oscillator Schr&ouml;dinger equation. It suffices to note that the equation *is* exactly solvable using techniques similar to those we've used for other systems, and that the solution is written in terms of (yet another) type of special function, the [Hermite polynomials](https://en.wikipedia.org/wiki/Hermite_polynomials):
# 
# \begin{align}
# H_0(y) &= 1 \\
# H_1(y) &= 2y \\
# H_2(y) &= 4y^2 - 2 \\
# H_3(y) &= 8y^3 - 12 \\
# H_n(y) &= 2y H_{n-1}(y) - 2(n-1)H_{n-2}(y)
# \end{align}
# 
# As with the associated Laguerre polynomials, one must be careful because there are (at least) two different definitions of the Hermite polynomials that are prevalent in the literature. These are the-called [physicist's Hermite polynomials](https://en.wikipedia.org/wiki/Hermite_polynomials#Definition). Specifically, we have:
# $$
# R_k(x) = \sqrt{\frac{1}{2^k k!}}\left(\frac{\mu \omega}{\pi \hbar} \right)^{\frac{1}{4}}H_k\left(x\sqrt{\frac{\mu \omega}{\hbar}}\right) \exp \left[-\frac{1}{2} \left(x\sqrt{\frac{\mu \omega}{\hbar}}\right)^2  \right]
# $$
# and the corresponding eigenvalues are
# $$
# E_k = \hbar \omega \left( k+ \tfrac{1}{2} \right) = \hbar \sqrt{\frac{\kappa_e}{\mu}} \left( k+ \tfrac{1}{2} \right) \qquad \qquad k=0,1,2,\ldots
# $$

# ### &#x1F5A9; Isotope Effects in Vibrational Spectroscopy (8 pts)
# For a diatomic molecule that is well-described by a harmonic oscillator, allowed vibrational transitions correspond to $\Delta k = \pm 1$. 
# 
# - A measurement informs you that the fundamental vibrational transition associated with $k=0$ to $k=1$ in ${}^7\text{Li}{}^{7}\text{Li}$ (note the isotope labels) is characterized by $\tilde{\nu} = \tfrac{1}{\lambda} = 351.43 \text{ cm}^{-1}$. **What is the force constant, $\kappa_e$, for the Lithium dimer in Newton/meter?** 
# - Assume that ${}^6\text{Li}{}^{6}\text{Li}$ molecule has the same force constant. **What is the wavenumber of the $k=0$ to $k=1$ transition of ${}^6\text{Li}{}^{6}\text{Li}$ in $\text{cm}^{-1}$?**
# 
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[ ]:


# Report your answers in this cell. I have initialize the variables to None.
kappa_e = None                #Force constant in N/m
wavenumber_6Li_2 = None       #wavenumber in cm-1

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(f"The force constant at equilibrium bond length of the Lithium dimer is {kappa_e:.2f} N/m.")
print(f"The wavenumber of the k=0 -> 1 transition in the Li-6 dimer is {wavenumber_6Li_2:.1f} cm-1.")


# YOUR ANSWER HERE

# ![Morse Potential](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Morse-potential.png/650px-Morse-potential.png "The Morse Potential, CC-SA3 by Somoza")
# ## The Morse Oscillator
# 
# ### Motivation
# The harmonic oscillator is not very realistic for two reasons
# - it predicts that negative bond lengths would be possible, since the potential energy curve does not diverge to infinity as $u \rightarrow 0$.
# - it predicts that chemical bonds never break, since the potential energy curve does not approach an asymptotic constant as $u \rightarrow \infty$. 
# 
# The last issue, which is the more severe one from the standpoint of qualitative chemical behavior, can be remedied by replacing the harmonic oscillator potential with the Morse potential,
# $$
# V_{\text{Morse}}(u) = D_e \left(1 - e^{-a(u-r_e)} \right)^2
# $$
# Here $D_e$ is the dissociation constant (the energy it takes to break the bond between the atoms) and $a$ is related to the force constant by
# $$
# a = \sqrt{\frac{\kappa_e}{2D_e}}
# $$
# Recall that 
# $$
# \kappa_e = V''_{\text{Morse}}(r_e)
# $$

# ![Comparison](https://upload.wikimedia.org/wikipedia/commons/a/aa/N2ground.png "Comparison of the Morse Potential and the Harmonic Oscillator, CC-SA4 by Chengouze")
# ### Solution
# The Schr&ouml;dinger equation for the Morse potential, 
# $$
# \left(-\frac{\hbar^2}{2\mu} \left( \frac{d^2}{du^2}
# + \frac{2}{u} \frac{d}{du}\right) + V_{\text{Morse}}(u) \right)
#       \phi_{k}(u) = E_{k}\phi_{k}(u)
# $$
# can also be solved exactly. The eigenfunctions are [quite complicated functions of the associated Laguerre polynomials](https://en.wikipedia.org/wiki/Morse_potential#Vibrational_states_and_energies) but the energies have a relatively simple expression,
# $$
# E_k = \hbar \omega_0 \left(k+\tfrac{1}{2}\right) - \frac{\left[ \hbar \omega_0 \left(k+\tfrac{1}{2}\right) \right]^2}{4 D_e}
# \qquad \qquad k=0,1,2,\ldots,k_{\max}
# $$
# where, just as in the harmonic oscillator, 
# $$
# \omega_0 = a \sqrt{\frac{2D_e}{\mu}} = \sqrt{\frac{\kappa_e}{\mu}}
# $$
# Unlike the harmonic oscillator, only a $k_{\max} < \infty$ states can be bound by the Morse potential, where
# $$
# k_{\max} = \left\lfloor \frac{2D_e}{\hbar \omega_0} - \frac{1}{2} \right\rfloor
# $$
# Here $\lfloor x \rfloor$ denotes the integer part of $x$. E.g., $\lfloor 20.3 \rfloor = 20$. The upshot of the equation for $k_{\max}$ is that the Morse oscillator has about twice as many states with energy less than $D_e$ as the harmonic oscillator does, because the states of the Morse oscillator become closer and closer together as the molecule gets closer to dissociation. The ability to have only a finite number of bound vibrational states is one way in which the Morse oscillator is more like a real vibrating molecule than the harmonic oscillator.

# ### &#x1F5A9; Compare the Morse and Harmonic Oscillators (8 pts)
# A measurement informs you that the fundamental vibrational transition associated with $k=0$ to $k=1$ in ${}^7\text{Li}{}^{7}\text{Li}$ (note the isotope labels) is characterized by $\omega_0 = 6.620\cdot 10^{-13} \text{Hz}$. Moreover, the dissociation energy is $1.6918\cdot 10^{-19} \text{ Joules}$.  
# - How many bound states does ${}^7\text{Li}_2$ have in the Morse oscillator? 
# - How many bound states does ${}^6\text{Li}_2$ have in the Morse oscillator? Assume that the Born-Oppenheimer approximation holds.
# - What is the zero-point energy of ${}^6\text{Li}_2$ in the harmonic oscillator in Joules? 
# - What is the zero-point energy of ${}^6\text{Li}_2$ in the Morse oscillator in Joules?
# 
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[ ]:


# Enter the answers for the variables below. I have initialized the variables to None.
n_boundst_7Li_2 = None       #integer; number of bound states in Li-7 dimer
n_boundst_6Li_2 = None       #integer; number of bound states in Li-6 dimer
zero_pt_6Li_2_Morse = None   #float. zero-point energy in Li-6 dimer in the Morse potential in Joules
zero_pt_6Li_2_harmosc = None #float. zero-point energy in Li-6 dimer in the harmonic oscillator in Joules

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert isinstance(n_boundst_7Li_2,int), "Type error: The number of bound states should be an integer."
assert isinstance(n_boundst_6Li_2,int), "Type error: The number of bound states should be an integer."

print(f"The number of bound states in the Morse oscillator for the Li-7 dimer is {n_boundst_7Li_2}.")
print(f"The number of bound states in the Morse oscillator for the Li-6 dimer is {n_boundst_6Li_2}.")
print(f"The zero-point energy of the Morse oscillator for the Li-6 dimer is {zero_pt_6Li_2_Morse:.3e} Joules.")
print(f"The zero-point energy of the harmonic oscillator for the Li-6 dimer is {zero_pt_6Li_2_harmosc:.3e} Joules.")


# YOUR ANSWER HERE

# ## Vibrating Diatomic Molecules  in an External Field
# ### Motivation
# For polar diatomic molecules, their dipole moment may be approximated as: 
# $$
# \mathbf{p} = q \left(\mathbf{R}_2 - \mathbf{R}_1 \right)
# $$
# where $q$ is the magnitude of the charges on the atoms and $\mathbf{R}_2$ is the positively charged atom. The energy of a polar diatomic molecule interacting with an electric field is then
# $$
# V_{\text{dipole}} = -\mathbf{p} \cdot \mathbf{E}
# $$
# This energy is minimized when the dipole aligns in the field, giving an energy lowering that is proportional to the product of the magnitude of the dipole moment and the electric field strength,
# $$
# V_{\text{dipole}} = -|\mathbf{p}| |\mathbf{E}| = - q u F
# $$
# where $q$ is the atomic charge, $u$ is the internuclear distance, and F is the field strength. This is a quite simple model, and neglects the following 
# - atomic charges change when the bond length changes
# - atoms are not simply point charges
# - a molecule's electrons rearrange in response to the electric field. To a first approximation, this means that the atomic charges change in the presence of the field.
# 
# Nonetheless, this model does capture some key features, notably the fact that in the presence of a uniform external field, the bond in a polar diatomic molecule tends to elongate. 
# 
# ### Hamiltonian for a Polar Diatomic Molecule in an External Uniform Electric Field
# The Hamiltonian for a vibrating molecule in an electric field can then be approximated as
# $$
# \left(-\frac{\hbar^2}{2\mu} \left( \frac{d^2}{du^2}
# + \frac{2}{u} \frac{d}{du}\right) + V(u) - q_e u F \right)
#       R_{k}(u) = E_{k}R_{k}(u)
# $$
# where $q_e$ is magnitude of the atomic charge for $u = r_e$. If the equilibrium dipole moment of the molecule is known, then 
# $$
# q_e = \frac{\left[\text{dipole moment in Debye}\right] \cdot 3.33564 \cdot 10^{-30} \text{ C/m}}{\text{bond length in meters}} \text{ Coulombs}
# $$
# or, in terms of the charge on the electron $e$, 
# $$
# q_e = \frac{\left[\text{dipole moment in Debye}\right] \cdot 2.08919 \cdot 10^{-11} e/\text{m}}{\text{bond length in meters}} e
# $$
# 
# The most interesting effects are not those that are associated with the classical interaction energy of the dipole with the field, we usually subtract that energy from the Hamiltonian, so that we only see the change in the molecule's energy that was *induced* by the field. I.e., we usually focus on the vibrational dipole polarization energy,
# $$
# E_k^{(\text{polarization})}(F) = E_k(F) - \left[ E_k(F=0) - q_e r_e F \right]
# $$
# The vibrational dipole polarization energy can be computed from the shifted Schr&ouml;dinger equation, 
# where
# 
# \begin{align}
# \left(-\frac{\hbar^2}{2\mu} \left( \frac{d^2}{du^2}
# + \frac{2}{u} \frac{d}{du}\right) + V(u) - q_e (u-r_e) F \right)
#       \psi_{k}(u) &= \left(E_k(F=0) + E_{k}^{(\text{polarization})}(F)\right)\psi_{k}(u) \\
#       &= E_{k}^{(\text{shifted})}(F)\psi_{k}(u) 
# \end{align}
# 
# where we have (re)defined the energy as
# $$
# E_k^{(\text{shifted})}(F) = E_k(0) + E_k^{(\text{polarization})}(F)
# $$
# 
# The total energy of the vibrating diatomic molecule can then be expressed as:
# $$
# E_k(F) = E_k(0) - q_e r_e F + E_k^{(\text{polarization})}(F)
# $$
# If one expands the vibrational polarization energy in a Taylor series, 
# $$
# E_k^{(\text{polarization})}(F) = -\tfrac{1}{2} \alpha_{\text{vib}} F^2 - \tfrac{1}{3!} \beta_{\text{vib}} F^3 - \tfrac{1}{4!} \gamma_{\text{vib}} F^3 + \cdots
# $$
# where $\alpha_{\text{vib}}$ is the vibrational contribution to the dipole polarizability (subject to the approximations mentioned above) and the higher-order coefficients are the first-, $\beta$, and higher-order vibrational dipole hyperpolarizabilities.
# 

# ### The Harmonic Oscillator in a Uniform External Electric Field
# To model a diatomic molecule vibrating in a uniform electric field, we need to choose a practical model for the vibrational potential energy function, $V(u)$. The simplest possible model is to use a Harmonic Oscillator, which leads to the Hamiltonian:
# $$
# \left(-\frac{\hbar^2}{2\mu} \left( \frac{d^2}{du^2}
# + \frac{2}{u} \frac{d}{du}\right) + \tfrac{1}{2}\kappa_e(u-r_e)^2 - q_e (u-r_e) F \right)
#       R_{k}(u) = E_{k}^{\text{shifted}}(F) R_{k}(u)
# $$
# 
# #### Sketch of Perturbative Approach
# One could treat this Hamiltonian with perturbation theory. By construction, $E_k^{(\text{shifted})}$ does not depend on the field to first order. Therefore, the leading-order term is the second-order contribution,
# $$
# \left[\frac{d^2 E_k}{dF^2}\right]_{F=0}
# =\left[\frac{d^2E_k^{(\text{polarization})}}{dF^2}\right]_{F=0}=\left[\frac{d^2E_k^{(\text{shifted})}}{dF^2}\right]_{F=0} = 2q_e \sum_{j=0\\j \ne k}^{\infty}\frac{ \left|\langle R_j(0) | u-r_e |R_k(0) \rangle \right|^2}{E_k(F=0) - E_j(F=0)} 
# $$
# 
# Evaluating this expression is feasible because the integrals that one needs,
# $$
# V_{kl} = \int_{-\infty}^{\infty} R_k(u)(u-r_e) R_l(u) du 
# $$
# have a simple explicit formulae. Specifically,
# $$
# V_{kl} = 
# \begin{cases}
# \sqrt{\frac{k}{2}}   & k=l+1 \\
# \sqrt{\frac{k+1}{2}} & k=l-1 \\
# 0  & \text{otherwise}
# \end{cases}
# $$
# 
# 
# #### Exact Solution by Completing the Square
# While a perturbative approach is possible, the harmonic oscillator in a uniform external electric field can be solved exactly. [Completing the square](https://en.wikipedia.org/wiki/Completing_the_square) on the potential,
# $$
# \tfrac{1}{2}\kappa_e(u-r_e)^2 - q_e (u-r_e) F = \tfrac{1}{2}\kappa_e\left(u - r_e - \frac{qF}{\kappa_e}\right)^2 - \frac{q^2F^2}{2 \kappa_e}
# $$
# The force constant in this new shifted harmonic oscillator is the still $\kappa_e$, but the bond length 
# $$
# r_e(F) = r_e + \frac{qF}{\kappa_e}
# $$
# and the energies
# $$
# E_k^{\text{shifted}}(F) = \hbar \sqrt{\frac{\kappa_e}{\mu}}\left(k+\frac{1}{2}\right) - \frac{q^2F^2}{2 \kappa_e}
# $$
# have chagned. Referring to the definitions above, the vibrational polarization energy is:
# $$
# E_k^{\text{polarization}}(F) = - \frac{q^2}{2 \kappa_e}F^2
# $$
# the vibrational polarizability is
# $$
# \alpha_{\text{vib}} = \frac{q^2}{\kappa_e}
# $$
# and the total vibrational energy of the diatomic molecule in the field
# $$
# E_k(F) = \hbar \sqrt{\frac{\kappa_e}{\mu}}\left(k+\frac{1}{2}\right) - q r_e F- \frac{q^2}{2 \kappa_e}F^2
# $$

# ### &#x1F5A9; Model the HF molecule in a uniform electric field in the Harmonic Oscillator Approximation. (8 pts)
# For the ${}^{1}\text{H}{}^{19}\text{F}$ molecule, $\mu = 6.361 \cdot 10^{-25} \text{ kg}$, $\kappa_e = 920 \text{ N/m} $, and $r_e = 91.68 \text{ pm}$. The dipole moment of HF is 1.91 Debye, which corresponds to a semi-reasonable charge of 0.44 $e$ on the hydrogen atom. Assume the electric field is 1,000,000 V/m.
# - How much does the bond elongate in the presence of the external electric field? Report your answer in picometers.
# - What value would you obtain if you used second-order perturbation theory to estimate the vibrational polarization energy, $E_k^{(\text{polarization})}$. Report your answer in Joules.
# 
# *Hint:* Results from the previous block of the notebook may be helpful.
# 
# 
# If you wish, you can use the markdown cell at the end to explain your answer.

# In[ ]:


# Report your answers in the variables below, which I have initialized to None.
re_shift = None
e_polarization = None

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print(f"The bond length of HF elongates by {re_shift:.3e} pm in a field of 1,000,000 V/m.")
print(f"The zero-point energy HF changes by {e_polarization:.3e} J in a field of 1,000,000 V/m.")


# YOUR ANSWER HERE

# ### The Morse Oscillator in an External Electric Field
# Instead of using a harmonic oscillator to describe the vibrational motion of a polar diatomic molecule, one could use the Morse Oscillator. In this case, the Schr&ouml;dinger equation is:
# 
# \begin{align}
# \left(-\frac{\hbar^2}{2\mu} \left( \frac{d^2}{du^2}
# + \frac{2}{u} \frac{d}{du}\right) + V_{\text{Morse}}(u) - q_e (u-r_e) F \right)
#       \phi_{k}(u) &= \left(E_k(F=0) + E_{k}^{(\text{polarization})}(F)\right)\phi_{k}(u) \\
#       &= E_{k}^{(\text{shifted})}(F)\phi_{k}(u) 
# \end{align}
# 
# Unlike the harmonic oscillator in an electric field, it is no longer possible to solve this system exactly. However, there are many possible ways to approximate the energy of a Morse oscillator in a uniform electric field, among them:
# - Use the harmonic-oscillator in an external field as a zeroth-order Hamiltonian, and use perturbation theory to estimate the change in energy associated with using the Morse potential instead.
# - Use the eigenfunctions of the harmonic oscillator in an electric field as a basis; expand the eigenfunctions of the Morse potential in an electric field in this basis.
# - Use the Morse potential without an electric field as a zeroth-order Hamiltonian; use perturbation theory to estimate the effects of the electric field.
# - Use the eigenfunctions of the Morse potential without an electric field as a basis; expand the eigenfunctions of the Morse potential in an electric field in this basis.
# 
# The first two approaches are arguably preferable mathematically, but the latter two are easier. This is because the matrix elements for the Morse potential in an electric field, 
# $$
# V_{mn} = \int_{-\infty}^{\infty} \phi_m(u;F=0) (u - r_e) \phi_n(u;F=0) du 
# $$
# are (relatively) easy to evaluate. Specifically we have:
# $$
# V_{m<n} = \frac{-1^{m-n+1}}{a(n-m)(2\lambda-n-m-1)}\left[\frac{n! \Gamma(2\lambda - n)(2\lambda - 2n - 1)(2\lambda - 2m - 1)}{m! \Gamma(2\lambda - m)} \right]^{\frac{1}{2}}
# $$
# In practice, this equation is numerically ill-conditioned when $m$, $n$, or $\lambda$ is large, because then some of the terms are gigantic. It is reasonable to cut off the expansion for large $m$ and large $n$; when $\lambda$ is large, one can use the Ramanujan expression for the $\Gamma$ function,
# $$
# \Gamma(y) = \sqrt{\pi} \left(\frac{y-1}{e} \right)^{y-1} \left(8(y-1)^3 + 4(y-1)^2 + (y-1) + \frac{1}{30} \right)^{\frac{1}{6}}
# $$
# to evaluate the square root of the ratio of the $\Gamma$ functions directly
# $$
# \frac{\Gamma(y)}{\Gamma(x)} = \left(\sqrt{\frac{y-1}{x-1}}\right)^{y-1} \left(\sqrt{\frac{e}{x-1}} \right)^{x-y}
# \left(\frac{8(y-1)^3 + 4(y-1)^2 + (y-1) + \frac{1}{30}}{8(x-1)^3 + 4(x-1)^2 + (x-1) + \frac{1}{30}}\right)^{\frac{1}{12}}
# $$
# The code below actually uses the (more complicted) Stirling expansion, because in practice it seemed more accurate.
# 
# The diagonal elements are:
# $$
# V_{mm} \approx \frac{\frac{3}{2} + 3m + \frac{13/12 + (7/2)(m^2+m)}{2 \lambda} + \frac{(m+1)^4}{4\lambda^2}}{2\lambda a}
# $$
# In these expressions, 
# $$
# \lambda = \frac{\sqrt{2 \mu D_e}}{a \hbar}
# $$
# Using the aforementioned definition of $a$,
# $$
# a = \sqrt{\frac{\kappa_e}{2D_e}}
# $$
# this simplifies to
# $$
# \lambda = \frac{2 D_e}{\hbar}\frac{\mu}{\kappa_e} = \frac{2 D_e}{\hbar \omega_0} 
# $$
# > Note. Technically in both perturbation theory and in a variational approach one would need to consider the continuum states, corresponding to the states of the dissociated diatomic molecule. We are neglecting that tricky business here, but that is the main reason that an approach starting from the harmonic oscillator is mathematically preferable.
# 
# > Note. The choice of $u = |\mathbf{R}_1 - \mathbf{R}_2|$ or $u = |\mathbf{R}_2 - \mathbf{R}_1|$ is arbitrary. This means, in practice, that whether one chooses a field oriented in the $+u$ or $-u$ direction is arbitrary. One should compute both choices, and pick the one which stabilizes the molecule more. For a Morse oscillator, this corresponds to a field with a negative sign.

# ### &#x1f469;&#x1f3fd;&#x200d;&#x1f4bb; Model the HF molecule in a uniform electric field using the Morse potential.  (8 pts)
# For the ${}^{1}\text{H}{}^{19}\text{F}$ molecule, $\mu = 6.361 \cdot 10^{-25} \text{ kg}$, $\kappa_e = 920 \text{ N/m} $, $D_e = 9.402 \cdot 10^{-19} J$, and $r_e = 91.68 \text{ pm}$. The dipole moment of HF is 1.91 Debye, which corresponds to a semi-reasonable charge of 0.44 $e$ on the hydrogen atom. Assume the electric field is 1,000,000 V/m.
# 
# Using the integrals provided below, compute the vibrational polarization energy, $E_{k}^{(\text{polarization})}(F)$, for the Morse Oscillator in a field using perturbation theory and/or basis-set expansion. 
# 1. Compute both first and second-order corrections to the polarization energy if you use perturbation theory. Note that in this case, the first-order contribution to the polarization energy is not exactly zero.
# 2. Summing over all bound states or using all bound states in the basis is not practical, but you should be sure to not use unbound states.
# 
# >Given how complicated this is, it is possible that *my* code below has some mistakes. I'm looking to test whether your code works well *assuming* that my matrix elements $V_{mn}$, are coded correctly.
# 
# ### &#x1f4b0; Bonus. Use the other approach. (8 pts)

# In[ ]:


# I've initialized key variables to None. These quantities are printed in the next cell.
epol_pt = None    #Energy of polarization computed using first and second-order perturbation theory, in Joules
epol_basis = None #Energy of polarization computed using basis-set expansion, in Joules

# The below code provides key quantities that are needed for this treatment. All inputs are assumed to be in SI units.
# You should print out key values in the next cell.

from scipy.linalg import eigh
from scipy.special import gamma,factorial
import math

def Ramanujan_ratio(x,m,n):
    """Computes (Gamma(2x-n)/Gamma(2x-m))^(1/2) using the Ramanujan approximation to the Gamma function"""
    ratio = np.sqrt((2*x-m-1)**(m+1))/np.sqrt((2*x-n-1)**(n+1))             * (cubic_poly(2*x-n-1)/cubic_poly(2*x-m-1))**(1./12)              * ((2*x-n-1)/(2*x-m-1))**x
    return ratio

def cubic_poly(y):
    """The cubic polynomial that shows up in the Ramanujan formula"""
    return 8*y**3 + 4*y**2 + 2*y + 1./30

def Stirling_ratio(x,y):
    """Computes (Gamma(y)/Gamma(x))^(1/2) using the Stirling approximation to the Gamma function
    This works best when x and y are approximately equal, and implicitly it is assumed that y < x.
    """
    ratio = (y/x)**(0.5*y-0.25) * np.sqrt(math.e/x)**(x-y) * np.sqrt(Stirling_poly(y)/Stirling_poly(x))
    return  ratio

def Stirling_poly(y):
    "Evaluates the polynomial part of the Stirling approximaton to the Gamma function"
    p = 0
    p = 1 + 1./(12*y) + 1./(288*y**2) - 139./(51840*y**3) - 571./(2488320*y**4)         + 163879/(209018880*y**5) + 5246819./(75246796800*y**6)
    return p

def compute_V(De, omega0, kappa_e, n_basis):
    """Compute the matrix <m|x|n> for a Morse oscillator
    
    Parameters
    ----------
    De : scalar 
        The depth energy of the Morse potential in SI units (Joules)
    omega0 : scalar
        the fundamental vibrational frequency parameter in Hz; equal to (kappa_e/mu)^(1/2) where mu is the reduced mass.
    kappa_e : scalar
        the force constant in N/m; the curvature at the bottom of the potential well.
    n_basis : scalar, int
        the number of rows/columns in the V matrix to be computed

    Returns
    -------
    V : array-like (nbasis, nbasis)
         Matrix elements V_mn = <m | (u - r_e) | n> for the Morse Oscillator in units of meters
         
    Note: based on equations in
        Vasan & Cross; The Journal of Chemical Physics 78, 3869–3871 (1983).
    
    """
    
    # Compute key parameters
    lmbda = 2*De / (constants.hbar * omega0)  #lambda is a special word in Python so we can't use it. :-(
    a = np.sqrt(kappa_e/(2*De))
    
    # This program will crash and burn if the number of states is too large, because factorials of large numbers
    # are too big. So 
    assert(n_basis < 150), "n_basis is too large, so we stop gracefully to avoid overflow"
    
    # initialize V to a zero matrix
    V = np.zeros((n_basis,n_basis))
    
    for n in range(n_basis):
        V[n,n] = (3/2 + 3*n + (13/12 + 7/12*(n**2 + n))/(2*lmbda)                   + (n+1)**4/(4*lmbda**2))/(2*lmbda*a)
        for m in range(n):
            prefactor = -1**(m-n+1)/a * 1/((n-m)*(2*lmbda -n - m -1))
            radicand = factorial(n)/factorial(m) * (2*lmbda - 2*n - 1) * (2*lmbda - 2*m - 1)
            if ((2*lmbda - min(m,n)) <= 50):
               #we can use the conventional expressions for the gamma function
               radicand *= gamma(2*lmbda - n)/gamma(2*lmbda - m)
               radical = np.sqrt(radicand) 
            else:
               radical = np.sqrt(radicand)
               #we need to use an asymptotic formula to estimate the gamma-function ratio. Using the Stirling
               #based formula because it seems to work better.
               radical *= Stirling_ratio(2*lmbda-m,2*lmbda-n)
            V[m,n] = prefactor * radical
            V[n,m] = V[m,n]
    
    return V

def compute_E0(De, omega0, n_basis):
    """Compute the eigenenerties of the Morse oscillator in the absence of an electric field
    
    Parameters
    ----------
    De : scalar 
        The depth energy of the Morse potential in SI units (Joules)
    omega0 : scalar
        the fundamental vibrational frequency parameter in Hz; equal to (kappa_e/mu)^(1/2) where mu is the reduced mass.
    n_basis : scalar, int
        the number of rows/columns in the V matrix to be computed

    Returns
    -------
    E0 : array-like (nbasis)
         eigenenergies of the Morse oscillator in units of Joules
               E0(m) =  hbar * omega0 (k + 1/2) - (hbar * omega0 (k + 1/2))^2 / 4 De
    
    """

    # initialize E0 to a zero vector
    E0 = np.zeros(n_basis)
                                           
    for m in range(n_basis):
        E0_harmosc = constants.hbar * omega0 * (m + 1/2)
        E0[m] = E0_harmosc - E0_harmosc**2/(4*De)

    return E0

def compute_H(De,omega0,kappa_e,charge,field,n_basis):
    """Compute the Hamiltonian matrix <m|H(field)|n> for a Morse oscillator of a molecular dipole in a field.
    
    Parameters
    ----------
    De : scalar 
        The depth energy of the Morse potential in SI units (Joules)
    omega0 : scalar
        the fundamental vibrational frequency parameter in Hz; equal to (kappa_e/mu)^(1/2) where mu is the reduced mass.
    kappa_e : scalar
        the force constant in N/m; the curvature at the bottom of the potential well.
    charge : scalar
        the charge on the positively-charged atom in the dipole, in Coulombs
    field : scalar
        the applied electric field, in Volts/meter
    n_basis : scalar, int
        the number of rows/columns in the H matrix to be computed

    Returns
    -------
    H : array-like (nbasis, nbasis)
         Matrix elements H_mn = <m | H(F=0) + charge*field(u-r_e) | n> for the Morse Oscillator in units of Joules
    """
    
    V = compute_V(De,omega0,kappa_e,n_basis)
    E0 = compute_E0(De,omega0,n_basis)
    
    #Initialize H to zeros:
    H = np.zeros((n_basis,n_basis))
    
    #Fill diagonal of H with the energies at zero field and add appropriated scaled multiple of V.
    np.fill_diagonal(H,E0) 
    
    H -= charge*field*V                      #Use negatively signed field.

    return H


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# 
# ## &#x1f4da; References
# My favorite sources for this material are:
# - [Randy's book](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/DumontBook.pdf?raw=true) (See Chapter 3)
# - [McQuarrie and Simon summary](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Map%3A_Physical_Chemistry_(McQuarrie_and_Simon)/05%3A_The_Harmonic_Oscillator_and_the_Rigid_Rotor)
# - [Rogelio's notes](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/HarmonicOscillator.pdf?raw=true)
# - [Python Notebook for Morse Oscillator](https://scipython.com/blog/the-morse-oscillator/)
# - [Vasan, V.S., Cross, R.J., 1983. Matrix elements for Morse oscillators. The Journal of Chemical Physics 78, 3869–3871.](https://aip.scitation.org/doi/10.1063/1.445164) Matrix elements for the Morse Oscillator in a field.
# - [Emanuel F de Lima and José E M Hornos 2005 J. Phys. B: At. Mol. Opt. Phys. **38** 815](https://iopscience.iop.org/article/10.1088/0953-4075/38/7/004/meta) Matrix elements for the Morse Oscillator in a field including the continuum.
# 
# There are also some excellent wikipedia articles:
# - [Harmonic Oscillator](https://en.wikipedia.org/wiki/Quantum_harmonic_oscillator)
# - [Morse Oscillator](https://en.wikipedia.org/wiki/Morse_potential)
# - [Other exactly solvable models](https://en.wikipedia.org/wiki/List_of_quantum-mechanical_systems_with_analytical_solutions)
