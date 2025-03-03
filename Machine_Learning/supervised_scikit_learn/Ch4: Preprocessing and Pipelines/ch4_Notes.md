# Scikit Learn requires numeric data, with no missing values
    Dataset with categorical features
    Need to preprocess the data into numeric
        We do this by splitting the features into multiple binary features called dummy variables
        0 means observation was not that category, 1 means it was
        If we have 10 categories, we make 9 dummy variables
            If an observation is not any of the first 9 categories, it is implicetly the final category
            We only create 9 so that we do not duplicate information, which may mess with certain models.
        We use scikitlearn's (OneHotEncoder) or pandas (GetDummies)
        After reading in and creating the dataframe, we assign the dummies to a var name
            Afterwards, we bring these dummy variables into the dataframe with pd.concat() as a list, with axis=1
            Lastly, we drop the the categories column with df.drop
        If there is only one categorical column, we can pass the entire df into pd.get_dummies()
            If we don't specify a column, each new column header will have the categorical column name prefixed to their names - such as genre_alt
            The original categorical column is also dropped
        To perform cross-validation, we first create a KFold object, instigate a linear regression model, and then call cross_value_score

# Handeling Missing Data
    Missing data is where there is a blank entry anywhere in a column - No value
        There may be no observation, or the data might be corrupt
    To quickly check how many missing values are in each column, we can use
        ```print(music_df.isna().sum().sort_values())```
    A common approach is to remove MVs accounting for less than 5% of all data
        Use pandas dropna method -> pd.dropna(subset=['column1', 'column2', etc.])
    Another option is to impute missing data with expert educated guesses
        Commonly, this is either the mean, median or mode 
        If we do this, we need to split our data first to avoid data leakage, or accidentally showing our model test set information
        Sklearn SimpleImputer
    ## Pipelines
        We can also impute witha pipeline, which is an object used to run a series of transformations and build a model in a single workflow
        ```from sklearn.pipeline import pipeline```
        To build a pipeline, we set a series of tasks and assign them to a var. The tasks should be tuples containing a string naming the step, and the command to instantiate the transformer or model. We pass this list when instantiating a pipeline
        steps = tuples!
        pipeline = Pipeline(steps)

# Centering and scaling
    Many models use some form of distance to inform themselves
    Features on largescales can disproportionately influence the models
        KNN uses distance explicetly when making predictions
            Therefore, it is important to have our data all lie on a similar scale
            To do so, we normalize or standardize our data
    ## Standardization
        For a given column, subtract the mean and divide by the varience
            Centers data around 0, with a varience of 1
        We could also subtract the minimum, and divide by the range
            Giving a min of 0, and a maximum of 1
    ## Normalization
        Changes all values to a range from -1 to 1

# Evaluating Multiple Models
    Different models are good for different scenarios
        Size of our feature set matters
            Fewer features = simpler model, faster loading times
            Some models require a vast amount of data to perform well
        Interpretability
            Some models are easier to explain
        Flexibility may be important to get the most accurate predictions
            Generally, flexible models make fewer assumptions about the data
            Example: KNN does not assume any linear relationships
    Regression models are evaluated using:
        RMSE
        R-squared
    Classification model performance is measured in:
        Accuracy
        Confusion Matrix
        Precision, recall, F1 score
        ROC AUC
    Therefore, we can train several models and a metric to evaluate performance out of the box

# A note on scaling
    Models affected by scaling:
        KNN
        Linear Regression
        Logistic Regression
        AI Neural Networks
        