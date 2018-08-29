"""
Write a program to
1. load the given dataset using pandas
2. create a column called "change"
3. Values in this column should be the difference between "Open" and "Close"

Format of the dataset
Date, Open, High, Low, Close, Volume, Adj Close
7/14/2014, 202, 216, 199.15, 212.05, 3014200, 212.05
"""
import pandas as pa
import matplotlib.pyplot as plt
#Reading the CSV file into a dataframe
df = pa.read_csv("ARVIND.NS.csv")
df['change'] = df['Open'] - df['Close']
print("Describe: ", df.describe())

"""
Both 2 and 3 are given here
"""


df = pa.read_csv("ARVIND.NS.csv")
adjColumnSeries = df[ ["Date","Adj Close"] ]
df = pa.DataFrame(adjColumnSeries)
df['MA'] = df["Adj Close"].rolling(window=10).mean()
df2 = df.tail(10)
print(df)

df = df.head(50)


plt.plot(df['Date'], df['Adj Close'], color = 'green',label='ARVIND' )
plt.plot(df['Date'], df['MA'], color = 'blue', label='mavg' )
plt.show()