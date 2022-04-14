
from typing import List
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import hvplot

df = pd.read_csv('data/Real estate.csv')
df = df.drop_duplicates(keep="first")
print(df.shape)
if np.isnan(df.values).any():
    df.fillna(df.means())


x = df.iloc[:, 2:8].values
y = df.iloc[:, -1].values

x_tr, x_t, y_tr, y_t = train_test_split(x, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_tr, y_tr)
y_p = regressor.predict(x_t)

mae = metrics.mean_absolute_error(y_t, y_p)
mse = metrics.mean_squared_error(y_t, y_p)

error = [['MAE', mae], ['MSE', mse]]
er = pd.DataFrame(error, columns=['Error', 'Value'])

print(er)

res_error = y_t-y_p
pt.scatter(y_t, res_error, color="red")
pt.xlabel('Test Value')
pt.ylabel('Residual Error')
pt.show()
