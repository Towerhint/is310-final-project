import pandas as pd
from jacky_chen_first_python_assignment import fin_df

# Step 1:
# Download and open the tools_dh_proceedings.csv file
# Get the next top ten tools, based on 2019 ratings

a = pd.read_csv('tools_dh_proceedings.csv').sort_values(
    '2019', ascending=False)  # Sort based on 2019 data
next_10 = a[5:15]  # Check the top 15 entries

# Step 2：
# Add functionality to calculate the total field for each new tool

fin_df = fin_df()
next_10.index = next_10['Tool']
# Reindex to tool and drop the same column
next_10 = next_10.drop('Tool', axis=1)

exten_df = pd.concat([fin_df, next_10])
sum = exten_df.sum(1)
exten_df['Sum_over_five_yrs'] = sum  # Recalculate
print("\nPrint the combined dataframe: \n", exten_df)

# Step 3:
# Figure out a way to output all the information for a tool if you input their name.

ask = input("\nWhat dh tool would you like to take a look? \n")

for index, row in exten_df.iterrows():
    if (ask.lower() == index.lower()):
        print(f"\nHere is the information of {ask} over the years:")
        print(row)

# Bonus:
# Create a way to input any year and return the top tool.

ask = str(input(
    "\nWhat year would you like to take a look? (select from 2015-2019)\n"))
print(f"\nFor {ask}, the most popular dh tool is:")
print(a.sort_values(ask, ascending=False).iloc[0][0])
