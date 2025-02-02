import numpy as np
import time
import matplotlib.pyplot as plt
import random

# Реалізація детермінованого QuickSort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Вибір середнього елемента
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Реалізація рандомізованого QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Випадковий вибір опорного елемента
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Генерація тестових даних
sizes = [10_000, 50_000, 100_000, 500_000]
num_trials = 5

deterministic_times = []
randomized_times = []

for size in sizes:
    arr = np.random.randint(0, 10**6, size)  # Заповнення випадковими числами

    # Вимірювання часу для детермінованого QuickSort
    det_time = []
    for _ in range(num_trials):
        arr_copy = arr.copy()
        start = time.time()
        deterministic_quick_sort(arr_copy)
        end = time.time()
        det_time.append(end - start)
    deterministic_times.append(np.mean(det_time))

    # Вимірювання часу для рандомізованого QuickSort
    rand_time = []
    for _ in range(num_trials):
        arr_copy = arr.copy()
        start = time.time()
        randomized_quick_sort(arr_copy)
        end = time.time()
        rand_time.append(end - start)
    randomized_times.append(np.mean(rand_time))

# Побудова графіку
plt.figure(figsize=(8, 6))
plt.plot(sizes, randomized_times, label="Рандомізований QuickSort", color="blue")
plt.plot(sizes, deterministic_times, label="Детермінований QuickSort", color="orange")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.legend()
plt.grid()
plt.show()

# Виведення результатів у термінал
for i, size in enumerate(sizes):
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {randomized_times[i]:.4f} секунд")
    print(f"   Детермінований QuickSort: {deterministic_times[i]:.4f} секунд")
