# Moments of the Particle-in-a-Box

The moments of the particle in a box Hamiltonian have the expression:
$$
m_{k,n} = \frac{2}{a} \int_0^a  x^k \sin^2\left(\tfrac{n \pi x}{a}\right) \,dx
$$

We first compute asymptotic limits. When $n$ is large, the probability of observing a particle in the box is nearly uniform. So
$$
m_{k,n\rightarrow \infty} = \frac{2}{a} \int_0^a  x^k \tfrac{1}{2} \,dx = \frac{a^k}{k+1}
$$
When $k$ is large, the integrand grows so rapidly, its value is negligible except near the upper boundary of the box. Because $\sin^2\left(\tfrac{n \pi x}{a}\right) \sim \left(\tfrac{n \pi}{a}\right)^2(x-a)^2 $ in that region, we have:
$$
\begin{align}
m_{k\rightarrow \infty,n} &= \frac{2}{a} \int_0^a  x^k \left(\tfrac{n \pi}{a}\right)^2(x-a)^2 \,dx \\
&= 2 \left(\frac{a^{k+2}}{k+1}-2\frac{a^{k+2}}{k+2}+\frac{a^{k+2}}{k+3} \right) \\
&=\frac{(2 n \pi)^2 a^{k}}{(k+1)(k+2)(k+3)}
\end{align}
$$
The exact expression can be computed using the (lower) incomplete Gamma function (with complex arguments): 
$$
\gamma(s,x)= \int_0^x t^{s-1} e^{-t} \, dt
$$
or, more directly, using the generalized hypergeometric function
$$
{}_1F_2\left(\tfrac{k+1}{2};\tfrac{1}{2},\tfrac{k+3}{2};-a^2 \right) = (k+1)\int_0^1
x^k \cos(2ax) \,dx $$

Using the [double-angle formula](https://en.wikipedia.org/wiki/List_of_trigonometric_identities#Double-angle_formulae)
$$
\sin^2 x = \tfrac{1}{2} \left(1-\cos 2x \right)
$$
and substituting $u = \frac{x}{a}$, gives
$$
\begin{align}
m_{k,n} &= \frac{2}{a} \int_0^1  (au)^k \sin^2\left(n \pi u\right) \,adu \\
&= a^k \int_0^1  u^k \left(1-\cos \left(2n \pi u\right) \right) \,du \\
&=\frac{a^k}{k+1} \left(1-{}_1F_2\left(\tfrac{k+1}{2};\tfrac{1}{2},\tfrac{k+3}{2};-(n \pi)^2 \right)\right)
\end{align}
$$

