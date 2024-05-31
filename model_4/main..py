import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def intensity_for_wavelength(N, d, a, x, L, lambda_, m):
    k = 2 * np.pi / lambda_  # волновое число
    beta = k * d / (2 * L) * x
    alpha = k * a * (x / L)

    # Интенсивность интерференционной картины для N щелей
    I = (np.sin(beta) / beta) ** 2 * (np.sin(N * alpha) / np.sin(alpha)) ** 2

    # Добавляем условие для максимумов и минимумов
    if m % 2 == 1:  # максимумы
        I = I * ((np.sin(N * alpha / 2)) / (N * np.sin(alpha / 2))) ** 2
    else:  # минимумы
        I = I * ((np.sin(N * alpha / 2)) / (N * np.sin(alpha / 2))) ** 2

    return I


def plot_intensity(x, I_total):
    plt.figure(figsize=(10, 6))
    plt.plot(x * 1e3, I_total, label='Интенсивность')
    plt.xlabel('Координата x на экране (мм)')
    plt.ylabel('Относительная интенсивность')
    plt.title('Интерференционная картина от N щелей')
    plt.legend()
    plt.grid(True)
    plt.show()

def intensity_to_rgb(intensity):
    norm_intensity = intensity / np.max(intensity)
    return cm.viridis(norm_intensity)

def plot_color_intensity(x, I_total):
    color_image = np.tile(intensity_to_rgb(I_total), (50, 1, 1))
    plt.figure(figsize=(12, 6))
    plt.imshow(color_image, extent=[x[0] * 1e3, x[-1] * 1e3, 0, 1], aspect='auto')
    plt.xlabel('Координата x на экране (мм)')
    plt.title('Цветное распределение интенсивности')
    plt.axis('off')
    plt.show()

# Задаем параметры
N = 5  # количество щелей
d = 0.2e-3  # ширина щели в метрах
a = 1e-3  # период (расстояние между центрами щелей) в метрах
wavelength_center = 500e-9  # центральная длина волны в метрах
wavelength_width = 20e-9  # ширина спектра (полоса) в метрах
L = 1  # расстояние до экрана в метрах

# Создаем массив длин волн для квазимонохроматического света
wavelengths = np.linspace(wavelength_center - wavelength_width / 2,
                          wavelength_center + wavelength_width / 2,
                          100)

# Определяем координаты на экране
x = np.linspace(-0.005, 0.005, 2000)  # экран от -10 мм до 10 мм

# Вычисляем интенсивность для каждой длины волны
I_total = np.zeros_like(x)
m_values = np.arange(1, 2 * N + 1)
for lambda_ in wavelengths:
    for m in m_values:
        I_total += intensity_for_wavelength(N, d, a, x, L, lambda_, m)
I_total /= (len(wavelengths) * len(m_values))

# Строим график интенсивности
plot_intensity(x, I_total)

# Отображаем цветное распределение интенсивности
plot_color_intensity(x, I_total)


# Нормируем интенсивность для отображения
I_total /= np.max(I_total)

# Строим график интенсивности
plot_intensity(x, I_total)

# Отображаем цветное распределение интенсивности
plot_color_intensity(x, I_total)
