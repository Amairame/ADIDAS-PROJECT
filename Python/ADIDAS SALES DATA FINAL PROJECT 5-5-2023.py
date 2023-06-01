#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#Load the sales data from th excel file
df = pd.read_excel(r"/Users/mariamasoumahoro/Desktop/Adidas US Sales Datasets2.xlsx")


# In[3]:


#Print first few rows of the data
print(df.head())


# In[8]:


#DATA PREPARATION
#Remove duplicate

df.drop_duplicates(inplace=True)

#datatypes of attributes

df.info()

#Checking unique values in dataset

df.apply(lambda x: len(x.unique()))


# In[9]:


#Check for null values

df.isnull().sum()


# In[11]:


#Change date format

from datetime import datetime

df['Date']= pd.to_datetime(df['Date'])


# In[12]:


#Check for categorical attributes

cat_col = []
for x in df.dtypes.index:
    if df.dtypes [x] =='object':
        cat_col.append(x)
    
cat_col


# In[13]:


#print the categorical columns

for col in cat_col:
    print(col)
    print(df[col].value_counts())
    print()


# In[17]:


#Import librariesimport matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns


# In[19]:


sns.distplot(df['Price per Unit'])


# In[20]:


sns.distplot(df['Total Sales'])


# In[21]:


sns.countplot(df["Product"])


# In[22]:


#Encode categorical variables 
df = pd.get_dummies(df, columns=['Retailer', 'Region', 'State', 'City', 'Product', 'Sales Method'])


# In[25]:


#Normalize the numerical variables

numerical_cols = ['Price per Unit', 'Units Sold','Total Sales','Operating Profit','Operating Margin']
df[numerical_cols] = (df[numerical_cols]-df[numerical_cols].mean())/df[numerical_cols].std()


# In[27]:


#Create new features based on existings ones

df['Revenue']  = df['Price per Unit'] * df['Units Sold']
df['Month'] = pd.to_datetime(df['Date']).dt.month


# In[28]:


print(df.head())


# In[30]:


#Model selection\

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# In[35]:


#SPLIT the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop(['Operating Margin','Operating Profit','Total Sales','Date'], axis=1), df['Total Sales'], test_size=0.2, random_state=42)


# In[37]:


# Train the linear regression model
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_preds = lr.predict(X_test)
lr_mae = mean_absolute_error(y_test, lr_preds)
lr_mse = mean_squared_error(y_test, lr_preds)
lr_r2 = r2_score(y_test, lr_preds)


# In[38]:


# Train and evaluate decision tree
dt = DecisionTreeRegressor()
dt.fit(X_train, y_train)
dt_preds = dt.predict(X_test)
dt_mae = mean_absolute_error(y_test, dt_preds)
dt_mse = mean_squared_error(y_test, dt_preds)
dt_r2 = r2_score(y_test, dt_preds)


# In[39]:


# Train and evaluate neural network
nn = MLPRegressor(hidden_layer_sizes=(50, 50))
nn.fit(X_train, y_train)
nn_preds = nn.predict(X_test)
nn_mae = mean_absolute_error(y_test, nn_preds)
nn_mse = mean_squared_error(y_test, nn_preds)
nn_r2 = r2_score(y_test, nn_preds)


# In[40]:


# Print the evaluation metrics for each model
print('Linear Regression - MAE:', lr_mae, 'MSE:', lr_mse, 'R-squared:', lr_r2)
print('Decision Tree - MAE:', dt_mae, 'MSE:', dt_mse, 'R-squared:', dt_r2)
print('Neural Network - MAE:', nn_mae, 'MSE:', nn_mse, 'R-squared:', nn_r2)


# In[41]:


#Model Training
# Train the linear regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Print the coefficients and intercept of the linear regression model
print('Coefficients:', lr.coef_)
print('Intercept:', lr.intercept_)


# In[42]:


#Model Evaluation
lr_preds = lr.predict(X_test)
lr_mae = mean_absolute_error(y_test, lr_preds)
lr_mse = mean_squared_error(y_test, lr_preds)
lr_r2 = r2_score(y_test, lr_preds)

# Print the evaluation metrics for the model
print('Linear Regression - MAE:', lr_mae, 'MSE:', lr_mse, 'R-squared:', lr_r2)


# In[ ]:




