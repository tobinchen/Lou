
# coding: utf-8

# In[110]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[111]:

#louDf=pd.read_csv("result.txt",header=None,names=['date','lou','square','number','amount','price'],parse_dates=True)
louDf=pd.read_csv("result.txt",header=None,names=['date','lou','square','number','amount','price'],parse_dates=True,index_col=['date'])
louDf.head(5)
#louDf.drop_duplicates(cols='date')

print louDf.index
# In[112]:

xc=louDf[louDf['lou']=='新城']
xc.head(2)


# In[113]:
dt=xc
print dt
dt=xc.loc[:,['date','number']]
#dt=dt.set_index('date')
dt=dt.sort()
#dt.sort_index(by='price')

dt[0:12]


# In[114]:

dt[12:24]


# In[115]:

plt.figure()
for n in range(2016-2006):
    #d=dt[n*12:(n+1)*12]
    #plt.plot(d,label=str(2006+n))
    #print d
    #d.plot(secondary_y=True,legend=True)

    #dt.ix[str(2006+n)].plot()

    plt.plot(dt.ix[str(2006+n)],label=str(2006+n))
plt.legend(loc='best')

#dt.plot()

plt.show()
#plt.plot(dt)
#plt.plot(xc.loc[12:23,['price']])

pd.TimeGrouper(freq='m')
