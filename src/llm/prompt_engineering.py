sql_context = '''TABLE analyst_price_targets(
   index BIGINT, -- analyst_price_targets index
   current DOUBLE, -- analyst_price_targets current
   low DOUBLE, -- analyst_price_targets low
   high DOUBLE, -- analyst_price_targets high
   mean DOUBLE, -- analyst_price_targets mean
   median DOUBLE, -- analyst_price_targets median
   Symbol VARCHAR, -- analyst_price_targets Symbol
   index BIGINT, -- analyst_price_targets index
   current DOUBLE, -- analyst_price_targets current
   low DOUBLE, -- analyst_price_targets low
   high DOUBLE, -- analyst_price_targets high
   mean DOUBLE, -- analyst_price_targets mean
   median DOUBLE, -- analyst_price_targets median
   Symbol VARCHAR, -- analyst_price_targets Symbol
)
 
TABLE balance_sheet(
   index VARCHAR, -- balance_sheet index
   2023-12-31 00:00:00 DOUBLE, -- balance_sheet 2023-12-31 00:00:00
   2022-12-31 00:00:00 DOUBLE, -- balance_sheet 2022-12-31 00:00:00
   2021-12-31 00:00:00 DOUBLE, -- balance_sheet 2021-12-31 00:00:00
   2020-12-31 00:00:00 DOUBLE, -- balance_sheet 2020-12-31 00:00:00
   2019-12-31 00:00:00 DOUBLE, -- balance_sheet 2019-12-31 00:00:00
   Symbol VARCHAR, -- balance_sheet Symbol
)
 
TABLE calendar(
   index BIGINT, -- calendar index
   Dividend Date DATE, -- calendar Dividend Date
   Ex-Dividend Date DATE, -- calendar Ex-Dividend Date
   Earnings Date DATE[], -- calendar Earnings Date
   Earnings High DOUBLE, -- calendar Earnings High
   Earnings Low DOUBLE, -- calendar Earnings Low
   Earnings Average DOUBLE, -- calendar Earnings Average
   Revenue High BIGINT, -- calendar Revenue High
   Revenue Low BIGINT, -- calendar Revenue Low
   Revenue Average BIGINT, -- calendar Revenue Average
   Symbol VARCHAR, -- calendar Symbol
)
 
TABLE cashflow(
   index VARCHAR, -- cashflow index
   2023-12-31 00:00:00 DOUBLE, -- cashflow 2023-12-31 00:00:00
   2022-12-31 00:00:00 DOUBLE, -- cashflow 2022-12-31 00:00:00
   2021-12-31 00:00:00 DOUBLE, -- cashflow 2021-12-31 00:00:00
   2020-12-31 00:00:00 DOUBLE, -- cashflow 2020-12-31 00:00:00
   2019-12-31 00:00:00 DOUBLE, -- cashflow 2019-12-31 00:00:00
   Symbol VARCHAR, -- cashflow Symbol
)
 
TABLE companies(
   symbol VARCHAR, -- companies symbol
   name VARCHAR, -- companies name
   summary VARCHAR, -- companies summary
   currency VARCHAR, -- companies currency
   sector VARCHAR, -- companies sector
   industry_group VARCHAR, -- companies industry_group
   industry VARCHAR, -- companies industry
   exchange VARCHAR, -- companies exchange
   market VARCHAR, -- companies market
   country VARCHAR, -- companies country
   state VARCHAR, -- companies state
   city VARCHAR, -- companies city
   zipcode VARCHAR, -- companies zipcode
   website VARCHAR, -- companies website
   market_cap VARCHAR, -- companies market_cap
   isin VARCHAR, -- companies isin
   cusip VARCHAR, -- companies cusip
   figi VARCHAR, -- companies figi
   composite_figi VARCHAR, -- companies composite_figi
   shareclass_figi VARCHAR, -- companies shareclass_figi
   sp_500 BOOLEAN, -- companies sp_500
)
 
TABLE earnings_dates(
   Earnings Date TIMESTAMP WITH TIME ZONE, -- earnings_dates Earnings Date
   EPS Estimate DOUBLE, -- earnings_dates EPS Estimate
   Reported EPS DOUBLE, -- earnings_dates Reported EPS
   Surprise(%) DOUBLE, -- earnings_dates Surprise(%)
   Symbol VARCHAR, -- earnings_dates Symbol
)
 
TABLE earnings_estimate(
   index VARCHAR, -- earnings_estimate index
   numberOfAnalysts BIGINT, -- earnings_estimate numberOfAnalysts
   avg DOUBLE, -- earnings_estimate avg
   low DOUBLE, -- earnings_estimate low
   high DOUBLE, -- earnings_estimate high
   yearAgoEps DOUBLE, -- earnings_estimate yearAgoEps
   growth DOUBLE, -- earnings_estimate growth
   Symbol VARCHAR, -- earnings_estimate Symbol
)
 
TABLE earnings_history(
   index TIMESTAMP_NS, -- earnings_history index
   epsEstimate DOUBLE, -- earnings_history epsEstimate
   epsActual DOUBLE, -- earnings_history epsActual
   epsDifference DOUBLE, -- earnings_history epsDifference
   surprisePercent DOUBLE, -- earnings_history surprisePercent
   Symbol VARCHAR, -- earnings_history Symbol
)
 
TABLE eps_revisions(
   index VARCHAR, -- eps_revisions index
   upLast7days BIGINT, -- eps_revisions upLast7days
   upLast30days BIGINT, -- eps_revisions upLast30days
   downLast7days INTEGER, -- eps_revisions downLast7days
   downLast30days BIGINT, -- eps_revisions downLast30days
   Symbol VARCHAR, -- eps_revisions Symbol
)
 
TABLE eps_trend(
   index VARCHAR, -- eps_trend index
   current DOUBLE, -- eps_trend current
   7daysAgo DOUBLE, -- eps_trend 7daysAgo
   30daysAgo DOUBLE, -- eps_trend 30daysAgo
   60daysAgo DOUBLE, -- eps_trend 60daysAgo
   90daysAgo DOUBLE, -- eps_trend 90daysAgo
   Symbol VARCHAR, -- eps_trend Symbol
)
 
TABLE growth_estimates(
   level_0 VARCHAR, -- growth_estimates level_0
   stock DOUBLE, -- growth_estimates stock
   industry DOUBLE, -- growth_estimates industry
   sector DOUBLE, -- growth_estimates sector
   index DOUBLE, -- growth_estimates index
   Symbol VARCHAR, -- growth_estimates Symbol
)
 
TABLE historical_meta_data(
   index BIGINT, -- historical_meta_data index
   currency VARCHAR, -- historical_meta_data currency
   symbol VARCHAR, -- historical_meta_data symbol
   exchangeName VARCHAR, -- historical_meta_data exchangeName
   fullExchangeName VARCHAR, -- historical_meta_data fullExchangeName
   instrumentType VARCHAR, -- historical_meta_data instrumentType
   firstTradeDate BIGINT, -- historical_meta_data firstTradeDate
   regularMarketTime BIGINT, -- historical_meta_data regularMarketTime
   hasPrePostMarketData BOOLEAN, -- historical_meta_data hasPrePostMarketData
   gmtoffset BIGINT, -- historical_meta_data gmtoffset
   timezone VARCHAR, -- historical_meta_data timezone
   exchangeTimezoneName VARCHAR, -- historical_meta_data exchangeTimezoneName
   regularMarketPrice DOUBLE, -- historical_meta_data regularMarketPrice
   fiftyTwoWeekHigh DOUBLE, -- historical_meta_data fiftyTwoWeekHigh
   fiftyTwoWeekLow DOUBLE, -- historical_meta_data fiftyTwoWeekLow
   regularMarketDayHigh DOUBLE, -- historical_meta_data regularMarketDayHigh
   regularMarketDayLow DOUBLE, -- historical_meta_data regularMarketDayLow
   regularMarketVolume BIGINT, -- historical_meta_data regularMarketVolume
   longName VARCHAR, -- historical_meta_data longName
   shortName VARCHAR, -- historical_meta_data shortName
   chartPreviousClose DOUBLE, -- historical_meta_data chartPreviousClose
   priceHint BIGINT, -- historical_meta_data priceHint
   currentTradingPeriod STRUCT(pre STRUCT(timezone VARCHAR, "end" INTEGER, "start" INTEGER, gmtoffset INTEGER), regular STRUCT(timezone VARCHAR, "end" INTEGER, "start" INTEGER, gmtoffset INTEGER), post STRUCT(timezone VARCHAR, "end" INTEGER, "start" INTEGER, gmtoffset INTEGER)), -- historical_meta_data currentTradingPeriod
   dataGranularity VARCHAR, -- historical_meta_data dataGranularity
   range VARCHAR, -- historical_meta_data range
   validRanges VARCHAR[], -- historical_meta_data validRanges
   Symbol_1 VARCHAR, -- historical_meta_data Symbol_1
)
 
TABLE income_stmt(
   index VARCHAR, -- income_stmt index
   2023-12-31 00:00:00 DOUBLE, -- income_stmt 2023-12-31 00:00:00
   2022-12-31 00:00:00 DOUBLE, -- income_stmt 2022-12-31 00:00:00
   2021-12-31 00:00:00 DOUBLE, -- income_stmt 2021-12-31 00:00:00
   2020-12-31 00:00:00 DOUBLE, -- income_stmt 2020-12-31 00:00:00
   2019-12-31 00:00:00 DOUBLE, -- income_stmt 2019-12-31 00:00:00
   Symbol VARCHAR, -- income_stmt Symbol
)
 
TABLE insider_purchases(
   index BIGINT, -- insider_purchases index
   Insider Purchases Last 6m VARCHAR, -- insider_purchases Insider Purchases Last 6m
   Shares BIGINT, -- insider_purchases Shares
   Trans BIGINT, -- insider_purchases Trans
   Symbol VARCHAR, -- insider_purchases Symbol
)
 
TABLE insider_roster_holders(
   index BIGINT, -- insider_roster_holders index
   Name VARCHAR, -- insider_roster_holders Name
   Position VARCHAR, -- insider_roster_holders Position
   URL VARCHAR, -- insider_roster_holders URL
   Most Recent Transaction VARCHAR, -- insider_roster_holders Most Recent Transaction
   Latest Transaction Date TIMESTAMP_NS, -- insider_roster_holders Latest Transaction Date
   Shares Owned Directly BIGINT, -- insider_roster_holders Shares Owned Directly
   Position Direct Date TIMESTAMP_NS, -- insider_roster_holders Position Direct Date
   Symbol VARCHAR, -- insider_roster_holders Symbol
)
 
TABLE insider_transactions(
   index BIGINT, -- insider_transactions index
   Shares BIGINT, -- insider_transactions Shares
   URL VARCHAR, -- insider_transactions URL
   Text VARCHAR, -- insider_transactions Text
   Insider VARCHAR, -- insider_transactions Insider
   Position VARCHAR, -- insider_transactions Position
   Transaction VARCHAR, -- insider_transactions Transaction
   Start Date TIMESTAMP_NS, -- insider_transactions Start Date
   Ownership VARCHAR, -- insider_transactions Ownership
   Value DOUBLE, -- insider_transactions Value
   Symbol VARCHAR, -- insider_transactions Symbol
)
 
TABLE institutional_holders(
   index BIGINT, -- institutional_holders index
   Date Reported TIMESTAMP_NS, -- institutional_holders Date Reported
   Holder VARCHAR, -- institutional_holders Holder
   pctHeld DOUBLE, -- institutional_holders pctHeld
   Shares BIGINT, -- institutional_holders Shares
   Value BIGINT, -- institutional_holders Value
   Symbol VARCHAR, -- institutional_holders Symbol
)
 
TABLE major_holders(
   index VARCHAR, -- major_holders index
   Value DOUBLE, -- major_holders Value
   Symbol VARCHAR, -- major_holders Symbol
)
 
TABLE mutualfund_holders(
   index BIGINT, -- mutualfund_holders index
   Date Reported TIMESTAMP_NS, -- mutualfund_holders Date Reported
   Holder VARCHAR, -- mutualfund_holders Holder
   pctHeld DOUBLE, -- mutualfund_holders pctHeld
   Shares BIGINT, -- mutualfund_holders Shares
   Value BIGINT, -- mutualfund_holders Value
   Symbol VARCHAR, -- mutualfund_holders Symbol
)
 
TABLE quarterly_balance_sheet(
   index VARCHAR, -- quarterly_balance_sheet index
   2024-06-30 00:00:00 DOUBLE, -- quarterly_balance_sheet 2024-06-30 00:00:00
   2024-03-31 00:00:00 DOUBLE, -- quarterly_balance_sheet 2024-03-31 00:00:00
   2023-12-31 00:00:00 DOUBLE, -- quarterly_balance_sheet 2023-12-31 00:00:00
   2023-09-30 00:00:00 DOUBLE, -- quarterly_balance_sheet 2023-09-30 00:00:00
   2023-06-30 00:00:00 DOUBLE, -- quarterly_balance_sheet 2023-06-30 00:00:00
   2023-03-31 00:00:00 DOUBLE, -- quarterly_balance_sheet 2023-03-31 00:00:00
   2022-12-31 00:00:00 DOUBLE, -- quarterly_balance_sheet 2022-12-31 00:00:00
   Symbol VARCHAR, -- quarterly_balance_sheet Symbol
)
 
TABLE quarterly_income_stmt(
   index VARCHAR, -- quarterly_income_stmt index
   2024-06-30 00:00:00 DOUBLE, -- quarterly_income_stmt 2024-06-30 00:00:00
   2024-03-31 00:00:00 DOUBLE, -- quarterly_income_stmt 2024-03-31 00:00:00
   2023-12-31 00:00:00 DOUBLE, -- quarterly_income_stmt 2023-12-31 00:00:00
   2023-09-30 00:00:00 DOUBLE, -- quarterly_income_stmt 2023-09-30 00:00:00
   2023-06-30 00:00:00 DOUBLE, -- quarterly_income_stmt 2023-06-30 00:00:00
   2023-03-31 00:00:00 DOUBLE, -- quarterly_income_stmt 2023-03-31 00:00:00
   2022-12-31 00:00:00 DOUBLE, -- quarterly_income_stmt 2022-12-31 00:00:00
   Symbol VARCHAR, -- quarterly_income_stmt Symbol
)
 
TABLE recommendations(
   index BIGINT, -- recommendations index
   period VARCHAR, -- recommendations period
   strongBuy BIGINT, -- recommendations strongBuy
   buy BIGINT, -- recommendations buy
   hold BIGINT, -- recommendations hold
   sell BIGINT, -- recommendations sell
   strongSell BIGINT, -- recommendations strongSell
   Symbol VARCHAR, -- recommendations Symbol
)
 
TABLE revenue_estimate(
   index VARCHAR, -- revenue_estimate index
   numberOfAnalysts BIGINT, -- revenue_estimate numberOfAnalysts
   avg BIGINT, -- revenue_estimate avg
   low BIGINT, -- revenue_estimate low
   high BIGINT, -- revenue_estimate high
   yearAgoRevenue BIGINT, -- revenue_estimate yearAgoRevenue
   growth DOUBLE, -- revenue_estimate growth
   Symbol VARCHAR, -- revenue_estimate Symbol
)
 
TABLE sec_filings(
   index BIGINT, -- sec_filings index
   date DATE, -- sec_filings date
   epochDate BIGINT, -- sec_filings epochDate
   type VARCHAR, -- sec_filings type
   title VARCHAR, -- sec_filings title
   edgarUrl VARCHAR, -- sec_filings edgarUrl
   exhibits MAP(VARCHAR, VARCHAR), -- sec_filings exhibits
   maxAge BIGINT, -- sec_filings maxAge
   Symbol VARCHAR, -- sec_filings Symbol
)
 
TABLE upgrades_downgrades(
   GradeDate TIMESTAMP_NS, -- upgrades_downgrades GradeDate
   Firm VARCHAR, -- upgrades_downgrades Firm
   ToGrade VARCHAR, -- upgrades_downgrades ToGrade
   FromGrade VARCHAR, -- upgrades_downgrades FromGrade
   Action VARCHAR, -- upgrades_downgrades Action
   Symbol VARCHAR, -- upgrades_downgrades Symbol
)
'''

