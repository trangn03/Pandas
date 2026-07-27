import pandas as pd
df = pd.read_csv('data/titanic.csv')

# First 5 rows
print(df.head())
# (Rows, Columns)
print(df.shape)
# List of columns name
print(df.columns)
# Data type of each column
print(df.dtypes)
# combo of the above + memory usage
print(df.info())
# Stats (mean, min, max, etc) for numeric columns
print(df.describe())

# Exercise 1
# 1. Load titanic.csv and print how many rows and columns it has.
# 2. Print the list of all column names.
print(df.columns.tolist())
# 3. Print the data type of the Fare column.
print(df['Fare'].dtype)
# 4. Use .describe() on just the Age column (hint: df['Age'].describe()). What's the average age?
print(df['Age'].describe())
# 5. Print the last 3 rows of the dataset (hint: look up .tail()).
print(df.tail(3))

# Exercise 2
# 1. Select just the Name-equivalent identifying column here, PassengerId, and Fare columns together.
print(df[['PassengerId', 'Fare']])
# 2. Print row index 10 in full.
print(df.loc[10])
# 3. Print the Embarked value for passenger at row index 5.
print(df.loc[5,'Embarked'])
# 4. Print rows 100 to 105 (inclusive), showing only Pclass and Survived.

# 5. Print the first 3 rows using .iloc.

# Exercise 3
# 1. Filter passengers who are female AND under age 18.
# 2. Filter passengers who paid a Fare over 100.
# 3. Filter passengers who were in Pclass 1 or 2 (use .isin).
# 4. Filter passengers who did NOT survive.
# 5. How many passengers embarked from 'Q'? (filter, then use .shape[0] or len())

# Exercise 4
# 1. Print how many missing values are in each column.
# 2. Fill missing Age values with the mean age instead of median.
# 3. Create a new column Sex_num that's 1 for female, 0 for male (don't overwrite Sex).
# 4. Count how many duplicate rows exist in the dataset.
# 5. Drop all rows where Age is missing and print the new shape.

# Exercise 5: Aggregating & Grouping
# 1. What's the survival rate grouped by Embarked?
# 2. What's the average Fare grouped by Pclass?
# 3. Group by Sex and Pclass together, and show the average Age.
# 4. Using .agg(), show the mean, min, and max Age per Pclass.
# 5. Which Embarked value has the most passengers? (.value_counts())

# Exercise 6: Transforming Columns
# 1. Create a FamilySize column (SibSp + Parch + 1).
# 2. Create an IsChild column that's 1 if Age < 12, else 0.
# 3. Sort the dataset by Age, oldest first, and print the top 5.
# 4. One-hot encode the Embarked column with pd.get_dummies, and print the new column names.
# 5. Rename Fare to TicketPrice.