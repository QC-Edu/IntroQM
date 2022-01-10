#!/usr/bin/env python
# coding: utf-8

# # Assignment: Google Colab
# 
# Hello Folks! In this tutorial we are going to cover basics steps of __editing__, __submitting__ and __analyzing__ our results using GitHub, along with some basic python skills.

# ## Receive the Assignment
# 
# This mock assignment is available via the [link](https://classroom.github.com/a/xBTR2JqC). Accept the assignment, as described [previously](https://qc-edu.github.io/IntroQM2022/ipynb/ghfundamentals.html)
# ![p1](pics_t0/1.png)
# 
# A new repository was created for this assignment ![p1](pics_t0/2.png)
# There is only one file &mdash; jupyter notebook (_\*.ipynb file_) &mdash; that you need to complete in order to complete this assignment. 
# 
# In the current repo this file is called **`Schrodinger.ipynb`**.

# ## Editing a Jupyter Notebook
# 
# As described in the [notes](https://qchem.qc-edu.org/ipynb/jupyter.html#what-is-jupyter), there are several ways to edit `.ipynb` files.
# 
# In this tutorial assignment we will show the how to work with Jupyter notebooks through google colab. There are two ways to do this.
# 
# ### Direct Download of the Repository
# 1. Download the .zip archive of the repo. In order to download it click `code` and `Download Zip` ![p4](pics_t0/3.png). 
# 1. When the repo is downloaded, go to [Google Colab](https://colab.research.google.com/) and add the .ipynb file from the repo: `File` $\rightarrow$ `Upload notebook` ![p5](pics_t0/4.png). This uploads the **Schrodinger.ipynb** file 
# 
# Voila! ![p6](pics_t0/5.png)
# 
# ### Using GitHub and Colab together.
# You can use GitHub and Colab together. It can be [relatively complicated](https://medium.com/analytics-vidhya/how-to-use-google-colab-with-github-via-google-drive-68efb23a42d) in [some cases](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb) but for a public repository, it's quite simple:
# > For a directory with the path `https://github.com/organization/repository/blob/branch/directory/subdirectory/filename.ipynb`, merely replace the first part of the path, so that one has `https://colab.research.google.com/github//organization/repository/blob/branch/directory/subdirectory/filename.ipynb`. That is, one replaces `github.com` with `colab.research.google.com/github`.
# 
# ### Extension for Chromium Browsers.
# If you use a browser like Google Chrome or Microsoft Edge, then you can use the [Open in Colab](https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo) browser extension. Then, 
# 1. View the target Jupyter Notebook on Github
# 2. Click  the extension to open the notebook in Colab.

# ## Understanding the assignment
# There is an instruction written in the notebook. All you need to do is to fill the code between 
# ```
# ### START YOUR CODE HERE
# ...
# ### END YOUR CODE HERE
# ```
# 
# Let's say I'm sensitive enough to assume that cat is 100% alive:
# ![p6](pics_t0/6.png)
# 
# Now, we can save and download the edited notebook: click `File` $\rightarrow$ `Save` and then `Download` $\rightarrow$ `Download .ipynb`
# ![p7](pics_t0/7.png)

# ## Submitting the assignment
# Submitting the assignment is a breeze!
# When you downloaded the final version of the file just go to your repo and click `Add file` $\rightarrow$ `Upload files` and upload your recently created file ![p9](pics_t0/9.png)
# 
# To commit your changes, just click `Commit changes` ![p10](pics_t0/10.png)

# ## Check the result
# 
# In order to check whether your code passed tests all you need to do is go to `Actions`. Be patient; the tests should have automatically been triggered when the tests were run.
# 
# Uh-oh.... the red cross indicates that there is something wrong. Let's try again.
# 
# Open Google Colab and now let's say that cat is alive _and_ dead simultaneously:
# ![p12](pics_t0/12.png)
# 
# If you can see green check mark.... ***CONGRATULATIONS!*** you passed the assignment
# 
# 
# Upload and commit new notebook and check if it passed the test:
# ![p14](pics_t0/14.png)
# 
# 
# Well done! We nailed it and now it's finally a time to reward yourself scrolling TikTok.
# 
# 
# 
# 

# ## Nota Bene
# If you can't pass the test, click at the commit name (`Wrong answer` in this particular case) and then contact me `@RichRick1` using the comment section
# ![p16](pics_t0/15.png) ![p17](pics_t0/16.png)

# ## Grading Scheme
# Completing the assignment earns you an **S**. To earn an **S+**, can you find another choice for `is_alive` and `is_dead` that *also* passes the tests? Explain why some choices of `is_alive` and `is_dead` pass the tests and others do not by adding a Markdown cell to the end of your Notebook. 

# 
