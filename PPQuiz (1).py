#!/usr/bin/env python
# coding: utf-8

# # Project Description

# My project is a quiz that will help users decide what programming language they should learn. When they start the program it will ask them what quiz they want to take. There are two options and each option allows the user to take a quiz with three different programming languages (they are listed). After they pick a quiz within the quiz it will ask the users name, print a greeting, and ask if they are ready to begin. If they say no they are not ready to begin then the quiz will quit and provide them the option to watch a video.
# 
# Within each quiz there are four questions that will be asked and each option will concatenate with the corresponding dictionary key. At the results part of the quiz it will check to make sure that there at least one of the keys has a value greater than 1. If there is a quiz the function will then provide a tie breaker question that corresponds to the tie between those specific keys.
# 
# The video function allows the user to choose a youtube lesson on the language of their choice. They are also able to skip this by clicking any key other than the ones with assigned outputs. This is the end of my project.
# 

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[1]:


from my_module.functions import game_choice, quiz1, quiz2, video


# In[2]:


game_choice()
video()


# #### Extra Credit (*optional*)
# 
# Replace all of this text with a brief explanation (~3 sentences) of: 
# 1. My only programming experience was two weeks of a C++ class that was cancled because not enough people were in it at my CC.
# 2. I went above and beyond in my project because I acocunted for all of the different variables that I could think of. For example if someone says no they dont want to take the quiz then the program quits. The hardest part for me to figure out was how to make sure there was no tie. You can see how i did that in the results function. I also taught myself how to import a video for each programming language. (I learned this from google).

# In[ ]:




