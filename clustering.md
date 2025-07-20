### Overview

K-Means and hierarchical clustering are unsupervised machine learning techniques which group data together based on similarity metrics.  K-Means uses a pre-specified number of clusters (k) while hierarchical clustering grows a hierarchy of clusters from the bottom-up.  Both methods allow the user to identify underlying patterns in the data across multiple features and can assist with reducing the dimension of large datasets.  

For this particular project, various quantitative features are analyzed via clustering to identify which items naturally cluster together and how their features are related.  For example, on the eBay data, is there a relationship between the seller's ratings and additional images posted on the listings?  Or, the seller's ratings and seller's count of current listings?  

____pictures from the 2D

For the Amazon data, of interest was the recent sales data and ratings scores and totals.  

____pictures from the 2D

Details are discussed below.

### Data
The dataframes used from ___ here continue to be analyzed.

For the eBay data, the numerical features used in this analysis were as follows: 

![](/images/2/features_iphones.png)

The seller feedback score represents the count of feedback received and the percentage represents the proportion of positive feedback out of total. 

For the Amazon data, the numerical features used in this analysis were as follow:  

![](/images/2/features_micro.png)

There are fewer quantitative features for this data and additional filtering needed to be completed as not all listings had a cubic feet (microwave size) description in the title.  

### Code
A link to the full code for this analysis is found ___here.


### Results
#### eBay iPhones Data
##### K-Means
On the eBay iPhone data, a K-Means elbow plot was created to identify a choice for k number of clusters.  

![](/images/2/elbow_iphone.png)

There is not a clear point in which the plot "bends"; although it does appear that around k=4 or 5, there is a decrease in the slope, but does seem to increase slightly again.



Then, a silhouette plot was created to assist with the selection of k. 

![](/images/2/silh_iphone.png)

Based on the peak at 4, which ______, k=4 was chosen for further analysis.  

![](/images/2/kclust_sum.png)

The above cluster summary shows the counts and mean feature values by cluster number.  

To plot the full data using the cluster colors, the dimensions were reduced to two via PCA projection (see __ tab for additional information on PCA).  

![](/images/2/kmeans_wPCA_micro.png)

Unfortunately, for this data, the reduction to two dimensions does not assist with the visualization of the clusters. 

Select features were plotted against each other to identify interesting patterns.  

One example was seller feedback vs. additional image count:

![](/images/2/feedback_vs_image_ct.png)

Animated clustering process:

![](/images/2/kmeans.gif)




##### Hierarchical
For hierarchical clustering, one needs to consider a linkage method when building the clusters up.  Some options include Ward, which minimizes the within cluster variances as they are built; complete, which considers the maximum distance between any pair of points within a cluster; and average, which considers the average distance of the points in a cluster.  These use Euclidean distance to measure; another option would be to consider cosine similarity as the distance measure, along with a link function (note that Ward uses Euclidean only). So, Ward and Complete linkage with Euclidean distance along with Complete linkage and cosine similarity distance were chosen to create dendograms.

![](/images/2/dendogram_iphone.png)


![](/images/2/hclust_counts.png)

Based on these, k=6 was selected with the complete linkage using cosine similarity distance, as it appears to have the most balanced clusters.



These clusters were plotted via PCA projection.

![](/images/2/hclust_iphone.png)

#### Amazon Microwaves Data
##### K-Means
The microwaves data from Amazon was selected to perform similar K-means clustering analysis. An elbow plot and silhouette plot were created to assist with the choice of k.  

![](/images/2/elbow_micro.png)

![](/images/2/silh_micro.png)

Based on both charts, k = 3 was selected for further analysis.

![](/images/2/kmeans_wPCA_micro.png)

The PCA projection shows some evidence of clusters, and the first two principal components contributed more explained variance (63%) compared with the iPhones data (50%).

Two select features were plotted, cubic feet (size) vs. ratings totals, and achieved convergence within ___ iterations.

![](/images/2/cu_vs_ratingtotal.png)

![](/images/2/kmeans_micro.gif)

### Summary

Ultimately, clustering found some interesting connections but it remained difficult to identify clear clusters in this data.  It is possible that the data is just not naturally clustered, or that the numerical features do not tell the whole story of of these datasets, and categorical feature analysis is required as well.












