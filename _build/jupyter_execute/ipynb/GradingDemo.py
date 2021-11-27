#!/usr/bin/env python
# coding: utf-8

# Assume that the grades one has are:
# - **Assignments:** 100, 100, 100, 30, 90, 50, 100, 0, 75, 80
# - **Final Exam/Project:** 70
# - **Extra Credit:** 500 problems

# In[1]:


import numpy as np #import numpy

assignments =  [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #assignment marks
final = 50       #final exam mark
extra = 700/1200*40 #percent of your final mark that is 100 due to extra credit
print('percentage of final mark that is 100 due to extra credit: ', extra)


# In[2]:


#replace assignment marks that are below the final mark with the final mark. 
new_assignments = np.where(assignments > np.array(final), assignments, final)

#Print out new assignments to make sure they are sensible.
print('New assignment grades after replacement with Final', new_assignments)
print('old assignment average:', np.mean(assignments))
print('new assignment average:', np.mean(new_assignments))


# In[3]:


#The overall mark is 20% from the final exam/project and 80% from the (revised) assignments
mark = .2*final + .8*np.mean(new_assignments)

#However, 50/1200 percent of the mark is a 100% due to the extra credit. 
adjusted_mark = extra + (1-extra/100)*mark

print('mark without extra credit: ', mark)
print('mark with extra credit:    ', adjusted_mark)


# In[ ]:





# In[ ]:




