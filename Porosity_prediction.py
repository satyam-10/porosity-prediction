#!/usr/bin/env python
# coding: utf-8

# # Porosity prediction model

# In[3]:


import pandas as pd


# In[4]:


df=pd.read_excel("C:/Users/KIIT/OneDrive/Desktop/DS/btp_data.xlsx")


# In[5]:


df


# In[6]:


df1=df.drop(['Well_Name'],axis=1)


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


df1.plot(subplots=True,figsize=(20,10))
plt.show()


# # new

# In[8]:


subset = df1.iloc[3800:11000]
df_test=pd.DataFrame(subset)


# In[9]:


df_test


# In[10]:


df_test = df_test.reset_index()


# In[11]:


df_test


# In[12]:


df_test = df_test.drop("index",axis=1)


# In[13]:


df_test


# In[14]:


df_test.plot(subplots=True,figsize=(20,10))
plt.show()


# In[15]:


Y =df_test["NPHI"]
Y.head()


# In[16]:


X =df_test.drop("NPHI",axis=1)
X.head()


# In[17]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30,random_state=0)


# In[18]:


from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor()
model.fit(X_train,Y_train)
random_pred= model.predict(X_test)


# In[19]:


model.score(X_test, Y_test)


# In[20]:


subset1 = df1.iloc[11001:14000]
df_pred=pd.DataFrame(subset1)


# In[21]:


df_pred


# In[22]:


df_pred = df_pred.reset_index()


# In[23]:


df_pred = df_pred.drop("level_0", axis=1)


# In[24]:


df_pred 


# In[25]:


df_pred.plot(subplots=True,figsize=(20,10))
plt.show()


# In[26]:


og_NPHI = df_pred["NPHI"]


# In[27]:


og_NPHI


# In[28]:


df_pred = df_pred.drop("NPHI",axis=1)


# In[29]:


df_pred


# In[31]:


df_pred = df_pred.drop("index",axis=1)


# In[32]:


random_pred= model.predict(df_pred)


# In[33]:


column_name = ['NPHI_pred']


# In[34]:


df2=pd.DataFrame(random_pred,columns=column_name)


# In[35]:


df2


# In[36]:


concatenated_df = pd.concat([og_NPHI , df2], axis=1)


# In[37]:


concatenated_df


# In[38]:


import matplotlib.pyplot as plt
plt.figure(figsize=(20, 10)) 
plt.scatter(concatenated_df['NPHI_pred'], concatenated_df['NPHI'] ,s=10, c='blue')
plt.xlabel('NPHI_pred')
plt.ylabel('NPHI')
plt.title('Graph of NPHI_pred vs NPHI')
plt.show()


# In[39]:


dept = df_pred["DEPT"]


# In[40]:


concatenated_df1 = pd.concat([concatenated_df , dept], axis=1)


# In[41]:


concatenated_df1


# In[42]:


plt.figure(figsize=(20, 10)) 
plt.plot(concatenated_df1['DEPT'], concatenated_df1['NPHI_pred'], color='blue', label='NPHI_pred')
plt.plot(concatenated_df1['DEPT'], concatenated_df1['NPHI'], color='red', label='NPHI',linewidth=0.7)
plt.xlabel('depth')
plt.ylabel('pororsity')
plt.title('variation of NPHI_pred and NPHI according to depth')
plt.legend()


# ## new2

# In[9]:


subset = df1.iloc[6000:12000]
df_test2=pd.DataFrame(subset)


# In[10]:


df_test2


# In[12]:


df_test2 = df_test2.reset_index()


# In[13]:


df_test2


# In[14]:


df_test2 = df_test2.drop("index",axis=1)


# In[48]:


df_test2 = df_test2.drop("level_0",axis=1)


# In[15]:


df_test2


# In[16]:


df_test2.plot(subplots=True,figsize=(20,10))
plt.show()


# In[17]:


Y =df_test2["NPHI"]
Y.head()


# In[18]:


X =df_test2.drop("NPHI",axis=1)
X.head()


# In[19]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30,random_state=0)


# In[20]:


from sklearn.ensemble import RandomForestRegressor
model1=RandomForestRegressor()
model1.fit(X_train,Y_train)
random_pred1= model1.predict(X_test)


# In[21]:


model1.score(X_test, Y_test)


# In[40]:


subset1 = df1.iloc[12001:14500]
df_pred2=pd.DataFrame(subset1)


# In[41]:


df_pred2


# In[42]:


df_pred2.plot(subplots=True,figsize=(20,10))
plt.show()


# In[43]:


df_pred2 = df_pred2.reset_index()


# In[44]:


df_pred2


# In[45]:


df_pred2 = df_pred2.drop("index", axis=1)


# In[46]:


df_pred2


# In[47]:


og_NPHI1 = df_pred2["NPHI"]


# In[48]:


df_pred2 = df_pred2.drop("NPHI",axis=1)


# In[49]:


df_pred2


# In[50]:


random_pred1= model1.predict(df_pred2)


# In[51]:


column_name = ['NPHI_pred']


# In[52]:


df3=pd.DataFrame(random_pred1,columns=column_name)


# In[53]:


df3


# In[54]:


concatenated_df2 = pd.concat([og_NPHI1 , df3], axis=1)


# In[55]:


concatenated_df2


# In[57]:


import matplotlib.pyplot as plt
plt.figure(figsize=(20, 10)) 
plt.scatter(concatenated_df2['NPHI_pred'], concatenated_df2['NPHI'] ,s=10, c='blue')
plt.xlabel('NPHI_pred')
plt.ylabel('NPHI')
plt.title('Graph of NPHI_pred vs NPHI')
plt.show()


# In[58]:


dept1 = df_pred2["DEPT"]


# In[59]:


concatenated_df3 = pd.concat([concatenated_df2 , dept1], axis=1)


# In[60]:


concatenated_df3 


# In[61]:


plt.figure(figsize=(20, 10)) 
plt.plot(concatenated_df3['DEPT'], concatenated_df3['NPHI_pred'], color='blue', label='NPHI_pred')
plt.plot(concatenated_df3['DEPT'], concatenated_df3['NPHI'], color='red', label='NPHI',linewidth=0.7)
plt.xlabel('depth')
plt.ylabel('pororsity')
plt.title('variation of NPHI_pred and NPHI according to depth')
plt.legend()


# In[77]:


df_test2


# In[78]:


df_test3 = df_test2.drop("DEPT",axis=1)


# In[79]:


df_test3


# # new3

# In[80]:


subsets = df1.iloc[6000:12000]
dftest2=pd.DataFrame(subset)


# In[81]:


dftest2


# In[83]:


dftest2 = dftest2.drop("DEPT",axis=1)


# In[84]:


dftest2


# In[86]:


dftest2 = dftest2.reset_index()


# In[87]:


dftest2


# In[91]:


dftest2 = dftest2.drop("index",axis=1)


# In[92]:


dftest2


# In[93]:


Y =dftest2["NPHI"]
Y.head()


# In[94]:


X =dftest2.drop("NPHI",axis=1)
X.head()


# In[95]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30,random_state=0)


# In[97]:


from sklearn.ensemble import RandomForestRegressor
model10=RandomForestRegressor()
model10.fit(X_train,Y_train)
random_pred10= model10.predict(X_test)


# In[98]:


model10.score(X_test, Y_test)


# In[152]:


import xgboost as xg
xgb_r = xg.XGBRegressor()
xgb_r.fit(Y_train,X_train)


# In[149]:


random_predX= modelx.predict(dftest3)


# In[150]:


column_name = ['NPHI_pred']
df11=pd.DataFrame(random_predX,columns=column_name)


# In[151]:


df11


# In[99]:


subset10 = df1.iloc[12001:14500]
dftest3=pd.DataFrame(subset10)


# In[100]:


dftest3


# In[102]:


dftest3 = dftest3.drop("DEPT",axis=1)


# In[103]:


dftest3 = dftest3.reset_index()


# In[104]:


dftest3


# In[105]:


dftest3 = dftest3.drop("index",axis=1)


# In[106]:


dftest3


# In[107]:


ogNPHI = dftest3["NPHI"]


# In[148]:


dftest3 = dftest3.drop("NPHI",axis=1)


# In[109]:


random_pred10= model10.predict(dftest3)


# In[110]:


column_name = ['NPHI_pred']
df10=pd.DataFrame(random_pred10,columns=column_name)


# In[111]:


df10


# In[112]:


concat_df = pd.concat([ogNPHI , df10], axis=1)


# In[113]:


concat_df


# In[114]:


import matplotlib.pyplot as plt
plt.figure(figsize=(20, 10)) 
plt.scatter(concat_df['NPHI_pred'], concat_df['NPHI'] ,s=10, c='blue')
plt.xlabel('NPHI_pred')
plt.ylabel('NPHI')
plt.title('Graph of NPHI_pred vs NPHI')
plt.show()


# In[ ]:


dept1 = df_test3["DEPT"]


# In[116]:





# In[117]:


subset11 = df1.iloc[12001:14500]
dftest4=pd.DataFrame(subset11)


# In[118]:


dftest4


# In[119]:


dftest4 = dftest4.reset_index()


# In[120]:


dftest4 = dftest4.drop("index",axis=1)


# In[121]:


dftest4


# In[122]:


depth10 = dftest4["DEPT"]


# In[123]:


depth10


# In[124]:


concatdf = pd.concat([concat_df , depth10], axis=1)


# In[125]:


concatdf


# In[126]:


plt.figure(figsize=(20, 10)) 
plt.plot(concatdf['DEPT'], concatdf['NPHI_pred'], color='blue', label='NPHI_pred')
plt.plot(concatdf['DEPT'], concatdf['NPHI'], color='red', label='NPHI',linewidth=0.7)
plt.xlabel('depth')
plt.ylabel('pororsity')
plt.title('variation of NPHI_pred and NPHI according to depth')
plt.legend()


# In[129]:


get_ipython().system('pip install xgboost')
from xgboost import XGBClassifier


# In[132]:


modelx = XGBClassifier() 


# In[139]:


modelx.fit(X_train,Y_train)  


# In[140]:





# In[ ]:




