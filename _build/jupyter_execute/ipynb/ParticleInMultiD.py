#!/usr/bin/env python
# coding: utf-8

# ![Particles in 2D confinement](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/MVZL4.jpg?raw=true "Particles in various types of 2-dimensional confinement")
# 
# # Multi-dimensional Particle-in-a-Box
# 
# ## 🥅 Learning Objectives
# - Hamiltonian for a two-dimensional particle-in-a-box
# - Hamiltonian for a three-dimensional particle-in-a-box
# - Hamiltonian for a 3-dimensional spherical box
# - Separation of variables
# - Solutions for the 2- and 3- dimensional particle-in-a-box (rectangular)
# - Solutions for the 3-dimensional particle in a box (spherical)
# - Expectation values

# ## The 2-Dimensional Particle-in-a-Box
# ![Particles in a 2-dimensional box](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/1024px-Particle2D.svg.png?raw=true "Particles in 2-dimensional box with nx=ny=2; image from wikipedia courtesy of Keenan Pepper")
# We have treated the particle in a one-dimensional box, where the (time-independent) Schr&ouml;dinger equation was:
# 
# $$ 
# \left(-\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V(x) \right)\psi_n(x) = E_n \psi_n(x)
# $$
# 
# where 
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
# However, electrons really move in three dimensions. However, just as sometimes electrons are (essentially) confined to one dimension, sometimes they are effectively confined to two dimensions. If the confinement is to a rectangle with side-widths $a_x$ and $a_y$, then the Schr&ouml;dinger equation is:
# 
# $$ 
# \left(-\frac{\hbar^2}{2m} \frac{d^2}{dx^2} -\frac{\hbar^2}{2m} \frac{d^2}{dy^2} + V(x,y) \right)\psi_{n_x,n_y}(x,y) = E_{n_x,n_y} \psi_{n_x,n_y}(x,y)
# $$
# 
# where
# 
# $$
# V(x,y) = 
# \begin{cases}
#     +\infty & x\leq 0 \text{ or }y\leq 0 \\
#     0       & 0\lt x \lt a_x \text{ and } 0 \lt y \lt a_y \\
#     +\infty & a_x \leq x \text{ or } a_y \leq y
# \end{cases}
# $$
# 
# The first thing to notice is that there are now two quantum numbers, $n_x$ and $n_y$. 
# > The number of quantum numbers that are needed to label the state of a system is equal to its dimensionality.
# 
# The second thing to notice is that the Hamiltonian in this Schr&ouml;dinger equation can be written as the sum of two Hamiltonians,
# 
# $$ 
# \left[\left(-\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V_x(x) \right)
# +\left(-\frac{\hbar^2}{2m} \frac{d^2}{dy^2} + V_y(y) \right) \right]\psi_{n_x,n_y}(x,y) = E_{n_x,n_y} \psi_{n_x,n_y}(x,y)
# $$
# 
# where 
# 
# $$
# V_x(x) = 
# \begin{cases}
#     +\infty & x\leq 0\\
#     0       & 0\lt x \lt a_x\\
#     +\infty & a_x \leq x
# \end{cases} \\
# V_y(y) = 
# \begin{cases}
#     +\infty & y\leq 0\\
#     0       & 0\lt y \lt a_y\\
#     +\infty & a_y \leq y
# \end{cases}
# $$
# 
# By the same logic as we used for the 1-dimensional particle in a box, we can deduce that the ground-state wavefunction for an electron in a rectangular box is:
# 
# $$
# \psi_{n_x n_y}(x,y) = \frac{2}{\sqrt{a_x a_y}} \sin\left(\tfrac{n_x \pi x}{a_x}\right) \sin\left(\tfrac{n_y \pi y}{a_y}\right) \qquad \qquad n_x=1,2,3,\ldots;n_y=1,2,3,\ldots
# $$
# 
# The corresponding energy is thus:
# 
# $$
# E_{n_x n_y} =  \frac{h^2}{8m}\left(\frac{n_x^2}{a_x^2}+\frac{n_y^2}{a_y^2}\right)\qquad \qquad n_x,n_y=1,2,3,\ldots
# $$
# 

# ## &#x1f4dd; Exercise: Verify the above equation for the energy eigenvalues of a particle confined to a rectangular box.

# ## Separation of Variables
# The preceding solution is a very special case of a general approach called separation of variables. 
# > Given a $D$-dimensional Hamiltonian that is a sum of independent terms,
# 
# $$
# \hat{H}(x_1,x_2,\ldots,x_D) = \sum_{d=1}^D\hat{H}_d(x_d)
# $$
# 
# where the solutions to the individual Schr&ouml;dinger equations are known:
# 
# $$
# \hat{H}_d \psi_{d;n_d}(x_d) = E_{d;n_d} \psi_{d;n_d}(x_d)
# $$
# 
# the solution to the $D$-dimensional Schr&ouml;dinger equation is
# 
# $$
# \hat{H}(x_1,x_2,\ldots,x_D) \Psi_{n_1,n_2,\ldots,n_D}(x_1,x_2,\ldots,x_D) = E_{n_1,n_2,\ldots,n_D}\Psi_{n_1,n_2,\ldots,n_D}(x_1,x_2,\ldots,x_D)
# $$
# 
# where the $D$-dimensional eigenfunctions are products of the Schr&ouml;dinger equations of the individual terms
# 
# $$
# \Psi_{n_1,n_2,\ldots,n_D}(x_1,x_2,\ldots,x_D) = \prod_{d=1}^D\psi_{d;n_d}(x_d)
# $$
# 
# and the $D$-dimensional eigenvalues are sums of the eigenvalues of the individual terms,
# 
# $$
# E_{n_1,n_2,\ldots,n_D} = \sum_{d=1}^D E_{d;n_d}
# $$
# 
# This expression can be verified by direct substitution. Interpretatively, in a Hamiltonian with the form 
# 
# $$
# \hat{H}(x_1,x_2,\ldots,x_D) = \sum_{d=1}^D\hat{H}_d(x_d)
# $$
# 
# the coordinates $x_1,x_2,\ldots,x_D$ are all independent, because there are no terms that couple them together in the Hamiltonian. This means that the probability of observing a particle with values $x_1,x_2,\ldots,x_D$ are all independent. Recall that when probabilities are independent, they are multiplied together. E.g., if the probability that your impoverished professor will be paid today is independent of the probability that will rain today, then 
# 
# $$
# p_{\text{paycheck + rain}} = p_{\text{paycheck}} p_{\text{rain}}
# $$
# 
# Similarly, because $x_1,x_2,\ldots,x_D$ are all independent,
# 
# $$
# p(x_1,x_2,\ldots,x_D) = p_1(x_1) p_2(x_2) \ldots p_D(x_D)
# $$
# 
# Owing to the Born postulate, the probability distribution function for observing a particle at $x_1,x_2,\ldots,x_D$ is the wavefunction squared, so 
# 
# $$
# \left| \Psi_{n_1,n_2,\ldots,n_D}(x_1,x_2,\ldots,x_D)\right|^2 = \prod_{d=1}^D \left| \psi_{d;n_d}(x_d) \right|^2
# $$
# 
# It is reassuring that the separation-of-independent-variables solution to the $D$-dimensional Schr&ouml;dinger equation reproduces this intuitive conclusion.

