#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


#reding file
customer_churn = pd.read_csv("E:/DATA ANALYST/DataSource/customer_churn.csv") 


# In[4]:


#finding the first few rows
customer_churn.head()


# In[5]:


#Extracting 5th column
customer_5=customer_churn.iloc[:,4] 
customer_5.head()


# In[6]:


#Extracting 15th column
customer_15=customer_churn.iloc[:,14] 
customer_15.head()


# In[7]:


#'Extracting male senior citizen with payment method-> electronic check'
senior_male_electronic=customer_churn[(customer_churn['gender']=='Male') & (customer_churn['SeniorCitizen']==1) & (customer_churn['PaymentMethod']=='Electronic check')]
senior_male_electronic.head()


# In[8]:


#tenure>70 or monthly charges>100
customer_total_tenure=customer_churn[(customer_churn['tenure']>70) | (customer_churn['MonthlyCharges']>100)]
customer_total_tenure.head()


# In[9]:


#cotract is 'two year', payment method is 'Mailed Check', Churn is 'Yes'
two_mail_yes=customer_total_tenure=customer_churn[(customer_churn['Contract']=='Two year') & (customer_churn['PaymentMethod']=='Mailed check') & (customer_churn['Churn']=='Yes')]
two_mail_yes


# In[10]:


#Extracting 333 random records
customer_333=customer_churn.sample(n=333)
customer_333.head()


# In[11]:


len(customer_333)


# In[12]:


#count of levels of churn column
customer_churn['Churn'].value_counts()


# In[13]:


#-------------------------------Data Visualization------------------#


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


#bar-plot for 'InternetService' column
plt.bar(customer_churn['InternetService'].value_counts().keys().tolist(),customer_churn['InternetService'].value_counts().tolist(),color='orange')
plt.xlabel('Categories of Internet Service')
plt.ylabel('Count of categories')
plt.title('Distribution of Internet Service')


# In[16]:


#histogram for 'tenure' column
plt.hist(customer_churn['tenure'],color='green',bins=30)
plt.title('Distribution of tenure')


# In[17]:


#scatterplot 
plt.scatter(x=customer_churn['tenure'],y=customer_churn['MonthlyCharges'],color='brown')
plt.xlabel('Tenure of Customer')
plt.ylabel('Monthly Charges of Customer')
plt.title('Tenure vs Monthly Charges')


# In[18]:


#Box-plot
customer_churn.boxplot(column='tenure',by=['Contract'])


# In[ ]:




