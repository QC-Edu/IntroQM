# Midterm Questions
&#x1f468;&#x200d;&#x1f3eb; **Overview:**
These questions are taken from the course notes, tutorial discussions, and previous years' oral exams.
&#x1f4dc; **Instructions:** Be prepared to discuss the following questions/topics. I will randomly select questions.

# MidTerm Questions. (First Set)

## &#x2753; Questions about Python/Jupyter

1. What is the difference between interpreted and compiled languages? What type of language is Python? Can you explain why we need two different types of languages?
1. What’s the relationship of a class and the instance of a class? Why do we need classes?
1. Why do we need functions? What is a recursive function?
1. What cell formats are supported in a Jupyter Notebook? What are magic commands and why are they useful?

## &#x1f501; Describe the following effects/experiments/equations, and explain their importance to the origins of quantum mechanics.

1. Black-Body Radiation and the Ultraviolet Catastrophe.
1. The Davisson-Germer experiment and Electron Scattering.
1. Compton Scattering.
1. The Photoelectric Effect
1. The Rydberg Formula

## &#x2753; Questions about Wave-Particle Duality and the Origins of Quantum Mechanics

1. How would you describe wave-particle duality in a simple way that a novice can understand?
1. Is it possible for the wavelength of the scattered photon in Compton Scattering to be infinite? (I.e., could the photon be entirely absorbed?)
1. What are the units of the wavefunction?
1. What are the eigenfunctions of the kinetic-energy operator?
1. What are the eigenfunctions of the momentum operator?
1. Justify why the quantum mechanical momentum operator is $\hat{p} = -i \hbar \nabla$.
1. Once upon a time, a person interviewing for a job as a quantum chemist was asked how it was possible that the kinetic energy of a quantum system was always positive, given that the quantum-mechanical operator for the kinetic energy was “the negative of something squared”, namely, $E = -\tfrac{1}{2m}\nabla^2$. How would you answer this question?
1. Demonstrate that the kinetic energy operator is linear.
1. Demonstrate that the kinetic energy operator is Hermitian.

## &#x2753; Questions about the Schr&ouml;dinger Equation and (especially) the Particle-in-a-Box
1. Suppose that one has an electron that is tethered to the origin by a spring, so that the force the electrons feels towards the origin, $F=-kx$, increases proportionally to its distance. What would the Hamiltonian be?
1. How would the wavefunction and ground-state energy change if you made a small change in the particle-in a box Hamiltonian, so that the right-hand-side of the box was a little higher than the left-hand-side?
1. Any system with a zero-point energy of zero is classical. Why?
1. How would you compute the probability of observing an electron at the center of a box if the box contained 2 electrons? If it contained 4 electrons?
1. The probability of observing an electron at the center of a box with 3 electrons is sometimes lower than the probability of observing an electron at the center of a box with 2 electrons. Why?
1. What is the lowest-energy excitation energy for the particle-in-a-box?
1. Suppose you wanted to design a one-dimensional box containing a single electron that absorbed blue light? How long would the box be?
1. How would you compute the uncertainty in $x^4$?
1. Explain why separation of variables is consistent with the Born Postulate that the square-magnitude of a particle's wavefunction is the probability distribution function for the particle.
1. What is the time-dependent Schr&ouml;dinger equation? If the Hamiltonian is time-independent, how can one solve the time-dependent Schr&ouml;dinger equation, and what is the form of the solution?
1. Describe the technique of separation of variables? When can it be applied?
1. What is the expression for the zero-point energy and ground-state wavefunction of an electron in a 4-dimensional box? Can you identify some states of the 4-dimensional box with especially high degeneracy?
1. What is the degeneracy of the k-th excited state of a particle confined to a circular disk? What is the degeneracy of the k-th excited state of a particle confined in a spherical ball?
1. Consider an electron confined to a circular harmonic well, $V=\tfrac{1}{2}k(x^2+y^2)$. What is the angular kinetic energy and angular wavefunction for this system?
1. How would you write the Hamiltonian for two electrons confined to a box? Could you solve this system with separation of variables? Why or why not?
1. Write the time-independent Schrödinger equation for an electron in an cylindrical box. What are its eigenfunctions and eigenvalues?
1. What is the definition of degeneracy? How does an “accidental” degeneracy differ from an ordinary degeneracy?
1. If there is any degenerate state (either accidental or due to symmetry) for the multi-dimensional particle-in-a-box, then there are always an infinite number of other degenerate states. Why?
1. Construct an example of a four-fold accidental degeneracy for a particle in a 2-dimensional rectangular (not square!) box.
1. What would the time-independent Schrödinger equation for electrons in an elliptical box look like? (You may find it useful to reference elliptical and ellipsoidal coordinates.)


