### Overview
Principal components analysis is a technique of reducing dimensionality by linear transformation.  The outputs of this analysis are called principal components which are new features that have been created from linear combinations of the originals.  The first principal component (PC1) is derived as a combination of the features which capture the maximum variance. PCA is way to reduce dimension for large-dimensional datasets and allows the user to visualize the data in 2D space by plotting PC1 / PC2.  

### Data
Principal Component Analysis (PCA) then completed on the eBay soccer jerseys data as well as the Amazon Lego data.    

Because PCA uses variance / covariance data to create the linear combinations, only numerical features are considered.

The following numerical features were used:

![](/images/2/features_soccer.png)

![](/images/2/features_lego.png)

Because the values are in different scales, the features are scaled in order to properly assess variance.  

### Code
The full code for the PCA analysis is found here____.


### Results
The data used in this project is not considered high-dimensional; there are ____ numerical features for the eBay data and ____ for the Amazon data.  However, PCA is needed for visualizing clusters in 2D, as well as identifying latent trends.  

#### eBay Soccer Jerseys
The following are the loadings from the soccer data:

![](/images/2/loadings_soccer.png)

The loadings represent how much the original features factor into the new principal components.  For example, PC1 is heavily influenced (positively) by title length and additional image count, which both point to a more detailed listed.  PC2 shows strong positive influence from a higher seller item count compared with a strong negative influence from a seller feedback score (total sales with feedback), so this contrasts higher vs lower volume sellers.  PC3 is driven by feedback percentage (proportion of positive feedback of total), which indicate a higher quality seller.  

![](/images/2/scree_soccer.png)

The scree plot shows that it takes five principal components to explain 80% of the variance in the data.  Because the original data had only numerical 7 features, this is not a meaningful reduction to dimension. 



#### Amazon Lego
The following are the loadings from the Lego data:

![](/images/2/loadings_lego.png)

PC1 appears to capture the connection with discounting and total ratings, whereas PC2 seems to capture discounts with negatively correlated recent sales, meaning items that are likely discounted to move.  PC3 almost exclusively factors in the product rating.  

![](/images/2/scree_lego.png)

The scree and cumulative variance plots show that it takes three PCs to obtain 80% of variance explained.  

![](/images/2/proj_lego.png)

The projection of the data in PC1 and 2 was plotted with a color gradient from the original feature recent sales, as this feature was moderately positive in PC1 (left-right direction) and moderately negative in PC2 (up-down direction).


![](/images/2/biplot_lego.png)

The biplot highlights the direction of the features in PC1 and 2.  

#### Summary
Because the original data is not high-dimensional, PCA was mostly used to find latent connections within the features.  Based on the loadings, it appeared to isolate high-quality listings and high-quality sellers (for eBay data) as well as the (negatively correlated) relationship between discount and recent sales in the case of Amazon data.  These are interesting connections that will be used in future analysis.  










