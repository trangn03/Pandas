# Learning Pandas Step by Step (with Titanic data)

Use the attached `titanic.csv` for every exercise below. Start every script with:

```python
import pandas as pd
df = pd.read_csv('titanic.csv')
```

Work through the steps in order. Each step: a short explanation, example code, then exercises.
**Don't peek at the solutions until you've tried each exercise yourself.** Solutions are at the bottom of each step.

---

## Step 1: Loading & Inspecting Data

The first thing you always do with a new dataset is look at it before touching anything.

```python
df = pd.read_csv('titanic.csv')
df.head()          # first 5 rows
df.shape            # (rows, columns)
df.columns          # list of column names
df.dtypes           # data type of each column
df.info()           # combo of the above + memory usage
df.describe()       # stats (mean, min, max, etc) for numeric columns
```

### Exercises — Step 1
1. Load `titanic.csv` and print how many rows and columns it has.
2. Print the list of all column names.
3. Print the data type of the `Fare` column.
4. Use `.describe()` on just the `Age` column (hint: `df['Age'].describe()`). What's the average age?
5. Print the last 3 rows of the dataset (hint: look up `.tail()`).

<details>
<summary>Solutions — Step 1</summary>

```python
# 1
df = pd.read_csv('titanic.csv')
print(df.shape)

# 2
print(df.columns.tolist())

# 3
print(df['Fare'].dtype)

# 4
print(df['Age'].describe())

# 5
print(df.tail(3))
```
</details>

---

## Step 2: Selecting Data

Two ways to grab data: by **column name** and by **position/label** using `.loc` / `.iloc`.

```python
df['Age']                       # one column (returns a Series)
df[['Age', 'Sex']]               # multiple columns (returns a DataFrame)

df.loc[0]                        # row with label/index 0
df.loc[0, 'Age']                 # specific cell
df.loc[0:4, ['Age','Sex']]       # rows 0-4, specific columns

df.iloc[0]                       # first row by POSITION (same as loc here)
df.iloc[0:5, 0:3]                # first 5 rows, first 3 columns, by position
```

`.loc` uses labels (column names, index values). `.iloc` uses pure integer position. For this dataset they behave the same on rows since the index is just 0,1,2..., but the distinction matters once you filter or sort data (the labels stay attached to their original row, position doesn't).

### Exercises — Step 2
1. Select just the `Name`-equivalent identifying column here, `PassengerId`, and `Fare` columns together.
2. Print row index 10 in full.
3. Print the `Embarked` value for passenger at row index 5.
4. Print rows 100 to 105 (inclusive), showing only `Pclass` and `Survived`.
5. Print the first 3 rows using `.iloc`.

<details>
<summary>Solutions — Step 2</summary>

```python
# 1
print(df[['PassengerId', 'Fare']])

# 2
print(df.loc[10])

# 3
print(df.loc[5, 'Embarked'])

# 4
print(df.loc[100:105, ['Pclass','Survived']])

# 5
print(df.iloc[0:3])
```
</details>

---

## Step 3: Filtering Rows

This is the pattern you'll use constantly: `df[condition]`.

```python
df[df['Age'] > 30]                            # one condition
df[(df['Age'] > 30) & (df['Sex'] == 'male')]   # AND — use &, and wrap each condition in ( )
df[(df['Pclass'] == 1) | (df['Pclass'] == 2)]  # OR — use |
df[df['Embarked'].isin(['S', 'C'])]            # matches any value in a list
df[~(df['Survived'] == 1)]                     # ~ means NOT
```

### Exercises — Step 3
1. Filter passengers who are female AND under age 18.
2. Filter passengers who paid a `Fare` over 100.
3. Filter passengers who were in `Pclass` 1 or 2 (use `.isin`).
4. Filter passengers who did NOT survive.
5. How many passengers embarked from 'Q'? (filter, then use `.shape[0]` or `len()`)

<details>
<summary>Solutions — Step 3</summary>

```python
# 1
print(df[(df['Sex'] == 'female') & (df['Age'] < 18)])

# 2
print(df[df['Fare'] > 100])

# 3
print(df[df['Pclass'].isin([1, 2])])

# 4
print(df[df['Survived'] == 0])

# 5
print(len(df[df['Embarked'] == 'Q']))
```
</details>

---

## Step 4: Cleaning Data

Real data always has gaps or wrong formats. Two core tools: `.isnull()` and `.fillna()`.

```python
df.isnull().sum()                  # count missing values per column
df['Age'].fillna(df['Age'].median(), inplace=True)  # fill missing with median
df.dropna()                        # drop any row with a missing value
df.dropna(subset=['Age'])          # drop rows only if Age is missing
df.duplicated().sum()              # count exact duplicate rows
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})  # recode text to numbers
```

### Exercises — Step 4
1. Print how many missing values are in each column.
2. Fill missing `Age` values with the **mean** age instead of median.
3. Create a new column `Sex_num` that's 1 for female, 0 for male (don't overwrite `Sex`).
4. Count how many duplicate rows exist in the dataset.
5. Drop all rows where `Age` is missing and print the new shape.

<details>
<summary>Solutions — Step 4</summary>

```python
# 1
print(df.isnull().sum())

# 2
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 3
df['Sex_num'] = df['Sex'].map({'male': 0, 'female': 1})

# 4
print(df.duplicated().sum())

# 5
df_clean = df.dropna(subset=['Age'])
print(df_clean.shape)
```
</details>

