import numpy as np
import matplotlib.pyplot as plt

# Параметры системы
k = 1.0  # Коэффициент жесткости пружины
L1 = 1.0  # Расстояние от точки крепления до пружины
m = 1.0  # Масса маятника
g = 9.81  # Ускорение свободного падения
L = 1.0  # Длина подвеса маятника
phi0 = 0.1  # Начальное отклонение угла
beta = 0.1  # Коэффициент затухания

# Вычисление нормальных частот
w1 = np.sqrt(g / L)
w2 = np.sqrt((g / L) + (2 * k * L1 ** 2) / (m * L ** 2))

# Создание временного массива с шагом 0.01 и до времени 10 секунд
times = np.arange(0, 10, 0.01)

# Списки для хранения значений углов отклонения и угловых скоростей
phi1_list = []
phi2_list = []
omega1_list = []
omega2_list = []

# Начальные условия для углов и угловых скоростей
phi1 = phi0
phi2 = phi0
omega1 = 0
omega2 = 0

# Основной цикл симуляции
for t in times:
    # Производные углов отклонения по времени
    dphi1_dt = omega1
    dphi2_dt = omega2

    # Производные угловых скоростей по времени с учетом сил и затухания
    domega1_dt = -(g / L) * np.sin(phi1) - (beta / (m * L ** 2)) * omega1 - (k / (m * L)) * (phi1 - phi2 - L1 / L)
    domega2_dt = -(g / L) * np.sin(phi2) - (beta / (m * L ** 2)) * omega2 - (k / (m * L)) * (phi2 - phi1 - L1 / L)

    # Обновление углов и угловых скоростей с использованием метода Эйлера
    phi1 += dphi1_dt * 0.01
    phi2 += dphi2_dt * 0.01
    omega1 += domega1_dt * 0.01
    omega2 += domega2_dt * 0.01

    # Сохранение текущих значений в списки
    phi1_list.append(phi1)
    phi2_list.append(phi2)
    omega1_list.append(omega1)
    omega2_list.append(omega2)

# Построение графиков
plt.figure(figsize=(12, 12))

# Графики для первого маятника
plt.subplot(2, 2, 1)
plt.plot(times, phi1_list, label='Угол Phi1')
plt.xlabel('Время (с)')
plt.ylabel('Угол (рад)')
plt.title('Угол первого маятника')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(times, omega1_list, label='Угловая скорость Omega1')
plt.xlabel('Время (с)')
plt.ylabel('Угловая скорость (рад/с)')
plt.title('Угловая скорость первого маятника')
plt.legend()

# Графики для второго маятника
plt.subplot(2, 2, 3)
plt.plot(times, phi2_list, label='Угол Phi2')
plt.xlabel('Время (с)')
plt.ylabel('Угол (рад)')
plt.title('Угол второго маятника')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(times, omega2_list, label='Угловая скорость Omega2')
plt.xlabel('Время (с)')
plt.ylabel('Угловая скорость (рад/с)')
plt.title('Угловая скорость второго маятника')
plt.legend()

plt.tight_layout()
plt.show()

# Вывод нормальных частот
print(f'Нормальные частоты: w1 = {w1}, w2 = {w2}')
