#!/usr/bin/env python
# coding: utf-8

# # The Schr&ouml;dinger Equation
# 
# >The underlying physical laws necessary for the mathematical theory of a large part of physics and the whole of chemistry are thus completely known, and the difficulty is only that the exact application of these laws leads to equations much too complicated to be soluble. It therefore becomes desirable that approximate practical methods of applying quantum mechanics should be developed, which can lead to an explanation of the main features of complex atomic systems without too much computation.
#     - Paul A. M. Dirac (1929)
# 
# 
# ## &#x1f945; Learning Objectives
# - Review of Plane Wave(functions)
# - "Derivation" of the Time-Dependent Schr&ouml;dinger Equation (TDSE)
# - The Hamiltonian
# - The Time-Independent Schr&ouml;dinger Equation (TISE)
# - Separation of Variables Method

# ## Motivation for the Schr&ouml;dinger Equation
# Just like Newton’s equations or Maxwell’s equations, the Schrödinger equation is a law of nature:  it cannot be “derived.”  Instead, it must be postulated, and then tested by experiment.  However, just as Newton’s equations can be justified insofar as they encapsulate the “laws of motion” formulated by Galileo and Newton, and Maxwell’s equations can be justified insofar as they encapsulate the “laws of electromagnetism” formulated by Gauss, Faraday, Coulomb, etc., Schr&ouml;dinger's equation can be justified by observing that it encapsulates the “laws” of Planck and De Broglie, namely that
# 
# $$ E = h \nu = \hbar \omega $$
# 
# $$ p = \tfrac{h}{\lambda} = \tfrac{h \nu}{c} = \hbar k = h \tilde{\nu} $$
# 
# ### Angular Frequency and Wavenumber
# In these equations I have introduced several new symbols, mostly related to the fact it is often convenient to use angular frequency, 
# 
# $$ \omega = 2 \pi \nu $$
# 
# which naturally pairs with 
# 
# $$ \hbar = \tfrac{h}{2 \pi} $$
# 
# Similarly, it is often convenient, especially in spectroscopic studies, to use wavenumber,
# 
# $$ \tilde{\nu} = \tfrac{1}{\lambda} = \lambda^{-1} $$
# 
# or its angular analogue
# 
# $$ k = \tfrac{2 \pi}{\lambda} = 2 \pi \tilde{nu} $$
# 
# Sometimes it is also useful to consider the period of the wave, 
# 
# $$ \text{T}  = \nu^{-1} $$
# 
# Recall that the wavelength, frequency, period, and wavenumber of a wave can be related to the speed of light by relations like:
# 
# $$ c = \lambda \nu = \tfrac{\lambda}{\text{T}} = \tilde{\nu} \nu $$
# 
# $$ c = \tfrac{\omega}{k} $$

# #### &#x1f4dd; Exercise: The photon emitted when a 4p electron in the Hydrogen atom deexcites into a 2s orbital has wavelength 486.1 nm. Compute its
# - **frequency in Hz**
# - **angular frequency in Hz**
# - **wavenumber, $\bar{\nu}$, in $\text{cm}^{-1}$.**
# - **angular wavenumber, $k$, in $\text{m}^{-1}$.**
# - **period in s.**
# - **momentum in m kg/s.**
# - **energy in Joules.**
# [Answer](SchrodingerExercise1.ipynb)

# ![1D Plane Wave](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/planewave1D.gif?raw=true? "Visualization of a the real part of a 1-dimensional travelling plane wave, from Szilágyi, András (2019): EMANIM: Interactive visualization of electromagnetic waves. Web application available at URL https://emanim.szialab.org")

# ### The Wavefunction
# 
# The use of angular frequency and wave number is especially useful when dealing with waves, because the need to explicitly include factors of $2 \pi$ to describe the periodic oscillations is removed. A one-dimensional plane wave, moving in the $x$ direction, with amplitude $A$, wavelength $\lambda = \tfrac{2 \pi}{k}$, and frequency $\nu = \tfrac{\omega}{2 \pi}$ is described by
# 
# $$ \Psi(x,t) = A e^{i (kx - \omega t)} = A\left(\cos(kx-\omega t) + i \sin(kx - \omega t) \right) $$
# 
# Since $\Psi(x,t)$ is the function that describes a wave, we call it a "wavefunction." 
# 
# ### Expression for the Total Energy
# Based on electromagnetism, we believe this equation should give us the essential insight we need to describe the "waviness of particles." We need, however, a second equation that will allow us to describe the "particulateness of waves." Since the energy of a wave is proportional to $\omega$ (Planck-Einstein relation) and the momentum of a wave is proportional to $k$ (De Broglie relation), an equation that relates the energy to the momentum is an obvious candidate. For example,
# 
# 
# $$
# \begin{align}
# \text{energy} &= \text{kinetic energy} + \text{potential energy}\\
# E &= T + V(x,t)\\
# E &= \frac{p^2}{2m} + V(x,t) 
# \end{align}
# $$
# 