# #### &#x1f4dd; Exercise: By direct substitution, verify that the above expressions for the eigenvalues and eigenvectors of a Hamiltonian-sum are correct.

# #### &#x1f4dd; Exercise: Write the Time-Dependent Schr&ouml;dinger equation for one particle, in three dimensions, confined by the time-dependent potential $V(x,y,z,t)$.
# [Answer](MultiDExercise1.md)

# ## Degenerate States
# When two quantum states have the same energy, they are said to be degenerate. For example, for a square box, where $a_x = a_y = a$, the states with $n_x=1; n_y=2$ and $n_x=2;n_y=1$ are degenerate because:
# 
# $$
# E_{1,2} =  \frac{h^2}{8ma^2}\left(1+4\right) = \frac{h^2}{8ma^2}\left(4+1\right) = E_{2,1}
# $$
# 
# This symmetry reflects physical symmetry, whereby the $x$ and $y$ coordinates are equivalent. The state with energy $E=\frac{5h^2}{8ma^2}$ is said to be two-fold degenerate, or to have degeneracy of two. 
# 
# For the particle in a square box, degeneracies of all levels exist. An example of a three-fold degeneracy is:
# 
# $$
# E_{1,7} = E_{7,1} = E_{5,5} = \frac{50h^2}{8ma^2}
# $$
# 
# and an example of a four-fold degeneracy is: 
# 
# $$
# E_{1,8} = E_{8,1} = E_{7,4} = E_{4,7} = \frac{65h^2}{8ma^2}
# $$
# 
# It isn't trivial to show that degeneracies of all orders are possible (it's tied up in the theory of [Diophantine equations](https://en.wikipedia.org/wiki/Diophantine_equation)), but perhaps it becomes plausible by giving an example with an eight-fold degeneracy:
# 
# $$
# E_{8,49} = E_{49,8} = E_{16,47} = E_{47,16} = E_{23,44} = E_{44,23} = E_{28,41} = E_{41,28}  = \frac{2465 h^2}{8ma^2}
# $$
# 
# Notice that all of these degeneracies are removed if the symmetry of the box is broken. For example, if a slight change of the box changes it from square to rectangulary, $a_x \rightarrow a_x + \delta x$, then the aforementioned states have different energies. This doesn't mean, however, that rectangular boxes do not have degeneracies. If $\tfrac{a_x}{a_y}$ is a rational number, $\tfrac{p}{q}$, then there will be an *accidental* degeneracies when $n_x$ is divisible by $p$ and $n_y$ is divisible by $q$. For example, if $a_x = 2a$ and $a_y = 3a$ (so $p=2$ and $q=3$), there is a degeneracy associated with  
# 
# $$
# E_{4,3} =  \frac{h^2}{8m}\left(\frac{4^2}{(2a)^2}+\frac{3^2}{(3a)^2}\right) 
# =  \frac{h^2}{8m}\left(\frac{2^2}{(2a)^2}+\frac{6^2}{(3a)^2}\right) = \frac{5h^2}{8ma^2}= E_{2,6}
# $$
# 
# This is called an *accidental* degeneracy because it is not related to a symmetry of the system, like the $x \sim y$ symmetry that induces the degeneracy in the case of particles in a square box. 

