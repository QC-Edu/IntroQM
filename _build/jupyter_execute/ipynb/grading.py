#!/usr/bin/env python
# coding: utf-8

# # Using Python, Numpy, Jupyter, and Syzygy
# ## Objective
# To practice using key tools that we'll need to use during this course.
# ## Instructions
# Before you turn this problem in, make sure everything runs as expected. First, restart the kernel (in the menubar, select Kernel → Restart) and then run all cells (in the menubar, select Cell → Run All).
# 
# Make sure you fill in any place that says YOUR CODE HERE or "YOUR ANSWER HERE". Don't forget to delete `raise NotImplementedError()`

# ## Problem Statement
# Write a Python function to compute the final mark for a student in this class. 
# - **Input**: a list of assignment grades, a final exam grade, and a number of pages of extra credit that have been provided.
# - **Output**: the final mark. 
# Grading Scheme:
# - Assignment grades are replaced by the final exam grade if the final exam grade is higher.
# - The final mark (without extra credit) is 
# 
# $$ 
# \text{total mark} = 0.2(\text{final exam grade}) + 0.8(\text{mean of assignment grades after replacements})
# $$
# - Extra credit counts by replacing a set percentage (up to 40%) of your final mark with a 100%. The percentage of your final mark that is replaced is given by the below formula. No more than 1200 pages of extra credit problems can be done.
# 
# $$
# \text{percent extra credit} = \frac{\text{number of pages of extra credit}}{1200} \cdot 40
# $$

# In[1]:


import numpy as np


def total_mark_xc(assignments, exam, extra_credit_pages=0):
    """Computes the final mark for one student in CHEM 3PA3 in 2021

    Parameters
    ----------
    assignments : array_like
        assignment grades.
    exam : scalar
        the grade on the final project/exam.
    extra_credit_pages : scalar, optional
        the number of extra credit pages. (default is 0)

    Returns
    -------
    total_mark_xc : scalar
         The final mark in the course, computed according to the syllabus.
    """

    # YOUR CODE HERE
    raise NotImplementedError()


# In[2]:


# It's good to always test to make sure your code is right.
np.testing.assert_almost_equal(total_mark_xc([100, 100, 100, 100], 0), 80)
np.testing.assert_almost_equal(total_mark_xc([0, 0], 100, 0), 100)
np.testing.assert_almost_equal(total_mark_xc([0, 0], 0, 1200), 40)


# ## Extend to Multiple students
# It is easy to use Numpy to extend this analysis to multiple students. Suppose that you had assignments, finals, and extra credit for more than one student. Rewrite your function so it works for that case too. This extra credit problem is worth 15 "points", so you can make a 115 on this assignment.
# 
# 

# In[ ]:


import numpy as np


def total_mark_xc_mult(assignments, exam, extra_credit_pages):
    """Computes the final mark for multiple students CHEM 3PA3 in 2021

    Parameters
    ----------
    assignments : array_like
        assignment grades; number-of-students by number-of-assignments
    exam : array_like
        the grade on the final project/exam for each student.
    extra_credit_pages : array_like
        the number of extra credit pages for each student

    Returns
    -------the
    total_mark_xc : array_like
         The final mark in the course for all students, computed according to the syllabus.
    """

    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


assignments = np.array([[100, 100, 100, 100], [0, 0, 0, 0], [0, 0, 0, 0]])
exam = np.array([0, 100, 0])
extra_credit_pages = np.array([0, 0, 1200])
np.testing.assert_almost_equal(
    total_mark_xc_mult(assignments, exam, extra_credit_pages), [80.0, 100.0, 40.0]
)

