# Unsupervised Learning in Python
    Unsupervised learning is a class of ML techniques to discover patterns in data. 
    Ex. finding "clusters" of customers based on their purchase histories or searching for patterns and correlations in these purchases, and using thes patters to express the data in a compressed form. 
        These are examples of clustering and dimension reduction
    
Supervised learning finds patterns for a prediction task
    Ex. Classify tumors as benign or cancerous (labeling)
Unsupervised is learning to find patterns in the data without labels
    Most importantly, without a specific prediction task in mind

# Dataset explanation and exploration
The iris dataset consits of measurements of 3 different species of iris:
    setosa
    versicolor
    virginica
Measurements: petal length, petal width, sepal length, sepal width
    These are the features of the dataset

Datasets in this course will be written as 2D NumPy arrays
    Columns are measurements (the features)
    Rows represent iris plants (the samples)

Because there are four measurements, this corresponds to points in a 4 dimensional space

First, we will explore the data using k-means clustering
    This finds clusters of samples
    The number of clusters must be specified

    If someone comes along with new samples, k-means can assign these new samples to existing clusters, without starting over
        k-means does this by remembering the mean of each cluster (the centroid) -> new samples are assigned to the coentroid which is closest
    
# Evaluating a Cluster
    A direct approach is to check the correspondance against the iris species
        What is there are no species to check against?
        We measure by the quality of clustering
            We use this to make an informed choice of how many clusters to look for
    First, lets check if the three clusters have any correspondance to the iris species
        We find that cluster 1 corresponds perfectly with the setosa species
    The table we saw in the video are called "cross-tabluations" -> constructed with the pandas library

    Assume the species of each sample is given as a list of strings
        import pandas, than create a 2 column df, first column being cluster labels and second being the species strings. Each row is a single sample
    ```import pandas as pd
        df = pd.DataFrame({'labels': labels, 'species': species})
        print(df)```

        ## Creating the crosstab
        ``` ct = pd.crosstab(df['labels'], df['species'])
            print(ct)```

    Cross tabs provide great insights into which sample is in which cluster, but in most datasets samples are not labelled by species
        This is why we measure clustering quality
            A good clustering has tight clusters, meaning each cluster is bunched together and not spread out. 
    Inertia measures cluster quality
        Inertia measures how spread out the clusters are (lower is better)
        Distance from each sample tot he centroid of the cluster
        After using the .fit() method, it is available as the attirbute inertia_
        ``` from skleanr.cluster import KMeans
            model = KMeans(n_clusters=3)
            model.fit(samples)
            print(model.inertia_)```
        Kmeans aims to place clusters in a way which minimizes inertia
    Choosing higher clusters is a trade-off
        A good clustering has tight clusters (and therefore low inertia)
        but not too many clusters!
        A good rule of thumb is to choose an elbow in the inertia point -> a point where the inertia begins to decrease more slowly.
    
# Transforming features for better clusterings
    Working with the Piedmont wines dataset
        178 samples of red wine
    Building a crosstab, we can see that the clustering into groups of 3 does not work well in separating them by region. 
    The problem is all the features have very different variences
        Varience measures the spread of its values
    The malic acid feature has a muuch higher varience than the od280 feature. 

    In kmeans clustering, the varience of a feature corresponds to its influence on the clustering algorithm.
        Therefore, we need to transform the data so that every feature has equal varience
            This can be achieved with the standard scalar from scikitlearn
                Transforms every feature to have mean 0 and varience 1
                    This "standardizes" the features
    Pipelines combine multiple steps:
    ```from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        scaler.fir(samples)
        StandardScalar(copy=True, with_mean=True, with_std=True)
        samples_scaled = scaler.transform(samples)

    The APIs for StandardScaler and KMeans have similar methods, with an important difference.
        StandardScaler transforms the data, and therefor has a transaform method
            Use fit() / transform() with SS
        Kmeans instead assigns cluster labels to samples, and this is done using predict()
            User fit() / predict() with KMeans

    In order to cluster our wines, we need to perform two steps:
        StandardScaler, then KMeans 
        This can be combined into one step using a scikitlearn pipeline
     ```from sklearn.preprocessing import StandardScaler
        from sklearn.cluster import KMeans
        sclaer = StandardScaler()
        kmeans = KMeans(n_clusters=3)
        from sklearn.pipeline import make_pipeline
        pipeline = make_pipeline(scaler, kmeans)
        pipeline.fit(samples)
        Pipeline(steps=...)
        labels = pipeline.predict(samples)



