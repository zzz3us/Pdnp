import pandas as pd

data = pd.read_excel('courses.xlsx')
# print(data)

df = pd.DataFrame(data)
# print(type(df))

print(df[df['Fee'] > 15000])

