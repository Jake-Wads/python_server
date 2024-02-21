#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Acquire the data
df = pd.read_csv('/Users/zach/ds/data/kickstarter.csv')

# A little bit of data prep
df = df[['category', 'location', 'status', 'goal', 'pledged', 'backers', 'duration', 'updates']]
df['state'] = df.location.str[-2:]
df = df.drop(columns='location')
df.category = df.category.str.replace('&amp;', '&')

# Restrict our analysis
states = ['CA', 'NY', 'IL', 'TX']
categories = ['Music', 'Film & Video', 'Art', 'Publishing']
df = df[df.goal < 5000]
df = df[df.pledged < 20_000]
df = df[df.backers > 10]
df = df[df.category.isin(categories)]
df = df[df.state.isin(states)]
df = df[df.status.isin(['failed', 'successful'])]

# The rest is demos of how to use seaborn + seaborn functions

# In[3]:


sns.relplot(y='pledged', x='goal', data=df, hue='category')


# In[4]:


sns.lmplot(y='pledged', x='goal', data=df, hue='status')


# In[5]:


sns.barplot(data=df, y='goal', x='category', hue='status')


# In[6]:


sns.barplot(y='status', x='goal', data=df)


# In[7]:


sns.boxplot(data=df, y='goal', x='category', hue='status')


# In[8]:


sample = df.sample(200)
sns.swarmplot(data=sample, y='duration', x='state')


# In[9]:


sns.violinplot(data=df, y='duration', x='state')


# In[10]:


sns.heatmap(pd.crosstab(df.category, df.state), cmap='Reds')


# In[11]:


sns.heatmap(df.corr(), center=0, cmap='Blues', annot=True)
plt.yticks(rotation=0)


# In[12]:


fig, axs = plt.subplots(2, 2, figsize=(16, 9))
fig.subplots_adjust(hspace=.3)

for ax, (state, data) in zip(axs.ravel(), df.groupby('state')):
    sns.barplot(x='status', y='duration', data=data, hue='category', ax=ax)
    ax.legend().remove()
    ax.set(title='{} (n={:,})'.format(state, data.shape[0]))

axs[0, 1].legend(loc='upper left')

