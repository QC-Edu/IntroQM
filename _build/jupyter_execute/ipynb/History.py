#!/usr/bin/env python
# coding: utf-8

# # From Newton to Schr&ouml;dinger
# 
# ## &#x1f945; Learning Objectives
# - To learn about the historical origins of quantum mechanics.
# - To introduce wave-particle duality and key concepts like the
#   - Planck-Einstein relation for the energy of a photon
#   - Einstein-Compton-De Broglie relation between momentum and wavelength
#   - quantization of energy levels
# - To introduce the Schr&ouml;dinger equation and the probabilistic interpretation thereof.

# ## What is Quantum Mechanics
# Starting in the late 1800’s, experimental physicists began to make observations that challenged the “classical” equations of physics.  What emerged was quantum mechanics. Quantum mechanics unifies and supersedes the theories of classical Newtonian mechanics and classical Maxwellian electromagnetism.  
# 
# In classical physics, radiation and matter are inherently different:  radiation and matter are governed by different physical laws and modeled with different equations.  Quantum mechanics abolishes the inherent difference between radiation and matter.  Radiation—e.g., light—has properties (a well-defined energy and momentum) that are associated with matter.  Matter—e.g., an electron—has properties (a wavelength) that are associated with radiation.  
# 
# The wave-like-ness of matter immediately leads to something called quantization. Matter is “chunky.”  There is no such thing as “half an electron.”  One always has an integer number of elementary particles.  So if I give you a system containing some number of electrons, you can safely say that the total mass of the system is

# $$ m_{\text{total}} = n_e m_e $$

# where $m_e$ is the mass of the electron and $n_e$ is a nonnegative integer. Using mass-energy equivalence, this means that the energy of these electrons should also be discrete

# $$ E_{\text{total}} = n_e m_e c^2 $$

# where $c$ is the speed of light.
#   
# Waves, however do not seem to be "chunky". If I want to put more energy into a wave, I can increase its amplitude or increase its frequency (by an noninteger amount).  So it would seem possible to make waves with any amount of energy.  It was Max Planck, in 1900, that proposed that there should also be a “quantization” of radiation, and that radiation should come in integer chunks, with the energy proportional to the frequency of the radiation:

# $$ E_{\text{total}} \propto n_{ph} \nu_{ph} $$

# The proportional constant is called *Planck's constant*:

# $$ E_{\text{total}} = h n_{ph} \nu_{ph} $$

# where

# $$
# \begin{align}
# h &= 6.626 \cdot 10^{-34} \; \text{J} \cdot \text{s} \\\\
#   &= 6.626 \cdot 10^{-34} \; \tfrac{\text{kg} \cdot \text{m}^2}{\text{s}} \\\\
#   &= 6.626 \cdot 10^{-34} \; \tfrac{\text{V} \cdot \text{s}}{\text{C}}
# \end{align}
# $$

# Planck's constant is very small, which explains why electromagnetic radiation does not seem to be "chunky" in everyday life. Similarly, the masses and charges of elementary particles are very small, which is why Newtonian mechanics is accurate enough to describe macroscopic phenomena. However, it is essential to include quantum effects when we deal with particles with very little mass (e.g., electrons). 
#   
# Planck proposed the quantization of radiation as a mathematical trick to provide a model for blackbody radiation.  In 1905, Einstein interpreted this trick in the most literal possible way, proposing the quantization of light.  This interpretation led to an interpretation of the photoelectric effect, which eventually earned Einstein the Nobel Prize in Physics.  Planck also won the Nobel Prize in physics.  