# Midterm Questions (Second Set)

## &#x2753;  What are the eigenfunctions and eigenvalues for the following Hamiltonians.

You should be able to explain key characteristics of the systems and the general strategy for (possibly approximate) solving the associated time-independent Schr&ouml;dinger equation.


$$
\begin{align}
\hat{H}_1 &= -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} -\frac{\hbar^2}{2m} \frac{d^2}{dy^2} + V_{a_x}(x) + V_{a_y}(y) \\
\hat{H}_2(\lambda) &= -\frac{\hbar^2}{2m} \frac{d^2}{dx_1^2} -\frac{\hbar^2}{2m} \frac{d^2}{dx_2^2} + V_{a}(x_1) + V_{a}(x_2)
- \lambda |x_1 - x_2|\\
\hat{H}_3(\lambda) &= -\tfrac{1}{2} \nabla_1^2 -\tfrac{1}{2} \nabla_2^2- \tfrac{Z}{r_1} - \tfrac{Z}{r_2} + \tfrac{\lambda}{|\mathbf{r}_1 - \mathbf{r}_2|}\\
\hat{H}_4 &= -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} -\frac{\hbar^2}{2m} \frac{d^2}{dy^2} -\frac{\hbar^2}{2m} \frac{d^2}{dz^2} + V_{a}\left(\sqrt{x^2 + y^2 +z^2}\right) \\
\hat{H}_5(\mathbf{R}_B) &=  -\tfrac{1}{2} \nabla_{\mathbf{r}}^2 - \tfrac{Z_A}{r} - \tfrac{Z_B}{|\mathbf{r} - \mathbf{R}_B|} \\
\hat{H}_6 &= -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} -\frac{\hbar^2}{2m} \frac{d^2}{dy^2} -\frac{\hbar^2}{2m} \frac{d^2}{dz^2} + V_{a_z}(z) + V_{a_r}(\sqrt{x^2+y^2}) \\
\hat{H}_7 &= -\frac{\hbar^2}{2m}\nabla^2 +\frac{a}{r^2} - \frac{b}{r}
\end{align}
$$

where

$$
V_a(x) =
\begin{cases}
    +\infty & x\leq 0\\
    0       & 0\lt x \lt a\\
    +\infty & a \leq x
\end{cases}
$$

## &#x2753;  Discuss the following in your own words.
1. What is a Slater determinant? Why does one use a Slater determinant for a many-fermion system? When is the exact ground-state wavefunction for a many-fermion system a Slater determinant?
1. What is the variational principle? How is it used to approximate the ground-state energy and wavefunction of realistic, not-exactly-solvable, Hamiltonians? Can you give an example of how it is used?
1. What is the Hartree-Fock method? What is the intuition behind it, and when is it used?
1. What is Perturbation Theory? When is perturbation theory most appropriate? Least appropriate?
1. What is the secular equation? How does it relate to the technique of expanding a wavefunction in a basis set?
1. What are the key postulates of quantum mechanics?
1. What is the Heisenberg Uncertainty Principle? What does it say about the fundamentals of quantum mechanics? What is the commutator between two operators, and how does it relate to the Heisenberg Uncertainty Principle?

## &#x2753; Questions about Quantum Mechanical Principles and Formalism
1. Write an expression for the expectation value of the energy without assuming that the wavefunction is normalized.
1. Show that the momentum operator is Hermitian.
1. Show that the eigenvalues of Hermitian operators are always real.
1. Show that the eigenvectors of a Hermitian operator with different eigenvalues are always orthogonal.
1. Show that the Laplacian is negative definite.
1. Show why the expectation value of an operator is always less than its maximum eigenvalue.
1. What is an example of a classical observable that is not a quantum-mechanical observable?
1. Give an example of two quantum-mechanical operators that commute. What about two operators that don’t commute?
1. Explain why minimizing the distance to the ground-state wavefunction variationally is different from minimizing the energy.
1. Show that the expansion coefficient for a wavefunction in a nonorthogonal basis can be determined by solving a system of linear equations.
1. Show that the eigenvectors of a Hermitian operator with the same eigenvalue can always be chosen to be orthogonal, but do not have to be.
1. Show, mathematically, that for a separable operator, $\hat{C}(x,y) = \hat{A}(x) + \hat{B}(y)$, the eigenvalues are the sum of the constituent operators' eigenvalues and the eigenvectors are the product of the constituent operators eigenvectors.

## &#x2753; Questions about Solving the Schr&ouml;dinger Equation.

1. Consider the hydrogen molecule ion, $\text{H}_2^+$. Is it more sensible to use the secular equation (basis-set-expansion) or perturbation theory? What if the bond length is very small? What if the bond length is very large?
1. How is the Hellmann-Feynman theorem related to perturbation theory?
1. What is perturbation theory? What is the expression for the first-order perturbed wavefunction?
1. What is the Hamiltonian for the one-electron atom? What are the eigenfunctions and eigenvalues of the one-electron atom?