# ## Electrons in a 3-dimensional box (cuboid)
# ![Particles in a 3-dimensional box](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/Particle3Dbox.png?raw=true "Particles in 3-dimensional box; image from Gary Drobny's online notes at Univ. of Washington")
# 
# Suppose that particles are confined to a [cuboid](https://en.wikipedia.org/wiki/Cuboid) (or rectangular prism) with side-lengths $a_x$, $a_y$, and $a_z$. Then the Schr&ouml;dinger equation is:
# 
# $$ 
# \left[-\frac{\hbar^2}{2m}\left( \frac{d^2}{dx^2} + \frac{d^2}{dy^2} + \frac{d^2}{dz^2} \right) + V(x,y,z) \right]\psi_{n_x,n_y,n_z}(x,y,z) = E_{n_x,n_y,n_z} \psi_{n_x,n_y,n_z}(x,y,z)
# $$
# 
# where 
# 
# $$
# V(x,y,z) = 
# \begin{cases}
#     +\infty & x\leq 0 \text{ or }y\leq 0 \text{ or }z\leq 0 \\
#     0       & 0\lt x \lt a_x \text{ and } 0 \lt y \lt a_y  \text{ and } 0 \lt z \lt a_z \\
#     +\infty & a_x \leq x \text{ or } a_y \leq y \text{ or } a_z \leq z
# \end{cases}
# $$
# 
# There are three quantum numbers because the system is three-dimensional. 
# 
# The three-dimensional second derivative is called the Laplacian, and is denoted 
# 
# $$
# \nabla^2 =  \frac{d^2}{dx^2} + \frac{d^2}{dy^2} + \frac{d^2}{dz^2} = \nabla \cdot \nabla
# $$
# 
# where 
# 
# $$
# \nabla = \left[ \frac{d}{dx}, \frac{d}{dy}, \frac{d}{dz} \right]^T
# $$
# 
# is the operator that defines the gradient vector. The 3-dimensional momentum operator is 
# 
# $$
# \hat{\mathbf{p}} = -i \hbar \nabla
# $$
# 
# which explains why the kinetic energy is given by
# 
# $$
# \hat{T} = \frac{\hat{\mathbf{p}} \cdot \hat{\mathbf{p}}}{2m} = -\frac{\hbar^2}{2m} \nabla^2
# $$
# 
# As with the 2-dimensional particle-in-a-rectangle, the 3-dimensional particle-in-a-cuboid can be solved by separation of variables. Rewriting the Schr&ouml;dinger equation as:
# 
# $$ 
# \left[\left(-\frac{\hbar^2}{2m} \frac{d^2}{dx^2} + V_x(x) \right)
# +\left(-\frac{\hbar^2}{2m} \frac{d^2}{dy^2} + V_y(y) \right) 
# +\left(-\frac{\hbar^2}{2m} \frac{d^2}{dz^2} + V_z(z) \right) \right]\psi_{n_x,n_y,n_z}(x,y,z) = E_{n_x,n_y,n_z} \psi_{n_x,n_y,n_z}(x,y,z)
# $$
# 
# where 
# 
# $$
# V_x(x) = 
# \begin{cases}
#     +\infty & x\leq 0\\
#     0       & 0\lt x \lt a_x\\
#     +\infty & a_x \leq x
# \end{cases} \\
# V_y(y) = 
# \begin{cases}
#     +\infty & y\leq 0\\
#     0       & 0\lt y \lt a_y\\
#     +\infty & a_y \leq y
# \end{cases} \\
# V_z(z) = 
# \begin{cases}
#     +\infty & z\leq 0\\
#     0       & 0\lt z \lt a_z\\
#     +\infty & a_z \leq z
# \end{cases} 
# $$
# 
# By the same logic as we used for the 1-dimensional particle in a box, we can deduce that the ground-state wavefunction for an electron in a cuboid is:
# 
# $$
# \psi_{n_x n_y n_z}(x,y,z) = \frac{2\sqrt{2}}{\sqrt{a_x a_y a_z}} \
# \sin\left(\tfrac{n_x \pi x}{a_x}\right) \sin\left(\tfrac{n_y \pi y}{a_y}\right)\sin\left(\tfrac{n_z \pi z}{a_z}\right) \qquad \qquad n_x=1,2,3,\ldots;n_y=1,2,3,\ldots;n_z=1,2,3,\ldots
# $$
# 
# The corresponding energy is thus:
# 
# $$
# E_{n_x n_y n_z} =  \frac{h^2}{8m}\left(\frac{n_x^2}{a_x^2}+\frac{n_y^2}{a_y^2}+\frac{n_z^2}{a_z^2}\right)\qquad \qquad n_x,n_y,n_z=1,2,3,\ldots
# $$
# 
# As before, especially when there is symmetry, there are many degenerate states. For example, for a particle-in-a-cube, where $a_x = a_y = a_z = a$, the first excited state is three-fold degenerate since:
# 
# $$
# E_{2,1,1} = E_{1,2,1} = E_{1,1,2} = \frac{6h^2}{8ma^2}
# $$
# 
# There are other states of even higher degeneracy. For example, there is a twelve-fold degenerate state:
# 
# $$
# E_{5,8,15} = E_{5,15,8} = E_{8,5,15} = E_{8,15,5} = E_{15,5,8} = E_{15,8,5} = E_{3,4,17} = E_{3,17,4} = E_{4,3,17} = E_{4,17,3} = E_{17,3,4} = E_{17,4,3} = \frac{314 h^2}{8ma^2}
# $$
# 

# ## &#x1f4dd; Exercise: Verify the expressions for the eigenvalues and eigenvectors of a particle in a cuboid.

# ## &#x1f4dd; Exercise: Construct an accidentally degenerate state for the particle-in-a-cuboid. 
# (Hint: this is a lot easier than you may think.)

# ## Particle-in-a-circle
# ### The Schr&ouml;dinger equation for a particle confined to a circular disk.
# ![Particle in a Ring](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/The_Well_(Quantum_Corral).jpg?raw=true "The states of particle confined by a ring of atoms (a quantum corral) is similar to a particle-in-acircle. Image licensed CC-SA by Julian Voss-Andreae")
# 
# What happens if instead of being confined to a rectangle or a cuboid, the electrons were confined to some other shape? For example, it is not uncommon to have electrons confined in a circular disk ([quantum corral](https://en.wikipedia.org/wiki/Quantum_mirage)) or a sphere ([quantum dot](https://en.wikipedia.org/wiki/Quantum_dot)). It is relatively easy to write the Hamiltonian in these cases, but less easy to solve it because Cartesian (i.e., $x,y,z$) coordinates are less natural for these geometries. 
# 
# The Schr&ouml;dinger equation for a particle confined to a circular disk of radius $a$ is:
# 
# $$ 
# \left(-\frac{\hbar^2}{2m} \nabla^2 + V(x,y) \right)\psi(x,y) = E \psi(x,y)
# $$
# 
# where 
# 
# $$
# V(x,y) = 
# \begin{cases}
#     0 & \sqrt{x^2 + y^2} \lt a\\
#     +\infty & a \leq \sqrt{x^2 + y^2}
# \end{cases}
# $$
# 
# However, it is more useful to write this in polar coordinates (i.e., $r,\theta$):
# 
# $$
# \begin{align}
# x &= r \cos \theta \\
# y &= r \sin \theta \\
# \\
# r &= \sqrt{x^2 + y^2} \\
# \theta &= \arctan{\tfrac{y}{x}}
# \end{align}
# $$
# 
# because the potential depends only on the distance from the center of the system,
# 
# $$ 
# \left(-\frac{\hbar^2}{2m} \nabla^2 + V(r) \right)\psi(r,\theta) = E \psi(r,\theta)
# $$
# 
# where
# 
# $$
# V(r) = 
# \begin{cases}
#     0 & r \lt a\\
#     +\infty & a \leq r
# \end{cases}
# $$
# 

