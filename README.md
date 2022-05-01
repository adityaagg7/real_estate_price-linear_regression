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

The model was made succesfully and the *mean squared error* and *mean absolute error* were found.

However, in the **Test Value V/S Residual Error** plot:

![TEST VALUE V/S Residual ERROR plot](/data/PLOT.png "Residual Error and True Value for Linear model")

we see that :
 
1. The plot is completely positive,
2. The plot is not normal accross the Test Values.

The average Residual error was found to be  -5.514624901304367e-13.


## Polynomial Regression:
Because the results from a Linear model weren't good, a polynomial is tried. We can see the difference explicitly in terms of this Residual Rrror and True Value graph(for degree=3):

![TEST VALUE V/S Residual ERROR plot](/data/PLOTSS_POLY.png "Residual Error and True Value for Polynomial model")

We immediately notice that:

1. The graph is more normally distributed along the x-axis,
2. It is more symmetrical about x-axis.
 
 Both these observations mean that the model fit better than a linear model.

 This is further suppoorted \by the values of the R<sup>2</sup> scores for both:

 Polynomial: ***0.9999999999999998***