# ## How was Quantum Mechanics Discovered?
# It is impossible to fully explain the historical foundations of quantum mechanics in a course like this one.  Instead, I will try to give you a very brief overview of some key experiments that changed physics.
# 
# 
# 
# ### [Black-body Radiation](https://en.wikipedia.org/wiki/Black-body_radiation)
# ![Color temperature](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/colortemp.jpg?raw=true "Light bulbs are rated based on the temperature of a black body that would have a similar spectrum; image from inlineelectric.com/color_temperature")
# ![Black-body radiation](https://upload.wikimedia.org/wikipedia/commons/1/19/Black_body.svg "The radiation of black body shifts from predominately in the infrared to lower wavelength--red-hot and white-hot, glowing in the visible--as the temperature increases. Classical theory predicts is accurate only at high wavelengths, erroneously predicting an ultraviolet catastrophe with intense radiation emitted at very short frequencies.")  
# 
# An inflammable object that absorbs all incident light, but does not transmit or reflect light, is called a black body. Because it is totally opaque and absorbs all light that falls upon it, a black body at zero Kelvin is the very definition of black. However, when you heat a blackbody, it glows. A good (but not perfect) example of a black body is a red-hot poker. An even better example is the sun.  Blackbody radiation has been observed by humans for millennia (or even longer): lava flows, molten glass, molten metal, and many other materials can be considered blackbodies. So it was extremely embarrassing to 19th-century physicists that they could not predict the spectrum—that is, which wavelengths of light occur with what intensity—of a blackbody. 
#   
# In principle the spectrum of a black body should be easy to describe with classical statistical mechanics. However, classical statistical mechanics predicted that most of the light emitted would have a very short wavelength, the so-called "ultraviolet catastrophe." Planck suggested that the vibrations of atoms in a black body, and ergo the light emitted therefrom, was quantized into chunks. Planck understood that his result was significant, but he still thought of it as a mathematical trick. 
# 
# ### [Photoelectric Effect](https://en.wikipedia.org/wiki/Photoelectric_effect)
# ![Photoelectric Effect](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/photoelectric.png?raw=true "In the photoelectric effect, light with enough energy to ionize electrons from a metal causes the electrons to emit, with maximum kinetic energy proportional to the excess energy of the photon beyond the work function of the metal. Image from hyperphysics.")
# 
# When one shines light on a metal surface, one observes that if the light has a low enough frequency (long enough wavelength), then no electrons escape from the surface. This holds (to an excellent approximation) no matter how intense the light is. However, with a sufficiently high frequency (short enough wavelength), electrons will start to escape from the surface. Importantly, the maximum kinetic energy of the electrons escaping from the surface grows as the frequency of the light increases, and the number of electrons escaping from the surface grows as the intensity of the light increases. But increasing the intensity of the light does not increase the maximum kinetic energy of the emitted electrons, nor does increasing the frequency of the light increase the number of electrons emitted.
# 
# Einstein decided to take Planck's mathematical expression at face value, and interpret light as coming in chunks called photons, with energy given by Planck's expression:

# $$ E_{ph} = h \nu_{ph} $$

# This allowed him to describe the photoelectric effect. Specifically, whenever $h \nu $ was less than a threshold value for the substance called its work function, $W$, no light would be emitted. (The work function can be thought of as the "ionization potential" for a metal.) But when $h \nu > W$, then photons had enough energy to remove an electron from the metal, and the surplus energy from the photon could be imparted to the electron as kinetic energy. Ergo

# $$ \text{Kinetic Energy}_{\text{max}} = h \nu - W $$

# As the light becomes more intense, the number of photons increases and the number of electrons emitted increases but, unless the light is very, very, very intense, the maximum kinetic energy of the electrons is left unaltered.
# 
# ### [Compton Effect](https://en.wikipedia.org/wiki/Compton_scattering)
# ![Compton Scattering](https://upload.wikimedia.org/wikipedia/commons/e/e3/Compton-scattering.svg "Shows how photons can inelastically scatter with electrons consistent with conservation of energy and momentum, licensed by Jabberwok under CC-SA 3")
# 
# When you shine light on an (isolated) electron sitting at rest, sometimes the light scatters inelastically&mdash;that is the emitted light has a lower frequency than the incident light. The change in energy between the incident and emitted light is manifest in the kinetic energy of the electron. However, it's observed that the electron does not move in an arbitrary direction, but instead moves in the direction that would be expected if a photon were a classical particle moving at the speed of light with effective mass $m_{ph,\text{eff}} = \tfrac{h \nu}{c^2}$. Note that the photon does not actually have mass. However, the photon does have momentum, which explains the inelastic scattering result. The formula is derived by *assuming* that one can set the rest-mass-energy expression, $E = m c^2$, to the Planck relation for the energy of a photon. Then 

