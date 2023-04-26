# Gujarat_2022_Election
## Anomaly assesment of 2022 Gujarat results- BJP vote share increase by 3% but seat share increase by 30%

### Gujarat-Demographic Voting pattern and the help of AAP to the BJP in ensuring the defeat of the Congress Party

Gujarat, a state where PM Narendra Modi served as Chief Minister for over 12 years, holds immense political significance in India. The Legislative Assembly elections in Gujarat were held in the first week of December 2022. The Bharatiya Janata Party (BJP) made history by securing 52.50% of votes and winning 156 out of 182 seats, the highest number of seats ever won by any party in Gujarat. In contrast, the opposition Indian National Congress secured just 28.28% of votes and won only 17 seats, the lowest in Gujarat's history.

### Analysis
To understand this unprecedented victory, we need to compare it with the results of the previous elections held in 2017. In 2017, the BJP secured 49.1% votes and won only 99 seats, while the Indian National Congress and its alliance won 81 seats with 41.4% votes. With just 3.45% additional votes in 2022, the BJP won 57 extra seats, which is 31.32% of the total seats.

This project aims to explain this anomaly by analyzing voters' preferences based on demography.

### Libraries
We used publicly available data from the Trivedi Centre for Political Data at Ashoka University and demography data of Gujarat from chanakyya.com. The data is available in CSV files in the project folder. We used NumPy, pandas, matplotlib, and sklearn libraries for data analysis.

### Code
Our code consists of four functions other than the main function. We prompt the user to enter the year of elections between 2017 and 2022 and to select one of the four demographic features: “URBAN”, “RURAL”, “SC”, and “ST”. One of these features would be the “basis” of regression analysis.

The function year_party_basis(year, basis) merges the two CSV files on constituency number using pandas, then selects the column to be used based on the user's feature selection. It filters the rows based on the year prompted by the user and returns the data frame PARTY_BASIS_YEAR with three columns: party, vote share percentage, and the selected demographic feature.

The three other functions are based on the three parties. They filter for their respective parties, train, test, and conduct linear regression analysis using the ordinary least square (OLS) method through sklearn. The Pearson coefficient r and p-value are returned to the main function under these three functions. We used 80% of the data for training and 20% for testing.

The main function prints the summary statistics and scatter chart with linear regression for all three parties for comparative analysis. The chart provides details such as the total average votes polled by each political party, the values of the r coefficient, and the p-values.

These charts indicate a correlation between the demographic feature selected and the political parties.

### Assesment
Our analysis reveals a clear correlation between BJP's vote share and demography, especially in rural areas. The charts clearly depict the decrease in BJP vote share as rural votes in an assembly constituency increase and vice-versa. Similarly, SC votes increase also favor the Congress Party.

The anomaly in terms of a disproportionate jump in the number of seats compared to the increase in the percentage of votes can be attributed to the presence of the Aam Aadmi Party (AAP) in the 2022 elections. In rural areas, the impact of AAP's support for the BJP is evident in 2022 compared to 2017.

In the 2022 scatter plot of Assembly Constituency-wise rural votes vs Party Votes, it is observed that there was a favorable impact of AAP on the BJP. This suggests that the presence of AAP in the 2022 elections had a significant role in BJP's win.
![Image description](https://github.com/makenajay/Gujarat_2022_Election/blob/master/Fig%202022%20RURAL.png)

On analyzing the 2017 scatter plot, it is evident that the Indian National Congress (INC) had a higher chance of winning in Assembly Constituencies (AC) with rural votes above 78% as compared to BJP. However, this "cross-over" is not visible in the 2022 chart, which could be attributed to the help provided by the AAP party to BJP.  
![Image description](https://github.com/makenajay/Gujarat_2022_Election/blob/master/Fig%202017%20RURAL.png)

Therefore, it can be assumed that the AAP party played a crucial role in the BJP's victory in the 2022 Gujarat elections. Despite having just a 3.45% increase in absolute vote share, the BJP managed to increase its seat share by ten times (i.e., 31.2%), which is an anomaly that can be explained by the AAP's assistance.
