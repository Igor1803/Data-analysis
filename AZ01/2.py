import pandas as pd

# Загрузка данных
df = pd.read_csv('dz.csv')

# Удаление строк с пропусками в 'City' или 'Salary'
df_clean = df.dropna(subset=['City', 'Salary']).copy()  # Явное копирование

# Преобразование 'Salary' в число (без предупреждения)
df_clean['Salary'] = pd.to_numeric(df_clean['Salary'], errors='coerce')

# Удаление строк, где Salary не число (NaN после преобразования)
df_clean = df_clean.dropna(subset=['Salary'])

# Расчет средней зарплаты
result = df_clean.groupby('City')['Salary'].mean().reset_index()

print(result)