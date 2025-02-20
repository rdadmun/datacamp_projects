import seaborn as sns
import matplotlib.pyplot as plt

def column_to_label(column):
    """
    Convert a column name to a more readable label.
    
    :param column: the column name to be converted
    :return: a string representing the readable label
    """
    # Example implementation, you can customize this as needed
    return column.replace('_', ' ').title()

def visualize_versus_price(clean_data, x):
    """
    Use seaborn and matplotlib to identify a pattern between avg_rating and 
    battery_capacity.
    
    :param clean_data: a pandas DataFrame containing cleaned smartphone data
    :param x: variable to be plotted on the x-axis
    :return: None
    """
    # Ensure x is a string
    if not isinstance(x, str):
        raise TypeError(f"Expected 'x' to be a string, but got {type(x)}")
    
    # Check if the column exists in the DataFrame
    if x not in clean_data.columns:
        raise ValueError(f"Column '{x}' not found in the data")
        
    # Create the scatterplot
    sns.scatterplot(x=x, y="price", data=clean_data, hue="os")
    
    # Add x and y labels
    plt.xlabel(column_to_label(x))
    plt.ylabel("Price ($)")
    
    # Add a title to the plot
    plt.title(f"{column_to_label(x)} vs. Price")
    plt.show()
    
# Call the functions
cleaned_data = prepare_smartphone_data("./data/smartphones.csv")
visualize_versus_price(cleaned_data, "processor_speed")