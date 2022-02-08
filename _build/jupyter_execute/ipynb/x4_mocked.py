#!/usr/bin/env python
# coding: utf-8

# # Computing the expectation value of $\langle x^4 \rangle$ for 1 dimensional particle in the box

# ### Here is an example of calculating $\langle x \rangle$  and $\langle x^2 \rangle$ for the one 1 dimenstional particle in the box.
# 
# The average position is expected to be 
# 
# $$
# \langle x \rangle =\tfrac{a}{2}
# $$
# 
# We can confirm this by explicit integration,
# 
# $$
# \begin{align}
# \langle x \rangle &= \int_0^a \psi_n^*(x)\, x \,\psi_n(x) dx \\
# &= \int_0^a \left(\sqrt{\tfrac{2}{a}} \sin\left(\tfrac{n \pi x}{a} \right)\right) x \left(\sqrt{\tfrac{2}{a}}\sin\left(\tfrac{n \pi x}{a} \right)\right) dx \\
# &= \tfrac{2}{a} \int_0^a  x \sin^2\left(\tfrac{n \pi x}{a} \right) dx \\
# &= \tfrac{2}{a} \left[ \tfrac{x^2}{4} - x \tfrac{\sin \tfrac{2n \pi x}{a}}{\tfrac{4 n \pi}{a}}  
# - \tfrac{\cos \tfrac{2n \pi x}{a}}{\tfrac{8 n^2 \pi^2}{a^2}}  
#  \right]_0^a \\
#  &= \tfrac{2}{a} \left[ \tfrac{a^2}{4} - 0 - 0 \right] \\
#  &= \tfrac{a}{2}
# \end{align} 
# $$
# 
# Similarly, we expect that the expectation value of $\langle x^2 \rangle$ will be proportional to $a^2$. We can confirm this by explicit integration, 
# 
# $$
# \begin{align}
# \langle x^2 \rangle &= \int_0^a \psi_n^*(x)\, x^2 \,\psi_n(x) dx \\
# &= \int_0^a \left(\sqrt{\tfrac{2}{a}} \sin\left(\tfrac{n \pi x}{a} \right)\right) x^2 \left(\sqrt{\tfrac{2}{a}}\sin\left(\tfrac{n \pi x}{a} \right)\right) dx \\
# &= \tfrac{2}{a} \int_0^a  x^2 \sin^2\left(\tfrac{n \pi x}{a} \right) dx \\
# &= \tfrac{2}{a} \left[ \tfrac{x^3}{6} 
#  - x^2 \tfrac{\sin \tfrac{2n \pi x}{a}}{\tfrac{4 n \pi}{a}}
#  - x \tfrac{\cos \tfrac{2n \pi x}{a}}{\tfrac{4 n^2 \pi^2}{a^2}}
#  - \tfrac{\sin \tfrac{2n \pi x}{a}}{\tfrac{8 n^3 \pi^3}{a^3}}
#  \right]_0^a \\
#  &= \tfrac{2}{a} \left[ \tfrac{a^3}{6} - 0 - \tfrac{a}{{\tfrac{4 n^2 \pi^2}{a^2}}} - 0 \right] \\
#   &= \tfrac{2}{a} \left[ \tfrac{a^3}{6} - \tfrac{a^3}{4 n^2 \pi^2} \right] \\
#   &= a^2\left[ \tfrac{1}{3} - \tfrac{1}{2 n^2 \pi^2} \right] 
# \end{align} 
# $$
# 
# ### Task:
# Use the above example to calculate $\langle x^4 \rangle$. You can follow next steps:
# 1. Complete the `compute_wavefunction` function by coding the expression for calculating wavefunction. Don't forget the normalization constant. Also, take into account that x values could be negative and greater than a as well as be presented as `numpy.ndarray` or `float`.
# 2. Using the `compute_wavefunction` function complete the `compute_probability` function
# 3. Fill the gaps in `compute_momentum`  function, where you can use  the `compute_probability` function.
# 4. Complete the function `check_momentum` by calculating the integrand experssion.
# 5. Now you are ready to calculate the average. Use the [quad](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html) function for numerical integration and complete the `calc_average` function. Compare you results with 
# 6. At the last step you can use your functions to calculate  the $\langle x^2 \rangle$ and compare it with the analytic value. We encourage you to play with different values of n, a
# 7. Submit your notebook as discribed at the [first tutorial](Tutorial_0.ipynb) and enjoy your work!

# In[1]:


import numpy as np
from scipy.integrate import quad



# Define a function for the wavefunction
def compute_wavefunction(x, n, a):
    """Compute 1-dimensional particle-in-a-box wave-function value(s).
    
    Parameters
    ----------
    x: float or np.ndarray
        Position of the particle.
    n: int
        Quantum number value.
    a: float 
        Length of the box.
    """
    # check argument n
    if not (isinstance(n, int) and n > 0):
        raise ValueError("Argument n should be a positive integer.")
    # check argument a
    if a <= 0.0:
        raise ValueError("Argument a should be positive.")
    # check argument x
    if not (isinstance(x, float) or hasattr(x, "__iter__")):
        raise ValueError("Argument x should be a float or an array!")
        
    # compute wave-function
    
    ### START YOU CODE HERE
    value = np.sqrt(2/a)*np.sin(np.pi*x*n/a)
    ### END YOUR CODE HERE
    

    # set wave-function values out of the box equal to zero
    
    ### START YOU CODE HERE
    if hasattr(x, "__iter__"):
      value[np.logigal_or(x>a, x<0)] = 0
    elif x<0 or x>a:
      value = 0
    
    ### END YOUR CODE HERE
    return value



# Define a function for the wavefunction squared
def compute_probability(x, n, a):
    """Compute 1-dimensional particle-in-a-box probablity value(s).
    
    See `compute_wavefunction` parameters.
    """
    ### START YOUR CODE HERE
    probability = compute_wavefunction(x, n, a)**2
    ### END YOUR CODE HERE
    return probability



def compute_moment(x, n, a, power):
    """Compute the x^power moment of the 1-dimensional particle-in-a-box.
    
    See `compute_wavefunction` parameters.
    """
    return compute_probability(x, n, a)*x**power



#Compute <x^power>, the expectation value of x^power
def calc_average(n, a, power):
    """
    Compute the average value by explicit integrating 
    """
    
    ### START YOUR CODE HERE
    avg, error = quad(compute_moment, 0, a, args=(n, a, power))
    ### END YOUR CODE HERE
    
    return avg


#This next bit of code just prints out the values.
def check_moments(n, a):
    #check the computed values of the moments against the analytic formula
    
    ### START YOUR CODE HERE
    power = 2
    avg_r2 = calc_average(n, a, power)
    ### END YOUR CODE HERE
    
    print(f"<r^2> computed = {avg_r2:.5f}")
    print(f"<r^2> analytic = {a**2*(1/3 - 1./(2*n**2*np.pi**2))}")

    
#Principle quantum number:
n = 1

#Box length:
a = 1

check_moments(a, n)