# ### The Schr&ouml;dinger Equation in Polar Coordinates
# In order to solve this Schr&ouml;dinger equation, we need to rewrite the Laplacian, $\nabla^2 = \frac{d^2}{dx^2} + \frac{d^2}{dy^2}$ in polar coordinates. Deriving the Laplacian in alternative coordinate systems is a standard (and tedious) exercise that you hopefully saw in your calculus class. (If not, cf. [wikipedia](https://en.wikipedia.org/wiki/Laplace_operator) or this [meticulous derivation](https://www.math.ucdavis.edu/~saito/courses/21C.w11/polar-lap.pdf).) The result is that:
# 
# $$
# \nabla^2 = \frac{d^2}{dr^2} + \frac{1}{r} \frac{d}{dr} + \frac{1}{r^2}\frac{d^2}{d\theta^2}
# $$
# 
# The resulting Schr&ouml;dinger equation is,
# 
# $$
# \left[-\frac{\hbar^2}{2m} \left(\frac{d^2}{dr^2} + \frac{1}{r} \frac{d}{dr} + \frac{1}{r^2}\frac{d^2}{d\theta^2} \right)+ V(r)  \right] \psi(r,\theta) = E \psi(r,\theta)
# $$
# 
# This looks like it might be amenable to solution by separation of variables insofar as the potential doesn't compute the radial and angular positions of the particles, and the kinetic energy doesn't couple the particles angular and radial momenta (i.e., the derivatives). So we propose the solution $\psi(r,\theta) = R(r) \Theta(\theta)$. Substituting this into the Schr&ouml;dinger equation, we obtain:
# 
# $$
# \begin{align}
# \left[-\frac{\hbar^2}{2m} \left(\frac{d^2}{dr^2} + \frac{1}{r} \frac{d}{dr} + \frac{1}{r^2}\frac{d^2}{d\theta^2} \right)+ V(r)  \right] R(r) \Theta(\theta) &= E R(r) \Theta(\theta) \\
# \left[-\Theta(\theta)\frac{\hbar^2}{2m} \left(\frac{d^2 R(r)}{dr^2} + \frac{1}{r} \frac{d R(r)}{dr} \right) -\frac{\hbar^2}{2m} \frac{R(r)}{r^2}\left(\frac{d^2 \Theta(\theta)}{d \theta^2} \right) + V(r) R(r) \Theta(\theta)  \right] &= E R(r)\Theta(\theta)
# \end{align}
# $$
# 
# Dividing both sides by $R(r) \Theta(\theta)$ and multiplying both sides by $r^2$ we obtain:
# 
# $$
# E r^2 +\frac{\hbar^2}{2m}\frac{r^2}{R(r)} \left(\frac{d^2 R(r)}{dr^2} + \frac{1}{r} \frac{d R(r)}{dr} \right) - r^2 V(r)=-\frac{\hbar^2}{2m} \frac{1}{\Theta(\theta)}\left(\frac{d^2 \Theta(\theta)}{d \theta^2} \right) 
# $$
# 
# The right-hand-side depends only on $r$ and the left-hand-side depends only on $\theta$; this can only be true for all $r$ and all $\theta$ if both sides are equal to the same constant. This problem can therefore be solved by separation of variables, though it is a slightly different form from the one we considered previously.

# ### The Angular Schr&ouml;dinger equation in Polar Coordinates
# To find the solution, we first solve the set the left-hand-side equal to a constant, which gives a 1-dimensional Schr&ouml;dinger equations for the angular motion of the particle around the circle,
# 
# $$
# -\frac{\hbar^2}{2m} \frac{d^2 \Theta_l(\theta)}{d \theta^2} = E_{\theta;l} \Theta_l(\theta)
# $$
# 
# This equation is identical to the particle-in-a-box, and has (unnormalized) solutions
# 
# $$
# \Theta_l(\theta) = e^{i l \theta} \qquad \qquad l = 0, \pm 1, \pm 2, \ldots
# $$
# 
# where $l$ must be an integer because otherwise the fact the periodicity of the wavefunction (i.e., that $\Theta_l(\theta) = \Theta_l(\theta + 2 k \pi)$ for any integer $k$) is not achieved. Using the expression for $\Theta_l(\theta)$, the angular kinetic energy of the particle in a circle is seen to be:
# 
# $$
# E_{\theta,l} = \tfrac{\hbar^2 l^2}{2m}
# $$
# 

# ### The Radial Schr&ouml;dinger equation in Polar Coordinates
# Inserting the results for the angular wavefunction into the Schr&ouml;dinger equation, we obtain
# 
# $$
# E r^2 +\frac{\hbar^2}{2m}\frac{r^2}{R(r)} \left(\frac{d^2 R(r)}{dr^2} + \frac{1}{r} \frac{d R(r)}{dr} \right) - r^2 V(r)=-\frac{\hbar^2}{2m} \frac{1}{\Theta_l(\theta)}\left(\frac{d^2 \Theta_l(\theta)}{d \theta^2} \right) = \frac{\hbar^2 l^2}{2m}
# $$
# 
# which can be rearranged into the radial Schr&ouml;dinger equation,
# 
# $$
# -\frac{\hbar^2}{2m} \left( \frac{d^2}{dr^2} + \frac{1}{r} \frac{d}{dr} - \frac{l^2}{r^2} \right)R_{n,l}(r) + V(r) R_{n,l}(r) = E_{n,l} R_{n,l}(r)
# $$
# 
# Notice that the radial eigenfunctions, $R_{n,l}(r)$, and the energy eigenvalues, $E_{n,l}$, depend on the angular motion of the particle, as quantized by $l$. The term $\frac{\hbar^2 l^2}{2mr^2}$ is exactly the centrifugal potential, indicating that it takes energy to hold a rotating particle in an orbit with radius $r$, and that the potential energy that is required grows with $r^{-2}$. Notice also that no assumptions have been made about the nature of the circular potential, $V(r)$. The preceding analysis holds for *any* circular-symmetric potential.

