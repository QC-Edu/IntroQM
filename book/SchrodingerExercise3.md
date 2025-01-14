# &#x1f4dd; Exercise

## Ground-State Energy of the Morse Potential
The Morse potential is often used as an approximate model for the vibrations of diatomic molecules. In convenient units where $\frac{\hslash ^{2}}{2m}=1$, the time-independent Schr&ouml;dinger equation for a Morse oscillator can be written as:

$$
\left(-\frac{d^{2}}{dx^{2}}+\lambda ^{2}\left(e^{-2x}-2e^{-x}\right)\right)\psi _{n}\left(x\right)=E_{n}\psi _{n}\left(x\right)
$$


The first two eigenfunctions of the Morse oscillator are given by the following expressions (which are not normalized)

$$
\begin{align}
\psi _{0}\left(x\right)&=\exp \left(-\left(\lambda -\tfrac{1}{2}\right)x-\lambda e^{-x}\right)\\
\psi _{1}\left(x\right)&=\exp \left(-\left(\lambda -\tfrac{3}{2}\right)x-\lambda e^{-x}\right)\left(2\lambda -2-2\lambda e^{-x}\right)
\end{align}
$$

**What is the expression for the ground-state energy for the Morse oscillator?**

This requires applying the Hamiltonian to the ground-state wavefunction of the Morse oscillator and finding the eigenvalue. It’s a straightforward but tedious exercise:

$$
\begin{align}
&\frac{d}{dx}\left[\exp \left(-\left(\lambda -\tfrac{1}{2}\right)x-\lambda e^{-x}\right)\right]=\exp \left(-\left(\lambda -\tfrac{1}{2}\right)x-\lambda e^{-x}\right)\cdot \frac{d}{dx}\left[-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right]\\
&\qquad=\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\cdot \left[-\left(\lambda -\frac{1}{2}\right)+\lambda e^{-x}\right]\\
&\frac{d^{2}}{dx^{2}}\left[\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\right]=\frac{d}{dx}\left(\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\cdot \left[-\left(\lambda -\frac{1}{2}\right)+\lambda e^{-x}\right]\right)\\
&\qquad=\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\cdot \left[-\left(\lambda -\frac{1}{2}\right)+\lambda e^{-x}\right]^{2}\\
&\qquad \qquad+\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\cdot \frac{d}{dx}\left[-\left(\lambda -\frac{1}{2}\right)+\lambda e^{-x}\right]\\
&\qquad =\left(\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\right)\cdot \left(\left[-\left(\lambda -\frac{1}{2}\right)+\lambda e^{-x}\right]^{2}-\lambda e^{-x}\right)\\
&\qquad =\left(\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\right)\cdot \left(\left(\lambda -\frac{1}{2}\right)^{2}-2\lambda \left(\lambda -\frac{1}{2}\right)e^{-x}+\lambda ^{2}e^{-2x}-\lambda e^{-x}\right)\\
&\qquad=\left(\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\right)\cdot \left(\left(\lambda -\frac{1}{2}\right)^{2}-2\lambda ^{2}e^{-x}+\lambda ^{2}e^{-2x}\right)\\
&\qquad=\left(\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\right)\cdot \left(\left(\lambda -\frac{1}{2}\right)^{2}+\lambda ^{2}\left(e^{-2x}-2e^{-x}\right)\right)
\end{align}
$$

Substituting into the Schr&ouml;dinger equation gives:

$$
\begin{align}
&\left(-\frac{d^{2}}{dx^{2}}+\lambda ^{2}\left(e^{-2x}-2e^{-x}\right)\right)\left[\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\right]\\
& \qquad =-\left(\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\right)\cdot \left(\left(\lambda -\frac{1}{2}\right)^{2}+\lambda ^{2}\left(e^{-2x}-2e^{-x}\right)\right)\\
&\qquad \qquad+\left[\lambda ^{2}\left(e^{-2x}-2e^{-x}\right)\right]\left(\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\right)\\
&\qquad =-\left(\lambda -\frac{1}{2}\right)^{2}\left(\exp \left(-\left(\lambda -\frac{1}{2}\right)x-\lambda e^{-x}\right)\right)
\end{align}
$$

So the ground-state energy of the Morse oscillator is $E=-\left(\lambda -\frac{1}{2}\right)^{2}$.