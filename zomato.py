import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2 - Create the data frame
dataframe = pd.read_csv(r"C:\Users\Ansh Nayan Gupta\OneDrive\Desktop\New folder (2)\Zomato data .csv")


def handleRate(value):
    value = str(value).split('/')  # Convert value to a string and split by '/'
    value = value[0]               # Take the first part before the slash
    return float(value)           # Convert it to a float and return

dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe.head)

sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type")
plt.title("Count of Each Type in 'listed_in(type)' Column")
plt.show()

grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})

# Plotting the result
result.plot(color="green", marker="o")

plt.xlabel("Type of restaurant", color="red", size=20)
plt.ylabel("Votes", color="red", size=20)

plt.show()

plt.hist(dataframe['rate'], bins=10)
plt.title("Ratings Distribution")
plt.show()


couple_data = dataframe['approx_cost(for two people)']

# Create a countplot
plt.figure(figsize=(10, 6)) # Adjust figure size for better readability
sns.countplot(x=couple_data)
plt.show()

sns.boxplot(x='online_order', y='rate', data=dataframe)

# Add title and labels for clarity
plt.title('Restaurant Rate by Online Order Availability')
plt.xlabel('Online Order Available')
plt.ylabel('Rate')

# Display the plot
plt.show()


pivot_table = dataframe.pivot_table(
    index="listed_in(type)",
    columns="online_order",
    aggfunc='size',
    fill_value=0
)

sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')

plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()