import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3],
    'B': ['foo', 'bar', 'baz'],
    'C': [0.1, 0.2, 0.3]
}
df = pd.DataFrame(data)

# Convert DataFrame to dictionary of lists
df = df.to_dict('list')

print(df)
