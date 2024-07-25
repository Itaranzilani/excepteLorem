import pandas as pd

# Example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Assigning None to a new column
df.loc[:, 'CommentSentPos'] = None

print(df)
