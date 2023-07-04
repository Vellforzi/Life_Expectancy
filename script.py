from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# load data
df = pd.read_csv("all_data.csv")
# print(df.head())
# print(df.shape)
print(f'-' * 200)

"""let's do some explore of data"""

# what countries do we have?
print(df.Country.unique())
print(f'-' * 200)

# which years are represented in the data?
print(df.Year.unique())
print(f'-' * 200)

# let's clean a column name
df = df.rename({"Life expectancy at birth (years)": "LEABY"}, axis="columns")
print(df.head())
print(f'-' * 200)

# plot histogram of GDP
plt.figure(figsize=(8, 6))
sns.histplot(df.GDP)
plt.xlabel("GDP in Trillions of U.S. Dollars")
# plt.show()
# Very right skewed where most of the values are on the left-hand side.
# This type of distribution could be described as a power law distribution

# plot histogram of LEABY
plt.figure(figsize=(8, 6))
sns.histplot(df.LEABY)
plt.xlabel("Life expectancy at birth (years)")
# plt.show()
# Very left skewed where most of the values are on the right-hand side.
# This is almost the opposite of what was observed in the GDP column.
# A further look might also identify different modes or smaller groupings of distributions within the range.

# Let's find the average LEABY and GDP by country.
df_Means = df.drop('Year', axis=1).groupby('Country').mean().reset_index()
print(df_Means)
print(f'-' * 200)

# let's plot bar plots to show the mean values for LEABY variable
plt.figure(figsize=(8, 6))
sns.barplot(x="LEABY", y="Country", data=df_Means)
plt.xlabel("Life expectancy at birth (years)")
# plt.show()
# All of the countries except for Zimbabwe have values in the mid-to-high 70s. That's why (probably) LEABY distribution
# is skewed.

# let's plot bar plots to show the mean values for GDP variable
plt.figure(figsize=(8, 6))
sns.barplot(x="GDP", y="Country", data=df_Means)
plt.xlabel("GDP in Trillions of U.S. Dollars")
# plt.show()
# US has a much higher value compared to the rest of the countries. Zimbabwe is not even visible. Chile is just barely
# seen. China, Germany and Mexico seem to be relatively close.

# We can have a look at distribution and its shape using violin plots for each country.
# fig, axes = plt.subplots(1, 2, sharey=True, figsize=(15, 5))
# axes[0] = sns.violinplot(ax=axes[0], x=df.GDP, y=df.Country)
# axes[0].set_xlabel("GDP in Trillions of U.S. Dollars")
# axes[1] = sns.violinplot(ax=axes[1], x=df.LEABY, y=df.Country)
# axes[1].set_xlabel("Life expectancy at birth (years)")
# plt.show()
# (GDP) China and the US have a relatively wide range, where Zimbabwe, Chile, and Mexico have shorter ranges.
# (LEABY) Many of the countries have shorter ranges except for Zimbabwe which has a range spanning from the high 30s to the high 60s.

# Now, let's make observationg of the same information more clearly by using swarm plot.
# fig, axes = plt.subplots(1, 2, sharey=True, figsize=(15, 5))
# axes[0] = sns.swarmplot(ax=axes[0], x=df.GDP, y=df.Country, size=2)
# axes[0].set_xlabel("GDP in Trillions of U.S. Dollars")
# axes[1] = sns.swarmplot(ax=axes[1], x=df.LEABY, y=df.Country, size=2)
# axes[1].set_xlabel("Life expectancy at birth (years)")
# plt.show()

# communicate violin and swarm plots
fig, axes = plt.subplots(1, 2, sharey=True, figsize=(15, 5))
axes[0] = sns.violinplot(ax=axes[0], x=df.GDP, y=df.Country, color="black")
axes[0] = sns.swarmplot(ax=axes[0], x=df.GDP, y=df.Country)
axes[0].set_xlabel("GDP in Trillions of U.S. Dollars")
axes[1] = sns.violinplot(ax=axes[1], x=df.LEABY, y=df.Country, color="black")
axes[1] = sns.swarmplot(ax=axes[1], x=df.LEABY, y=df.Country)
axes[1].set_xlabel("Life expectancy at birth (years)")
# plt.show()

# GDP and LEABY over the years through line charts
plt.figure(figsize=(8, 6))
sns.lineplot(x=df.Year, y=df.GDP, hue=df.Country)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.ylabel("GDP in Trillions of U.S. Dollars")
# plt.show()
# US and China have seen substantial gains between 2000-2015
# The rest of the countries did not see increases in this magnitude.

# But I want to separate each country and place them on a different faceted plots which makes it easier to compare
# the shape of their GDP over the years without the same scale.
graphGDP = sns.FacetGrid(df, col="Country", col_wrap=3, hue="Country", sharey=False)
graphGDP = (graphGDP.map(sns.lineplot, "Year", "GDP").add_legend()
            .set_axis_labels("Year", "GDP in Trillions of U.S. Dollars"))
# plt.show()

# OK, now is Life Expectancy
plt.figure(figsize=(8, 6))
sns.lineplot(x=df.Year, y=df.LEABY, hue=df.Country)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.ylabel("Life expectancy at birth (years)")
# plt.show()
# Zimbabwe has seen the greatest increase after a bit of a dip around 2004 and rest of all countries
# has been increasing their life expectancy.

# Separate each country again.
graphLEABY = sns.FacetGrid(df, col="Country", col_wrap=3, hue="Country", sharey=False)
graphLEABY = (graphLEABY.map(sns.lineplot, "Year", "LEABY").add_legend()
              .set_axis_labels("Year", "Life expectancy at birth (years)"))
plt.show()
# Now life expectancy seems more clear.

