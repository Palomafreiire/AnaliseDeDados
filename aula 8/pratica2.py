import pandas as pd

data = {
    'a': [10, 20, 30],
    'b': [5, 15, 25],
    'c': [2, 4, 6]
}

df = pd.DataFrame(data)

#sum()
# é a soma dos elementos da coluna
df = sum('a')
print(df)
