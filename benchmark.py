import time
import random
import matplotlib.pyplot as plt

from bubble_sort import bubble_sort
from quick_sort import quick_sort

sizes = [100, 1000]
bubble_times = []
quick_times = []

for size in sizes:
    data = [random.randint(1, 10000) for _ in range(size)]
    
    data_copy1 = data.copy()
    t0 = time.time()
    bubble_sort(data_copy1)
    bubble_times.append(time.time() - t0)
    
    data_copy2 = data.copy()
    t1 = time.time()
    quick_sort(data_copy2)
    quick_times.append(time.time() - t1)

plt.figure(figsize=(7, 4.5))
plt.plot(sizes, bubble_times, label='сортировка пузырьком', color='red', linewidth=1.5)
plt.plot(sizes, quick_times, label='быстрая сортировка', color='green', linewidth=1.5)

plt.title('сравнение скорости сортировок')
plt.xlabel('кол-во элементов (N)')
plt.ylabel('время(s)')
plt.xticks(sizes)
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig('sorting_benchmark.png', dpi=300)