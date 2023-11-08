import pandas as pd

# Read in a data file
df = pd.read_csv('data/raw/shopping_behavior_updated.csv')

# calculate summary statistics on the Purchase Amount column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?
# s1 = df['Purchase Amount (USD)'].mean()
# s2 = df['Purchase Amount (USD)'].median()
# s3 = df['Purchase Amount (USD)'].max()
# s4 = df['Purchase Amount (USD)'].min()
# s5 = df['Purchase Amount (USD)'].std()

# Describe displays all the summary statistics
df['Purchase Amount (USDD)'].describe()

# calculate summary statistics on the Age column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?
df['Age'].describe()

# summary statistics
# TODO: is there another function we can use to calculate metrics on groups?

df.groupby('Season').describe()

# keep all columns except for "Customer", & "Discount Applied"
# TODO: is there a more efficient way to exclude columns in your dataset?

df = df.drop(['Customer', 'Discount Applied'], axis=1)

# figure out most popular payment method in NY
# TODO: is there anyway we could modularize this behavior to apply to all
# TODO: possible states? (OR possibly use a pandas function that does this
# TODO: for us already?)

df['Payment Method'].nunique()

# Write this updated data out to csv file
df.to_csv('data/processed/cleaned_data.csv', index=False)
