# Discovering Interpretable Features
## Non Negative Matrix Factorization (NMF)
    NMF, like PCA, is a dimension reduction technique. However, NMF models are interpretable
        Easier to understand yourself, and easier to explain to others. 
        Cannot be applied to every dataset - it demands that all samples be non-negative 
    Achieves interpretability by decomposing samples as sums of their parts
        NMF decomposes documents as combinations of common themes, and images as combinations of common patterns.
        Same fit/transform patterns as PCA - but desired number of components MUST be specified
        works with numpy arrays and csr_matrices

## NMF learns interpretable parts
    The components of NMF represent patterns that frequewntly occur in samples
        Word Frequency Array
            20,000 articles (rows)
            800 words (columns)
        We fit an NMF model with 10 components to the articles. 
        Choosing a component, we then look at the values for the component, which tell us which words have the highest values, we can see they fit a theme.
        So if NMF is applied to documents, and the components represent topics, and the NMF features reconstruct documents from the topics., and
        If NMF is applied to a collection of images on the other hand, thewn components represent patterns that frequently occur in images. 
            Therefore, we need to know how to represent a collection of images as a non-negative array.
            A collection of images of the same size can be encoded as a 2D (flattened) array, where each row corresponds to an image, and each column corresponds to a pixel. 
## Building recommender systems using NMF
    Suppose we are an engineer at a large online newspaper. 
        Task - recommend articles similar to the article being read by the user. 
        # Strategy
            Apply NMF to the word-frequency array
            NMF features describe the topic mixture of an article
                similar articles will have similar NMF features
                articles is a word frequency array.
            Versions of articles come into play - different versions of the same document will have the same topic proportions
                Exact feature values may be different (due to fluff words)
                    Because of this, we need to compare documents using the cosine similarity, which uses the angle between the two lines. 
                        Higher values indicate a greater similarity. -> Max of 1, when the angle =0
                        
                
