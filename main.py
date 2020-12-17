import pandas as pd

df = pd.read_excel('KN-4.xlsx')
print(df)

print(df.shape, df.columns)
print(df.loc[6])

df.fillna(0, inplace=True)
print(df)

df.loc[df['Lab1'] == '+', 'Lab1'] = 2
df.loc[df['Lab1'] == '/', 'Lab1'] = 1
print(df.head())

tmp = df['Lab7'].str.split('/')
df['L7'] = tmp.apply(lambda x: x[0]).astype(int)
print(df)

print(df[['Lab1', 'Lab2', 'L7', 'Test']].sum())
print(df[['Lab1', 'Lab2', 'L7', 'Test']].sum(axis=1))
df = df.rename(columns={'L7': 'Lab7'})
print(df.head())

df['Sum'] = df[['Lab1', 'Lab2', 'Lab7', 'Test']].sum(axis=1)
print(df.head())

print('Найбільша сума:', df['Sum'].max())

print('Порядковий номер студента, у якого найбльша сума:', df['Sum'].argmax())

print('Найбільшу суму має', df['Student'].loc[df['Sum'].argmax()])

print('Сумарний нуль мають: \n', df.where(df['Sum'] == 0).dropna())

print('Сумарний бал більше 15 у: \n', df.where(df['Sum'] > 15.).dropna())

print(len(df.where(df['Sum'] > 15.).dropna()), 'Студентів мають сумарний бал більше 15 \n')

df.sort_values(by=['Sum'],inplace=True)
print(df)

print('Студенти, які здали 1 лабораторну: \n', df[df['Lab1'].isin([2,1])])

df['Lab4']=2
print(df)

print(df[['Student','Sum']])
df['Dopusk']=df['Sum'].apply(lambda x: "dopusk" if x>15 else "no")
print('Студенти у яких є допуск: \n', df.where(df['Dopusk'] == 'dopusk').dropna())
