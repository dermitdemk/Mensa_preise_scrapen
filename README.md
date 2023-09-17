# Mensa_preise_scrapen
this is the code for a scraper of the Mensa of the uni Erfurt


This automatically pulls the prices of the Mensa meals of this day. This is built to track the Mensa price and how many meals are vegan.
The data is on year of tracking the prices, but was tracked by an old version of the scraper and becaus of changes in the mensa webseit has false value if the meal is vegan or not. The Mensa change the method of displaying vegan meals which the scraper dident noticed.
The new version now also writs the data in an sql database instead of csv file but the option to writ it in a file is still there.

# Results
![menas_data](https://github.com/dermitdemk/Mensa_preise_scrapen/assets/60017842/e716032a-3efb-4b56-ad50-4a0a4d7e3647)
Thies are the daily prices for the students, is the minimum, average and maximum price. In march the mense hand an almost daily "salattheke" which was charged per 100g. Thats why the prices starting in march are so low.


visualization of the data was done thru grafan
