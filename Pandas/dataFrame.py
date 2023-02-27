# -*- coding: utf-8 -*-

import pandas as pd

data = [10,20,30,40,50]
df = pd.DataFrame(data)
print(df)

data2 = [["Berke",20,"Kırklareli"],["Sedef",28,"İstanbul"],["Güler",48,"İstanbul"]]
df2 = pd.DataFrame(data2,columns=["İsim","Yaş","Şehir"],index=[1,2,3])
# print(df2)

data3 = {"İsim":["Berke","Sedef","Güler"],
          "Yaş":[20,28,48],
          "Şehir":["Kırklareli","İstanbul","İstanbul"]}
df3 = pd.DataFrame(data3,columns=["İsim","Yaş","Şehir"],index=[1,2,3])
print(df3["Yaş"])
del df3["Şehir"]
df3.pop("Şehir")
print(df3)

print(df3.loc[2])
print(df3.iloc[2])

df4 = df3.append(df2)
print(df4)
print(df4.head())
print(df4.tail())
df4.drop(2)
print(df4)




