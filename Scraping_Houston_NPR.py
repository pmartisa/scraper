#!/usr/bin/env python
# coding: utf-8

# ## Scrape the Houston NPR website
# 
# I want a CSV file called `npr.csv` that includes a row for each story in the top section, with these columns:
# 
# * `section`, the section of the story (e.g. "Transportation", "Harris County")
# * `title`, the title of the story
# * `url`, the full URL to the story
# 
# If you want to start by printing these out, that's fine, but the end result is hopefully a CSV. If you'd like to filter out the rows without a title before saving that would be nice.

# In[12]:


import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.houstonpublicmedia.org/")
doc = BeautifulSoup(response.text)


# In[13]:


len(doc.find_all('article'))


# In[14]:


len(doc.find_all(class_='post'))


# In[15]:


for story in doc.find_all('article'):
    print(story.text.strip())


# In[16]:


stories = doc.find_all(class_='post')


# In[17]:


stories = doc.select('.post')


# In[18]:


dataset = []
for story in stories:
    data = {}
    data['section'] = story.find('h3').text
    data['title'] = story.find('h2').text
    data['url'] = story.find('a')['href']
    dataset.append(data)
dataset


# In[19]:


import pandas as pd
df = pd.DataFrame(dataset)
df.head()


# In[20]:


df.to_csv("npr.csv", index=False)


# In[ ]:




