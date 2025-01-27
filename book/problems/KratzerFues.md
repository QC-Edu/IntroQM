# Kratzer-Fues Potential

The Kratzer-Fues potential is a [reasonable model for a diatomic molecule rotating and vibrating in 3 dimensions](https://doi.org/10.1063/1.1841277), or even a ion-pair complex (e.g., an single ion pair from an ionic solvent in the gas phase). It has the form

$$
V_{\text{Kratzer-Fues}}(r) = \frac{a}{r^2} - \frac{b}{r} \qquad \qquad a>0 \text{ and } b>0
$$

and so the Schr&ouml;dinger equation has the form:

$$
\left(-\frac{\hbar^2}{2m}\nabla^2 +\frac{a}{r^2} - \frac{b}{r} \right) \psi(\mathbf{r}) = E\psi(\mathbf{r}) 
$$

This is a spherically-symmetric Schr&ouml;dinger equation in 3 dimensions. This means that the solution is  the product of a radial part and a spherical harmonic,

$$
\psi_{nlm_l}(r,\theta,\phi) = R_{nl}(r) Y_l^{m_l} (\theta,\phi)
$$

and the radial wavefunction, $R_{nl}(r)$ satisfies the radial Schr&ouml;dinger equation for a 3-dimensional system,

$$
\left(-\frac{\hbar^2}{2m} \left( \frac{d^2}{dr^2}+ \frac{2}{r} \frac{d}{dr}\right) 
      + \frac{\hbar^2 l(l+1)}{2mr^2} + \frac{a}{r^2} - \frac{b}{r} \right)
      R_{n,l}(r) 
= E_{n,l}R_{n,l}(r)
$$

or, simplifying slightly,

$$
\left(-\frac{\hbar^2}{2m} \left( \frac{d^2}{dr^2}+ \frac{2}{r} \frac{d}{dr}\right) 
      + \frac{\hbar^2 l(l+1) + 2ma}{2mr^2} - \frac{b}{r} \right)
      R_{n,l}(r) 
= E_{n,l}R_{n,l}(r)
$$

This is a spherically-symmetric Schr&ouml;dinger equation in 3 dimensions. This means that the solution is  the product of a radial part and a spherical harmonic,

$$
\psi_{nlm_l}(r,\theta,\phi) = R_{nl}(r) Y_l^{m_l} (\theta,\phi)
$$

and the radial wavefunction, $R_{nl}(r)$ satisfies the radial Schr&ouml;dinger equation for a 3-dimensional system,

$$
\left(-\frac{\hbar^2}{2m} \left( \frac{d^2}{dr^2}+ \frac{2}{r} \frac{d}{dr}\right) 
      + \frac{\hbar^2 l(l+1)}{2mr^2} + \frac{a}{r^2} - \frac{b}{r} \right)
      R_{n,l}(r) 
= E_{n,l}R_{n,l}(r)
$$

or, simplifying slightly,

$$
\left(-\frac{\hbar^2}{2m} \left( \frac{d^2}{dr^2}+ \frac{2}{r} \frac{d}{dr}\right) 
      + \frac{\hbar^2 l(l+1) + 2ma}{2mr^2} - \frac{b}{r} \right)
      R_{n,l}(r) 
= E_{n,l}R_{n,l}(r)
$$

Notice that the radial Hamiltonian for the Kratzer-Fues potential looks *a lot* like the Hydrogenic atom, which has the Hamiltonian,

$$
\left(-\frac{1}{2} \left( \frac{d^2}{dr^2}+ \frac{2}{r} \frac{d}{dr}\right) 
      + \frac{l(l+1)}{2r^2} - \frac{Z}{r} \right)
      R_{n,l}(r) 
= E_{n,l}R_{n,l}(r)
$$

Returning to the Kratzer-Fues case, if one uses atomic units multiplies both sides of the equation by $m$, then

$$
\left(-\frac{1}{2} \left( \frac{d^2}{dr^2}+ \frac{2}{r} \frac{d}{dr}\right) 
      + \frac{l(l+1) + 2ma}{2r^2} - \frac{bm}{r} \right)
      R_{n,l}(r) 
= \left(mE_{n,l}\right)R_{n,l}(r)
$$

If you then defined a value, $l'$, such that

$$
l'(l'+1) = l(l+1) + 2ma
$$

the solutions would be Hydrogenic, 

$$
E_{\text{Kratzer-Fues},n} = -\frac{mb^2}{2n^2}
$$

and

$$
R_{n,l}(r) \propto \left( \frac{2mbr}{n} \right)^{l'} L_{n-1-l'}^{2l'+1}\left(\frac{2mbr}{n}\right) e^{-\frac{mbr}{n}}
$$

This treatment is quite naive, insofar as there is no guarantee that $l'$ is an integer. In practice, this solution is not quite right except for the exceptional cases where $l'$ is an integer less than $n$. But this is the *idea* of the solution. The exact solution can be found various places, see, [for](https://arxiv.org/abs/0802.0589v1) [example](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.741.7716&rep=rep1&type=pdf). The detailed solution can be found at in 
> S. Flügge *Practical Quantum Mechanics* (Berlin:Springer, 1957)

