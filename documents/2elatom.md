# Approximate Energies for the 2-electron A tom

This is a set of notes on determining the energy of a 2-electron atom in various approximations. In atomic units, the molecular Hamiltonian is:

$$
\hat{\mathrm{H}}=-\frac{1}{2} \nabla_{1}^{2}-\frac{\mathrm{z}}{\mathrm{r}_{1}}-\frac{1}{2} \nabla_{2}^{2}-\frac{\mathrm{z}}{\mathrm{r}_{2}}+\frac{1}{\left|\mathrm{r}_{1}-\mathrm{r}_{2}\right|}
$$

and if we ignore the electron-electron repulsion term, this is a sum of two hydrogenic Hamiltonians, with ground-state energy

$$
\mathrm{E}_{\text {no-eerepulsion }}=-\frac{\mathrm{Z}^{2}}{2 \mathrm{n}_{1}^{2}}-\frac{\mathrm{Z}^{2}}{2 \mathrm{n}_{2}^{2}}
$$

and wavefunction

$$
\Psi_{\text {no-e-repulsion }}=\frac{1}{\sqrt{2}}\left|\begin{array}{lc}
\psi_{n_{1} l_{1} m_{1}}\left(\mathbf{r}_{1}\right) \sigma_{1}(1) & \psi_{n_{2} l_{2} m_{2}}\left(\mathbf{r}_{1}\right) \sigma_{2}(1) \\
\psi_{n_{1} l_{1} m_{1}}\left(\mathbf{r}_{2}\right) \sigma_{1}(2) & \psi_{n_{2} l_{2} m_{2}}\left(\mathbf{r}_{2}\right) \sigma_{2}(2)
\end{array}\right|
$$

For the ground state, this is

$$
\begin{gathered}
\mathrm{E}_{\text {no-ee-repulsion }}=-\frac{\mathrm{Z}^{2}}{2}-\frac{\mathrm{Z}^{2}}{2}=-\mathrm{Z}^{2}<\mathrm{E}_{\text {g.s. }} \text { (true) } \\
\Psi_{\text {no-ee-repulsion }}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right)=\frac{\mathrm{Z}^{3}}{\pi} \mathrm{e}^{-Z\left(\mathrm{r}_{1}+\mathrm{r}_{2}\right)}\left(\frac{\alpha(1) \beta(2)-\alpha(2) \beta(1)}{\sqrt{2}}\right)
\end{gathered}
$$

This energy must be below the true energy because one has neglected a positive term (the electronelectron repulsion) in the Hamiltonian.

# $\underline{1^{\text {st-order perturbation theory correction: }}}$

Now, to estimate the effect of the electron-electron repulsion using perturbation theory, we add a parameter to the Hamiltonian, writing

$$
\hat{H}(\lambda)=-\frac{1}{2} \nabla_{1}^{2}-\frac{z}{r_{1}}-\frac{1}{2} \nabla_{2}^{2}-\frac{z}{r_{2}}+\frac{\lambda}{\left|r_{1}-r_{2}\right|}
$$

noting that $\hat{H}(\lambda=0)$ is the "easy" system we just solved and $\hat{H}(\lambda=1)$ is the true physical system we want to solve. Then, at the level of first-order perturbation theory,

$$
\mathrm{E}(\lambda)=\mathrm{E}(0)+\left.\lambda \frac{\mathrm{dE}}{\mathrm{d} \lambda}\right|_{\lambda=0}
$$

and for the $\lambda=1$ case of interest,

$$
E(1)=E_{1 \text {-orderpT }}=E(0)+\left.\frac{d E}{d \lambda}\right|_{\lambda=0}
$$

and, from the Hellmann-Feynman theorem,

$$
\begin{aligned}
\left.\frac{d E}{d \lambda}\right|_{\lambda=0} &=\int \Psi_{\text {no-e-repulsion }}^{*}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right) \frac{d \hat{H}}{d \lambda} \Psi_{\text {no-ee-repulsion }}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right) \mathrm{d} \mathbf{r}_{1} \mathrm{~d} \mathbf{r}_{2} \\
&=\frac{\mathrm{Z}^{6}}{\pi^{2}} \iint \frac{\mathrm{e}^{-\mathrm{Z}\left(\mathbf{r}_{1}+\mathbf{r}_{2}\right)} \mathrm{e}^{-Z\left(\mathbf{r}_{1}+\mathbf{r}_{2}\right)}}{\left|\mathbf{r}_{1}-\mathbf{r}_{2}\right|} \mathrm{d} \mathbf{r}_{1} \mathrm{~d} \mathbf{r}_{2} \\
&=\frac{5}{8} \mathrm{Z}
\end{aligned}
$$

The last integral I am giving to you. (I don't expect you to be able to solve it, at least not in the limited time allowed on an exam.)

So the energy of the 2-electron atom is

$$
\mathrm{E}_{1-\text { orderPT }}=-\mathrm{Z}^{2}+\frac{5}{8} \mathrm{Z}>\mathrm{E}_{\text {g.s. }}(\text { true })
$$

I know this is greater than the true ground-state energy because

$$
\mathrm{E}_{1 \text {-orderPT }}=\iint \Psi_{\lambda=0}^{*}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right) \hat{H} \Psi_{\lambda=0}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right) \mathrm{d} \mathbf{r}_{1} \mathrm{~d} \mathbf{r}_{2}>\mathrm{E}_{\text {g.s. }} \text { (true) }
$$

based on the variational principle.

# $\underline{\text { Variational Refinement: }}$

Now we can imagine trying to refine the wavefunction using an effective nuclear charge.

The new wavefunction we consider is

$$
\Psi_{\zeta}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right)=\frac{\zeta^{3}}{\pi} \mathrm{e}^{-\zeta\left(\mathrm{r}_{1}+\mathrm{r}_{2}\right)}\left(\frac{\alpha(1) \beta(2)-\alpha(2) \beta(1)}{\sqrt{2}}\right)
$$

which we notice is the exact wavefunction for the Hamiltonian without any electron-electron repulsion with nuclear charge $\zeta$,

$$
\hat{H}_{\text {no-ee-repulsion }}(\zeta)=-\frac{1}{2} \nabla_{1}^{2}-\frac{\zeta}{\mathrm{r}_{1}}-\frac{1}{2} \nabla_{2}^{2}-\frac{\zeta}{\mathrm{r}_{2}}
$$

Merely substituting Eq. (1.11) into (1.8) gives the expectation value for the electron-electron repulsion as

$$
\begin{aligned}
\left\langle\mathrm{V}_{\mathrm{ee}}\right\rangle &=\int \Psi_{\zeta}^{*}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right) \frac{1}{\left|\mathbf{r}_{1}-\mathbf{r}_{1}\right|} \Psi_{\zeta}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right) \mathrm{d} \mathbf{r}_{1} \mathrm{~d} \mathbf{r}_{2} \\
&=\frac{\zeta^{6}}{\pi^{2}} \iint \frac{\mathrm{e}^{-\zeta\left(\mathbf{r}_{1}+\mathbf{r}_{2}\right)} \mathrm{e}^{-\zeta\left(\mathbf{r}_{1}+\mathbf{r}_{2}\right)}}{\left|\mathbf{r}_{1}-\mathbf{r}_{2}\right|} \mathrm{d} \mathbf{r}_{1} \mathrm{~d} \mathbf{r}_{2} \\
&=\frac{5}{8} \zeta
\end{aligned}
$$

To determine the other contributions to the energy, note that from the Hellmann-Feynman theorem,

$$
\begin{aligned}
\frac{\mathrm{dE}_{\text {no-eerepulsion }}(\zeta)}{\mathrm{d} \zeta} &=\int \Psi_{\text {no-ee-repulion }}^{*}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right) \frac{\mathrm{d} \hat{\mathrm{H}}_{\mathrm{no}-e-\mathrm{erppusion}}(\zeta)}{\mathrm{d} \zeta} \Psi_{\text {no-ee-repusion }}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right) \mathrm{d} \mathbf{r}_{1} \mathrm{~d} \mathbf{r}_{2} \\
\frac{d\left(\frac{-\zeta^{2}}{\mathrm{n}^{2}}\right)}{\mathrm{d} \zeta} &=\frac{\zeta^{6}}{\pi^{2}} \iint \mathrm{e}^{-\zeta\left(\mathbf{r}_{1}+\mathrm{r}_{2}\right)}\left(-\frac{1}{\mathrm{r}_{1}}-\frac{1}{\mathrm{r}_{2}}\right) \mathrm{e}^{-\zeta\left(\mathbf{r}_{1}+\mathrm{r}_{2}\right)} \mathrm{d} \mathbf{r}_{1} \mathrm{~d} \mathbf{r}_{2} \\
\frac{-2 \zeta}{\mathrm{n}^{2}} &=\frac{\zeta^{6}}{\pi^{2}} \iint \mathrm{e}^{-\zeta\left(\mathbf{r}_{1}+\mathrm{r}_{2}\right)}\left(-\frac{1}{\mathrm{r}}-\frac{1}{\mathrm{r}_{2}}\right) \mathrm{e}^{-\zeta\left(\mathbf{r}_{1}+\mathrm{r}_{2}\right)} \mathrm{d} \mathbf{r}_{1} \mathrm{~d} \mathbf{r}_{2}
\end{aligned}
$$

Notice, now, that the electron-nuclear attraction integral is 

$$
\begin{aligned}
\left\langle\mathrm{V}_{\mathrm{ne}}\right\rangle &=\left\langle-\frac{\mathrm{Z}}{\mathrm{r}_{1}}-\frac{\mathrm{Z}}{\mathrm{r}_{2}}\right\rangle=\frac{\zeta^{6}}{\pi^{2}} \iint \mathrm{e}^{-\zeta\left(\mathrm{r}_{1}+\mathrm{r}_{2}\right)}\left(-\frac{\mathrm{Z}}{\mathrm{r}_{1}}-\frac{\mathrm{Z}}{\mathrm{r}_{2}}\right) \mathrm{e}^{-\zeta\left(\mathrm{r}_{1}+\mathrm{r}_{2}\right)} \mathrm{d} \mathbf{r}_{1} \mathrm{~d} \mathbf{r}_{2} \\
&=\mathrm{Z} \frac{\zeta^{6}}{\pi^{2}} \iint \mathrm{e}^{-\zeta\left(\mathrm{r}_{1}+\mathrm{r}_{2}\right)}\left(-\frac{1}{\mathrm{r}_{1}}-\frac{1}{\mathrm{r}_{2}}\right) \mathrm{e}^{-\zeta\left(\mathrm{r}_{1}+\mathrm{r}_{2}\right)} \mathrm{d} \mathbf{r}_{1} \mathrm{~d} \mathbf{r}_{2} \\
&=\frac{-2 \mathrm{Z} \zeta}{\mathrm{n}^{2}}
\end{aligned}
$$

The kinetic-energy integral could also be determined from the Hellman-Feynman theorem (use non-atomic-units and differentiate with respect to $\hbar$ ). However, for the exact Hamiltonian, we know that

$$
\begin{aligned}
\mathrm{E}_{\text {no-ee-repulsion }}(\zeta) &=-\frac{\zeta^{2}}{\mathrm{n}^{2}}=\langle\mathrm{T}\rangle+\left\langle\mathrm{V}_{\mathrm{ne}}(\zeta)\right\rangle \\
-\frac{\zeta^{2}}{\mathrm{n}^{2}} &=\langle\mathrm{T}\rangle-\frac{2 \zeta^{2}}{\mathrm{n}^{2}} \\
\langle\mathrm{~T}\rangle &=\frac{\zeta^{2}}{\mathrm{n}^{2}}
\end{aligned}
$$

So the eneray expression we have is:

$$
\begin{aligned}
\mathrm{E}(\zeta) &=\int \Psi_{\text {no-ee-repulsion }}^{*}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right) \hat{H}_{\text {no-ee-repulsion }}(\zeta) \Psi_{\text {no-ee-repulsion }}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right) \mathrm{d} \mathbf{r}_{1} \mathrm{~d} \mathbf{r}_{2} \\
&=\langle\mathrm{T}\rangle+\left\langle\mathrm{V}_{\mathrm{ne}}(\mathrm{Z})\right\rangle+\left\langle\mathrm{V}_{\mathrm{ee}}\right\rangle \\
&=\zeta^{2}-2 \zeta \mathrm{Z}+\frac{5}{8} \zeta
\end{aligned}
$$

We find the optimal effective nuclear charge by differentiation this expression,

$$
\begin{aligned}
&0=\frac{\mathrm{dE}}{\mathrm{d} \zeta}=2 \zeta-2 \mathrm{Z}+\frac{5}{8} \\
&\zeta=\mathrm{Z}-\frac{5}{16}
\end{aligned}
$$

Substituting this expression into Eq. (1.17) gives the best variational energy (which is still above the true energy),

$$
\begin{aligned}
\mathrm{E}\left(\zeta_{\min }\right) &=\left(\mathrm{Z}-\frac{5}{16}\right)^{2}-2 \mathrm{Z}\left(\mathrm{Z}-\frac{5}{16}\right)+\frac{5}{8}\left(\mathrm{Z}-\frac{5}{16}\right) \\
&=\left(\mathrm{Z}-\frac{5}{16}\right)\left(\left(\mathrm{Z}-\frac{5}{16}\right)-2 \mathrm{Z}+\frac{5}{8}\right) \\
&=-\left(\mathrm{Z}-\frac{5}{16}\right)\left(-\mathrm{Z}+\frac{5}{16}\right) \\
&=-\left(\mathrm{Z}-\frac{5}{16}\right)^{2}
\end{aligned}
$$
