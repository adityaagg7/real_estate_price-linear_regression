# real_estate_price-linear_regression
## About
A multiple linear regression model to determine the price per unit area of property.


## Packages Used
- numpy
- matplotlib
- pandas
- sklearn

The dataset can be found [HERE](https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction
).

## Observation

The model was made succesfully and the *mean squared error* and * mean absolute error* were found.

However, in the **Test Value V/S Residual Error** plot:

![TEST VALUE V/S Residual ERROR plot](/data/PLOT%20SS.png)

we see that :
 
1. The plot is not symmetric about x-axis,
2. The plot is not normal accross the Test Values.


Both of these observations suggest that a Linear model is not suited for this data.