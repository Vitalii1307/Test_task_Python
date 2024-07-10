import pandas as pd

df = pd.read_csv('test-1.csv')

df = df.fillna(value=pd.NA)

# Grouping by "Text" column
grouped = df.groupby('Text', dropna=False)

for name, group in grouped:
    print(f"Group: {name}")
    print(group)
    print()
