from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_excel('data_set.xlsx')
#print(data)
#ex=np.zeros(100)
x=data['X']
y=data['Y']
#x=pd.DataFrame([x,ex])
feature=PolynomialFeatures(degree=2,include_bias=True)
x_poly=feature.fit_transform(x)
x_train,x_test,y_train,y_test=train_test_split(x,y)
model=LinearRegression()
model.fit(x_train,y_train)
accu=model.score(x_test,y_test)
print(accu)

