# PyIEX Changelog

### v0.4.0 September 23, 2018
+ Added surprisePercent to pyiex_earnings
+ Added ttmEPS to pyiex_earnings
+ Renamed surpriseEPS to surpriseDollar (pyiex_earnings)
+ Created pyiex_keystats
+ Added beta
+ Added shortInterest
+ Added shortDate
+ Added dividentRate
+ Added dividendYield
+ Added exDividentRate
+ Added sharesOutstanding
+ Added float
+ Added returnOnEquity
+ Added ebitda
+ Added revenue
+ Added grossProfit
+ Added cash
+ Added debt
+ Added revenuePerShare
+ Added revenuePerEmployee
+ Added peRatioHigh
+ Added peRatioLow
+ Added returnOnAssets
+ Added returnOnCapital
+ Added profitMargin
+ Added priceToSales
+ Added priceToBook
+ Added day200MovingAvg
+ Added day50MovingAvg
+ Added institutionPercent
+ Added insiderPercent
+ Added shortRatio
+ Added year5ChangePercent
+ Added year2ChangePercent
+ Added year1ChangePercent
+ Added ytdChangePercent
+ Added month6ChangePercent
+ Added month3ChangePercent
+ Added month1ChangePercent
+ Added day5ChangePercent

### v0.3.1 September 23, 2018
+ Fixed issue #2 - sectorPerformance now returns a precise dict with
the following key:pair {sector:performance}

### v0.3.0 September 23, 2018
+ Created pyiex_quote to access /stock/{symbol}/quote information
+ Added calculationPrice
+ Added openPrice
+ Added openTime
+ Added closePrice
+ Added closeTime
+ Added highPrice
+ Added lowPrice
+ Added latestPrice
+ Added latestSource
+ Added latestTime
+ Added latestUpdate
+ Added latestVolume
+ Added iexRealtimePrice
+ Added iexRealtimeSize
+ Added iexLastUpdated
+ Added delayedPrice
+ Added delayedPriceTime
+ Added extPrice
+ Added extChange
+ Added extChangePercent
+ Added extPriceTime
+ Added changePrice
+ Added changePercent
+ Added iexMarketPercent
+ Added iexVolume
+ Added avgTotalVolume
+ Added iexBidPrice
+ Added iexBidSize
+ Added iexAskPrice
+ Added iexAskSize
+ Added marketCap
+ Added peRatio
+ Added yearHigh
+ Added yearLow
+ Added ytdChange


### v0.2.1 September 23, 2018
+ Removed unnessecary repeats of the actualEPS function in pyiex_earnings

### v0.2.0: September 22, 2018
+ Created pyiex_config.py to store global config data & commands
+ Separated "Company" API calls into its own module (pyiex_company)
+ Separated miscellaneous API calls into its own module (pyiex_misc)

The objective of separating different API calls into independent modules
is to increase organization and to allow the end-user to import only
the modules they need for a specific application. In addition, I chose to
import global variables & config settings from an outside file so if something
were to need updating, it would only need to be changed in one place.

+ Added a dedicated changelog file
+ Removed changelog from readme
+ Formatted my code to more closely adhere to convention
+ Changed all instances of variable "ticker" to "symbol"
+ Created pyiex_earnings
+ Added pyiex_earnings.actualEPS(symbol, quarter)

Input a symbol and optionally a number for the quarter you'd like actual EPS
for. Quarter accepts values 0 thru 3, with 0 being the most recent quarter
published. Values greater than 3 automatically change to 3. Returns a
dictionary of fiscalQuarter:actualEPS. Fiscal quarter is returned as "Q# 20##"

+ Created a generic function to access earnings data.
+ Specific earnings functions call the generic earnings function.
+ Added pyiex_earnings.consensusEPS(symbol, quarter)
+ Added pyiex_earnings.estimatedEPS(symbol, quarter)
+ Added pyiex_earnings.numberEstimates(symbol, quarter)
+ Added pyiex_earnings.surpriseEPS(symbol, quarter)
+ Added pyiex_earnings.reportDate(symbol, quarter)
+ Added pyiex_earnings.fiscalEnd(symbol, quarter)
+ Added pyiex_earnings.yearAgo(symbol, quarter)
+ Added pyiex_earnings.yearCP(symbol, quarter)
+ Added pyiex_earnings.estCP(symbol, quarter)


### v0.1.0: September 21, 2018
+ Finally updated the GitHub repo
+ Consolidated some lines of code
+ Added name(ticker)
+ Added exchange(ticker)
+ Added description(ticker)
+ Added industry(ticker)
+ Added website(ticker)
+ Added CEO(ticker)
+ Added type(ticker)
+ Added sector(ticker)
+ Added tags(ticker)
+ Added sectorPerformance(sector)
+ Added listTickers(sector)
