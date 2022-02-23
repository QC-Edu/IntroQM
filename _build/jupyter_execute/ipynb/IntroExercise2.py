#!/usr/bin/env python
# coding: utf-8

# # &#x1f4dd; Exercise
# **What is the momentum and energy of a photon with angular wavenumber $k=10^8 \text{m}^{-1}$? Give your answer in SI units.** 

# We can start with the equation for the momentum, which is easy:
# 
# $$ p = \hbar k $$
# 
# 
# The equation for the energy can deduced directly as $E = pc$, but if you forgot this, then,
# 
# $$ E = h \nu = \frac{hc}{\lambda} = p c $$
# 
# using the Planck relation (first equality) and the De Broglie relation (last equality).

# In[1]:


import scipy
from scipy import constants

p_from_k = constants.hbar * 1e8
E_from_k = constants.c * p_from_k

print("The momentum of a photon with an angular wavenumber of 1e7 1/m is {0:.3e} m kg/s.".format(p_from_k))
print("The energy of a photon with an angular wavenumber of 1e7 1/m is {0:.3e} J.".format(E_from_k))


# In[ ]:




