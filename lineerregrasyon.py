# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("başladı*************************")
data=pd.read_csv("linear.csv")
#print(data)

x=data["metrekare"]
y=data["fiyat"]

print(x)
print(y)

plt.scatter(x,y)

m,b=np.polyfit(x,y,1)

a=np.arange(150)
plt.scatter(x,y)
plt.plot(m*a+b)
z=int(input("Kaç metre kare"))
tahmin = m*z+b
print(tahmin,"Tahminizmiz" )

plt.scatter(z,tahmin,c="red",marker=">")

plt.show()
print("y=",m,"x+",b)