# ### The Time-Dependent Schr&ouml;dinger Equation (TDSE)
# We need to find a way to combine the key equations from the previous two sections. To do this, note that
# 
# $$ \frac{\partial \Psi(x,t)}{\partial t} = (-i \omega) A e^{i (kx - \omega t)} = (-i \omega) \Psi(x,t) $$
# 
# We can link this to Planck's equation for the energy of a photon by multiplying both sides by $i \hbar$, 
# 
# $$
# \begin{align}
# i \hbar \frac{\partial \Psi(x,t)}{\partial t} &= (i \hbar) (-i \omega) \Psi(x,t)  = \hbar \omega \Psi(x,t) \\
# &= E \Psi(x,t) 
# \end{align}
# $$
# 
# Similarly, differentiating with respect to position,
# 
# $$
# \begin{align}
# \frac{\partial \Psi(x,t)}{\partial x} &= (i k) A e^{i (kx - \omega t)} \\
# \frac{\partial^2 \Psi(x,t)}{\partial x^2} &= (i k)^2 A e^{i (kx - \omega t)} = -k^2 \Psi(x,t) 
# \end{align}
# $$
# 
# Multiplying both sides by $-\hbar^2$ provides a link to the De Broglie relation,
# 
# $$
# -\hbar^2 \frac{\partial^2 \Psi(x,t)}{\partial x^2} = (\hbar k)^2 \Psi(x,t) = p^2 \Psi(x,t)
# $$
# 
# Now, let's consider our expression for the energy,
# 
# $$
# \begin{align}
# E &= \frac{p^2}{2m} + V(x,t) \\
# E \Psi(x,t) &= \frac{p^2}{2m} \Psi(x,t) + V(x,t)\Psi(x,t)
# \end{align}
# $$
# 
# Substituting in the equations for the energy and the momentum-squared in terms of wavefunction derivatives, we have:
# 
# $$ i \hbar \frac{\partial \Psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi(x,t)}{\partial x^2} + V(x,t)\Psi(x,t) $$
# 
# This is the [*time-dependent Schr&ouml;dinger equation*](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation#Time-dependent_equation), which we often abbreviate as the TDSE.
# 
# The biggest limitations of the Schrödinger equation is that it was derived using the nonrelativistic expression for the kinetic energy of a particle, $T = \tfrac{p^2}{2m}$. For this reason, the Schrödinger equation is not valid for particles that are moving at a substantial fraction of the speed of light (where relativistic effects are important) or for light itself. Quantum mechanics can be extended to such cases, and relativistic quantum mechanics is quite important for the heavier atoms in the periodic table. (Typically relativity is neglected for atoms up to Zinc (Z=30) or Krypton (Z=36), and the included past that. However there are a few molecules containing lighter elements&mdash;e.g., the Sulfur dimer&mdash;where there are chemically (or at least spectroscopically) interesting relativistic effects.) The full relativistic treatment of quantum mechanics leads to “quantum electrodynamics,” which is a rich and interesting subject that we, alas, will not have time to cover.  

# #### &#x1f4dd; Exercise: Show that the time-dependent Schr&ouml;dinger equation for the complex conjugate of the wavefunction, $\Psi^*$, is:
# $$ 
# -i \hbar \frac{d \Psi^*(x,t)}{dt} = - \frac{\hbar}{2m} \frac{d^2 \Psi^*(x,t)}{dx^2} + V(x,t)\Psi^*(x,t) 
# $$
# 
# #### &#x1f4dd; Exercise: What is the complex conjugate of 
# $$ 
# \Psi(x,t) = A e^{(a+bi)(kx - \omega t)} 
# $$
# [Answer](SchrodingerExercise2.ipynb)

