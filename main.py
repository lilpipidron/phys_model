import math
import matplotlib.pyplot as plt


class Battery:
    def __init__(self, w, m):
        self.w = w
        self.m = m


# w - запас энергии батареи; eta - КПД двигателя; n - мощносность расходуемая пропеллерами
def flight_time(w, eta, n):
    return w * eta / n


# p - вес коптера без батареи; e - эффективность пропеллера (H/Вт)
def propeller_power(p, e):
    return p / e


# w - удельная энергоемксоть аккумулятора (Вт*Ч/кг); m - масса батареи(кг)
def energy_reserve(w, m):
    return w * m


# q - безразмерный коэффициент аэродинамического качества пропеллера; ro - плотность воздуха (кг/куб.м);
# d - диаметр пропеллера(м); f - нагрузка на пропеллер(тяга, развиваемая пропеллером)(H)
def propeller_efficiency(q, ro, d, f):
    return q * d * math.sqrt(ro / f)


# p - вес коптера, n - количество пропеллеров
def propeller_load(p, n):
    return p / n


if __name__ == '__main__':
    # В данном случае возьмем дрон DJI Mavic 3
    p = 0.560
    n = 4
    q = 0.5
    ro = 1.2754
    d = 0.239
    eta = 0.9
    battery = [Battery(20, 0.1), Battery(23.5, 0.132), Battery(43.6, 0.240), Battery(59.29, 0.297), Battery(77, 0.335),
               Battery(93.32, 0.54),
               Battery(100, 0.6), Battery(110, 0.75), Battery(129, 1), Battery(200, 2.3)]
    flight_times = []
    for bt in battery:
        full_p = (p + bt.m) * 10
        self_propeller_load = propeller_load(full_p, n)
        self_propeller_efficiency = propeller_efficiency(q, ro, d, self_propeller_load)
        self_propeller_power = propeller_power(full_p, self_propeller_efficiency)
        self_energy_reserve = energy_reserve(bt.w, bt.m)
        self_flight_time = flight_time(bt.w, eta, self_propeller_power)
        flight_times.append(self_flight_time * 60)

    battery_weight = [bt.m for bt in battery]
    plt.plot(battery_weight, flight_times, 'o-')
    plt.xlabel('Масса аккумулятора(кг)')
    plt.ylabel('Время полета (мин)')
    plt.show()

    battery_capacity = [bt.w for bt in battery]
    plt.plot(battery_capacity, flight_times, 'o-')
    plt.xlabel('Емкость аккумулятора (Вт*Ч/кг)')
    plt.ylabel('Время полета (мин)')
    plt.show()
