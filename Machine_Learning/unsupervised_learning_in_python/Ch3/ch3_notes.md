# Visualiuzing the PCA Transformation
    Moving on to dimension reduction
    Dimension reduction finds patterns in data, and uses these patterns to re-express it in a compressed form. Makes subsequent computation much more efficient
        Most important function is to reduce dataset to its 'bare-bones'
            Remove less informative "noise" features
            Noise causes big problems for supervised learningf tasks like regression and classification
    The most fundamental technique is called Principal Component Analysis (PCA)
        Operates in two steps:
            The first one, decorrolation, doesn't change the dimension of the data at all. 
            Second step reduces dimensions
                This video is focused on the first step. 
        # Step 1
            PCA rotates the samples so they are aligned with the coordinate axes
            Additionally shifts the samples so they have a mean of 0.
            No information is lost. 
        Scikit-learn has an implementation of PCA, and it has fit and transform methods like StandardScaler
            The fit() method learnes how to shift and rotate the samples, but does not actually change them. 
            The transform() method applies the transsformations that fit() learned. 
                transform() can be applied to new, unseen samples
            Due to the rotation it performs on the data, de-corrlates data, even if they are corrolated in the original data.
                The Pearson Corrolation measures linear correlation of features. 
                    Larger values indicate a stronger corrolation. 0 = None
        Its called PCA because ti learns the "principal components" of the data. 
            These are the directions in which samples vary the most. 
                After a PCA model has been fit, the principal components are available as the components attribute. 

# Intrinsic dimension
    Consider a dataset with 2 features: Latitude and Longitude
        Dataset appears 2 dimensional, yet it turns out that it can be closely approximated using only 1 feature - displacement along the flight path
            Therefore, it is intrinsically 1 dimensional
    The intrinsic dimension of a dataset is the number of features required to approximate it.
        this informs dimension reduction, because it tells us how much a dataset can be compressed
    Let's get a basic understanding of intrinsic dimensions, and use PCA to identify it in real-world datasets that have thousands of features. 
    
    Using the Versicolor (iris) dataset
        Using only 3 features: sepal length, sepal width and petal width:
            Each sample is represented as a point in 3 dimensional space
                Within a 3D scatter plot, we can see they all lie very close to a flat, 2 dimensional sheet
                    Therefore has intrinsic dimension 2
        Scatter plots only work if samples have 2-3 features
            How do we do it with more? - PCA
        PCA identifies intrinsic dimensions when samples have any number of features.
            Intrinsic dimensions are identified by counting the PCA features that have high varience. 

# Dimension Reduction with PCA
    Dimension reduction represents the same data with less features, and is vital for building ML pipelines
    PCA features are in decreasing order of varience
        PCA assumes low varience is noise, and retains higher varience PCA features, which it assumes to be informative.
            We need to specify how many features to keep -> PCA(n_components=2) is 2 features
            A great choice is the intrinsic dimension of the dataset, if you know it. 
                Like all assumptions, there are cases where this doesn't hold. 
                    Then we can use an alternative implementation of PCA. 
                In a word frequency array, each row corresponds to a document, and words are the columns
                    Most frequencies are zero, as those words do not appear in multiple documents
                        This is a 'sparse' array - or a csr_array
                            csr_arrays save space by only remembering the non-zero entries
                            PCR does not support CSR arrays - instead we will ahve to use Truncated SVDs