# ### The Hamiltonian
# An equation like Schr&ouml;dinger’s may seem mysterious to us now, but at the time it was derived it seemed very natural. A top-rate physicist like Schr&ouml;dinger had a rich background in classical physics, and he would have understood that there were many results, from classical physics, that suggested that the equations for radiation and for matter could be combined.  One of the strongest such suggestions came from two principles: “Fermat’s principle of least time” and the “Hamilton-Lagrange principle of least action.” Fermat’s principle says that a ray of light goes from point A to point B in the fastest possible way, and can be used to derive all of classical optics. The Hamilton-Lagrange principle says that a particle goes from point A to point B in a way that makes minimizes its action (the product of its momentum and its change in position) along the path. Schr&ouml;dinger would have noticed that Planck’s constant had units of action, and then quickly ascertained that laws of quantum mechanics might be governed by an equation similar to the Hamilton-Jacobi equation for the action, 
# 
# 
# $$\frac{1}{2m}\left(\frac{\partial S}{\partial x}\right)^2 + V(x,t) = \frac{\partial S}{\partial t} $$
# 
# or, equivalently,
# 
# $$ S \left(-\frac{1}{2m} \frac{\partial^2S}{\partial x^2} + V(x,t) \right) = \frac{\partial S}{\partial t} - \frac{1}{2m}\frac{\partial^2S^2}{\partial x^2}$$
# 
# The second term on the right-hand-side of this equation ordinarily integrates to zero (owing to the divergence theorem).
# 
# Similarly, as hinted at in the previous set of notes, the Schr&ouml;dinger equation can be deduced from the (quantum-mechanical) principle of least (really stationary) action. Indeed, the stationary-action principle is more fundamental than the Schr&ouml;dinger equation, and is the basis for quantum electrodynamics, which is the relativistic theory for matter and electromagnetic radiation that undergirds classical mechanics and classical electromagnetism (in the $\hbar \rightarrow 0$ limit) and the Schr&ouml;dinger equation (for nonrelativistic matter, without concern for how matter and radiation interact). Feynman and Schwinger won the Nobel Prize for quantum electrodynamics, but its origins go back to Schr&ouml;dinger's and Dirac's observations about the links between the (least) action principle and the Schr&ouml;dinger equation.
# 
# The Schr&ouml;dinger equation is usually written in the form:
# 
# $$ {\color{blue}\left( -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2}+V(x,t)\right)} \Psi(x,t) = i \hbar \frac{\partial \Psi(x,t)}{\partial t} $$
# 
# The term in <span style="color:blue">blue</span> is the [Hamiltonian](https://en.wikipedia.org/wiki/Hamiltonian_(quantum_mechanics)) operator, $\hat{H}(x,t)$; it is the operator for the energy in quantum mechanics. In classical mechanics, the [Hamiltonian](https://en.wikipedia.org/wiki/Hamiltonian_mechanics) is exactly the equation that we started with when we wrote a (classical) expression for the energy of matter, $H(x,t) = \tfrac{p^2}{2m} + V(x,t)$. 
# 
# Using the Hamiltonian, we can then write the TDSE in a compact form,  
# 
# $$ {\color{blue}\hat{H}(x,t)}\Psi(x,t) = i \hbar \frac{\partial \Psi(x,t)}{\partial t} $$
# 
# As in classical mechanics, the Hamiltonian is the operator for the energy. In quantum mechanics, every observable quantity corresponds to an operator. For example, the kinetic energy operator is
# 
# $$ \hat{T} = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} $$
# 
# Moreover, the values of the properties of any quantum-mechanical operator correspond to its eigenvalues,
# 
# $$ (\text{operator}) \Psi = (\text{eigenvalue}) \Psi $$
# 
# This suggests that there should be another equation with the form
# 
# $$ \hat{H}\Psi = E \Psi $$
# 
# This equation is called the [time-independent Schr&ouml;dinger equation](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation#Time-independent_equation) (TISE).
# 
# My father, an organic chemist, always says he knew that quantum mechanics would be problematic the first time he saw the Schr&ouml;dinger equation. He still refers to $\Psi$ as "Satan's pitchfork" and $\hat{H}$ as the "hell operator." Most people, however, call $\hat{H}$ the Hamiltonian and $\Psi$ the wavefunction.