# $$
# \begin{align}
# m_{ph,\text{eff}} c^2 &= h \nu \\\\
# m_{ph,\text{eff}} &= \tfrac{h \nu}{c^2}
# \end{align} 
# $$

# and the momentum of the photon would be its effective mass times its speed, $c$:

# $$ p_{ph} = \tfrac{h \nu}{c} $$

# Recall that the wavelength, $\lambda$, and frequency, $\nu$ of light are related according to the relation

# $$ \nu = \tfrac{c}{\lambda} $$

# This means that the momentum of light can be expressed as

# $$ p_{ph} = \tfrac{h}{\lambda} $$

# This is called the [De Broglie relation](https://en.wikipedia.org/wiki/Matter_wave). One of the key results of quantum mechanics is that the De Broglie relation holds for both waves (photons) and particles.
# 
# ### [Davisson-Germer Experiment](https://en.wikipedia.org/wiki/Davisson%E2%80%93Germer_experiment)
# ![Electron Double Slit Experiment](https://upload.wikimedia.org/wikipedia/commons/6/69/Interference_electrons_double-slit_at_10cm.png "Double slit experiment with electrons showing constructive and deconstructive interference. Licensed by Alexandre Gondran under CC-SA 4")
# 
# Based on the results of Compton and De Broglie, one should expect that a beam of electrons should diffract, with patterns of constructive and deconstructive interference, according to their wavelength. The Davisson-Germer experiment confirmed this, showing that electrons (particles) can constructively and deconstructively interfere like waves.
# 
# ### [Rydberg Formula](https://en.wikipedia.org/wiki/Rydberg_formula)
# ![Rydberg Formula](https://upload.wikimedia.org/wikipedia/commons/2/21/Visible_spectrum_of_hydrogen.jpg "The Rydberg formula describes the observed emission/absorption wavelengths for any 1-electron atom. Here is the visible spectrum of the Hydrogen atom, licensed Jan Homan under CC-SA 3")
# 
# By the late 1800s, it was known that when an dilute atomic gas was heated, it did not emit as a black body, but only at certain characteristic wavelengths. Rydberg managed to describe the specific wavelengths of the emission by the empirical formula
# 
# $$
# \frac{1}{\lambda} \propto \frac{1}{n^2} - \frac{1}{m^2}
# $$
# 

# where $n$ and $m$ are positive integers: $n,m = 1,2,3,4,\ldots$. Recalling the link between frequency and wavelength, $\nu = \tfrac{c}{\lambda}$ and the Planck-Einstein relation for the energy of a photon,
# 
# $$
# h \nu \propto \frac{1}{n^2} - \frac{1}{m^2}
# $$
# 
# This suggests that photons are associated with transitions between energy levels that are labelled by indices, suggesting that the electronic energy levels of atoms are not arbitrary, but only have certain, quantized, values. The Rydberg formula is accurate for all one-electron atoms (at least until relativistic effects become nonneglible). It is also valid for highly-excited states (so-called Rydberg excitations) of many-electron atoms, where a single highly-excited electron is much further from the nucleus than the other electrons.
# 
# ### Wave-Particle Duality
# 
# 
# > It seems as though we must use sometimes the one theory and sometimes the other, while at times we may use either. We are faced with a new kind of difficulty. We have two contradictory pictures of reality; separately neither of them fully explains the phenomena ... but together they do.
#     - Albert Einstein
# 
# The previous experiments, among many others, established that particles like electrons have wave-like properties, that electromagnetic radiation is composed of discrete photons with particle-like momentum and energy. The fact particles possess wave-like properties and waves provide particle-like properties is called [wave-particle duality](https://en.wikipedia.org/wiki/Wave%E2%80%93particle_duality): there is only one type of "stuff" in the universe and that stuff is "chunky" (like particles) and can constructively and deconstructively interfere (like waves). Moreover, the energies of atoms and molecules are quantized, having only specific discrete values.

