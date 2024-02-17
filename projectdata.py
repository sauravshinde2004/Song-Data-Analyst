import pandas as pd
import matplotlib.pyplot as plt

# Assuming your data is stored in a DataFrame called df
# Replace 'df' with the actual DataFrame name
df = pd.read_csv("Song.csv")

# Bar chart
df[['Sales', 'Streams', 'Downloads', 'Radio Plays']].sum().plot(kind='bar')
plt.title('Total Sales, Streams, Downloads, and Radio Plays')
plt.ylabel('Count')
plt.xlabel('Metric')
plt.show()

# Line plot
df.groupby('Year').sum().plot(kind='line')
plt.title('Trends over Years')
plt.ylabel('Count')
plt.xlabel('Year')
plt.show()

# Scatter plot
plt.scatter(df['Sales'], df['Streams'])
plt.title('Sales vs. Streams')
plt.xlabel('Sales')
plt.ylabel('Streams')
plt.show()

# Histogram
df['Rating'].plot(kind='hist')
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Box plot
df[['Sales', 'Streams', 'Downloads', 'Radio Plays']].plot(kind='box')
plt.title('Distribution of Sales, Streams, Downloads, and Radio Plays')
plt.ylabel('Count')
plt.show()