# #### &#x1f4dd; Exercise: Ground-State Energy of the Morse Potential
# The Morse potential is often used as an approximate model for the vibrations of diatomic molecules. In convenient units where $\frac{\hslash ^{2}}{2m}=1$, the time-independent Schr&ouml;dinger equation for a Morse oscillator can be written as:
# 
# $$
# \left(-\frac{d^{2}}{dx^{2}}+\lambda ^{2}\left(e^{-2x}-2e^{-x}\right)\right)\psi _{n}\left(x\right)=E_{n}\psi _{n}\left(x\right)
# $$
# 
# 
# The first two eigenfunctions of the Morse oscillator are given by the following expressions (which are not normalized)
# $$
# \begin{align}
# \psi _{0}\left(x\right)&=\exp \left(-\left(\lambda -\tfrac{1}{2}\right)x-\lambda e^{-x}\right)\\
# \psi _{1}\left(x\right)&=\exp \left(-\left(\lambda -\tfrac{3}{2}\right)x-\lambda e^{-x}\right)\left(2\lambda -2-2\lambda e^{-x}\right)
# \end{align}
# $$  
# 
# **What is the expression for the ground-state energy for the Morse oscillator?**
# 
# [Answer](SchrodingerExercise3.md)

# ### The Time-Independent Schr&ouml;dinger Equation (TISE)
# In much of chemistry, the Hamiltonian operator is not time-dependent.  For examples, the electrons in a molecule feel a fixed (time-independent) attraction to the nuclei in the molecule and, to a first approximation, the (very small) motion of the nuclei can be neglected.  Similarly, in the absence of a time-varying external field, a molecule as a whole (containing both electrons and nuclei) does not feel a time-varying potential. 
# 
# To derive the time-independent Schr&ouml;dinger equation, we insert the time-independent Hamiltonian, 
# 
# $$\hat{H}(x) = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} +V(x)$$
# 
# into the time-dependent Schr&ouml;dinger equation,
# 
# $$ \hat{H}(x)\Psi(x,t) = i \hbar \frac{\partial \Psi(x,t)}{\partial t} $$
# 
# and then rearrange the equation into the form
# 
# $$ \left( \hat{H}(x) - i\hbar \frac{\partial}{\partial t} \right) \Psi(x,t) = 0 $$
# 
# This is a differential equation that can be solved by the general technique of [separation of variables](https://en.wikipedia.org/wiki/Separation_of_variables). Specifically,
# 
# > [**Separation of Variables**](https://en.wikipedia.org/wiki/Separation_of_variables#Partial_differential_equations) Given an operator that is a sum of two operators that depend on different (sets of) variables,
# 
# $$ \hat{A}(x,y) = \hat{A}_x(x) + \hat{A}_y(y) $$
# 
# The solution to the eigenvalue equation
# 
# $$ \hat{A}(x,y) \Psi(x,y) = a \Psi(x,y) $$
# 
# is 
# 
# $$\Psi(x,y) = \Psi_x(x) \cdot \Psi_y(y) $$
# 
# $$ a = a_x + a_y $$
# 
# where 
# 
# $$\hat{A}_x(x) \Psi_x(x) = a_x \Psi_x(x) $$
# 
# $$\hat{A}_y(y) \Psi_y(y) = a_y \Psi_y(y) $$
# 
# 
# This tells us that for a time-independent Hamiltonian, the wavefunction has the form $\Psi(x,t) = \psi(x) \phi(t)$, where
# 
# $$\hat{H}(x) \psi(x) = E \psi(x) $$
# 
# $$- i\hbar \frac{\partial}{\partial t} \phi(t) = -E\phi(t) $$
# 
# In the first equation, we have chosen the eigenvalue of the TDSE to be the energy since we know that the Hamiltonian is the quantum-mechanical operator for the energy. The second equation is a separable differential equation, which can be solved as follows:
# 
# $$
# \begin{align}
# -i\hbar \frac{\partial}{\partial t} \phi(t) &= -E\phi(t) \\
# \frac{1}{\phi} d\phi &= -\frac{i}{\hbar}E dt \\ 
# \int \frac{1}{\phi} d\phi = \int \frac{-i}{\hbar}E dt \\
# \ln \phi(t) &= \frac{-iEt}{\hbar} + \text{constant of integration}\\
# \phi(t)  &\propto e^{\frac{-iEt}{\hbar}}
# \end{align}
# $$
# 
# Therefore,
# 
# $$ \Psi(x,t) = \psi(x) \phi(t) \propto \psi(x) e^{\frac{-iEt}{\hbar}} $$
# 
# The constant of proportionality is not important here, because the time-dependent and time-independent Schr&ouml;dinger equations are satisfied even if $\Psi(x)$ and $\phi(t)$ are multiplied by constants.
# 

