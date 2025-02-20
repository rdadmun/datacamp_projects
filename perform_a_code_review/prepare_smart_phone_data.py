import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def column_to_label(df, column):
    """
    Prepares the column by ensuring necessary transformation
    """
    if isinstance(column_name, str):
        return " ".join(column_name.split("_")).title()
    else:
        raise Exception("Please makes sure to pass a value of type 'str'.")
    
def prepare_smartphone_data(file_path):
    """
    To prepare the smartphone data for visualization, a number of transformations 
    will be applied after reading in the Raw DataFrame to memory, including:
        - reducing the number of columns to only those needed for later analysis
        - removing records without a battery_capacity value
        - divide the price column by 100 to find the dollar amount
    
    :param file_path: the file path where the raw smartphone data is stored
    :return: a cleaned dataset having had the operations above applied to it
    """
    
    if os.path.exists(file_path):
        RawData = pd.read_csv(file_path)
    else:
        raise Exception(f"File containing smartphone data not found at path {file_path}")

    columns_to_keep = [
        "brand_name",
        "os",
        "price",
        "avg_rating",
        "processor_speed",
        "battery_capacity",
        "screen_size"
    ]
    # Reduced columns and drop unecessary rows
    TrimmedData=RawData[columns_to_keep]
    
    # Remove records without a battery_capacity or os value
    ReducedData=TrimmedData.dropna(subset=["battery_capacity", "os"])
    
    # Divide the price column by 100 to find the dollar amount
    ReducedData["price"] = ReducedData["price"] / 100
    
    return ReducedData