# ### The Radial Schr&ouml;dinger Equation for a Particle Confined to a Circular Disk
# For the circular disk, where
# 
# $$
# V(r) = 
# \begin{cases}
#     0 & r \lt a\\
#     +\infty & a \leq r
# \end{cases}
# $$
# 
# it is somewhat more convenient to rewrite the radial Schr&ouml;dinger equation as a [homogeneous linear differential equation](https://en.wikipedia.org/wiki/Homogeneous_differential_equation)
# 
# $$
# -\frac{\hbar^2}{2m} \left(r^2 \frac{d^2 R_{n,l}(r)}{dr^2} + r \frac{d R_{n,l}(r)}{dr} + \left[\left(\frac{2m E_{n,l}}{\hbar^2} \right) r^2 - l^2\right]R_{n,l}(r) \right) + r^2 V(r) R_{n,l}(r) = 0
# $$
# 
# Using the specific form of the equation, we have that, for $0 \lt r \lt a$, 
# 
# $$
# -\frac{\hbar^2}{2m} \left(r^2 \frac{d^2 R_{n,l}(r)}{dr^2} + r \frac{d R_{n,l}(r)}{dr} + \left[\left(\frac{2m E_{n,l}}{\hbar^2} \right) r^2 - l^2\right]R_{n,l}(r) \right) = 0
# $$
# 
# While this equation can be solved by the usual methods, that is [beyond the scope of this course](https://opencommons.uconn.edu/cgi/viewcontent.cgi?article=1013&context=chem_educ). However, we recognize that this equation is strongly resembles [Bessel's differential equation](https://en.wikipedia.org/wiki/Bessel_function),
# 
# $$
# x^2 \frac{d^2 f}{dx^2} + x \frac{df}{dx} + \left(x^2 - \alpha^2 \right) f(x) = 0
# $$
# 
# The solutions to Bessel's equation are called the *Bessel functions of the first kind* and denoted, $J_{\alpha}(r)$. However, the radial wavefunction must vanish at the edge of the disk, $R_{n,l}(a) = 0$, and the Bessel functions generally do not satisfy this requirement. Recall that the boundary condition in the 1-dimensional particle in a box was satisfied by moving from the generic solution, $\psi(x) \propto \sin(x)$ to the scaled solution, $\psi(x) \propto \sin(k x)$, where $k=\tfrac{2 \pi}{a}$ was chosen to satisfy the boundary condition. Similarly, we write the solutions as $R_{n,l}(r) \propto J_l(kr)$. Substituting this form into the Schr&ouml;dinger equation and using the fact that:
# 
# $$
# (kr)^n \frac{d^n}{d(kr)^n} = r^n \frac{d^n}{dr^n} \qquad \qquad n=1,2,\ldots 
# $$
# 
# we have
# 
# $$
# -\frac{\hbar^2}{2m} \left((kr)^2 \frac{d^2 J_{l}(kr)}{d(kr)^2} + (kr) \frac{d J_{l}(kr)}{d(kr)} + \left[\left(\frac{2m E_{n,l}}{k^2 \hbar^2} \right) (kr)^2 - l^2\right]J_{l}(kr) \right) = 0
# $$
# 
# Referring back to the Bessel equation, it is clear that this equation is satisfied when 
# 
# $$
# \frac{2m E_{n,l}}{k^2 \hbar^2} = 1
# $$
# 
# or, equivalently,
# 
# $$
# E_{n,l} = \frac{\hbar^2 k^2}{2m}
# $$
# 
# where $k$ is chosen so that $J_l(ka) = 0$. If we label the zeros of the Bessel functions,
# 
# $$
# J_l(x_{n,l}) = 0 \qquad \qquad n=1,2,3,\ldots \\
# x_{1,l} \lt x_{2,l} \lt x_{3,l} \lt \cdots
# $$
# 
# then 
# 
# $$
# k_{n,l} = \frac{x_{n,l}}{a}
# $$
# 
# and the energies of the particle-in-a-disk are
# 
# $$
# E_{n,l} = \frac{\hbar^2 x_{n,l}^2}{2ma^2} = \frac{h^2 x_{n,l}^2}{8 m \pi^2 a^2}
# $$
# 
# and the eigenfunctions of the particle-in-a-disk are:
# 
# $$
# \psi_{n,l}(r,\theta) \propto J_{l}\left(\frac{x_{n,l}r}{a} \right) e^{i l \theta}
# $$
# 

# ### Eigenvalues and Eigenfunctions for a Particle Confined to a Circular Disk
# ![Vibrations of a Circular Drum-Head](https://upload.wikimedia.org/wikipedia/commons/b/bc/Vibrating_drum_Bessel_function.gif "An eigenfunction of the Particle-in-a-Circle. CC-SA4 license by Sławomir Biały at English Wikipedia")
# The energies of a particle confined to a circular disk of radius $a$ are:
# 
# $$
# E_{n,l} = \frac{\hbar^2 x_{n,l}^2}{2ma^2} = \frac{h^2 x_{n,l}^2}{8 m \pi^2 a^2} \qquad \qquad n=1,2,\ldots; \quad l=0,\pm 1,\pm 2, \ldots
# $$
# 
# and its eigenfunctions are:
# 
# $$
# \psi_{n,l}(r,\theta) \propto J_{l}\left(\frac{x_{n,l}r}{a} \right) e^{i l \theta}
# $$
# 
# where $x_{n,l}$ are the zeros of the Bessel function, $J_l(x_{n,l}) = 0$. The first zero is $x_{1,0} = 2.4048$. These solutions are exactly the resonant energies and modes that are associated with the vibration of a circular drum whose membrane has uniform thickness/density. 
# 
# You can find elegant video animations of the eigenvectors of the particle-in-a-circle at the following links:
# - [Interactive Demonstration of the States of a Particle-in-a-Circular-Disk](https://demonstrations.wolfram.com/ParticleInAnInfiniteCircularWell/)
# - [Movie animation of the quantum states of a particle-in-a-circular-disk](https://www.reddit.com/r/dataisbeautiful/comments/mfx5og/first_70_states_of_a_particle_trapped_in_a/?utm_source=share&utm_medium=web2x&context=3)
# 
# A subtle result, [originally proposed by Bourget](https://en.wikipedia.org/wiki/Bessel_function#Bourget's_hypothesis), is that no two Bessel functions ever have the same zeros, which means that the values of $\{x_{n,l} \}$ are all distinct. A corollary of this is that eigenvalues of the particle confined to a circular disk are either nondegenerate ($l=0$) or doubly degenerate ($|l| /ge 1$). There are no accidental degeneracies for a particle in a circular disk. 
# 
# The energies of an electron confined to a circular disk with radius $a$ Bohr are: 
# 
# $$
# E_{n,l} = \tfrac{x_{n,l}^2}{2a^2}
# $$
# 
# The following code block computes these energies. 

# In[1]:


from scipy import constants
from scipy import special
import ipywidgets as widgets
import mpmath


# In[2]:


# Define a function for the energy (in a.u.) of a particle in a circular disk
# with length a, principle quantum number n, and angular quantum number l
# The length is input in Bohr (atomic units).
def compute_energy_disk(n, l, a):
    "Compute 1-dimensional particle-in-a-spherical-ball energy."
    #Compute the first n zeros of the Bessel function
    zeros = special.jn_zeros(l,n)
    #Compute the energy from the n-th zero.
    return  (zeros[-1])**2/ (2 * a**2)

#This next bit of code just prints out the energy in atomic units
def print_energy_disk(a, n, l):
    print(f'The energy of an electron confined to a disk with radius {a:.2f} a.u.,'
       f' principle quantum number {n}, and angular quantum number {l}'
       f' is {compute_energy_disk(n, l, a):.3f} a.u..')
    
    
#Principle quantum number slider:
n = 1

#Angular quantum number slider:
l = 0

#Box length slider:
a = 1


print_energy_disk(a, n, l)


