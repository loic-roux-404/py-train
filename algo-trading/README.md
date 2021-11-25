# Kedge Business School

## Fundamentals of Computer Programming

```
Note: For Question 1, 2 and 3, please hand in all source codes and the result.
```
## ( 4 pts) Q1: Basic IO operation

A valid email contains the @ symbol in a string, with user’s name and domain name.

( 2 pts) (A). Import email.txt and implement a function checking to recognize all invalid email addresses
and export them to invalid.txt.

( 2 pts) (B). Continue with (A). When you register an account, the account should have at least 6 characters
in length. Therefore, a valid email address should satisfy two requirements (1) the user's name is longer
than or equal to 6 and (2) with a symbol @. Please implement a refined email checker to recognize all
invalid email addresses and export them to a refined_invalid.txt.

## ( 6 pts) Q2: Descriptive analysis of data is essential for business analytics

Bordeaux Metropole is composed of City of Bordeaux and its neighboring towns. Work on the data set
Bordeaux_Metropole.csv and postalcode.txt.

Bordeaux_Metropole.csv contains the following columns:

```
o date_mutation: date of transaction
o valeur_fonciere: property value
o code_postal: postal code
o section: section
o type_local: type of property (apartment or house)
o surface_relle_bati: size of property (in m^2 )
o nombre_pieces_principales: number of rooms
o surface_terrain: size of land (in m^2 )
```
In postalcode.txt, there are two columns, i.e., name of city and its postal code.

( 3 pts) (A) Please write a Python code to read all postal codes and save them in a list.

( 3 pts) (B) Continue with (A). Please export descriptive statistics of the price and size of apartments
(i.e., mean, std, min, max, median, Q25 and Q75) for every postal code (that you read in A) as a CSV

## file (e.g., 33110.csv, 33440.csv and so on) in Bordeaux Metropole.

## ( 10 pts) Q3: Data analysis and Visualization

Work on TESLA daily price data, i.e., TSLA_2017_2020.xlsx, to apply a momentum as we have done in
the lecture.

( 2 pts) (A) For long strategy, we choose simple-moving average (SMA) pairs (i.e., 5 - day SMA and 10 - day
SMA) to analyze the trend in the stock market. Please compute 5 - day SMA and 10 - day SMA of the close
price sequence, plot, and labels 5 - day SMA and 10 - day SMA with blue and red solid curves, respectively.
Please attach the figure in the report.


( 2 pts) (B) If golden cross (i.e., the buying signal) occurs when 5 - day SMA crosses over 10 - day SMA and
the death cross (i.e., the selling signal) occurs when 10 - day SMA crosses over 5 - day SMA. Please write a
python code to simulate the revenue of this trading strategy given your trade is executed at the next day’s
open price. Please report the total number of transactions and your average revenue that you have traded
to Q 3 _b.xlsx.

( 2 pts) (C) Continue with (B) Please visualize the strategy over 3 years in a graph, where the black solid
line is used for the open price sequence with a blue pentagon for golden cross (buy) and red pentagon for
death cross (sell), respectively. Please attach the figure in the report.

( 2 pts) (D) Compare the simple-moving average (SMA) pairs you worked in (B), i.e., 5 - day SMA and 10 -
day SMA with another simple-moving average (SMA) pairs of 5 - day SMA and 20 - day SMA. Please
indicate which one is the better strategy in average revenue. Please provide the evidence in your report
for these two trading pairs.

( 2 pts) (E) Continue with (B) Write a python to close your position at the end of the trading period, that is,
sell all your stocks at the best price for closing your position. Please export your accumulated revenue to
Q3_e.xlsx.


