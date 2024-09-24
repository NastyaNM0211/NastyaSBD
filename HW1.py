# Синхронное чтение кода состояния

import time
import requests
import threading

def read_example() -> None:
  response = requests.get('https://www.example.com')
  print(response.status_code)

sync_start = time.time()

read_example()
read_example()

sync_end = time.time()

print(f'Синхронное выполнение заняло {sync_end - sync_start:.4f} с.')

# Многопоточная версия

def read_example() -> None:
  response = requests.get('https://www.example.com')
  print(response.status_code)

thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

thread_start = time.time()

thread_1.start()
thread_2.start()

print('Все потоки работают!')

thread_1.join()
thread_2.join()

thread_end = time.time()

print(f'Многопоточное выполнение заняло {thread_end - thread_start:.4f} с.')

# Декоратор для измерения времени выполнения функции
def time_decorator(func): #Функция-декоратор, воспринимающая функцию funk в качестве переменной
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Запоминаем время начала
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        end_time = time.time()  # Запоминаем время окончания
        print(f'Время выполнения {func.__name__}: {end_time - start_time:.4f} с.')
        return result  # Возвращаем результат оригинальной функции
    return wrapper

@time_decorator  # Применяем декоратор к функции (то есть при вызове функции read_example будет фактически вызываться функция wrapper из декоратора)
def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)

# Синхронное выполнение
sync_start = time.time()

read_example()
read_example()

sync_end = time.time()

print(f'Синхронное выполнение заняло {sync_end - sync_start:.4f} с.')

# Многопоточное выполнение
thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

thread_start = time.time()

thread_1.start()
thread_2.start()

print('Все потоки работают!')

thread_1.join()
thread_2.join()

thread_end = time.time()

print(f'Многопоточное выполнение заняло {thread_end - thread_start:.4f} с.')