# ## Particle-in-a-Spherical Ball
# 
# ### The Schr&ouml;dinger equation for a particle confined to a spherical ball
# ![Quantum Dot](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Colloidal_nanoparticle_of_lead_sulfide_%28selenide%29_with_complete_passivation.png/842px-Colloidal_nanoparticle_of_lead_sulfide_%28selenide%29_with_complete_passivation.png "A quantum dot is a model for a particle spherically confined. CC-SA3 licensed by Zherebetskyy")
# 
# The final model we will consider for now is a particle confined to a spherical ball with radius $a$,
# 
# $$ 
# \left(-\frac{\hbar^2}{2m} \nabla^2 + V(x,y,z) \right)\psi(x,y,z) = E \psi(x,y,z)
# $$
# 
# where 
# 
# $$
# V(x,y,z) = 
# \begin{cases}
#     0 & \sqrt{x^2 + y^2 + z^2} \lt a\\
#     +\infty & a \leq \sqrt{x^2 + y^2 + z^2}
# \end{cases}
# $$
# 
# However, it is more useful to write this in spherical polar coordinates (i.e., $r,\theta, \phi$): 
# 
# $$
# \begin{align}
# x &= r \sin \theta \cos \phi\\
# y &= r \sin \theta \sin \phi\\
# z &= r cos \theta \\
# \\
# r &= \sqrt{x^2 + y^2 + z^2} \\
# \theta &= \arccos{\tfrac{z}{r}} \\
# \phi &= \arctan{\tfrac{y}{x}}
# \end{align}
# $$
# 
# because the potential depends only on the distance from the center of the system, 
# 
# $$ 
# \left(-\frac{\hbar^2}{2m} \nabla^2 + V(r) \right)\psi(r,\theta, \phi) = E \psi(r,\theta, \phi)
# $$
# 
# where
# 
# $$
# V(r) = 
# \begin{cases}
#     0 & r \lt a\\
#     +\infty & a \leq r
# \end{cases}
# $$

# ### The Schr&ouml;dinger Equation in Spherical Coordinates
# In order to solve the Schr&ouml;dinger equation for a particle in a spherical ball, we need to rewrite the Laplacian, $\nabla^2 = \frac{d^2}{dx^2} + \frac{d^2}{dy^2} + \frac{d^2}{dz^2}$ in polar coordinates. A meticulous derivation of the [Laplacian](https://en.wikipedia.org/wiki/Laplace_operator) and its [eigenfunctions](http://galileo.phys.virginia.edu/classes/252/Classical_Waves/Classical_Waves.html) The result is that: 
# 
# $$
# \nabla^2 = \frac{1}{r^2}\frac{d}{dr}r^2\frac{d}{dr} + \frac{1}{r^2 \sin \theta}\frac{d}{d\theta}\sin\theta\frac{d}{d\theta} + \frac{1}{r^2 \sin^2 \theta} \frac{d^2}{d\phi^2}
# $$
# 
# which can be rewritten in a more familiar form as:
# 
# $$
# \nabla^2 = \frac{d^2}{dr^2}+ \frac{2}{r}\frac{d}{dr} + \frac{1}{r^2}\left[\frac{1}{\sin \theta}\frac{d}{d\theta}\sin\theta\frac{d}{d\theta} + \frac{1}{\sin^2 \theta} \frac{d^2}{d\phi^2}\right]
# $$
# 
# Inserting this into the Schr&ouml;dinger equation for a particle confined to a spherical potential, $V(r)$, one has:
# 
# $$
# \left({}  -\frac{\hbar^2}{2m} \left( \frac{d^2}{dr^2}
# + \frac{2}{r} \frac{d}{dr}\right) 
#       - \frac{\hbar^2}{2mr^2}\left[\frac{1}{\sin \theta}\frac{d}{d\theta}\sin\theta\frac{d}{d\theta} 
# + \frac{1}{\sin^2 \theta} \frac{d^2}{d\phi^2}\right] \\ 
#       + V(r) \right)\psi_{n,l,m_l}(r,\theta,\phi) 
# = E_{n,l,m_l}\psi_{n,l,m_l}(r,\theta,\phi)
# $$
# 
# The solutions of the Schr&ouml;dinger equation are characterized by three quantum numbers because this equation is 3-dimensional.
# 
# Recall that the classical equation for the kinetic energy of a set of points rotating around the origin, in spherical coordinates, is:
# 
# $$
# T = \sum_{i=1}^{N_{\text{particles}}} \frac{p_{r;i}^2}{2m_i} + \frac{\mathbf{L}_i \cdot \mathbf{L}_i}{2m_i r_i^2} 
# $$
# 
# where $p_{r,i}$ and $\mathbf{L}_i$ are the radial and [angular momenta](https://en.wikipedia.org/wiki/Angular_momentum#In_Hamiltonian_formalism) of the $i^{\text{th}}$ particle, respectively. It's apparent, then, that the quantum-mechanical operator for the square of the angular momentum is:
# 
# $$
# \hat{L}^2 = - \hbar^2 \left[\frac{1}{\sin \theta}\frac{d}{d\theta}\sin\theta\frac{d}{d\theta} 
# + \frac{1}{\sin^2 \theta} \frac{d^2}{d\phi^2}\right]
# $$
# 
# The Schr&ouml;dinger equation for a spherically-symmetric system is thus,
# 
# $$
# \left(-\frac{\hbar^2}{2m} \left( \frac{d^2}{dr^2}
# + \frac{2}{r} \frac{d}{dr}\right) 
#       + \frac{\hat{L}^2}{2mr^2} + V(r) \right)
#       \psi_{n,l,m_l}(r,\theta,\phi) 
# = E_{n,l,m_l}\psi_{n,l,m_l}(r,\theta,\phi)
# $$
# 

# ### The Angular Wavefunction in Spherical Coordinates
# ![Spherical Harmonics](https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Spherical_Harmonics.png/1024px-Spherical_Harmonics.png "Representation of the real spherical harmonics, licensed CC-SA3 by Inigo.quilez")
# 
# The Schr&ouml;dinger equation for a spherically-symmetric system can be solved by separation of variables. If one compares to the result in polar coordinates, it is already clear that the angular wavefunction has the form $\Theta(\theta,\phi) = P(\theta)e^{im_l\phi}$. From this starting point we could deduce the eigenfunctions of $\hat{L}^2$, but instead we will just present the eigenfunctions and eigenvalues,
# 
# $$
# \hat{L}^2 Y_l^{m_l} (\theta, \phi) = \hbar^2 l(l+1)Y_l^{m_l} (\theta, \phi) \qquad l=0,1,2,\ldots m_l=0, \pm 1, \ldots, \pm l
# $$
# 
# The functions [$Y_l^{m_l} (\theta, \phi)$](https://en.wikipedia.org/wiki/Spherical_harmonics) are called [spherical harmonics](https://mathworld.wolfram.com/SphericalHarmonic.html), and they are the fundamental vibrational modes of the surface of a spherical membrane. Note that these functions resemble s-orbitals ($l=0$), p-orbitals ($l=1$), d-orbitals ($l=2$), etc., and that the number of choices for $m_l$, $2l+1$, is equal to the number of $l$-type orbitals.
# 

