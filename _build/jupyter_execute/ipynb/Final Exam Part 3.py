#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Final-Exam-Part-3" data-toc-modified-id="Final-Exam-Part-3-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Final Exam Part 3</a></span><ul class="toc-item"><li><span><a href="#🔁-Describe-the-following-effects/experiments/equations,-and-explain-their-importance-to-the-origins-of-quantum-mechanics." data-toc-modified-id="🔁-Describe-the-following-effects/experiments/equations,-and-explain-their-importance-to-the-origins-of-quantum-mechanics.-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>🔁 Describe the following effects/experiments/equations, and explain their importance to the origins of quantum mechanics.</a></span></li><li><span><a href="#🔁-Explain-the-following-topics." data-toc-modified-id="🔁-Explain-the-following-topics.-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>🔁 Explain the following topics.</a></span></li><li><span><a href="#🔁-What-are-the-eigenfunctions-and-eigenvalues-for-the-following-Hamiltonians." data-toc-modified-id="🔁-What-are-the-eigenfunctions-and-eigenvalues-for-the-following-Hamiltonians.-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>🔁 What are the eigenfunctions and eigenvalues for the following Hamiltonians.</a></span></li><li><span><a href="#🤔-Discuss-the-following-in-your-own-words." data-toc-modified-id="🤔-Discuss-the-following-in-your-own-words.-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>🤔 Discuss the following in your own words.</a></span></li></ul></li></ul></div>

# # Final Exam Part 3
# &#x1f468;&#x200d;&#x1f3eb; **Overview:**
# This is Part 3 of 3 Parts of your Final Exam/Project. 
# - **Part 1.** Questions on the Course Material. (40%)
# - **Part 2.** Applying the Course material. (40%)
# - **Part 3.** Discussing your exam and the Course Material. (20%) 
# 
# **You must submit your Jupyter notebooks for Part 1 and Part 2 at least 48 hours prior to your appointment for Part 3.** You will be given your grade on Part 1 and Part 2 before the oral exam, so that you know what your status is. *For late submission of Part 1 and/or Part 2, I will deduct 2 points per hour.
# 
# &#x1f4d6; **Rules for "Open Book" Exam:**
# **Like all other portions of this exam, this part of the exam is open notes and open library. It is "open internet search" but you (obviously!) can't post questions on an internet discussion board or homework/problem/exam help site. You are not allowed to communicate with your classmates or any other human being (except me) about these questions or your responses, and this includes human beings (singular or plural, known or anonymous) online.**
# 
# &#x1f4af; **Grading:**
# When we discuss Parts 1 and 2 of the exam, your grade will be "plus", "minus" or "neutral." You can gain, or lose, up to 20 points based on your performance on the oral portion of the exam.
# - A "plus" response indicates that you know the answer to the question, and can expound upon it and related topics with mastery. 
# - A "minus" response indicates that while you may have answered a question correctly, you "got the right answer for the wrong reason" or your understanding of the topic being tested is only superficial. A "minus" response is also indicative of cases where you simply can't answer a question. If for whatever reason you do not schedule an oral exam, that will be taken as a "minus" response for *all* questions. Don't do this: it will be -40% on your final exam grade.
# - A "neutral" response is the default, and is anything except mastery ("plus") or na&iuml;vt&eacute; ("minus"). I anticipate that most responses will be "neutral".
# 
# In addition to discussing your answers in Parts 1 and 2, we will discuss the following questions. Each question group has 6 questions in it. I will randomly select one question from each group; we will then discuss that question. Each question will be graded "plus" (5 points) "minus" (0 points) or "neutral" (3 points). You can score up to 20 points on this portion of the exam, and the "default" score would be about 12 points. 
# 
# &#x1f4dc; **Instructions:** Be prepared to discuss the following questions/topics. I will randomly select 1 question from each group.

# ## &#x1f501; Describe the following effects/experiments/equations, and explain their importance to the origins of quantum mechanics.
# 1. Black-Body Radiation and the Ultraviolet Catastrophe.
# 1. The Davisson-Germer experiment and Electron Scattering.
# 1. Compton Scattering.
# 1. The Photoelectric Effect
# 1. The Rydberg Formula
# 1. The Stern-Gerlach Experiment

