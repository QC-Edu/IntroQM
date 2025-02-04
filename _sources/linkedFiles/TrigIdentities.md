# Trigonometric Identities
There are a large number of trigonometric identities that one can memorize, but I tend to remember only a few bare essentials. Specifically, I remember the following angle-addition identities:

$$
\begin{aligned}
\sin(x \pm y) &= \sin x \cos y \pm \sin y \cos x \\
\cos(x \pm y) &= \cos x \cos y \mp \sin x \sin y
\end{aligned}
$$

Note that in fact you need to memorize only the identities with the $+$ sign, because the others can be deduced by changing $y \rightarrow -y$ and remembering that the cosine is an even function and the sine is an odd function,

$$
\begin{aligned}
\cos(-x) &= \cos(x) \\
\sin(-x) &= - \sin(x)
\end{aligned}
$$

So in fact I only "memorize"

$$
\begin{aligned}
\sin(x + y) &= \sin x \cos y + \sin y \cos x \\
\cos(x + y) &= \cos x \cos y - \sin x \sin y
\end{aligned}
$$

From these I can deduce many other identities very easily. For example, by choosing $x=y$ in the angle-addition identities, I can deduce the double-angle identities and the Pythagorean identity:

$$
\begin{aligned}
\sin(2x) &= 2 \sin x \cos x \\
\cos(2x) &= \cos^2 x - \sin^2 x \\
\cos(0) &= 1 = \cos^2 x + \sin^x
\end{aligned}
$$

Adding the second two equations gives

$$
\cos 2x + 1 = 2 \cos^2 x
$$

and subtracting the second two equations gives

$$
1 - \cos 2x = 2 \sin^2 x
$$

Alternatively, going back to the angle-addition identities, you can deduce (by adding and subtracting each equation from itself) the product-to-sum identities:

$$
\begin{aligned}
2 \sin x \cos y &= \sin(x+y) + \sin(x-y) \\
2 \sin x \sin y &= \cos(x-y) - \cos(x+y) \\
2 \cos x \cos y &= \cos(x-y) + \cos(x+y)
\end{aligned}
$$

The double-angle formulas could also be deduced by setting $x = y$ in these equations. One can also deduce the sum-to-product identities:

$$
\begin{aligned}
\sin x + \sin y &= 2\sin \left(\tfrac{a + b}{2}\right)\cos \left(\tfrac{a - b}{2}\right) \\
\cos x + \cos y &= 2\cos \left(\tfrac{a + b}{2}\right)\cos \left(\tfrac{a - b}{2}\right) \\
\cos x - \cos y &= -2\sin \left(\tfrac{a + b}{2}\right)\sin \left(\tfrac{a - b}{2}\right)
\end{aligned}
$$