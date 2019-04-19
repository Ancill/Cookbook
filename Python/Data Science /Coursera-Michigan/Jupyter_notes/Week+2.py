
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.0** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # The Series Data Structure

# In[23]:


import pandas as pd
get_ipython().magic('pinfo pd.Series')


# In[24]:


animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)


# In[25]:


numbers = [1, 2, 3]
pd.Series(numbers)


# In[26]:


animals = ['Tiger', 'Bear', None]
pd.Series(animals)


# In[27]:


numbers = [1, 2, None]
pd.Series(numbers)


# In[28]:


import numpy as np
np.nan == None


# In[29]:


np.nan == np.nan


# In[30]:


np.isnan(np.nan)


# In[31]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[32]:


s.index


# In[33]:


s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s


# In[34]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
s


# # Querying a Series

# In[35]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[36]:


s.iloc[3]


# In[37]:


s.loc['Golf']


# In[38]:


s[3]


# In[39]:


s['Golf']


# In[40]:


sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)


# In[41]:


s[0] #This won't call s.iloc[0] as one might expect, it generates an error instead


# In[42]:


s = pd.Series([100.00, 120.00, 101.00, 3.00])
s


# In[43]:


total = 0
for item in s:
    total+=item
print(total)


# In[44]:


import numpy as np

total = np.sum(s)
print(total)


# In[45]:


#this creates a big series of random numbers
s = pd.Series(np.random.randint(0,1000,10000))
s.head()


# In[46]:


len(s)


# In[47]:


get_ipython().run_cell_magic('timeit', '-n 100', 'summary = 0\nfor item in s:\n    summary+=item')


# In[48]:


get_ipython().run_cell_magic('timeit', '-n 100', 'summary = np.sum(s)')


# In[49]:


s+=2 #adds two to each item in s using broadcasting
s.head()


# In[50]:


for label, value in s.iteritems():
    s.set_value(label, value+2)
s.head()


# In[161]:


get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0,1000,10000))\nfor label, value in s.iteritems():\n    s.loc[label]= value+2')


# In[162]:


get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0,1000,10000))\ns+=2')


# In[163]:


s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
s


# In[164]:


original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)


# In[110]:


original_sports


# In[111]:


cricket_loving_countries


# In[112]:


all_countries


# In[113]:


all_countries.loc['Cricket']


# # The DataFrame Data Structure

# In[114]:


import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()


# In[115]:


df.loc['Store 2']


# In[116]:


type(df.loc['Store 2'])


# In[117]:


df.loc['Store 1']


# In[118]:


df.loc['Store 1', 'Cost']


# In[119]:


df.T


# In[120]:


df.T.loc['Cost']


# In[121]:


df['Cost']


# In[122]:


df.loc['Store 1']['Cost']


# In[123]:


df.loc[:,['Name', 'Cost']]


# In[124]:


df.drop('Store 1')


# In[125]:


df


# In[126]:


copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
copy_df


# In[127]:


get_ipython().magic('pinfo copy_df.drop')


# In[128]:


del copy_df['Name']
copy_df


# In[129]:


df['Location'] = None
df


# # Dataframe Indexing and Loading

# In[130]:


costs = df['Cost']
costs


# In[131]:


costs+=2
costs


# In[132]:


df


# In[133]:


get_ipython().system('cat olympics.csv')


# In[134]:


df = pd.read_csv('olympics.csv')
df.head()


# In[135]:


df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
df.head()


# In[136]:


df.columns


# In[137]:


for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 

df.head()


# # Querying a DataFrame

# In[138]:


df['Gold'] > 0


# In[139]:


only_gold = df.where(df['Gold'] > 0)
only_gold.head()


# In[140]:


only_gold['Gold'].count()


# In[141]:


df['Gold'].count()


# In[142]:


only_gold = only_gold.dropna()
only_gold.head()


# In[143]:


only_gold = df[df['Gold'] > 0]
only_gold.head()


# In[144]:


len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)])


# In[145]:


df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]


# # Indexing Dataframes

# In[146]:


df.head()


# In[147]:


df['country'] = df.index
df = df.set_index('Gold')
df.head()


# In[148]:


df = df.reset_index()
df.head()


# In[149]:


df = pd.read_csv('census.csv')
df.head()


# In[150]:


df['SUMLEV'].unique()


# In[151]:


df=df[df['SUMLEV'] == 50]
df.head()


# In[152]:


columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
df.head()


# In[153]:


df = df.set_index(['STNAME', 'CTYNAME'])
df.head()


# In[154]:


df.loc['Michigan', 'Washtenaw County']


# In[155]:


df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]


# # Missing values

# In[156]:


df = pd.read_csv('log.csv')
df


# In[157]:


get_ipython().magic('pinfo df.fillna')


# In[158]:


df = df.set_index('time')
df = df.sort_index()
df


# In[159]:


df = df.reset_index()
df = df.set_index(['time', 'user'])
df


# In[160]:


df = df.fillna(method='ffill')
df.head()

