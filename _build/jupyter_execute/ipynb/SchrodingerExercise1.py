#!/usr/bin/env python
# coding: utf-8

# #### &#x1f4dd; Exercise 
# **The photon emitted when a 4p electron in the Hydrogen atom deexcites into a 2s orbital has wavelength 486.1 nm. Compute its**
# - **frequency in Hz**
# - **angular frequency in Hz**
# - **wavenumber, $\bar{\nu}$, in $\text{cm}^{-1}$.**
# - **angular wavenumber, $k$, in $\text{m}^{-1}$.**
# - **period in s.**
# - **momentum in m kg/s.**
# - **energy in Joules.**

# In[1]:


import scipy
import math
from scipy import constants

frequency = None         #Frequency in Hz.
omega = None             #Angular frequency in Hz.
wavenumber = None        #Wavenumber, nu-bar, in cm^-1
k = None                 #Angular wavenumber, k, in m^-1
period = None            #Period in s
momentum = None          #Momentum in SI units.
energy = None            #Energy in SI units.

### BEGIN SOLUTION
# It is helpful to first convert the wavelength into m (SI units)
wavelength_m = 486.1e-9 
#wavelength * frequency = speed of light. So:
frequency = constants.c/wavelength_m

# Angular frequency is 2 pi times the frequency
omega = 2*math.pi*frequency

#wavenumber is either 1/wavelength or 2pi/wavelength. 
#In this context we are using nu-bar, which is the former. 
#However, we want it in cm^-1. So
wavelength_cm = 485.1e-7      #Wavelength in cm
wavenumber = (wavelength_cm)**-1

#Angular wavenumber is easier, just 2*pi/wavelength (in m)
k = 2*math.pi/wavelength_m

#Period is one over frequency. So
period = 1/frequency

#momentum = h/lambda, where h is Planck's constant. So
momentum = constants.h/wavelength_m

#Energy is h * frequency or h * c / lambda or momentum times c. Using the former,
energy = constants.h * frequency

#Print it all out:
print(f"The frequency of a photon with wavelength 486.1 nm is {frequency:.3e} Hz.")
print(f"The angular frequency of a photon with wavelength 486.1 nm is {omega:.3e} Hz.")
print(f"The wavenumber, nu-bar, of a photon with wavelength  486.1 nm is {wavenumber:.3e} cm^-1.")
print(f"The angular wavenumber, k, of a photon with wavelength  486.1 nm is {k:.3e} m^-1.")
print(f"The period of a photon with wavelength  486.1 nm is {period:.3e} s.")
print(f"The momentum of a photon with wavelength  486.1 nm is {momentum:.3e} kg m/s.")
print(f"The energy of a photon with wavelength  486.1 nm is {energy:.3e} Joules.")

