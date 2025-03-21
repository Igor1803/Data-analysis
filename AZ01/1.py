import pandas as pd
df = pd.read_csv('Mobiles Dataset (2025) .csv', encoding='latin-1')


#print(df)
#print(df.describe())
#print(df.info())
#print(df.head())
#print(df.tail())
#print(df['Company Name'])

#print(df.loc[250])
print(df[df['Company Name'] == 'Apple'])
