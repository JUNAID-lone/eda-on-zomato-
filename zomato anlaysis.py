#!/usr/bin/env python
# coding: utf-8

# ## zomato dataset Exploratory data Analysis
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[148]:


df=pd.read_csv("zomato.csv",encoding='latin-1')
df.head(4)


# In[3]:


df.columns


# In[4]:


df.info()


# In[5]:


df.describe()


# ## what all Thing we do
# 1. missing value
# 2. Explore about the numerical variables
# 3. EXPLORE about categorical variable
# 4. finding relationship between features

# In[7]:


df.shape


# In[8]:


df.isnull().sum()


# In[9]:


[features  for features in df.columns if df[features].isnull().sum()>0]


# In[10]:


sns.heatmap(df.isnull(),yticklabels=False,)#we  have huge amount of rows so thats why we dont  get missing


# In[11]:


#import json file
df_country=pd.read_excel('Country-Code.xlsx')
df_country


# In[12]:


df_country.head()


# In[13]:


df.columns


# In[14]:


final_df=pd.merge(df,df_country,on='Country Code',how='left')


# In[15]:


final_df.head(3)


# In[16]:


final_df.columns


# In[17]:


country_names=final_df.Country.value_counts().index#To get a list of unique categories (like countries) in sorted order


# In[18]:


country_val=final_df.Country.value_counts().values#Count of how many times each country appears.


# In[19]:


##pie chart-- top three countrys
plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.1f%%')
plt.show()


# observation:zomato maximum records or transaction are from india After that untited state and united kingdom

# In[21]:


final_df.columns


# In[22]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'rating count'})


# In[23]:


ratings


# ## observation
# 1. when the rating is between 4.5 to 4.9----> excellent
# 2. when the rating are between 4.0 to 3.4---> very goog
# 3. when the rating is between 3.5 to 3.9--->good
# 4. when the rating is betweeen 2.5 to 2.9--->average
# 5. when the rating is between 2.0 to 2.4--->poor

# In[25]:


ratings.head()


# In[26]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(x="Aggregate rating",y="rating count",data=ratings)
##plt.figure(figsize=(12,6))
plt.show()


# In[27]:


sns.barplot(x="Aggregate rating",y="rating count",hue='Rating color',data=ratings,palette=['white','red','orange','yellow','green','green'])


# 1.not rated count is very high
# 2.maximum number of rating are between 2.4 to 3.9

# In[152]:


sns.countplot(x="Rating color",data=ratings,palette=['white','red','orange','yellow','green','green'])
plt.show()


# In[30]:


# find the countries name that has given 0 ratings
final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)


# observation:
# maximum number of zero ratings are from india customers

# In[32]:


#find out whic currency is used by which country
final_df.columns


# In[33]:


final_df.groupby(['Country','Currency']).size().reset_index()


# In[35]:


#which country do have online deliveries option
final_df[final_df['Has Online delivery']=="Yes"].Country.value_counts()


# In[36]:


final_df.groupby(['Has Online delivery','Country']).size().reset_index()


# OBSERVATION :
# ONLINE DELIVERIES ARE AVAILABLE IN INTDIA AND UEA

# In[45]:


## CREATE A PIE CHART FOR top 5 CITIES DISTRIBUTION


# In[46]:


final_df.City.value_counts().index


# In[95]:


city_value=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index
print(city_value)
print(city_labels)


# In[103]:


plt.pie(city_value[:5],labels=city_labels[:5],autopct='%1.2f%%')
plt.show()


# In[107]:


final_df.columns


# In[133]:


cu_value=final_df.Cuisines.value_counts().values
c_value=final_df.Cuisines.value_counts().index


# In[143]:


plt.pie(cu_value[:10],labels=c_value[:10],autopct='%1.2f%%')
plt.show()


# In[129]:


final_df.Cuisines.value_counts()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




