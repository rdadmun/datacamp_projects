# Linear Regressiong: Linearizing a regrssion minimizes a loss function
# It chooses a coefficient (a) for each feature plus (b)
# Large coefficients can lead to overfitting
    # We want to peanlize large coefficient
    
# Types
    # We want to use a Loss function - the Ridge regression 
    # When using Ridge, we need to choose the alpha value to fit and predict
        # We choode the alpha for which our model performs best
        # Similar to picking K in KNN
        # In Ridge, alpha is a Hyperparameter - the variable used to optomize models
        # Alpha controls complexity
        # Alpha = 0, we are performing OLS
        # High Alpha means high coefs are peanlized, which can lead to underfitting
            # Implementation
                # to highlight to impact of different alpha values in a for loop
                # Fit on the training data, and predict on the test data
                # Out of the loop, we print the scores - we see that performance decreases as alpha gets very large
    # Lasso Regression = OLS Function plus
    # OLS plus the absolute value of each function, plus a coef
        # Lasso can select important features from a dataset
        # Shrinks coeddicients of less important features to zero
        # Features not shrunk to zero are selected by Lasso
        
# Ridge Regression
# Import Ridge
from sklearn.linear_model import Ridge
import matplotlib as plt

alphas = [0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0]
ridge_scores = []
for alpha in alphas:
  
  # Create a Ridge regression model
  ridge = Ridge(alpha=alpha)
  
  # Fit the data
  ridge.fit(X_train,y_train)
  
  # Obtain R-squared
  score = ridge.score(X_test, y_test)
  ridge_scores.append(score)
print(ridge_scores)

# Lasso Regression
# Import Lasso
from sklearn.linear_model import Lasso

# Instantiate a lasso regression model
lasso = Lasso(alpha=0.3)

# Fit the model to the data
lasso.fit(X,y)

# Compute and print the coefficients
lasso_coef = lasso.coef_
print(lasso_coef)
plt.bar(sales_columns, lasso_coef)
plt.xticks(rotation=45)
plt.show()