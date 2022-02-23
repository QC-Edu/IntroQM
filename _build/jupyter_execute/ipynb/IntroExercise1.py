#!/usr/bin/env python
# coding: utf-8

# # &#x1f4dd; Exercise
# **Suppose you are given a photon with an energy of 2 eV. What is its momentum in 
# $\frac{\text{m} \cdot \text{kg}}{\text{s}}$? What is its frequency in Hz?** 

# First we can compute the frequency of the photon as:
# 
# $$ \nu = \frac{E}{h} $$
# 
# but there is the slight complication that the energy was given in electron-volts. Fortunately we have this constant built into to scipy.constants. 
# 
# The momentum of the photon can be computed from the De Broglie relation,
# 
# $$ p = \frac{h}{\lambda} = \frac{h}{\tfrac{c}{\nu}} = \frac{h \nu}{c} = \frac{E}{c} $$
# 
# Where the last formula, which was proposed long ago by Einstein and Compton and appeared in the notes, could have been used directly had you remembered it. However, because our energy is in electron-volts, it's a bit easier to use the next-to-last formula.
# 

# In[1]:


import scipy
from scipy import constants

# frequency = E/h
# get Planck's constant in useful units.
h_in_eVs = scipy.constants.value("Planck constant in eV/Hz")
frequency_d9 = 2.0/h_in_eVs

#Now useful to use Planck's constant in nice units.
momentum_d9 = constants.h*frequency_d9/constants.c

print("The frequency of a photon with an energy of 2 eV is {0:.3e} Hz".format(frequency_d9))
print("The momentum of a photon with an energy of 2 eV is {0:.3e} m kg/s".format(momentum_d9))


# In[ ]:




