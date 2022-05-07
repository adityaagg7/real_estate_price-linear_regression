from sklearn.metrics import r2_score

from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
df = pd.read_csv('data/Real estate.csv')
df = df.drop_duplicates(keep="first")
print(df.shape)

if np.isnan(df.values).any():
    df.fillna(df.means())

x = df.iloc[:, 1:8].values
y = df.iloc[:, -1].values


poly_feat = PolynomialFeatures(degree=3)
x_poly = poly_feat.fit_transform(x)

x_poly_train, x_poly_test, y_train, y_test = train_test_split(
    x_poly, y, test_size=0.2, random_state=0)
print(x.shape)
print(x_poly.shape)

poly_lin_regressor = LinearRegression()
poly_lin_regressor.fit(x_poly_train, y_train)
y_pred = poly_lin_regressor.predict(x_poly_test)


mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)

error = [['MAE', mae], ['MSE', mse]]
er = pd.DataFrame(error, columns=['Error', 'Value'])

print(er)


res_error = y_test-y_pred
print(r2_score(y_test, y_pred))
pt.scatter(y_test, res_error, color='Red')
pt.xlabel('Test Value')
pt.ylabel('Residual Error')
pt.show()
