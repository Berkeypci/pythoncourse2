# -*- coding: utf-8 -*-
import pandas as pd

data1 = {
            'id':[1,2,3,4],
            'ad':["Berke","Güler","Cemal","Sedef"],
            'soyad':["Yapıcı","Yapıcı","Yapıcı","Yapıcı"]
        }

data2 = {
            'id':[1,3,4,7],
            'ad':["Nesrin","Sevim","Muharrem","John"],
            'soyad':["Yapıcı","Yapıcı","Yapıcı","Cash"]
        }

data1Df=pd.DataFrame(data1)
data2Df=pd.DataFrame(data2)

# print(data1Df)
# print(data2Df)

# print(pd.merge(data1Df,data2Df,on='id',how='inner'))
# print(pd.merge(data1Df,data2Df,on='id',how='left'))
# print(pd.merge(data1Df,data2Df,on='id',how='right'))

print(pd.concat([data1Df,data2Df],axis=1))






