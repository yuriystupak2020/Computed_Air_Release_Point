import wind_sensor_connect

import numpy as np


# wind_sensor_connect.wind_data()

def wind():
    x = wind_sensor_connect.wind_data()
    y = wind_sensor_connect.wind_data()
    print("X: ", x)
    print("Y: ", y)
    return x, y

A = 1 #1 m^2 площа поверхні тіла
Va = 1 # швидкість дрона і обєкта
p = 1.26 # плотность повітря
Cd = 0.575 # коеф лобового супротиву


Fd = 1/2*Cd*A*p*(Va**2)  # сила дії на об'кт

Fd = 1/2*0.5*1*1.26*(1)
print(Fd)


# x_pos = [x, y, z, Vx, Vy, Vz].T
# x_pos = [1,2,3,4,5,6].T
# print(x_pos)

# Створення матриці
matrix = np.array([[1, 2], [3, 4], [5, 6]])

# Транспонування матриці
transposed_matrix = matrix.T

# Вивід результатів
print("Матриця:")
print(matrix)
print("Транспонована матриця:")
print(transposed_matrix)




if __name__ == '__main__':
    wind()


