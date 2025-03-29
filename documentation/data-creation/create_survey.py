"""
Generate breakfast survey.

This code was created for the next project.
https://github.com/ZoltanNyaradi/Guest-Survey-Analysis-to-Improve-Hotel-Breakfast

It loads Seaborn's Diamond datasets
and transform it for a survey.
Drops 2 column.
Target will be an apropiet categorical column.
Featchers will be transformed to numerical ratings from 1 to 10.
"""

import pandas as pd
import seaborn as sns
import random

# Load dataset
df = sns.load_dataset("diamonds", cache=True)
# Delete 2 columns
df = df.drop(labels=["clarity", "color"], axis=1)

# Delet very good and premium rows
df = pd.concat([
    df[df["cut"] == "Good"],
    df[df["cut"] == "Ideal"],
    df[df["cut"] == "Fair"]
])

# Make z column product of z and target value
# Reduce correlation with a random number
# Reduce correlation of y with target and other features
for index, row in df.iterrows():
    rnd = random.uniform(7, 13)
    rnd2 = random.uniform(8, 12)
    cut = 0
    if row["cut"] == "Ideal":
        cut = 3
    elif row["cut"] == "Good":
        cut = 4
    else:
        cut = 5
    df.at[index, "z"] = row["z"] * cut * rnd
    df.at[index, "y"] = row["y"] * rnd2

# Delete outliers
for i in range(0, 3):
    for column in df.columns:
        if df[column].dtype == int or df[column].dtype == float:
            delete_rows = pd.concat([
                df[column].sort_values(ascending=False)[0:25],
                df[column].sort_values(ascending=True)[0:10]]
            )
            for row in delete_rows.index:
                df = df.drop(index=[row])

# Replace Diamond quality with guest respone
df["cut"].replace({
    "Premium": "Yes, again",
    "Fair": "Yes, again",
    "Ideal": "No",
    "Good": "Yes, next time not",
    "Very Good": "Yes, next time not"
}, inplace=True)

# Reset indexes
df = df.reset_index(drop=True)

# Turn numerical data into 1-10 score
for column in df.columns:
    if column != "cut":

        min_value = df[column].min()
        value_range = df[column].max()-min_value
        single_rate_range = value_range/10

        min_value *= 0.999
        single_rate_range *= 1.05

        row = 0

        for value in df[column]:
            rate = 0
            while value > min_value:
                value -= single_rate_range
                rate += 1

            df.at[row, column] = rate

            row += 1

# Rename cut to breakfast
df.rename(columns={"cut": "breakfast"}, inplace=True)

# Create an array with new column names
column_names = [
    "appearance",
    "service",
    "staff",
    "variety",
    "price",
    "taste",
    "hotel"
]

# Rename the columns and set int type
column_index = 0
for column_name in column_names:
    if df.columns[column_index] == "breakfast":
        column_index += 1
    df.rename(columns={
        df.columns[column_index]: column_name}, inplace=True)
    df[column_name] = df[column_name].astype(int)
    column_index += 1

# Shuffle df
df = df.sample(frac=1)
# Reindex df
df = df.reset_index(drop=True)

# Save df in a csv file
df.to_csv("BreakfastSurvey.csv", index=True)
