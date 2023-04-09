"""
Рост взрослого населения города X имеет нормальное распределение.
Причем, средний рост равен 174 см, а среднее квадратичное отклонение
равно 8 см. Какова вероятность того, что случайным образом выбранный взрослый
человек имеет рост:
а). больше 182 см
б). больше 190 см
в). от 166 см до 190 см
г). от 166 см до 182 см
д). от 158 см до 190 см
е). не выше 150 см или не ниже 190 см
ё). не выше 150 см или не ниже 198 см
ж). ниже 166 см.
"""

from statistics import NormalDist


def z_value(height):
    return (height - 174) / 8


# а)

z = z_value(182)
z

P = 1 - NormalDist().cdf(z_value(182))
print(f"Ответ для варианта 'а' = {P:.4f}")
print()

# б)

z = z_value(190)
z

P = 1 - NormalDist().cdf(z)
print(f"Ответ для варианта 'б' = {P:.4f}")
print()

# в)

z1 = z_value(166)
z1

z2 = z_value(190)
z2

P = NormalDist().cdf(z2) - NormalDist().cdf(z1)
print(f"Ответ для варианта 'в' = {P:.4f}")
print()

# г)

z1 = z_value(166)
z1

z2 = z_value(182)
z2

P = NormalDist().cdf(z2) - NormalDist().cdf(z1)
print(f"Ответ для варианта 'г' = {P:.4f}")
print()

# д)

z1 = z_value(158)
z1

z2 = z_value(190)
z2

P = NormalDist().cdf(z2) - NormalDist().cdf(z1)
print(f"Ответ для варианта 'д' = {P:.4f}")
print()

# е)

z1 = z_value(150)
z1

z2 = z_value(190)
z2

P = NormalDist().cdf(z1) + (1 - NormalDist().cdf(z2))
print(f"Ответ для варианта 'е' = {P:.4f}")
print()

# ё)

z1 = z_value(150)
z1

z2 = z_value(198)
z2

P = NormalDist().cdf(z1) + (1 - NormalDist().cdf(z2))
print(f"Ответ для варианта 'ё' = {P:.4f}")
print()

# ж)

z = z_value(166)
z

P = NormalDist().cdf(z)
print(f"Ответ для варианта 'ж' = {P:.4f}")
print()
