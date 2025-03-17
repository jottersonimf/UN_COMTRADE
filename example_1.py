import comtradeapicall

"""
From: Cabezon, Francisco <fcabezon@imf.org> 
Sent: Monday, March 17, 2025 4:01 PM
To: Otterson, James Joaquim <jotterson@imf.org>; Tang, Li <LTang@imf.org>
Subject: RE: Comtrade data

Hi James,

I have been working with the comtrade website and now I know exactly which data I need:

-	SITC: all at the three digit level (including total)
-	Periods: 1990-2023
-	Reporters: all
-	Partners: world
-	Trade flows: exports
-	Variables must include: year reporterISO  qty altQty netWgt grossWgt cifvalue fobvalue primaryValue

Can you help me with this?

Best,
Francisco

"""

import os 

subscription_key = os.getenv('COMTRADE_API_KEY')  # get the API key from the environment variable 

today = date.today()
yesterday = today - timedelta(days=1)
lastweek = today - timedelta(days=7)


# Call preview final data API to a data frame, max to 500 records, no subscription key required
# This example: Australia imports of commodity code 91 in classic mode in May 2022
mydf = comtradeapicall.previewFinalData(subscription_key, typeCode='C', freqCode='M', clCode='HS', period='202205',
                                        reporterCode='36', cmdCode='91', flowCode='M', partnerCode=None,
                                        partner2Code=None,
                                        customsCode=None, motCode=None, maxRecords=500, format_output='JSON',
                                        aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)


mydf = comtradeapicall.previewFinalData(subscription_key, typeCode = 'C', freqCode='M', clCode='HS', period='202205',
                                        reporterCode='36', cmdCode='91', flowCode='M', partnerCode=None,
                                        partner2Code=None,
                                        customsCode=None, motCode=None, maxRecords=500, format_output='JSON',
                                        aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)



