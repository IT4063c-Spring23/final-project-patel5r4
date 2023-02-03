#!/usr/bin/env python
# coding: utf-8

# # Can stress lead to high blood pressure?📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 <!-- Answer Below -->
# 
# Excessive stress negatively impacts health and might lead to anxiety and depression, and can also lead to cardiovascular diseases. The American Psychological Association (APA), reports that Millenials and Gen X experience high-than-average stress levels. Can hypertension or stress increase blood pressure?  

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->
# 
# My specific question is if there is a connection between stress-levels and experiencing high blood pressure.

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->
# 
# A hypothesized answer will be - excessive stress impacts blood pressure levels in human beings. 

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->
# 
# 1. CSV file from data.world - This is data from Teen Stress & Mental Health Poll, where users are asked how much of a role stress plays in their lives, and how they manage it. 
# 
# Questions asked:
# 
# How often are you stressed?
# 
# What stresses you out the most?
# 
# What are you most likely to do with you're stressed?
# 
# What resources do you use to help?
# 
# 
# Results:
# 
# 16,101 (44.88%) teens say they are stressed "all the time"
# 
# Only 6.3% of teams (2,261) state that they are "never" stressed
# 
# Relationships were the most likely cause of stress at 27.22%
# 
# 
# Data:
# 
#     import pandas as pd
# df = pd.read_csv('https://query.data.world/s/4dgpmb77g3amqv5tigoisytzbh67hu') or https://query.data.world/s/4dgpmb77g3amqv5tigoisytzbh67hu (download link)
# 
# 2. Infographic on Stress and its impact on ability to function, by the APA 
# 
# Link: https://www.apa.org/news/press/releases/stress/2022/infographics/infographic-ability-function
# 
# 3. Infographic on Younger adults feeling completely overwhelmed by stress
# 
# Link: https://www.apa.org/news/press/releases/stress/2022/infographics/infographic-younger-adults
# 
# 4. Data Visualization on high blood pressure across countries; aged 50 and over; 2007-2010 by census.gov
# 
# Link: https://www.census.gov/content/dam/Census/newsroom/blogs/2012/05/high-blood-pressure-not-just-an-american-problem/SAGE-figure.jpg
# 
# 

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->
# 
# The first data source shares the number of people from the survey who are stressed "all the time", this can be used to show the increasing levels of stress in today's generation.
# 
# The next two data sources (infographics) can be used to show that stress impacts the ability to function and that younger adults feel completely overwhelmed by stress, by age groups. Further, this can be used to match data on high pressure levels by age group, and find any links between stress and blood pressure levels. 
# 
# The fourth data source has visualization on hypertension being one of the top three chronic conditions by age group across countries. Hypertension tops the list, again that can be matched with stress levels in those countries to find links between stress and blood pressure levels. 
# 

# In[1]:


# Start your code here 


# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->
# 
# 1. Data.world
# 
# 2. American Psychological Association
# 
# 3. Census.gov

# In[2]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

