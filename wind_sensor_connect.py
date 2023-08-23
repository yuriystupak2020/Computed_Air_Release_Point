import serial
import random
from time import sleep



# Для передачі даних від датчика вітру в Python можна використовувати різні способи
# Залежно від типу датчика і використовуваної технології передачі даних.
# Один із поширених способів передачі даних від датчика вітру - це використання
# інтерфейсу UART (Universal Asynchronous Receiver/Transmitter)
# для зв'язку з мікроконтролером. У цьому випадку дані від датчика вітру передаються по послідовному порту.
# (COM-порт) і можуть бути прочитані в Python за допомогою модуля PySerial.
# Ось приклад коду на Python, який читає дані з COM-порту, використовуючи модуль PySerial:


# ser = serial.Serial('COM1', 9600)  # сстворюємо об'єкт для роботи з  COM-портом

def wind_data():
    wind = []
    for i in range(50):
        wind_power = random.randint(-5, 5)
        wind.append(wind_power)
        sleep(0.001)
    #print(wind)
    return wind

#wind_data()



# while True:
#     # data = ser.readline()  # читаємо данні з COM-порту
#     # print(data)
#     wind_data()
#     sleep(1)

