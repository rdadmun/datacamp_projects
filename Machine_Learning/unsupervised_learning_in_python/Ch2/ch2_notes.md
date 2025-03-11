# Visualizing Hierarchies
A huge part of working as a data scientist will be the communication of insights.
Enter visualizations.
2 Unsupervised techniques for visualization: t-SNE and heirarchial clustering
t-SNE creates a 2D map of a dataset, conveying useful information about the proximity of samples to one another
This chapter is on Hierarchial Clustering:
    Quick breakdown: This arranges samples into a heirarchy of clusters
    New Dataset: Scores at Eurovision 2016.
        Countries gave scores to songs performed
        2D array of scores
        Rows of countries, columns are songs
            Visualized as a tree like diragram called a dendrogram
            Dendrogram organizes samples into larger and larger clusters - one such cluster is geographic proximity
                Or that have close cultural or political ties,
                or that belong to a single language group
    Heirarchal clustering proceeds in steps:
        In the beginning, every country is its own cluster - there are as manby clusters as there are countries!
            At each s tep, the two closest clusters are merged
                Eventually, there is only one cluster left, containing all the countries. 
                    This is essentially "Agglomerative clustering", which is the opposite of "divisive clustering"
        We will use functions with SciPy to perform heirarchal clustering on the array of scores
            We will also need a list of names as labels (coutntry_names)

# CLustering labels in heirarchal clustering
In this video, we learn how to extract the clusters from the intermideiate stages of a hierarchal clustering. 
These can then be used in other computations, such as cross tablulations, just like cluster labels from kmeans. 
    These are specified by choosing a height on the dendrogram
    What is the meaning of height on the dendrogram?
        Height = distance between merging clusters
            So, height on the dendrogram specifies the maximum distance between merging clusters
                Also read: "I am specifying that the heirarchal clustering method should stop merging clusters when all clusters are at least {height} far apart
        Distance between clusters is measured using a linkage method.
            In our example, we used a 'complete' linkage: distance between clusters is the maximum distance between their samples
                Different linkage methods give different heirarchal clusters!
    Labels for intermediate clusters can be extracted using the fcluster() function.
        Returns a NumPy array of cluster labels. 
     ```from scipy.cluster.hierarchy import linkage
        mergings = linakage(samples, method = 'complete')
        from scipy.cluster.hierarchy import fcluster
        labels = fcluster(mergings, 15, criterion='distance')
        print(labels)```
    To align the cluster labels with country names, we use a dataframe
     ```import pandas as pd
        pairs = pd.DataFrame({'labels': labels, 'countries': county_names})
        print(pairs.sort_values('labels'))```

# t-SNE for 2 dimensional maps
    t-SNE = t-distributed stochastic neighbor embedding
    This maps samples from their high-dimensional space into a 2 or 3 dimensional space to be visualized
    Does a great job of approcimately representing the distance between samples
        Great for inspecting datasets
    Iris samples are in a 4 dimensional space, where each dimension is one of the four iris measurements. 
    t-SNE was given the data on the samples, but not that they were of different species.
        However, it will still keep the species separated into groups after it's analysis.
        We see that two of the species are close tohgether in space -> could interpret that the iris dataset has 2 clusters instead of 3. 
    t-SNE is in the scikitlearn package, but works a litle differently
         ```import matplotlib.pyplot as ply
        from sklearn.manifold import TSNE
        model = TNSE(learning_rate=100)
        transformed = model.fit_transform(samples)
        xs = transformed[:,0]
        ys = transformed[:,1]
        plt.scatter(xs, ys, c=species)
        plt.show()```

    t-SNE only has a fit_transform method
        simoultaneously fits the model and transforms the data.
        t-SNE does NOT have separate fit() or transform() methods
            this means it can't extend the t-SNE map to include new samples. 
            Instead, you have to start over each time. 
        The learning rate also makes t-SNE more complicated than other methods. You may need to try different learning rates for different data sets
            It's clear when you've made a bad chouce, as all the samples will appear bunched together in the scatter plot. 
                The axes of a t-SNE plot do not have any interpretable meaning. They are different every time.




        
