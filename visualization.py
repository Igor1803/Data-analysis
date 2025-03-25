import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.figure(figsize=(10, 5))
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title("Гистограмма нормального распределения")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.grid(True)
plt.show()

# Генерация двух наборов случайных данных для диаграммы рассеяния
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 5))
plt.scatter(x, y, color='red', alpha=0.5, edgecolors='black')
plt.title("Диаграмма рассеяния случайных данных")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

# Создание и вывод массива из 5 случайных чисел
random_array = np.random.rand(5)
print("Массив из 5 случайных чисел:", random_array)