---

## Step 5: Aggregating & Grouping

`groupby` answers "what's the average/count/etc of X, broken down by Y?" — the single most useful tool for finding patterns.

```python
df['Survived'].mean()                          # overall rate
df.groupby('Sex')['Survived'].mean()           # rate per sex
df.groupby(['Pclass','Sex'])['Survived'].mean()  # rate per class AND sex
df.groupby('Pclass')['Fare'].agg(['mean','min','max'])  # multiple stats at once
df['Pclass'].value_counts()                    # count of each category
```

### Exercises — Step 5
1. What's the survival rate grouped by `Embarked`?
2. What's the average `Fare` grouped by `Pclass`?
3. Group by `Sex` and `Pclass` together, and show the average `Age`.
4. Using `.agg()`, show the mean, min, and max `Age` per `Pclass`.
5. Which `Embarked` value has the most passengers? (`.value_counts()`)

<details>
<summary>Solutions — Step 5</summary>

```python
# 1
print(df.groupby('Embarked')['Survived'].mean())

# 2
print(df.groupby('Pclass')['Fare'].mean())

# 3
print(df.groupby(['Sex','Pclass'])['Age'].mean())

# 4
print(df.groupby('Pclass')['Age'].agg(['mean','min','max']))

# 5
print(df['Embarked'].value_counts())
```
</details>

---

## Step 6: Transforming Columns

Turning categories into numbers, and creating new columns from existing ones.

```python
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1     # new column from math on others
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)  # new column from a condition
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)  # one category -> multiple 0/1 columns
df.sort_values('Fare', ascending=False)              # sort rows by a column
df.rename(columns={'Pclass': 'PassengerClass'})      # rename a column
```

### Exercises — Step 6
1. Create a `FamilySize` column (SibSp + Parch + 1).
2. Create an `IsChild` column that's 1 if `Age` < 12, else 0.
3. Sort the dataset by `Age`, oldest first, and print the top 5.
4. One-hot encode the `Embarked` column with `pd.get_dummies`, and print the new column names.
5. Rename `Fare` to `TicketPrice`.

<details>
<summary>Solutions — Step 6</summary>

```python
# 1
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# 2
df['IsChild'] = (df['Age'] < 12).astype(int)

# 3
print(df.sort_values('Age', ascending=False).head())

# 4
df_dummies = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
print(df_dummies.columns.tolist())

# 5
df = df.rename(columns={'Fare': 'TicketPrice'})
```
</details>

---

## Step 7: Working with Strings

Pandas has powerful built-in text processing tools accessed via `.str`.

```python
df['Name'].str.lower()                           # lowercase all text
df['Name'].str.contains('Mr\.')                  # boolean mask: does it contain 'Mr.'?
df['Name'].str.split(',', expand=True)           # split string into multiple columns
```

### Exercises — Step 7
1. Filter the dataset to show only passengers whose name contains "Miss.".
2. Create a new column `LastName` by splitting `Name` on `,` and keeping the first part.

<details>
<summary>Solutions — Step 7</summary>

```python
# 1
print(df[df['Name'].str.contains('Miss.')])

# 2
df['LastName'] = df['Name'].str.split(',').str[0]
```
</details>

---

## Step 8: Applying Custom Functions

Sometimes built-in methods aren't enough, and you need to run your own custom logic on a column. `apply()` lets you apply a function to every value in a column.

```python
# Create a simple function
def categorize_fare(fare):
    if pd.isna(fare): return 'Unknown'
    if fare < 10: return 'Cheap'
    elif fare < 50: return 'Medium'
    else: return 'Expensive'

# Apply the function to a column
df['FareCategory'] = df['Fare'].apply(categorize_fare)

# Apply using a lambda (one-liner anonymous function)
df['FareRounded'] = df['Fare'].apply(lambda x: round(x) if pd.notna(x) else x)
```

### Exercises — Step 8
1. Write a function that takes an age and returns 'Adult' if age >= 18, and 'Minor' if age < 18.
2. Use `.apply()` to create a new column `AgeGroup` using your function.

<details>
<summary>Solutions — Step 8</summary>

```python
# 1
def get_age_group(age):
    if pd.isna(age): return 'Unknown'
    if age >= 18: return 'Adult'
    return 'Minor'

# 2
df['AgeGroup'] = df['Age'].apply(get_age_group)
```
</details>

---

## Step 9: Saving Data

Once you've cleaned and transformed your data, you'll want to save it so you don't have to repeat the process.

```python
# Save to CSV (index=False prevents Pandas from saving the row numbers as a new column)
df.to_csv('titanic_cleaned.csv', index=False)

# Save to Excel
df.to_excel('titanic_cleaned.xlsx', index=False)
```

### Exercises — Step 9
1. Save your current DataFrame to a new file called `my_titanic_analysis.csv` without saving the index.

<details>
<summary>Solutions — Step 9</summary>

```python
# 1
df.to_csv('my_titanic_analysis.csv', index=False)
```
</details>

---

## Final Challenge — Put it all together

Using only what's above:

1. Load the data fresh.
2. Fill missing `Age` with the median.
3. Create a `FamilySize` column.
4. Filter to only passengers with `FamilySize` > 3.
5. Group that filtered data by `Pclass` and show the average `Survived` rate.
6. In one sentence, describe what the result tells you about large families and class.

This mirrors exactly what real data cleaning looks like before feeding data into a model — which is exactly what we'll go back to next in Project 1.
