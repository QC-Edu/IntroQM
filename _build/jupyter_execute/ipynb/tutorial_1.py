#!/usr/bin/env python
# coding: utf-8

# # Assignment: Normalizing Wavefunctions with Jupyter and Colab
# 
# ##  &#x1f3af; Objective¶
# To practice Jupyter and Colab.
# 
# ## &#x1f4dc; Instructions
# 1. Presuming you already have a GitHub account, [connect to GitHub Classroom](https://classroom.github.com/a/1DZ_qS9k). You'll see ![p1](pics/2.png)
# 1. Click `Accept the assignment` and then update the page ![p2](pics/3.png). You will see a new repository with the task ![p3](pics/4.png)
# 1. To complete the assignment you need to complete the Jupyter notebook **`Normalizing_eigenfunctions.ipynb`**.

# ## Editing a Jupyter Notebook from GitHub
# 
# As described in the [notes](https://qchem.qc-edu.org/ipynb/jupyter.html#what-is-jupyter), there are several ways to edit `.ipynb` files.
# 
# ### Using Google Colab (direct download and upload)
# In this tutorial we will show how to work with Jupyter notebooks through Google Colab.
# 1. Download the `.zip` archive of the GitHub repo. In order to download it click `code` and `Download Zip` ![p4](pics/5.png)
# 1. When the repo is downloaded, go to [Google Colab](https://colab.research.google.com/) and add the `.ipynb` file from the repo: `File` $\rightarrow$ `Upload notebook` ![p5](pics/6.png)
# You will see this window ![p6](pics/7.png)
# 1. Upload the `.ipynb` file 
# 
# Voila! ![p7](pics/8.png)
# 
# ### Extension for Chromium Browsers.
# If you use a browser like Google Chrome or Microsoft Edge, then you can use the [Open in Colab](https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo) browser extension. Then, 
# 1. View the target Jupyter Notebook on Github
# 2. Click the extension to open the notebook in Colab.
# 3. When you do this, you may need to grant Google/Microsoft (Colab/GitHub) permission to interchange information.

# ### Understanding the assignment
# There is an instruction written in the notebook. All you need to do is to fill the code between 
# ```
# ### START YOUR CODE HERE
# ...
# ### END YOUR CODE HERE
# ```
# ![p8](pics/9.png)
# 
# The purpose of this assignment is to compute the normalization constant for the particle-in-a-box. The particle-in-a-box is perhaps the simplest (bound) quantum system. You do not need to know much about the particle-in-a-box to complete this assignment however: referring to the relevant section of the [notes](https://qchem.qc-edu.org/ipynb/ParticleIn1DBox.html#normalization-of-wavefunctions), one sees that one can choose $A_n = \sqrt{\frac{2}{a}}$.
# 
# Once the code is completed, you can click the play button to evaluate the cell.
# When you are satisfied with a code just click `File` $\rightarrow$ `Save` and then `Download` $\rightarrow$ `Download .ipynb`
# ![p9](pics/10.png)

# ## Submitting an assignment
# 
# Submitting the assignment is breeze!
# When you downloaded the final version of the file just go to your repo and click `Add file` $\rightarrow$ `Upload files`; then upload your newly created file ![p10](pics/11.png)
# Now commit your changes and click `Commit changes` ![p11](pics/12.png)

# ## Check the result
# 
# In order to check whether your code passed tests all you need to do is go to `Actions`$\rightarrow$ `Your commit` $\rightarrow$ `Test with pytest`. ![p12](pics/13.png) ![p13](pics/14.png) In most cases the tests will run automatically, and you do not need to explicitly invoke Pytest.
# 
# If you see a green check mark: ***CONGRATULATIONS!*** you passed the assignment 
# 
# If there is a bug, then the following may occur:
# ![p14](pics/15.png) ![p15](pics/16.png)
# 
# Try to find your mistake but if you get stuck, contact me `@RichRick1`
# ![p16](pics/17.png) ![p17](pics/18.png)

# ## Grading Scheme
# Completing the assignment earns you an **S**. To earn an **S+**, explore whether there are other choices for the normalization constant that also pass the tests. Can you find a (correct) choice for the normalization constant that nonetheless fails the tests? How is this possible!

# 
