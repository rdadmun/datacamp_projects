import numpy as np
import pandas as pd

import pandas as pd

sales_data = [
    {"tv": 13000.0, "radio": 9237.76, "social_media": 2409.57, "sales": 46677.90},
    {"tv": 41000.0, "radio": 15886.45, "social_media": 2913.41, "sales": 150177.83},
    {"tv": 25000.0, "radio": 12000.50, "social_media": 3100.75, "sales": 87000.65},
    {"tv": 37000.0, "radio": 14500.30, "social_media": 2750.10, "sales": 134500.22},
    {"tv": 15000.0, "radio": 10250.75, "social_media": 2200.55, "sales": 54000.10},
    {"tv": 29000.0, "radio": 13200.25, "social_media": 2600.30, "sales": 110300.55},
    {"tv": 42000.0, "radio": 16050.40, "social_media": 3000.20, "sales": 155500.80},
    {"tv": 5000.0, "radio": 8000.90, "social_media": 1800.75, "sales": 26000.25},
    {"tv": 33000.0, "radio": 14000.60, "social_media": 2900.90, "sales": 120400.15},
    {"tv": 28000.0, "radio": 12750.85, "social_media": 2500.65, "sales": 105000.70},
]

sales_df = pd.DataFrame(sales_data)
print(sales_df)

# Create X from the radio column's values
X = sales_df['radio'].values

# Create y from the sales column's values
y = sales_df['sales'].values

# Reshape X
X = X.reshape(-1, 1)

# Check the shape of the features and targets
print(X.shape, y.shape)