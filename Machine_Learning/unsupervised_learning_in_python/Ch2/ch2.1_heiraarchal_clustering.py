# Hierarchical clustering of the grain data
# In the video, you learned that the SciPy linkage() function performs hierarchical clustering 
# on an array of samples. Use the linkage() function to obtain a hierarchical clustering of the 
# grain samples, and use dendrogram() to visualize the result. A sample of the grain measurements 
# is provided in the array samples, while the variety of each grain sample is given by the list varieties.

# Perform the necessary imports
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Calculate the linkage: mergings
mergings = linkage(samples, method = 'complete')

# Plot the dendrogram, using varieties as labels
dendrogram(mergings,
           labels=varieties,
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.show()

# Hierarchies of stocks
# In chapter 1, you used k-means clustering to cluster companies according to their stock price movements. 
# Now, you'll perform hierarchical clustering of the companies. You are given a NumPy array of price movements 
# movements, where the rows correspond to companies, and a list of the company names companies. 
# SciPy hierarchical clustering doesn't fit into a sklearn pipeline, so you'll need to use the normalize() 
# function from sklearn.preprocessing instead of Normalizer.

# Import normalize
from sklearn.preprocessing import normalize

# Normalize the movements: normalized_movements
normalized_movements = normalize(movements)

# Calculate the linkage: mergings
mergings = linkage(normalized_movements, method = 'complete')

# Plot the dendrogram
dendrogram(mergings,
            labels = companies,
            leaf_rotation = 90,
            leaf_font_size=6)
plt.show()


# Different linkage, different hierarchical clustering!
# In the video, you saw a hierarchical clustering of the voting countries at the Eurovision song contest 
# using 'complete' linkage. Now, perform a hierarchical clustering of the voting countries with 'single' 
# linkage, and compare the resulting dendrogram with the one in the video. Different linkage, different hierarchical clustering!

# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Calculate the linkage: mergings
mergings = linkage(samples, method='single')

# Plot the dendrogram
dendrogram(mergings,
            labels=country_names,
            leaf_rotation=90,
            leaf_font_size=6)
plt.show()

# Perform the necessary imports
import pandas as pd
from scipy.cluster.hierarchy import fcluster

# Use fcluster to extract labels: labels
labels = fcluster(mergings, 6, criterion='distance')

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# Create crosstab: ct
ct = pd.crosstab(df['labels'], df['varieties'])

# Display ct
print(ct)


# Import TSNE
from sklearn.manifold import TSNE

# Create a TSNE instance: model
model = TSNE(learning_rate=200)

# Apply fit_transform to samples: tsne_features
tsne_features = model.fit_transform(samples)

# Select the 0th feature: xs
xs = tsne_features[:,0]

# Select the 1st feature: ys
ys = tsne_features[:,1]

# Scatter plot, coloring by variety_numbers
plt.scatter(xs, ys, c=variety_numbers)
plt.show()

# A t-SNE map of the stock market
# -SNE provides great visualizations when the individual samples can be labeled. 
# In this exercise, you'll apply t-SNE to the company stock price data. A scatter plot of the 
# resulting t-SNE features, labeled by the company names, gives you a map of the stock market! 
# The stock price movements for each company are available as the array normalized_movements (these have already been normalized for you). 

# Import TSNE
from sklearn.manifold import TSNE

# Create a TSNE instance: model
model = TSNE(learning_rate=50)

# Apply fit_transform to normalized_movements: tsne_features
tsne_features = model.fit_transform(normalized_movements)

# Select the 0th feature: xs
xs = tsne_features[:,0]

# Select the 1th feature: ys
ys = tsne_features[:,1]

# Scatter plot
plt.scatter(xs, ys, alpha=0.5)

# Annotate the points
for x, y, company in zip(xs, ys, companies):
    plt.annotate(company, (x, y), fontsize=5, alpha=0.75)
plt.show()
