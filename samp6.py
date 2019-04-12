import pandas as pd
from pandas import DataFrame
#import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm
#import tensorflow as tf

house_prices = pd.read_csv(r'data_truck.csv')
df = DataFrame(house_prices,columns=['id','date','price','cylinders','strokeratio','sqcm_basearea','condition','grade','yr_estd'])
'''
'id','date','price','cylinders','strokeratio','sqcm_basearea','condition','grade','yr_estd'

'''
X = df[['cylinders','strokeratio','condition','grade']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression,  X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['price']
 
# with Linear Regression
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)


# prediction with sklearn
New_cylinders = 2
New_strokeratio = 1.75
New_condition = 3
New_grade = 3
print ('Predicted Price with tensorflow regression: ', abs(regr.predict([[New_cylinders ,New_strokeratio,New_condition,New_grade]])))
print ('Predicted Price with linear regression:',abs(regr.intercept_ + (regr.coef_[0]*New_cylinders) + (regr.coef_[1]*New_strokeratio)+ 
       (regr.coef_[2]*New_condition)+(regr.coef_[3]*New_grade)))

