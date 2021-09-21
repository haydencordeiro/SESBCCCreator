
import pandas as pd
from datetime import datetime


df = pd.read_excel("1.xlsx")
print(df.keys())
l=(df["Email Address"])
ol=[]
for i in range(0,len(l),50):
    temp=list(l[i:i+47])
    temp.append("grejo00@gmail.com")
    temp=",".join(temp)
    ol.append(temp)
for i in ol:
    print(i)
    print()