# ### The Radial Schr&ouml;dinger equation in Spherical Coordinates
# Using separation of variables, we write the wavefunction as:
# 
# $$
# \psi_{n,l,m_l}(r,\theta,\phi) = R_{n,l}(r) Y_l^{m_l}(\theta,\phi) 
# $$
# 
# Inserting this expression into the Schr&ouml;dinger equation, and exploiting the fact that the spherical harmonics are eigenfunctions of $\hat{L}^2$, one obtains the radial Schr&ouml;dinger equation:
# 
# $$
# \left(-\frac{\hbar^2}{2m} \left( \frac{d^2}{dr^2}
# + \frac{2}{r} \frac{d}{dr}\right) 
#       + \frac{\hbar^2 l(l+1)}{2mr^2} + V(r) \right)
#       R_{n,l}(r) 
# = E_{n,l}R_{n,l}(r)
# $$
# 
# Inside the sphere, $V(r) = 0$. Rearranging the radial Schr&ouml;dinger equation for the interior of the sphere as a homogeneous linear differential equation,
# 
# $$
# r^2 \frac{d^2R_{n,l}}{dr^2}
# + 2r \frac{dR_{n,l}}{dr}
# + \left( \frac{2mr^2E_{n,l}}{\hbar^2} - l(l+1) \right)
#       R_{n,l}(r) = 0
# $$
# 
# This equation strongly resembles the differential equations satisfied by the [spherical Bessel functions](https://en.wikipedia.org/wiki/Bessel_function#Spherical_Bessel_functions:_jn,_yn), $j_l(x)$
# 
# $$
# x^2 \frac{d^2 j_l}{dx^2} + 2x \frac{dj_l}{dx} + \left(x^2 - l(l+1) \right)j_l(x) = 0
# $$
# 
# The spherical Bessel functions are eigenfunctions for the particle-in-a-spherical-ball, but do not satisfy the boundary condition that the wavefunction be zero on the sphere, $R_{n,l}(a) = 0$. To satisfy this constraint, we propose
# 
# $$
# R_{n,l}(r) = j_l(k r)
# $$
# 
# Using this form in the radial Schr&ouml;dinger equation, we have
# 
# $$
# (kr)^2 \frac{d^2 j_l(kr)}{d(kr)^2}
# + 2kr \frac{d j_l(kr)}{d(kr)}
# + \left( \frac{2m(kr)^2E_{n,l}}{\hbar^2k^2} - l(l+1) \right)
#       j_l(kr) = 0
# $$
# 
# Referring back to the differential equation satisfied by the spherical Bessel functions, it is clear that this equation is satisfied when 
# 
# $$
# \frac{2m E_{n,l}}{k^2 \hbar^2} = 1
# $$
# 
# or, equivalently,
# 
# $$
# E_{n,l} = \frac{\hbar^2 k^2}{2m}
# $$
# 
# where $k$ is chosen so that $j_l(ka) = 0$. If we label the zeros of the spherical Bessel functions,
# 
# $$
# j_l(y_{n,l}) = 0 \qquad \qquad n=1,2,3,\ldots \\
# y_{1,l} \lt y_{2,l} \lt y_{3,l} \lt \cdots
# $$
# 
# then
# 
# $$
# k_{n,l} = \frac{y_{n,l}}{a}
# $$
# 
# and the energies of the particle-in-a-ball are
# 
# $$
# E_{n,l} = \frac{\hbar^2 y_{n,l}^2}{2ma^2} = \frac{h^2 y_{n,l}^2}{8 m \pi^2 a^2}
# $$
# 
# and the eigenfunctions of the particle-in-a-ball are:
# 
# $$
# \psi_{n,l,m}(r,\theta,\phi) \propto j_l\left(\frac{y_{n,l}r}{a} \right) Y_l^{m_l}(\theta, \phi)
# $$
# 
# Notice that the eigenenergies have the same form as those in the particle-in-a-disk and even the same as those for a particle-in-a-one-dimensional-box; the only difference is the identity of the function whose zeros we are considering.

# ## &#x1f4dd; Exercise: Use the equation for the zeros of $\sin x$ to write the wavefunction and energy for the one-dimensional particle-in-a-box in a form similar to the expressions for the particle-in-a-disk and the particle-in-a-sphere.

# ### Solutions to the Schr&ouml;dinger Equation for a Particle Confined to a Spherical Ball
# ![Eigenfunction Animation](https://upload.wikimedia.org/wikipedia/commons/8/86/Hydrogen_Wave.gif "Schematic of an eigenfunction of a spherically-confined particle, with the n, l, and m quantum numbers specified")
# The energies of a particle confined to a spherical ball of radius $a$ are:
# 
# $$
# E_{n,l} = \frac{\hbar^2 y_{n,l}^2}{2ma^2} \qquad n=1,2,\ldots; \quad l=0,1,\ldots; \quad m=0, \pm1, \ldots, \pm l
# $$
# 
# and its eigenfunctions are:
# 
# $$
# \psi_{n,l,m}(r,\theta,\phi) \propto j_l\left(\frac{y_{n,l}r}{a} \right) Y_l^{m_l}(\theta, \phi)
# $$
# 
# where $y_{n,l}$ are the zeros of the spherical Bessel function, $j_l(y_{n,l}) = 0$. The first spherical Bessel function, which corresponds to s-like solutions ($l=0$), is 
# 
# $$
# j_l(y) = \frac{\sin y}{y}
# $$
# 
# and so 
# 
# $$
# y_{n,0} = n \pi
# $$
# 
# This gives explicit and useful expressions for the $l=0$ wavefunctions and energies,
# 
# $$
# E_{n,0} = \frac{h^2 n^2}{8 m a^2}
# $$
# 
# and its eigenfunctions are:
# 
# $$
# \psi_{n,0,0}(r,\theta,\phi) \propto \frac{a}{n \pi r} \sin \left( \frac{n \pi r}{a} \right)
# $$
# 
# Notice that the $l=0$ energies are the same as in the one-dimensional particle-in-a-box and the eigenfunctions are very similar. 
# 
# In atomic units, the energies of an electron confined to a spherical ball with radius $a$ Bohr are: 
# 
# $$
# E_{n,l} = \tfrac{y_{n,l}^2}{2a^2}
# $$
# 
# The following code block computes these energies. It uses the relationship between the spherical Bessel functions and the ordinary Bessel functions,
# 
# $$
# j_l(x) = \sqrt{\frac{\pi}{2x}} J_{l+\tfrac{1}{2}}(x)
# $$
# 
# which indicates that the zeros of $j_l(x)$ and $J_{l+\tfrac{1}{2}}(x)$ occur the same places.

# In[3]:


# Define a function for the energy (in a.u.) of a particle in a spherical ball
# with length a, principle quantum number n, and angular quantum number l
# The length is input in Bohr (atomic units).
def compute_energy_ball(n, l, a):
    "Compute 1-dimensional particle-in-a-spherical-ball energy."
    #Compute the energy from the n-th zero.
    return float((mpmath.besseljzero(l+0.5,n))**2/ (2 * a**2))

#This next bit of code just prints out the energy in atomic units
def print_energy_ball(a, n, l):
    print(f'The energy of an electron confined to a ball with radius {a:.2f} a.u.,'
       f' principle quantum number {n}, and angular quantum number {l}'
       f' is {compute_energy_ball(n, l, a):5.2f} a.u..')
    

#Principle quantum number slider:
n = 1

#Angular quantum number slider:
l = 0

#Box length slider:
a = 1


print_energy_ball(a, n, l)


# ## &#x1f4dd; Exercise: For the hydrogen atom, the 2s orbital ($n=2$, $l=0$) and 2p orbitals ($n=2$,$l=1$,$m_l=-1,0,1$) have the same energy. Is this true for the particle-in-a-ball?

# ## &#x1fa9e; Self-Reflection
# - Can you think of other physical or chemical systems where a multi-dimensional particle-in-a-box Hamiltonian would be appropriate? What shape would the box be? 
# - Can you think of another chemical system where separation of variables would be useful?
# - Explain why separation of variables is consistent with the Born Postulate that the square-magnitude of a particle's wavefunction is the probability distribution function for the particle.
# - What is the expression for the zero-point energy and ground-state wavefunction of an electron in a 4-dimensional box? Can you identify some states of the 4-dimensional box with especially high degeneracy?
# - What is the degeneracy of the k-th excited state of a particle confined to a circular disk? What is the degeneracy of the k-th excited state of a particle confined in a spherical ball?
# - Write a Python function that computes the normalization constant for the particle-in-a-disk and the particle-in-a-sphere.
# 
# ## &#x1f914; Thought-Provoking Questions
# - How would you write the Hamiltonian for two electrons confined to a box? Could you solve this system with separation of variables? Why or why not? 
# - Write the time-independent Schr&ouml;dinger equation for an electron in an cylindrical box. What are its eigenfunctions and eigenvalues? 
# - What would the time-independent Schr&ouml;dinger equation for electrons in an elliptical box look like? (You may find it useful to reference [elliptical](https://en.wikipedia.org/wiki/Elliptic_coordinate_system) and [ellipsoidal](https://en.wikipedia.org/wiki/Ellipsoidal_coordinates) coordinates.
# - Construct an example of a four-fold *accidental* degeneracy for a particle in a 2-dimensional rectangular (not square!) box. 
# - If there is any degenerate state (either accidental or due to symmetry) for the multi-dimensional particle-in-a-box, then there are always an infinite number of other degenerate states. Why?
# - Consider an electron confined to a circular harmonic well, $V(r) = k r^2$. What is the angular kinetic energy and angular wavefunction for this system? 
# 
# ## &#x1f501; Recapitulation
# - Write the Hamiltonian, time-independent Schr&ouml;dinger equation, eigenfunctions, and eigenvalues for two-dimensional and three-dimensional particles in a box.
# - What is the definition of degeneracy? How does an "accidental" degeneracy differ from an ordinary degeneracy? 
# - What is the zero-point energy for an electron in a circle and an electron in a sphere? 
# - What are the spherical harmonics? 
# - Describe the technique of separation of variables? When can it be applied?
# - What is the Laplacian operator in Cartesian coordinates? In spherical coordinates?
# - What are *boundary conditions* and how are they important in quantum mechanics?
# 
# ## &#x1f52e; Next Up...
# - 1-electron atoms
# - Approximate methods for quantum mechanics
# - Multielectron particle-in-a-box
# - Postulates of Quantum Mechanics
# 
# ## &#x1f4da; References
# My favorite sources for this material are:
# - [Randy's book](https://github.com/PaulWAyers/IntroQChem/blob/main/documents/DumontBook.pdf?raw=true) (See Chapter 3)
# - Also see my (pdf) class [notes]
# (https://github.com/PaulWAyers/IntroQChem/blob/main/documents/PinBox.pdf?raw=true).
# - [McQuarrie and Simon summary](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Map%3A_Physical_Chemistry_(McQuarrie_and_Simon)/03%3A_The_Schrodinger_Equation_and_a_Particle_in_a_Box)
# - [Wolfram solutions for particle in a circle](https://demonstrations.wolfram.com/ParticleInAnInfiniteCircularWell/)
# - [Meticulous solution for a particle confined to a circular disk](https://opencommons.uconn.edu/cgi/viewcontent.cgi?article=1013&context=chem_educ)
# - [General discussion of the particle-in-a-region, which is the same as the classical wave equation](http://galileo.phys.virginia.edu/classes/252/Classical_Waves/Classical_Waves.html)
# - [More on the radial Schr&ouml;dinger equation](https://quantummechanics.ucsd.edu/ph130a/130_notes/node222.html)
# - Python tutorial ([part 1](https://physicspython.wordpress.com/2020/05/28/the-problem-of-the-hydrogen-atom-part-1/) and [part 2](https://physicspython.wordpress.com/2020/06/04/the-problem-of-the-hydrogen-atom-part-2/)) on the Hydrogen atom.
# 
# There are also some excellent wikipedia articles:
# - [Particle in a Sphere](https://en.wikipedia.org/wiki/Particle_in_a_spherically_symmetric_potential)
# - [Other exactly solvable models](https://en.wikipedia.org/wiki/List_of_quantum-mechanical_systems_with_analytical_solutions)

# In[ ]:




