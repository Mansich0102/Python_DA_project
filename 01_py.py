#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install pandas')


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[12]:


df =pd.read_csv('Diwali.csv',encoding='unicode_escape')


# In[13]:


df.shape


# In[14]:


df.head()


# In[15]:


df.info()


# In[16]:


#drop column inplace save
df.drop(['Status','Unnamed'],axis=1,inplace=True)


# In[17]:


df.info()


# In[19]:


#null checking 
pd.isnull(df).sum()


# In[21]:


#drop null values
df.dropna(inplace=True)


# In[22]:


df.shape


# In[23]:


#null checking 
pd.isnull(df).sum()


# In[36]:


data_set={
    "name":["mansi","pallavi","mahi"],
    "age":[12,34,89]}


# In[37]:


data_set =pd.DataFrame(data_set)


# In[27]:


data_set


# In[28]:





# In[38]:


#change datatype
df['Amount']=df['Amount'].astype('int')


# In[39]:


df['Amount'].dtypes


# In[41]:


df.columns # columns name


# In[46]:


#changing name of the column
df.rename(columns={'Marital_Status':'Shaadi'})


# In[47]:


#describe () method return description of the data in the dataframe
df.describe()


# In[50]:


#describe for specific columns
df[['Age','Orders','Amount']].describe()


# In[51]:


#Exploraotory Data Analysis
df.columns


# In[54]:


ax=sns.countplot(x='Gender',data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[58]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# sales_gn=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
# 
# sns.barplot(x='Gender',y='Amount',data=sales_gn)

# In[ ]:


From above graph we can see that most of the buyers are females and even the purchasing power are greater than man


# AGES

# In[60]:


df.columns


# In[64]:


sns.countplot(data=df,x='Age Group', hue='Gender')


# In[65]:


ay=sns.countplot(data=df,x='Age Group', hue='Gender')

for bars in ay.containers:
    ay.bar_label(bars)


# In[66]:


#total amount vs age group 
sales_age= df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y="Amount", data=sales_age)


# From above graphs we can see that most of the buyers are of age between 26-35 yrs female

# In[ ]:


STATE


# In[69]:


state= df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=state,x="State",y="Orders")


#  From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# In[ ]:


Marital Status


# In[71]:


az=sns.countplot(data=df,x="Marital_Status")

sns.set(rc={"figure.figsize":(7,5)})
for bars in az.containers:
    az.bar_label(bars)



# In[72]:


marital= df.groupby(['Marital_Status',"Gender"], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=marital,x="Marital_Status",y="Amount", hue="Gender")


# In[ ]:


From above graphs we can aee that most of the buyers are married(women) and they have high purchasing power


# In[ ]:


Occupation


# In[73]:


sns.set(rc={"figure.figsize":(20,5)})
aa=sns.countplot(data=df, x="Occupation")

for bars in aa.containers:
    aa.bar_label(bars)


# In[74]:


occupation= df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=occupation,x="Occupation",y="Amount")


# In[ ]:


From above graphs we can see that most of the buyers are working in IT,Aviation and Healthcare sector


# In[ ]:


Product Category


# In[75]:


sns.set(rc={"figure.figsize":(20,5)})
ab=sns.countplot(data=df,x="Product_Category")

for bars in ab.containers:
    ab.bar_label(bars)


# In[78]:


Product_Category= df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(data=Product_Category,x="Product_Category",y="Amount")


# In[ ]:


from above graphs we can see that most of the sold products are from Food,Footwear and Electronis category


# In[79]:


Product_ID= df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(25,5)})
sns.barplot(data=Product_ID,x="Product_ID",y="Orders")


# In[ ]:


Conclusion:

Married women age group 26-35 yrs from UP,Maharashtra and Karnataka working in IT,Healthcare and Aviation are more likely to buy products from Food Clothing and Electronics category

