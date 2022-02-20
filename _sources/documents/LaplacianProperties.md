# Properties of the Laplacian

## Show that the Laplacian is a linear, Hermitian, operator.
To show that $\nabla^2$ is linear, we need only recall that it is the second derivative operator. We know that differentiation is a linear operator. I.e., differentiation of a constant times a function is equal to a constant, times the value obtained by differentiating the function. Similarly, differentiation of a sum of functions is equal to summing the derivatives of the functions. Mathematically,
$$
\frac{d^k}{dx^k} \text{constant} \cdot f(x) = \text{constant} \cdot\frac{d^kf}{dx^k} 
$$
and
$$
\frac{d^k\left(f(x) + g(x) \right)}{dx^k} = \frac{d^kf(x)}{dx^k} + \frac{d^kg(x)}{dx^k}
$$
So $\nabla^2$ (corresponding to $k=2$) is linear.

One can show that $\nabla^2$ is Hermitian using integration by parts, similar to how we did in the course notes. You can also recognize that the Hermitian property follows directly from [Green's second identity](https://en.wikipedia.org/wiki/Green%27s_identities#Green's_second_identity) . (In both cases you use the fact that the wavefunction and its derivatives vanish at the end of the interval of integration.)

However, we also know that $\nabla^2$ is closely related to the momentum operator. 
$$
\hat{p}^2 = -i \hbar \nabla \cdot -i \hbar \nabla = - \hbar^2 \nabla^2
$$
In atomic units, then, $\nabla^2 = - \hat{p}^2$. The following math uses the fact that the momentum operator is Hermitian. 

We need to show that 
$$
\int \Phi(x)^* \nabla^2 \Psi(x) dx = \int \left( \nabla^2 \Phi(x) \right)^* \Psi(x) dx 
$$
To this end, we start with the relationship between the Laplacian and the momentum operator, then (repeatedly) invoke the fact the momentum operator is Hermitian. So:
$$
\begin{align}
\int \Phi(x)^* \nabla^2 \Psi(x) dx &=\int \Phi(x)^* \left(-\hat{p}^2\right) \Psi(x) dx \\
&=-\int \Phi(x)^* \left(\hat{p}\hat{p} \right) \Psi(x) dx \\
&=-\int \left(\hat{p}\Phi(x)\right)^* \hat{p} \Psi(x) dx \\
&=-\int \left(\hat{p}\hat{p}\Phi(x)\right)^* \Psi(x) dx \\
&=\int \left(-\hat{p}^2\Phi(x)\right)^* \Psi(x) dx \\
&=\int \left(\nabla^2\Phi(x)\right)^* \Psi(x) dx
\end{align}
$$

## Show that the Laplacian is negative definite.

One can show that $\nabla^2$ is negative-definite using [Green's first identity](https://en.wikipedia.org/wiki/Green%27s_identities#Green's_first_identity) or integration by parts. However, as with the first part of this problem, one can also directly invoke the connection to the momentum operator, $\nabla^2 = - \hat{p}^2$. Since the square of an operator is positive definite, it's clear that the negative of the square of an operator is negative definite. However, more explicitly:
$$
\begin{align}
\int \Psi(x)^* \nabla^2 \Psi(x) dx &=\int \Psi(x)^* \left( -\hat{p}^2 \right) \Psi(x) dx \\
&=-\int \Psi(x)^* \hat{p}\hat{p} \Psi(x) dx \\
&=-\int \left(\hat{p}\Psi(x)\right)^* \hat{p} \Psi(x) dx \\
&=-\int \left|\hat{p}\Psi(x)\right|^2 dx \\
&<0
\end{align}
$$