# ## The Schr&ouml;dinger Equation
# 
# ![Schrodinger Equation](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/GraveSchrodinger.png?raw=true "The grave of Schrodinger, with his equation. Image from Victor Blacus licensed under Creative Commons SA 3")
# 
# It seems that, in physics, the more we learn, the simpler things become. We used to believe that there were two types of things, "particles" (matter) and "waves" (radiation). Now we understand that there is really only one type of entity, perhaps call it a *wavicle* if you must give it a name. Electromagnetic radiation comes in discrete chunks (photons) just like particles (e.g., electrons). Photons and particles have position(ish), momentum(ish), and energy(ish), just like classical particles of matter; both also can manifest constructive and deconstructive interference, just like classical waves. The difference between matter and radiation is merley one of perspective.
# 
# In 1925-26, Heisenberg and Schr&ouml;dinger, working independently, built mathematical frameworks to describe the wave-particle duality of quantum particles. Nowadays we usually (except sometimes in spectroscopy) prefer Schr&ouml;dinger's formulation. We will discuss the Schr&ouml;dinger equation in more detail in the next unit, but for now it is worth merely comparing it to other equations from classical mechanics and classical electromagnetism, just to intuitively show how it encapsulates wave-particle duality. Of course, a [more rigorous justification for the Schr&ouml;dinger equation](http://en.wikipedia.org/wiki/Theoretical_and_experimental_justification_for_the_Schr%C3%B6dinger_equation) is beyond the scope of this course.
#   
# For simplicity, we will only consider systems in one dimension.
# > [**Wave Equation**](https://en.wikipedia.org/wiki/Wave_equation) (classical electromagnetism)
# > 
# $$
# \frac{d^2u(x,t)}{dt^2} = c^2 \frac{d^2u(x,t)}{dx^2}
# $$
# 
#   
# > [**Hamilton-Jacobi Equation**](https://en.wikipedia.org/wiki/Hamilton%E2%80%93Jacobi_equation) (classical mechanics)
# > 
# $$
# -\frac{dS(x,t)}{dt} = H 
# $$
# 
# > where $H = T + V$ is the sum of the kinetic energy, $T$, and the potential energy, $V$, written a function of $S$, $x$, and $t$. In the simplest case, one has: 
# > 
# $$
# -\frac{dS(x,t)}{dt} = \left( \frac{1}{2m} \frac{dS(x,t)}{dx} \cdot \frac{dS(x,t)}{dx} + V(x,t) \right)
# $$
# 
# > because the momentum can be identified as $p(x,t) = \tfrac{dS(x,t)}{dx} $.
# 
# > [**Schr&ouml;dinger Equation**](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation) (quantum mechanics)
# > 
# $$ \frac{i h}{2 \pi} \frac{d \Psi(x,t)}{dt} =  \left( -\frac{h^2}{2m (2 \pi)^2 } \frac{d^2 \Psi(x,t)}{dx^2} + V(x,t)\Psi(x,t) \right) $$
# 
# The solution, $\Psi(x,t)$ to the Schr&ouml;dinger equation is called the [*wavefunction*](https://en.wikipedia.org/wiki/Wave_function). A key postulate of quantum mechanics is that the wavefunction contains all the information needed to fully specify the observable properties of a quantum system. 
# 
# All three equations have strong resemblance. But, in particular, the Schr&ouml;dinger equation and the Hamilton-Jacobi equation are consistent with each other. Suppose one uses the wavefunction ansatz,
# 
# $$ \Psi(x,t) = \psi_0(x,t) e^{\frac{2 \pi i S(x,t)}{h}} $$
# 
# where $\psi_0(x,t)$ and $S(x,t)$ are, without loss of generality, assumed to be real-valued functions. We will insert this expression into the Schr&ouml;dinger equation, but first it is useful to define the quantity 
# $$ \hbar = \tfrac{h}{2 \pi} $$
# 
# One then can rewrite the wavefunction and the Schr&ouml;dinger equation without the pesky factors of $2 \pi$, respectively,
# 
# $$ \Psi(x,t) = \psi_0(x,t) e^{\frac{i S(x,t)}{\hbar}} $$
# 
# $$ i \hbar \frac{d \Psi(x,t)}{dt} =  \left( -\frac{\hbar^2}{2m} \frac{d^2 \Psi(x,t)}{dx^2} + V(x,t)\Psi(x,t) \right) $$
# Inserting the wavefunction into the Schr&ouml;dinger equation, the left-hand-side is
# 
# $$
#  i \hbar \frac{d \Psi(x,t)}{dt} =e^{\frac{i S(x,t)}{\hbar}} \left( i \hbar \frac{d \psi_0(x,t)}{dt}-\psi_0(x,t) \frac{d S(x,t)}{dt} \right)
# $$
# 
# and the right-hand-side is
# 
# $$
# \begin{align}
# & \left( -\frac{\hbar^2}{2m} \frac{d^2 \Psi(x,t)}{dx^2} +V(x,t)\Psi(x,t) \right) \\\\
# & = e^{\frac{i S(x,t)}{\hbar}} \left(-\frac{\hbar^2}{2m} \frac{d^2 \psi_0(x,t)}{dx^2} - \frac{i \hbar}{m}\frac{d \psi_0(x,t)}{dx}\frac{d S(x,t)}{dx} - \frac{i \hbar}{2m} \psi_0(x,t) \frac{d^2 S(x,t)}{dx^2} + \frac{1}{2m}\psi_0(x,t)\left(\frac{d S(x,t)}{dx}\right)^2 + V(x,t) \psi_0(x,t) \right) 
# \end{align}
# $$
# 
# Inserting these equations into the Schr&ouml;dinger equation and dividing through by $e^{\frac{i S(x,t)}{\hbar}}$ gives:
# 
# $$
# \begin{align} 
# & \left( i \hbar \frac{d \psi_0(x,t)}{dt}-\psi_0(x,t) \frac{d S(x,t)}{dt} \right) \\\\
# & = \left(-\frac{\hbar^2}{2m} \frac{d^2 \psi_0(x,t)}{dx^2} - \frac{i \hbar}{m}\frac{d \psi_0(x,t)}{dx}\frac{d S(x,t)}{dx} - \frac{i \hbar}{2m} \psi_0(x,t) \frac{d^2 S(x,t)}{dx^2} + \frac{1}{2m}\psi_0(x,t)\left(\frac{d S(x,t)}{dx}\right)^2 + V(x,t) \psi_0(x,t) \right) 
# \end{align}
# $$
# 
# The real and imaginary parts of this equation must be separately equal to each other. The real part of the equation is 
# 
# $$
# \begin{align}
# -\psi_0(x,t) \frac{d S(x,t)}{dt}
# = \left(-\frac{\hbar^2}{2m} \frac{d^2 \psi_0(x,t)}{dx^2} + \frac{1}{2m}\psi_0(x,t)\left(\frac{d S(x,t)}{dx}\right)^2 + V(x,t) \psi_0(x,t) \right) 
# \end{align}
# $$
# 
# Dividing both sides by $\psi_0(x,t)$ and taking the classical limit, where $\hbar \rightarrow 0$, gives back the Hamilton-Jacobi equation,
# 
# $$ - \frac{d S(x,t)}{dt}
# = \left(\frac{1}{2m}\left(\frac{d S(x,t)}{dx}\right)^2 + V(x,t) \right) $$
# 
# The imaginary part of the equation is:
# 
# $$ \hbar \frac{d \psi_0(x,t)}{dt} 
# = - \left(\frac{\hbar}{m}\frac{d \psi_0(x,t)}{dx}\frac{d S(x,t)}{dx} + \frac{\hbar}{2m} \psi_0(x,t) \frac{d^2 S(x,t)}{dx^2} \right) $$
# 
# We notice that this expression is zero in the classical limit. Dividing through by $\hbar$ and using the chain rule, $\frac{d \left(\psi_0(x,t)\right)^2}{dt} = 2 \psi_0(x,t) \frac{d \psi_0(x,t)}{dt}$, we can rewrite this expression as
# 
# $$ \frac{d \left(\psi_0(x,t)\right)^2}{dt} 
# = - \frac{d}{dx} \left(\psi_0(x,t)\right)^2 \left(\frac{1}{m}\frac{d S(x,t)}{dx}\right) $$
# 
# This expression resembles the [*equation of continuity*](https://en.wikipedia.org/wiki/Continuity_equation) from classical physics,
# 
# $$ \frac{d \rho(x,t)}{dt} = -\nabla \cdot \rho(x,t) \nabla v(x,t) $$
# 
# where $v(x,t)$ is the velocity and $\rho(x,t)$ is the density, the probability of observing a particle at the point $x$ and the time $t$. This (re)confirms that $\nabla S$ is an expression for the momentum, and suggests that
# 
# $$\rho(x,t) = \psi_0(x,t)^2 = \Psi(x,t) \Psi(x,t)^* = |\Psi(x,t)|^2 $$ 
# 
# is an expression for the probability of observing a particle at a point in space. The identification of the square-magnitude of the quantum-mechanical wavefunction with probability is called the [*Born postulate*](https://en.wikipedia.org/wiki/Born_rule).
# 
# 
# In the end, the Schr&ouml;dinger equation was not accepted because of its mathematical elegance, but because it worked to accurately describe key phenomena. In fact, as we shall see, the (originally empirical) Rydberg formula can be easily justified using the Schr&ouml;dinger equation.
# 
# We can rationalize the form of the quantum mechanical momentum operator, $\hat{p} = -i \hbar \frac{d}{dx} $
# , by a similar argument. Applying the hypothesized momentum operator to the wavefunction, one obtains:
# 
# $$
# \begin{align}
# -i \hbar \frac{d\Psi(x,t)}{dx} &= -i \hbar \frac{d\psi_0(x,t)}{dx} e^{\frac{i S(x,t)}{\hbar}} + \psi_0(x,t) e^{\frac{i S(x,t)}{\hbar}} \frac{dS(x,t)}{dx} \\\\
# &= \text{[imaginary part]} + \frac{dS(x,t)}{dx} \Psi(x,t) \\\\
# &= \text{[imaginary part]} + \text{[classical expression for momentum]}\Psi(x,t)
# \end{align}
# $$
# 
# This indicates that the quantum-mechanical momentum operator is consistent with the classical expression for the momentum, to which it reduces in the classical limit where $\hbar \rightarrow 0$.
# 