# ## Summary
# When solving the time-independent Schr&ouml;dinger equation, we need to find all the possible values of E that solve this equation. There are almost always very many different values of E that work and, for this reason, we usually label the solutions to the equation, which are the eigenfunctions (eigenvectors) and eigenvalues of the Hamiltonian operator, accordingly:
# 
# $$ \hat{H}(x)\psi_k(x) = E_k \psi_k(x) $$
# 
# This course is largely about the “art” of solving the TISE
# 
# Sometimes in chemistry we cannot use the time-independent Schr&ouml;dinger equation, and need to use the time-dependent Schr&ouml;dinger equation instead. This is particular important in spectroscopy, where we want to understand how a molecule responds to a time-dependent external electromagnetic field.
# 

# ## &#x1fa9e; Self-Reflection
# The Hamiltonian operator enters the Schr&ouml;dinger equation in a special way, and in this sense is a "more important" operator than other quantum-mechanical operators. Why do you think this is the case? 

# ## &#x1f914; Thought-Provoking Questions
# - Once upon a time, one of the professors at McMaster was asked "why is the quantum-mechanical momentum operator associated with the derivative" and, unable to answer the student, sent the student to me for clarification. Can you justify why the quantum mechanical momentum operator is $\hat{p} = -i \hbar \nabla$?
# - Once upon a time, a person interviewing for a job as a quantum chemist was asked how it was possible that the kinetic energy of a quantum system was always positive, given that the quantum-mechanical operator for the kinetic energy was "the negative of something squared", namely, $\hat{T} = \tfrac{-1}{2m}\nabla^2$. How would you answer this question?
# - What are the eigenfunctions of the momentum operator?
# - What are the eigenfunctions of the kinetic-energy operator?
# - Is every eigenfunction of the momentum operator also an eigenfunction of the kinetic-energy operator? Is the [converse](https://en.wikipedia.org/wiki/Converse_(logic)) also true? 
# - Suppose that one has an electron that is tethered to the origin by a spring, so that the force the electrons feels towards the origin, $x=0$, increases proportionally to its distance, $F = -kx$. What would the Hamiltonian be?
# - What are the eigenfunctions of the kinetic-energy operator?
# - What are the eigenfunctions of the momentum operator?
# - Show, mathematically, that the eigenvectors and eigenvalues of a separable operator, $\hat{A}(x,y) = \hat{A}(x) + \hat{A}(y)$ are given by the above expressions.

# ## &#x1f501; Recapitulation
# - Write the quantum-mechanical operator for the energy, kinetic-energy, potential energy, and momentum.
# - Write the time-independent and time-dependent Schr&ouml;dinger equations.
# - What is the form of the time-dependent wavefunction that solves the TDSE when the Hamiltonian is time-independent.
# 
# ## &#x1f52e; Next Up...
# - Study a particle confined to a box with infinite sides.
# - Explore the postulates of quantum mechanics.

# ## &#x1f4da; References
# My favorite sources for this material are:
# - R. Eisberg and R. Resnick, Quantum Physics of Atoms, Molecules, Solids, Nuclei, and Particles (Wiley, New York, 1974)
# - R. Dumont, [An Emergent Reality, Part 2: Quantum Mechanics](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/DumontBook.pdf?raw=true) (Chapters 1 and 2).
# - Also see my (pdf) class [notes](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/IntroQM.pdf?raw=true).
# - [Davit Potoyan's](https://www.chem.iastate.edu/people/davit-potoyan) Jupyter-book course "derives" the Schrodinger equation in a somewhat different way. [Chapter 3](https://dpotoyan.github.io/Chem324/Lec3-0.html) is especially relevant here.
# 
# There are also some excellent wikipedia articles:
# - [Plane Wave](https://en.wikipedia.org/wiki/Sinusoidal_plane_wave)
# - [Wavelength-Frequency Relation](https://en.wikipedia.org/wiki/Wavelength)
# - Schr&ouml;dinger Equation
#   - [Schr&ouml;dinger Equation](http://en.wikipedia.org/wiki/Schrodinger_equation)
#   - [Theoretical Justification of S.E.](http://en.wikipedia.org/wiki/Theoretical_and_experimental_justification_for_the_Schr%C3%B6dinger_equation).
#   - [Momentum Operator](http://en.wikipedia.org/wiki/Momentum_operator)