## &#x2753; Questions about Electronic Systems.
1. Suppose electrons did not repel each other. Can you write the wavefunction for a many-electron atom in that case?
1. Why do you think solving the Schrödinger equation for the one-electron molecule is more complicated than solving the Schrödinger equation for the one-electron atom?
1. For what atomic number, $Z$, is the energy of a one-electron atom comparable to the rest-mass energy of an electron, $m_e c^2$? For atomic numbers close to this value, relativistic effects become extremely important.
1. What are eigenfunctions for the $n=l+1$ state of a one-electron atom?
1. Show that if you minimize the energy as a function of the basis-set coefficients using the variational principle, then you obtain the secular equation.
1. The Hellmann-Feynman theorem indicates that given the ground-state wavefunction for a molecule, the force on the nuclei can be obtained. Explain how.
1. What does it mean that perturbation theory is inaccurate when the perturbation is large?
1. Can you explain why the energy goes down when the electron-in-a-box is placed in an external electric field? (Assume that the point where the potential is defined to be zero is in the center of the box, so that the _average_ potential is not changing.)
1. For a sufficiently-highly excited state, the effect of an external electric field is negligible. Why is this true intuitively? Can you show it graphically? Can you explain it mathematically?
1. If a uniform external electric field of magnitude $F$ in the $\hat{\mathbf{u}} = [\hat{u}_x,\hat{u}_y,\hat{u}_z]^T$ direction is applied to a particle with charge $q$, the potential $V(x,y,z) = -qF(u_x x + u_y y + u_z z)$ is added to the Hamiltonian. (This follows from the fact that the force applied to the particles is proportional to the electric field, $\text{force} = q \vec{E} = q F \hat{\mathbf{u}}$ and the force is $\text{force} = - \nabla V(x,y,z)$. If the field is weak, then perturbation theory can be used, and the energy can be written as a Taylor series. The coefficients of the Taylor series give the dipole moment ($\mu$), dipole polarizability ($\alpha$), first dipole hyperpolarizability ($\beta$), second dipole hyperpolarizability ($\gamma$) in the $\hat{\mathbf{u}}$ direction.
   - The dipole moment, $\mu$, of any spherical system is zero. Explain why.
   - The polarizability, $\alpha$, of any system is always positive. Explain why.

$$
\begin{align}
E_k(F) &= E_k(0) + F \left[\frac{dE_k}{d F} \right]_{F=0}
+ \frac{F^2}{2!} \left[\frac{d^2E_k}{d F^2} \right]_{F=0}
+ \frac{F^3}{3!} \left[\frac{d^3E_k}{d F^3} \right]_{F=0}
+ \frac{F^4}{4!} \left[\frac{d^4E_k}{d F^4} \right]_{F=0} + \cdots \\
&= E_k(0) - F \mu_{F=0}
- \frac{F^2}{2!} \alpha_{F=0}
- \frac{F^3}{3!} \beta_{F=0}
- \frac{F^4}{4!} \gamma_{F=0} + \cdots \\
\end{align}
$$

## &#x2753; Questions about Many-Electron Systems and their Approximation.

1. What are bosons? What are fermions? How do the wavefunctions differ?
1. What is the fundamental assumption that underlies the orbital approximation?
1. What is a Slater determinant?
1. What is the fundamental idea behind Hartree-Fock theory?
1. How does one use the secular equation to approximate the wavefunction for a many-electron system?
1. Explain what the Hartree-Fock approximation has to do with the concept of effective nuclear charge.
1. Can you think of a system where a single Slater determinant would be an extremely poor approximation?
1. To what extent is the shape of the spherical harmonic intuitive, especially the doughnut shapes associated with an electron's angular momentum around the z axis.
1. Derive the Rydberg formula.
1. Can you derive a Rydberg-like formula for the wavenumber of excitations for a particle-in-a-box? How would this formula become more complicated for particles-in-a-box in higher dimensions?
1. An [advanced](https://www.weimer.itp.uni-hannover.de/fileadmin/weimer-group/qdt.pdf) (and approximate) version of the [Rydberg formula](https://en.wikipedia.org/wiki/Rydberg_state) holds for highly-excited states of most atoms and molecules, and is particularly accurate for excitations from the highest occupied ($ns$ orbital) of [alkali metal atoms](https://en.wikipedia.org/wiki/Rydberg_atom). The basic idea is that the excitation energy can be expressed as a formula like the below, where the [quantum defect](https://en.wikipedia.org/wiki/Quantum_defect), $\delta_{l}$, [depends on the orbital angular momentum of the state](https://www.weimer.itp.uni-hannover.de/fileadmin/weimer-group/qdt.pdf). Can you understand where the below formula for the excitation energy comes from? Why does the quantum defect depend on angular momentum? Why does the quantum defect decrease as the angular momentum of the state? (For example, for Rubidium, $\delta_0 = 3.13$ but $\delta_2 = 1.35$.) Why does the quantum defect increase for heavier alkali metal atoms? (For example, for Li, $\delta_0 = 0.41$ but for Cs, $\delta_0 = 4.13$.)

\begin{equation*}
   \Delta E_{ns \rightarrow n'l'} \approx \frac{1}{2}\left(\frac{1}{(n-\delta_0)^2}-\frac{1}{(n'-\delta_{l'})^2}\right)
\end{equation*}

12. For conjugated linear molecules like the cyanine dyes, the $\pi$-electrons are really confined to a 3-dimensional region, but the size of the region that is perpendicular to the conjugation is much smaller. For example, one could consider a 3-dimensional box or a 3-dimension cylinder:
   $$
   \hat{H}_{\text{p-in-3d-box}} = - \frac{\hbar^2}{2m} \nabla^2 + V_{a_x}(x) + V_{a_y}(y) + V_{a_z}(z)
   $$
   $$
   \hat{H}_{\text{p-in-cylinder}} = - \frac{\hbar^2}{2m} \nabla^2 + V_{a_z}(z) + V_{a_r}(r)
   $$
   $$
   V_a(x) =
   \begin{cases}
       +\infty & x\leq 0\\
       0       & 0\lt x \lt a\\
       +\infty & a \leq x
   \end{cases}
   $$

- What are the eigenfunctions and eigenenergies for these systems?
- Why is the one-dimensional particle-in-a-box model sufficient for describing the _spectroscopy_ of cyanine dyes?

## &#x2753; Quiz Questions
You may be asked a question from the quizzes on units 3 (QM Intro) 4 (Sch&ouml;dinger equation), or 5 (1D Particle-in-a-box).



