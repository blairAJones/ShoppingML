This project provided insight into how well various machine learning models can classify and predict prices of certain products based on a variety of features from from the listings on online retail sites like eBay and Amazon.  The original data sets were iPhone and Soccer Jerseys from eBay and Microwaves and Lego from Amazon.  The Amazon data had fewer data points, especially after data cleaning and pre-processing.  In general, performance was not as strong on this data, and ultimately mostly the eBay data sets were the point of focus.  The Amazon API LINK was limited for the free tier and so more data was not readily available at this time.  In future versions of this project, additional data sources can be considered.        


The unsupervised learning portion of the project led to some insights on feature consolidation, but ultimately showed that it is a challenge to find natural clustering of this data.  Principal component analysis attempted to combine features in meaningful ways, like high-quality listing and high-quality seller.  However, due to the limited continuous numerical features, dimension reduction was not needed as much as would be using other data sets.  K-Means and Hierarchical clustering also requires only continuous numerical features, and thus it was difficult in finding natural clustering of the data.  Other methods such as K-Modes and K-Prototypes methods, which allow for categorical features, will be explored in future analysis.


The supervised learning models included k-nearest neighbors and naive Bayes, decision trees, support vector machines, and neural networks.  Model performance was mixed depending on model type.  For the most part, classification models were built to determine price buckets or tiers.  Naive Bayes suffered likely due to the feature independence assumption.  Support vector machines only handle two-class separation, so a simple "Is High Price" classifier, based on median, was created from the price field.  While the classes are balanced in this case, there could be an issue if many data points are very close to the median and thus a strong boundary isn't available.  SVM allow the flexibility to transform the data into higher dimensional spaces for separation, but are limited in that only continuous numerical features are able to be used.  Decision trees and neural networks are more flexible in terms of feature usage; although categorical features require pre-processing into a one-hot-encoder, but because they aren't based on a distance measure, they are still an option for training.  In addition, decision trees can be used for multi-class classification.  Because of the high number of categorical and binary features for this data, decision trees, particularly random forests, as well as neural networks, are better fits for the data.  Additional analysis could be done on random forest regression and additional ensemble methods, like XGBoost.  


The data cleaning and processing continued throughout the whole project. A number of fields were created based on information found in the title field.  Fields were even introduced in the middle of the project; for example, after analyzing mis-classes on the iPhone data set, the writer noted a <em>Model Type</em> (Plus, Pro Max, etc.) in most listings that likely have an influence on the price and thus would be beneficial to have as a feature.  Some of the created features weren't available for all listings; for example, <em>year</em> in the soccer jerseys listings, which was extracted for many but some were blank.  Models like random forests can handle missing values, but most other models cannot.  A decision then needs to be made to remove the missing data points and still use that feature, or to exclude that field as a feature.  In future versions of the project, performance could be compared on models that include features with fewer data points versus models that exclude those particular features.  


