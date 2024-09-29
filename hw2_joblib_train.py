import time
from functools import wraps
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

Data_X = [[3,3, 3], [2,3,2],[3,2,2],[2,2, 3]]
Data_Y = ['h','h',"p", "p"]

# Декоратор для измерения времени выполнения функции
def measure_time(func):
    @wraps(func)
    def timed_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Функция {func.__name__} завершилась за {elapsed_time:.8f} секунд")
        return result
    return timed_function

@measure_time
def model_creating(X, Y):
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X, Y)
    return model

# Обучение модели
trained_model = model_creating(Data_X, Data_Y)

# Cохранениe модели
@measure_time
def model_saving (model_instance, model_filename):
    dump(model_instance, model_filename)

model_saving(trained_model, "model.joblib")

import time
from functools import wraps
from joblib import load as model_load

# Декоратор для измерения времени выполнения функции
def measure_time(func):
    @wraps(func)
    def timed_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Функция {func.__name__} завершилась за {elapsed_time:.8f} секунд")
        return result
    return timed_function

@measure_time
def open_model(file):
    return model_load(file)

# Загрузка модели
random_forest_model = open_model("model.joblib")

# Выполнение прогноза
input_sample = [[3, 3, 3]]
result = random_forest_model.predict(input_sample)
print(f"Предсказание для {input_sample}: {result}")