# ## &#x1f501; Explain the following topics. 
# 1. What are the key postulates of quantum mechanics?
# 1. What is the Heisenberg Uncertainty Principle? What does it say about the fundamentals of quantum mechanics? What is the commutator between two operators, and how does it relate to the Heisenberg Uncertainty Principle? 
# 1. Explain what the Born-Oppenheimer Approximation is and why it is important.
# 1. Explain what the united-atom and separated-atom limit are for a diatomic molecule. How do these limits relate to molecular-orbital theory and the linear-combination-of-atomic-orbitals technique.
# 1. What are the quantum numbers that describe the state of an atom (neglecting relativity)? What do these quantum numbers have to do with term symbols? What do these quantum numbers have to do with simultaneous observables?
# 1. What is the Stern Gerlach experiment? Can you describe what is happening in the following diagram?
# ![SG3](https://github.com/PaulWAyers/IntroQChem/blob/main/linkedFiles/SternGerlach3.jpg?raw=true "Describe what is happening in this picture")

# ## &#x1f501; What are the eigenfunctions and eigenvalues for the following Hamiltonians. 
# You should be able to explain key characteristics of the systems and the general strategy for (possibly approximate) solving the associated time-independent Schr&ouml;dinger equation.
# 
# \begin{align}
# \hat{H}_1 &= -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} -\frac{\hbar^2}{2m} \frac{d^2}{dy^2} + V_{a_x}(x) + V_{a_y}(y) \\
# \hat{H}_2(\lambda) &= -\frac{\hbar^2}{2m} \frac{d^2}{dx_1^2} -\frac{\hbar^2}{2m} \frac{d^2}{dx_2^2} + V_{a}(x_1) + V_{a}(x_2) 
# - \lambda |x_1 - x_2|\\
# \hat{H}_3(\lambda) &= -\tfrac{1}{2} \nabla_1^2 -\tfrac{1}{2} \nabla_2^2- \tfrac{Z}{r_1} - \tfrac{Z}{r_2} + \tfrac{\lambda}{|\mathbf{r}_1 - \mathbf{r}_2|}\\
# \hat{H}_4 &= -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} -\frac{\hbar^2}{2m} \frac{d^2}{dy^2} -\frac{\hbar^2}{2m} \frac{d^2}{dz^2} + V_{a}\left(\sqrt{x^2 + y^2 +z^2}\right) \\
# \hat{H}_5(\mathbf{R}_B) &=  -\tfrac{1}{2} \nabla_{\mathbf{r}}^2 - \tfrac{Z_A}{r} - \tfrac{Z_B}{|\mathbf{r} - \mathbf{R}_B|} \\
# \hat{H}_6 &= -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} -\frac{\hbar^2}{2m} \frac{d^2}{dy^2} -\frac{\hbar^2}{2m} \frac{d^2}{dz^2} + V_{a_z}(z) + V_{a_r}(\sqrt{x^2+y^2})
# \end{align}
# where
# $$
# V_a(x) = 
# \begin{cases}
#     +\infty & x\leq 0\\
#     0       & 0\lt x \lt a\\
#     +\infty & a \leq x
# \end{cases}
# $$

# ## &#x1f914; Discuss the following in your own words.
# 1. What is a Slater determinant? Why does one use a Slater determinant for a many-fermion system? When is the exact ground-state wavefunction for a many-fermion system a Slater determinant?
# 1. What is the variational principle? How is it used to approximate the ground-state energy and wavefunction of realistic, not-exactly-solvable, Hamiltonians? Can you give an example of how it is used?
# 1. What is the Hartree-Fock method? What is the intuition behind it, and when is it used? 
# 1. What is Perturbation Theory? When is perturbation theory most appropriate? Least appropriate? 
# 1. What is the secular equation? How does it relate to the technique of expanding a wavefunction in a basis set?
# 1. What is electron correlation? How can one approximate the effects of electron correlation?
