## Undertanding Shopping Trends using ML

In 2024, eBay.com had 8.6Bn marketplace [revenue](https://investors.ebayinc.com/financial-information/sec-filings/sec-filings-details/default.aspx?FilingId=18232012) and Amazon.com had 530Bn [revenue](https://s2.q4cdn.com/299287126/files/doc_financials/2025/ar/Amazon-2024-Annual-Report.pdf).  For better or worse, online shopping is a significant source of revenue for some of the largest corporations in the world and is a near daily habit for millions of people.  

eBay maintains an [API service](https://developer.ebay.com/) for developer accounts which can return data on current listings for user-defined browsing categories.  Unfortunately, the API service which tracked actual sales was deprecated in 2024.  However, it is believed that current listings can tell a story on market prices for select items, and various quantitative and qualitative features can be used to model price prediction and the flagging of competitively priced or overpriced items.  

Amazon listings were obtained from a 3rd party service called [Rainforest API](https://app.rainforestapi.com/playground).  This service allows the user to obtain current listings based on search term or drill-down specifically on items based on asin (Amazon.com specific ID). 

To start, eBay was searched for two different types of products:  first, iPhone 16, which is a recent and popular consumer good that has many listings and some differentiation (model type, storage, etc.). Then, another eBay search was completed on soccer jerseys, which are highly specific, with some seen as "collectible".  This specific search was of interest because of the upcoming World Cup in 2026 (both club and country jerseys appeared in this search).

On Amazon, there were two searches performed:  Microwaves, a fairly homogeneous product with potential large price impacts from recent tariff actions, and Lego, a popular product that can have a "style" factor.  Depending on if data can be made available from another 3rd party service which tracks historical Amazon prices, additional analysis on price increases in the last year would be compelling. 

![](/images/summary_table.png)

The project plans to work with the available retail data and answer the following questions:

- Can item prices be accurately predicted based on current listings, including information like days-on-hand, markdowns, seller/product ratings, recent sales (Amazon)?
- Which features are most significant in these predictions?
- Do these models vary based on item type?  For example, iPhone 16 vs soccer jerseys where there is some differention with phone model types but lots of similar listings, compared with soccer jerseys which are highly specific.  
- Do prices follow a normal distribution, or would a log transformation be prudent?  Or possibly modeling based on another distribution, like using Poission for recent sales counts, for example.  
- Can a machine learning model help determine which items or listings are competitively priced or overpriced, compared to others?
- On eBay, do longer titles and more pictures indicate a higher quality listing?
- Are there differences in feature significance with seller ratings on eBay compared with product ratings on Amazon?
- Will tree-based models peform better on this data given the number of qualitative features?
- How could a recommender system and / or sentiment analysis of reviews be incorporated into future versions of the model?
- (Likely for future analysis) Have the announcements for recent tariffs caused preemptive or necessary increases in prices for home goods (microwaves)?  Answering this would require gaining access to another API service which tracks historical Amazon prices.   