# ## &#x1fa9e; Self-Reflection
# Imagine you were assigned to describe Quantum Mechanics to a room full of irrascible tweens. 
# - How would you motivate them to be interested in quantum mechanics? 
# - How would you describe wave-particle duality in a way they could understand? 

# ## &#x1f914; Thought-Provoking Questions
# - Is it possible for the wavelength of the scattered photon in Compton Scattering to be infinite? (I.e., could the photon be entirely absorbed?)
# - What are the units of the wavefunction?

# ## &#x1f501; Recapitulation
# - What are the following phenomena/experiments/theories, and why were they important to the establishment of the quantum theory?
#   - black-body radiation and the ultraviolet catastrophe
#   - the photoelectric effect
#   - Compton scattering
#   - the Davisson-Germer experiment (and electron scattering/diffraction in general)
#   - the spectral lines of one-electron atoms, and the Rydberg relation
# - What are the following key equations, and why are they important?
#   - Planck-Einstein relation for the energy of a photon
#   - De Broglie relation between momentum and wavelength
#   - the Schr&ouml;dinger equation
# - What is the quantum mechanical operator for the momentum of a particle?
# - List as many properties/characteristics of the wavefunction as you can.

# ## &#x1f52e; Next Up...
# - Motivate the time-dependent Schr&ouml;dinger equation
# - Derive the time-independent Schr&ouml;dinger equation
# - Explore the quantum-mechanical operator for momentum
# - Study simple one-dimensional Hamiltonians

