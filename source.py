#!/usr/bin/env python
# coding: utf-8

# # Does the vehicle type affect the chances of rollover and injury?📝
# 
# <!-- Are SUV rollover rates declining? -->
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 <!-- Answer Below -->
# 
# I think the bigger the vehicle, the safer it is on the road. However, bigger vehicle like SUVs and trucks are believed to be more likely to rollover than passenger cars. But that may not necessarily mean that the accidents will always be fatal. Some data even says that the rollover rates for SUVs are declining (article: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3217479/). 
# 
#    

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->
# 
# Although certain road and traffic conditions increase the likelihood of fatal accidents, does it matter what type of vehicle are we driving? Are there more rollover chances for SUVs than cars?

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->
# 
# A hypothesized answer will be - SUVs are more likely to rollover due to their design (they are generally taller and narrower), but the rates are declining and the accidents are not always fatal.   

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->
# 
# 1. https://www.iihs.org/topics/fatality-statistics/detail/passenger-vehicle-occupants?_gl=1*1t3lna3*_ga*YW1wLU5uWExTOC00UnpJamxTZ2M5RlNOUEE.#fn1ref1 
# 
# This webpage has multiple data tables on death and rollover rates by vehicle type. 
# 
# 2. https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/809438 
# 
# This documnent has data tables that show the number of rollovers by vehicle type.
# 
# 3. https://www.kaggle.com/datasets/usdot/nhtsa-traffic-fatalities?select=vehicle_2016 
# 
# This dataset is from Kaggle - it has traffic fatality records.  
# 
# 

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->
# 
# These sources have data about crashes, deaths and rollovers. These can be merged together - for example, total crashes and rollover by vehicle type will show what type of vehicle is most likely to rollover and if the SUV rollover rates are really declining. 
# 

# In[1]:


# Start your code here 


# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->
# 
# 1. National Highway Traffic Safety Administration (NHTSA)
# 
# 2. Kaggle 
# 
# 3. Insurance Institute for Highway Safety (IIHS)

# In[1]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

