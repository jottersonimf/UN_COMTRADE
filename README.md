# UN COMTRADE data

webpage: https://comtradedeveloper.un.org/ </br>
official documentation: https://uncomtrade.org/

<blockquote>
<h3> UN COMTRADE - world's most comprehensive global trade data platform </h3>

<p>The United Nations Comtrade database aggregates detailed global annual 
and monthly trade statistics by product and trading partner...</p>

<p>It provides detailed import and export statistics in goods and services reported by statistical authorities of close to 200 countries/areas since 1962. With tens of billions of data points, it is considered the most comprehensive online trade database available [representing more than 99% of the world's merchandise
trade]. </p>
</blockquote>


## Setting up
<details>
<summary> Getting an API Key </summary>
<p>
Go to the UN COMTRADE 
[website](https://comtradeplus.un.org/)
login using your IMF email. Go to "Profile" and 
generate or read our Primary and Secondary keys.  Store the keys as environment
variables (say, using the name "API_KEY_UNCOMTRADE").  Using an IMF email 
is crucial as it allows access to "Premium Institutional" subscription.  
</p>
</details>

<details>
<summary> User accounts limits and access </summary>

<p>

There are [four types](https://uncomtrade.org/docs/subscriptions/) of subscriptions: 
| Subscription | Limits | API access |
| ---- | ---- | --- |
| Public | 500 records, 1 period, and 1 product per call | Preview API |
| Basic Individual | 500 calls/day  | Preview, and Data APIs |
| Premium Individual | 5000 calls/day | Preview, Data, Bulk, and Async APIs |
| Premium Institutional  | unlimited | Preview, Data, Bulk, and Async APIs |
</p>
</details>

</br>

## API overview

The main databases of interest are the "Trade" ones.  There are also:

   * derivative tables of interest (Tarifflines) that are close to datasets 
countries submitted to the UN and are the building blocks of the "Trade" tables.
   * metadata tables which provide information on the 
parametes needed to specify a Trade table (eg, country codes, 
trade classification tables), 
   * overall information about 
Trade tables (eg, if a table with given parameters exists,
and if so how many entries it has).  
   * Finally, there are experimental tables, which are discontinued, that tracked
   maritime trade information.


## Metadata tables

There are metadata information on the inputs needed to specify a table, 
and on the the table variables (columns).  

<details>
<summary> Input parameters specifying a table </summary>

There

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
</details>


<details>
<summary> Output parameters of a table </summary>
There are APIs providing descriptions of the output variables (the columns 
of output tables).

```python
# (1) To get the list of APIs providing information on output variables:
comtradeapicalls.listReference()

# (2) examples of API calls:

# The overall description of all output variables
comtradeapicall.getReference('dataitem') 

# HS classification of goods, 2022 version 
# NOTE: see listReference() above for the list of all APIs describing commodity 
# classification schemes.
comtradeapicall.getReference('cmd:H6')  
```

</details>

## Data tables