# ## &#x1f4da; References
# My favorite sources for this material are:
# - R. Eisberg and R. Resnick, Quantum Physics of Atoms, Molecules, Solids, Nuclei, and Particles (Wiley, New York, 1974)
# - R. Dumont, [An Emergent Reality, Part 2: Quantum Mechanics](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/DumontBook.pdf?raw=true) (Chapters 1 and 2).
# - Also see my (pdf) class [notes](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/IntroQM.pdf?raw=true).
# - The introductory material in [Davit Potoyan's](https://www.chem.iastate.edu/people/davit-potoyan) Jupyter-book course is very good. Roughly [chapters 1 and 2](https://dpotoyan.github.io/Chem324/intro.html) are especially relevant here.
# 
# There are also some excellent wikipedia articles:
# - On General Quantum Mechanics
#   - [Introduction to Quantum Mechanics](http://en.wikipedia.org/wiki/Introduction_to_quantum_mechanics)
#   - [Quantum Mechanics](http://en.wikipedia.org/wiki/Quantum_mechanics)
#   - [Mathematical Formulation of Quantum Mechanics](http://en.wikipedia.org/wiki/Mathematical_formulation_of_quantum_mechanics)
#   - [Basic Concepts of Quantum Mechanics](http://en.wikipedia.org/wiki/Basic_concepts_of_quantum_mechanics). See [also].(https://github.com/PaulWAyers/IntroQChem/blob/main/documents/quantum_summary.pdf?raw=true)
#   - [Planck's Constant](http://en.wikipedia.org/wiki/Planck_constant)
#   - [Wave-particle Duality](http://en.wikipedia.org/wiki/Wave-particle_duality)
# - Black-Body Radiation
#   - [What is a Black Body?](http://en.wikipedia.org/wiki/Black_body)
#   - [Ultraviolet Catastrophe](http://en.wikipedia.org/wiki/Ultraviolet_catastrophe)
#   - [Raleigh-Jeans Law for Classical Black Bodies](http://en.wikipedia.org/wiki/Rayleigh-Jeans_law)
#   - [Planck's Law for Black-Body Radiation](http://en.wikipedia.org/wiki/Planck%27s_law)
#   - [Wien's Displacement Law for the Peak Wavelength of a Black Body](http://en.wikipedia.org/wiki/Wien%27s_displacement_law)
# - [Photoelectric Effect](http://en.wikipedia.org/wiki/Photoelectric_effect)
# - [Compton Scattering](http://en.wikipedia.org/wiki/Compton_scattering)
# - [De Broglie Wavelength](http://en.wikipedia.org/wiki/Matter_wave)
# - Electron/Particle Diffraction
#   - [Davisson-Germer Experiment](http://en.wikipedia.org/wiki/Davisson%E2%80%93Germer_experiment)
#   - [Electron Diffraction](http://en.wikipedia.org/wiki/Electron_diffraction)
#   - [Electron Crystallography](http://en.wikipedia.org/wiki/Electron_crystallography)
#   - [Electron Microscope](http://en.wikipedia.org/wiki/Electron_microscopy)
#   - [Transmission Electron Microscope](http://en.wikipedia.org/wiki/Transmission_Electron_Microscopy)
# - Spectral lines in simple atoms
#   - [Franck-Hertz Experiment, the first experiment to show discrete atomic energy levels](http://en.wikipedia.org/wiki/Franck%E2%80%93Hertz_experiment)
#   - [Balmer formula, a predecessor of the Rydberg formula](http://en.wikipedia.org/wiki/Balmer_series)
#   - [Rydberg formula](http://en.wikipedia.org/wiki/Rydberg_formula)
#   - [Spectral Lines](http://en.wikipedia.org/wiki/Spectral_line)
#   - [Atomic Spectral Lines](http://en.wikipedia.org/wiki/Atomic_spectral_line)
# - Schr&ouml;dinger Equation
#   - [Schr&ouml;dinger Equation](http://en.wikipedia.org/wiki/Schrodinger_equation)
#   - [Theoretical Justification of S.E.](http://en.wikipedia.org/wiki/Theoretical_and_experimental_justification_for_the_Schr%C3%B6dinger_equation). See [also](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/SchrodingerHJeq.pdf?raw=true).
#   - [Momentum Operator](http://en.wikipedia.org/wiki/Momentum_operator)

# 
