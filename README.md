# UN COMTRADE data

webpage: https://comtradeplus.un.org/

Description as per website: 
<blockquote>
<h3> The world's most comprehensive global trade data platform </h3>

<p>The United Nations Comtrade database aggregates detailed global annual 
and monthly trade statistics by product and trading partner... </p>

<p>Data compiled by the United Nations Statistics Division covers approximately 200 countries 
and represents more than 99% of the world's merchandise trade. [No services data.]</p>

</blockquote>

## Setting up
Go to the UN COMTRADE website, login using your IMF email. Go to "Profile" and 
generate or read our Primary and Secondary keys.  Store the keys as environment
variables (say, using the name "API_KEY_UNCOMTRADE").  Using an IMF email 
is crucial as it allows access to "Premium Institutional" subscription.  Click on "Products" to see 
the list of APIs.  

### User accounts and APIs

There are [four types](https://uncomtrade.org/docs/subscriptions/) of subscriptions: 
| Subscription | Limits | API access |
| ---- | ---- | --- |
| Public | 500 records, 1 period, and 1 product per call | Preview Data API |
| Basic Individual | 500 calls/day  | Preview Data, and Data APIs |
| Premium Individual | 5000 calls/day | Preview Data, Data, Bulk, and Async APIs |
| Premium Institutional  | unlimited | Preview Data, Data, Bulk, and Async APIs |





## Description of main functions:

| Function | Description |
| -------  | ----------- |
| previewFinalData | | 



## Issue with package


## Description of request options

| Name| In| Required| Type| Description| 
| --- | -- | --- | --- | ----|
| typeCode| template| true| string| Type of trade: C for commodities and S for service|
|freqCode| template| true| string| Trade frequency: A for annual and M for monthly|
|clCode| template| true| string| Trade (IMTS) classifications: HS, SITC, BEC or EBOPS.|
|reporterCode| query| false| string| Reporter code (Possible values are M49 code of the countries separated by comma (,))|
|period| query| false| string| Year or month. Year should be 4 digit year. Month should be six digit integer with the values of the form YYYYMM. Ex: 201002 for 2010 February. Multi value input should be in the form of csv (Codes separated by comma (,))|
|partnerCode| query| false| string| Partner code (Possible values are M49 code of the countries separated by comma (,))|
|partner2Code| query| false| string| Second partner/consignment code (Possible values are M49 code of the countries separated by comma (,))|
|cmdCode| query| false| string| Commodity code. Multi value input should be in the form of csv (Codes separated by comma (,))|
|flowCode| query| false| string| Trade flow code. Multi value input should be in the form of csv (Codes separated by comma (,))|
|customsCode| query| false| string| Customs code. Multi value input should be in the form of csv (Codes separated by comma (,))|
|motCode| query| false| string| Mode of transport code. Multi value input should be in the form of csv (Codes separated by comma (,))|
|aggregateBy| query| false| csv| Add parameters in csv list on which you want the results to be aggregated|
|breakdownMode| query| false| csv| Mode to choose from|
|includeDesc| query| false| boolean| Include descriptions of data variables|
