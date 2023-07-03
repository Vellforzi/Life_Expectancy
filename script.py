from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# load data
df = pd.read_csv("all_data.csv")
# print(df.head())
# print(df.shape)
print(f'-' * 200)

# what countries do we have?
print(df.Country.unique())
print(f'-' * 200)

# which years are represented in the data?
print(df.Year.unique())
print(f'-' * 200)

# let's clean a column name
df = df.rename({"Life expectancy at birth (years)": "LEABY"}, axis="columns")
print(df.head())


plt.figure(figsize=(8, 6))
sns.histplot(df.GDP)
plt.xlabel("GDP in Trillions of U.S. Dollars")
plt.show()
