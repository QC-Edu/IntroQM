#!/usr/bin/env python
# coding: utf-8

# # Using Python, Numpy, Jupyter, and Syzygy
# ## &#x1f3af; Objective
# To practice using key tools that we'll need to use during this course.
# ## &#x1f4dc; Instructions
# Before you turn this problem in, make sure everything runs as expected. First, restart the kernel (in the menubar, select Kernel → Restart) and then run all cells (in the menubar, select Cell → Run All).
# 
# Make sure you delete the placeholder code/text and fill in any place that says "YOUR CODE HERE" or "YOUR ANSWER HERE". Please also fill in your name, username (the prefix to your @university.ext e-mail), and student ID number in the cell below.

# In[1]:


Name = "First M. Last"
email_user_name = "username"
ID_number = 1234567


# ## &#128105;&#8205;&#128187; Compute Final Mark for a Single Student
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

# In[2]:


get_ipython().run_line_magic('load_ext', 'nb_black')


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

    ### BEGIN SOLUTION
    # Compute fraction of final mark that will be 100 due to extra credit
    # Using the built-in 'min' function in Python
    xc_fraction = (min(extra_credit_pages, 1200) / 1200) * (40 / 100)

    # Replace assignment grades that are below the final exam/project mark with that mark.
    assignments = np.where(assignments > np.array(exam), assignments, exam)

    # Compute final mark ignoring extra credit
    total_mark = 0.2 * exam + 0.8 * np.mean(assignments)

    # Compute final mark including extra credit
    total_mark = xc_fraction * 100 + (1 - xc_fraction) * total_mark

    return total_mark


# Special case just to test:
assignments = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
exam = 0
print("the final mark for the student in CHEM 3PA3: ", total_mark_xc(assignments, exam))
### END SOLUTION


# In[2]:


# It's good to always test to make sure your code is right.
np.testing.assert_almost_equal(total_mark_xc([100, 100, 100, 100], 0), 80)
np.testing.assert_almost_equal(total_mark_xc([0, 0], 100, 0), 100)
np.testing.assert_almost_equal(total_mark_xc([0, 0], 0, 1200), 40)

### BEGIN HIDDEN TESTS
np.testing.assert_almost_equal(total_mark_xc([0, 0], 0, 2400), 40)
assignments = [100, 100, 100, 30, 90, 50, 100, 0, 75, 80]
np.testing.assert_almost_equal(total_mark_xc(assignments, 70, 500), 85.333333333333333)
assignments = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
np.testing.assert_almost_equal(total_mark_xc(assignments, 50, 700), 70.03030303030303)
### END HIDDEN TESTS


# ## &#128105;&#8205;&#128187; Extend to Multiple students
# You can use Numpy to extend this analysis to multiple students. Suppose that you had assignments, finals, and extra credit for more than one student. Rewrite your function so it works for that case too. This extra credit problem is worth 15 "points", so you can make a 115 on this assignment.
# 
# 

# In[5]:


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

    ### BEGIN SOLUTION
    # Compute fraction of final mark that will be 100 due to extra credit
    # Using the built-in 'min' function in Python
    xc_fraction = (np.minimum(extra_credit_pages, np.repeat(1200, len(extra_credit_pages))) / 1200) * (40 / 100)

    # Replace assignment grades that are below the final exam/project mark with that mark.
    assignments = np.where(assignments > np.array(exam)[:, np.newaxis], assignments, exam[:, np.newaxis])
    
    # Compute final mark ignoring extra credit
    total_mark = 0.2 * exam + 0.8 * np.mean(assignments,axis=1)

    # Compute final mark including extra credit
    total_mult = xc_fraction * 100 + (1 - xc_fraction) * total_mark

    return total_mult


def total_mark_xc_mult_for(assignments, exam, extra_credit_pages):
    """Computes the final mark for multiple students CHEM 3PA3 in 2021 using a for loop.

    Parameters
    ----------
    assignments : array_like
        assignment grades; number-of-students by number-of-assignments
    exam : array_like
        the grade on the final project/exam for each student.
    extra_credit_pages : array_like
        the number of extra credit pages for each student

    Returns
    -------
    total_mark_xc : array_like
         The final mark in the course for all students, computed according to the syllabus.
    
    Notes
    -----
    This implementation is slower than the numpy-based solution, but should still be plenty fast.
    
    """
    
    # Compute number of students
    n_students = len(extra_credit_pages)
    total_mult = []
    for i in range(n_students):
        total_mult.append(total_mark_xc(assignments[i], exam[i], extra_credit_pages[i]))

    return total_mult

# Special case just to test:
assignments = np.array([[100, 100, 100, 100], [0, 0, 0, 0], [0, 0, 0, 0]])
exam = np.array([0, 100, 0])
extra_credit_pages = np.array([0, 0, 1200])
print("the final mark for the student in CHEM 3PA3: ", total_mark_xc_mult(assignments, exam,extra_credit_pages))
print("the final mark for the student in CHEM 3PA3: ", total_mark_xc_mult_for(assignments, exam,extra_credit_pages))
### END SOLUTION


# In[6]:


assignments = np.array([[100, 100, 100, 100], [0, 0, 0, 0], [0, 0, 0, 0]])
exam = np.array([0, 100, 0])
extra_credit_pages = np.array([0, 0, 1200])
np.testing.assert_almost_equal(
    total_mark_xc_mult(assignments, exam, extra_credit_pages), [80.0, 100.0, 40.0]
)
### BEGIN HIDDEN TESTS
assignments = np.array(
    [
        [100, 100, 100, 100],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 40, 70, 100],
    ]
)
exam = np.array([0, 100, 0, 0, 50])
extra_credit_pages = np.array([0, 0, 1200, 1800, 700])
np.testing.assert_almost_equal(
    total_mark_xc_mult(assignments, exam, extra_credit_pages),
    [80.0, 100.0, 40.0, 40.0, 72.4],
)

### END HIDDEN TESTS

