#!/usr/bin/env python
# coding: utf-8

# # Python _and_ GitHub fundamentals
# 
# 
# Hello Folks! In this tutorial we are going to cover basics steps of __editing__, __submitting__ and __analyzing__ our results using GitHub environment along with basic python skills.

# ## Receive the assignments
# 
# 
# This mock assignment is available via the [link](https://classroom.github.com/a/8eHJCZ35). Accept the assignment, as described in [GitHub fundamentals](https://qc-edu.github.io/IntroQM2022/ipynb/ghfundamentals.html)
# ![p1](pics_t0/1.png)
# 
# Now you will see that a new repository was created with the task ![p1](pics_t0/2.png)
# There is only one file --jupyter notebook (_\*.ipynb file_)-- that you need to complete in order to have your assignment done. 
# 
# In the current repo this file is called **Schrodinger.ipynb**

# ## Editing a Jupyter Notebook
# 
# There are several ways to edit .ipynb file. 
# 1. Using [Google Colab](https://colab.research.google.com/). **Recommended!**
# 1. Using [Binder](https://mybinder.org/). 
# 1. You can, in general, use any online Jupyter Hub (e.g. [syzygy](https://mcmaster.syzygy.ca/)). However, it can be difficult to ensure that the dependencies you need are installed.
# 1. You can edit Jupyter Notebooks locally. It is relatively easy to use [jupyter](https://docs.anaconda.com/ae-notebooks/user-guide/basic-tasks/apps/jupyter/index.html) through [Anaconda](https://www.anaconda.com/products/individual). One can also use [Visual Studio Code](https://code.visualstudio.com/) to edit [notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
# 
# We will ensure that assignments work with colab. We'll try to help people using other platforms, but make no promises.
# 
# In this tutorial we will cover the how to work with Jupyter notebooks through google colab. To do this, you need to download the .zip archive of the repo. In order to download it click `code` and `Download Zip` ![p4](pics_t0/3.png)
# 
# When the repo is downloaded you need to go to to [Google Colab](https://colab.research.google.com/) and add the .ipynb file from the repo: `File` $\rightarrow$ `Upload notebook` ![p5](pics_t0/4.png)
# Upload the **Schrodinger.ipynb** file 
# 
# Voila! ![p6](pics_t0/5.png)
# 
# ## Understanding the assignment
# There is an instruction written in the notebook. All you need to do is to fill the code between 
# ```
# ### START YOUR CODE HERE
# ...
# ### END YOUR CODE HERE
# ```
# Let's say I'm sensetive enough to assume that cat is 100% alive:
# ![p6](pics_t0/6.png)
# 
# Now, we can save and download edited notebook: click `File` $\rightarrow$ `Save` and then `Download` $\rightarrow$ `Download .ipynb`
# ![p7](pics_t0/7.png)
# 
# 
# ## Submitting an assignment
# 
# Submitting the assignment is breeze!
# When you downloaded the final version of the file just go to your repo and click `Add file` $\rightarrow$ `Upload files` and upload recently created file ![p9](pics_t0/9.png)
# Now commit your changes and click `Commit changes` ![p10](pics_t0/10.png)
# 
# 
# ## Check the result
# 
# In order to check whether your code passed tests all you need to do is go to `Actions`$\rightarrow$ `Your commit` $\rightarrow$ `Test with pytest`. ![p11](pics_t0/11.png)
# 
# 
# Ooops.... red cross indicates that there is something wrong. Let's try again.
# 
# Open Google Colab and now let's say that cat is alive _and_ dead simultaneously:
# ![p12](pics_t0/12.png)
# 
# If you can see green check mark - ***CONGRATULATIONS!*** you passed the assignment
# 
# 
# Upload and commit new notebook and check if it passed the test:
# ![p14](pics_t0/14.png)
# 
# 
# Well done! We nailed it and now it's finally a time to reward yourself scrolling Tik Tok
# 
# 
# 
# __Nota Bene__
# In case you can't pass the test click at the commit name (`Wrong answer` in this particular case) and then contact me `@RichRick1`at the comment section
# ![p16](pics_t0/15.png) ![p17](pics_t0/16.png)
# 
# 

# 
