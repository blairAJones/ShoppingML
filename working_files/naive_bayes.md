### Overview

Naive Bayes is classifier model that uses probability for classification, and has a major assumption (thus, the "Naive" name) that features are conditionally independent given the class.  This model uses the concepts from Bayes theorem:

$P(K | X) = \displaystyle \frac{P(X | K) \cdot P(K)}{P(X)}$

With $P(K | X)$ representing the posterior probability of class $K$ given the data, $X$; $P(X | K)$ representing the likelihood of the data features X given the class K; $P(K)$ is the prior probability of the class K; and $P(X)$ is the evidence. Because of the feature independence assumption, the likelihood calculation ends up being $\prod_i P(X_i | K)$.  Naive Bayes can be done using binary features (Bernoulli NB), count features (Multinomial NB) and continuous features (Gaussian NB).

K-Nearest Neighbors is a supervised learning method where data points are classified based on a plurality vote of its K (positive integer) nearest neighbors.  As it is based on distance, numerical features are necessary and should be scaled prior to training.  The choice of K can be tuned during training. 

### Data
For classification methods, a classifier response was created.  "Is High Price" was added as a feature based on the product's median price.  For decision tree classification here, another method was considered.  

To use Bernoulli Naive Bayes, binary features were selected:

<pre style="font-size: 11px;"><code class="language-python">
binary_features_iphone = ["topRatedBuyingExperience", "priorityListing", "discount_flag",
                          "unlocked"]
binary_features_lego = ["is_prime", "sponsored", "has_coupon", "top_theme"]

response = "is_high_price"
</code></pre>

As discussed in the Data Prep / EDA tab, some of these binary features were from the original data, like "Top Rated Buying Experience", "Priority Listing" for the eBay data, and "Is Prime", "Sponsored", "Is Small Business" and "Has Coupon" for the Amazon data.  Others, like "Discount Flag" and "Top Club" were created to enhance the data exploration.  

For Gaussian Naive Bayes and K-Nearest Neighbors, numerical features were selected:

<pre style="font-size: 11px;"><code class="language-python">
num_features_iphone = ["seller.feedbackPercentage", "seller.feedbackScore", "days_listed",  
                       "seller_item_count", "model_number", "additional_image_count", "title_length"]
num_features_lego = ["rating", "ratings_total", "recent_sales_num", "discount$", 
                     "discount%"]
response = "is_high_price"
</code></pre>

Similar to the binary features, some numerical features were obtained from the original data, and some were created (like "Seller Item Count", "Additional Image Count", "Title Length" and "Discount$ and %").  

There is another Naive Bayes model, Multinomial, which is used for count data.  Some of the numerical features are counts (e.g. seller item count) and others are more continuous (feedback score).  All numerical features were scaled and thus the Gaussian NB was used for the above.  


### Code
The code can be found here.



### Results

All data sets were split into training and testing sets (80/20 split). For classification methods, the following metrics on the test set were considered along with the confusion matrix image:  accuracy, the percentage of correctly classified points; recall, the percentage of true positives (how many true positives were accurately predicted?); and the F1 score, which is a mix of recall and precision (how many predicted positives are actually positive?).  

#### iPhone

For Naive Bayes analysis on the iPhone data, the following was noted:

<div style="display: flex; justify-content: center; gap: 10px; margin-top: 20px;">
  <img src="images/3/cm_nbb_iphone.png" alt="Image 1" width="300">
  <img src="images/3/cm_nbg_iphone.png" alt="Image 2" width="300">
</div>

All metrics improved on the Gaussian model.  For the Bernoulli model, recall (how many true positives were accurately predicted) was worse than overall accuracy while for the Gaussian model, it was significantly better. Note that this model is for predicting price buckets and there is not a high risk of low recall (as there would be in medical detection or fraud cases).  

A KNN model was run on various k values with the following:

![](images/3/knn_plot_iphone.png)

With K=2, accuracy was  , recall was  and F1 score was  .  This is significantly improved from the Naive Bayes models.  After projecting into 2D with PCA, the true and predicted labels using KNN were plotted:

![](images/3/knn_pca_iphone.png)


#### Lego

For Naive Bayes analysis on the Lego data, the following was noted:

<div style="display: flex; justify-content: center; gap: 10px; margin-top: 20px;">
  <img src="images/3/cm_nbb_lego.png" alt="Image 1" width="300">
  <img src="images/3/cm_nbg_lego.png" alt="Image 2" width="300">
</div>

The Bernoulli model had mixed results -- accuracy was poor and recall was significantly higher.  This shows that the model thinks most items are true (price should be higher than median).  The Gaussian model had more consistent metrics.  For this data, the binary features are not good predictors by themselves.  

As discussed here, PCA is a technique to reduce dimensionality by creating new features that are linear combinations of the originals.  The new features are orthogonal to each other; therefore, non-correlated.  Note that this does not mean independence.

A Gaussian NB on PCA features (5) was created.

![](images/3/cm_nbg_pca_lego.png)


A KNN model was run on various k values with the following:

![](images/3/knn_plot_lego.png)

With K=7, accuracy was  , recall was  and F1 score was  . 

After projecting into 2D with PCA, the true and predicted labels using KNN were plotted:

![](images/3/knn_pca_lego.png)

### Summary
The Naive Bayes models had mixed results.  This is expected due to the nature of the data.  Since these are product listings 