Ultimately, as it was proposed in the Introduction (LINK), decision trees, particular random forests with tuned hyperparameters, performed well and gave the best trade-off between performance and interpretability.  Decision trees can be visualized with understandable cut-offs for decisions and feature importance can be easily extracted from the final models.  As mentioned above, these models can handle missing values as well as categorical and binary features, of which there are many for this data. Neural networks provided similar flexibility with feature selection; however, remain difficult to interpret and extract how the individual features influenced the model.  Future versions of this project will dive deeper into decision tree and ensemble models (like boosting) as well as additional neural network refinement.  



   <p>The following questions were posed at the beginning of the project, now along with answers based on the
        results.</p>
      <ul>
        <li>
          <strong style="display: block; margin-bottom: 0.8em;">
            Can item prices be accurately predicted based on current listings, including information like days-on-hand,
            markdowns, seller/product ratings, and recent sales (Amazon)?
          </strong>
          <p style="margin-left: 1.2em; color: #555;">
            Yes, a neural network regression (compared with baseline multiple linear regression) was able to predict prices of iPhones and soccer jerseys well below the standard deviation of the price data, meaning the models have some predictive power.  The tuned random forest classification models were able to predict price tiers with minimal low/high mis-classes.  
          </p>
        </li>
        <li>
          <strong style="display: block; margin-bottom: 0.8em;">
            Which features are most significant in model predictions?
          </strong>
          <p style="margin-left: 1.2em; color: #555;">
            This depends on the data set.  For iPhones, model number, and by a smaller measure, the model type, were important features, along with days listed.  For soccer jerseys, the seller feedback score was the top feature, with days listed, year and title length all noted as well.  For Microwaves, the cubic feet (product size) was by far the top feature.  And with Lego, the number of ratings and discount amount were noted as the top features.
          </p>
        </li>
        <li>
          <strong style="display: block; margin-bottom: 0.8em;">
            Do machine learning models vary based on product type? For example, iPhone 16 vs. soccer jerseys, where
            there is some differentiation with phone model types but lots of similar listings, compared with soccer
            jerseys which are highly specific.
          </strong>
          <p style="margin-left: 1.2em; color: #555;">
            Random Forests and Neural Nets performed well for both the iPhone and Soccer data.  It should be noted that the iPhone NN regression model showed no improvement over the baseline MLR model; while the Soccer NN regression model did.  This could indicate that there are inherent differences in the data itself (some amount of linearity vs. flexibility).
          </p>
        </li>
        <li>
          <strong style="display: block; margin-bottom: 0.8em;">
            Do prices follow a normal distribution, or would a log transformation be prudent? Or possibly modeling based
            on another distribution, like using Poisson for recent sales counts, for example.
          </strong>
          <p style="margin-left: 1.2em; color: #555;">
            Prices generally do not follow a normal distribution.  Log transformation of prices did not improve the performance of the regression models used; however, the majority of models tested in this project were classification and thus not relevant.  More analysis is needed if additional regression-based models are trained.   
          </p>
        </li>
        <li>
          <strong style="display: block; margin-bottom: 0.8em;">
            Can a machine learning model help determine which items or listings are competitively priced or overpriced,
            compared to others?
          </strong>
          <p style="margin-left: 1.2em; color: #555;">
            On the models that allow multi-class classification, the writer was able to split the data into low, medium and high pricing tiers.  Potentially overpriced items were considered those that were predicted <em>low</em> but had a <em>high</em> true value, with potentially underpriced items the opposite.  Additional analysis should be completed on those specific items to see if additional information can be extracted from the listing that may prove to be a meaningful feature ("retro" or "rare" in title, for example.)
          </p>
        </li>
        <li>
          <strong style="display: block; margin-bottom: 0.8em;">
            On eBay, do longer titles and more pictures indicate a higher quality listing?
          </strong>
          <p style="margin-left: 1.2em; color: #555;">
            In PCA analysis, longer titles and additional images had the most influence on PC1, which indicates there is a relationship between these two variables.  <em>High-quality listing</em> is challenging to measure, but there appears to be some influence of these features with each other and on modeling price (based on RF feature importance).
          </p>
        </li>
        <li>
          <strong style="display: block; margin-bottom: 0.8em;">
            Are there differences in feature significance with seller ratings on eBay compared with product ratings on
            Amazon?
          </strong>
          <p style="margin-left: 1.2em; color: #555;">
            Seller ratings and product ratings both appeared in the top 10 feature imporatances for the eBay and Amazon products, respectively.  They appear to be important in both cases. 
          </p>
        </li>
        <li>
          <strong style="display: block; margin-bottom: 0.8em;">
            Will tree-based models perform better on this data given the number of qualitative features?
          </strong>
          <p style="margin-left: 1.2em; color: #555;">
            Based on overall accuracy metrics, random forest models performed well on this data.  The ability to include categorical and binary features, along with the ability to train on some that have missing values, was important for this data, given the low number of truly continuous numerical features.  
          </p>
        </li>
        <li>
          <strong style="display: block; margin-bottom: 0.8em;">
            How could a recommender system and / or sentiment analysis of reviews be incorporated into future versions
            of the model?
          </strong>
          <p style="margin-left: 1.2em; color: #555;">
            This is to be determined.  It would be interesting to see if sentiment analysis was in-line with the numerical ratings on the Amazon data. 
          </p>
        </li>
        <li>
          <strong style="display: block; margin-bottom: 0.8em;">
            (Likely for future analysis) Have the announcements for recent tariffs caused preemptive or necessary
            increases in prices for home goods (e.g. microwaves)? Answering this would require gaining access to another
            API service which tracks historical Amazon prices.
          </strong>
          <p style="margin-left: 1.2em; color: #555;">
            This is to be determined.  All data used in this analysis was static, based on the current prices as of the run date (July 10, 2025).
          </p>
        </li>
      </ul>
    