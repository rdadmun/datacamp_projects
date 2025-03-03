# How good is your model
## Classification metics
    Measuring model performance with accuracy:
        Fraction of correctly classified samples
        Not always a useful metric
    Class imbalance
        Classification for rpedicting fraudulent bank transactions
            Only 1% are actually fraudulent
               Model would be 99% accurate, but fail at its intended purpose
        Where one class is more prevalent than other, this is called Class Imbalance.
    Confusion Matrix
        Y axis - Actual Legit, Actual Fraud
        X axis - Predicted Legit, Predicted Fraud
            We can then assign our model tags against the test to the matrix
        Accuracy is the sum of the true predictions over the total rpedictions
        Precision is true positives over all positives
        Recall is true positives over sum( true positives + False negatives)
        F1 score is the harmonic mean of precision and recall
            2 * (precision * recall / (precision + recall)) -> equlal rates
            
# Logistic Regression
## Used for binary classification
    Outputs probabilities
    Calculates the probability p that belongs to class 1 or 2
    If p > 0.5
        This creates a linear deicion boundary
        
    The ROC Curve
        Recieving Operator Characteristic
        The ROC curve visualizes the true positive rate and the false positive rate and shows how they vary as the deicison threshold changes. 

# Optomizing the model
## HP = Hyperparameter
    For Ridge and Lasso Regressions, our HP is alpha
    For KNN -> HP is choosing n_neighbors
    Hyperparameters are parameters we specify before the model
    We use cross-validation to ensure we do not overfit the set
        We can still split the data and perform cross-validation on the traingin set
        We withhold the test set for final evaluation
# First Approach - Grid Search cross-validation
    We choose a grid of possible HP values to try.
    For KNN, it is a different type of metric, and a different number of neighbors
    Limitations
        The number of fits is
            Number of hyperparamters * number of values * number of folds
            Exponential very very quickly.
# Second approach - RandomizedSearchCV
    Picks random HP values, rather than picking through exhaustively. 