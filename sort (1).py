import random
import timeit
import time


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

    # Heap Sort in python


def heapifySort(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapifySort(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2, -1, -1):
        heapifySort(arr, n, i)

    for i in range(n - 1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify root element
        heapifySort(arr, i, 0)


def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


def countingSort(array: list, min_num: int, max_num: int):
    inc = max_num - min_num + 1  # количество возможных чисел (от 13 до 25 их 13)
    count = [0 for i in range(inc)]  # массив счетчиков чисел, индекс каждого эемента соответствует значению числа - min_num, то есть по индексу 0 хранится кол-во попаданий числа 13
    for i in array:
        count[i - min_num] += 1  # увеличиваем счетчик очередного числа

    # а теперь просто сохраняем значения массива в соответствии с подсчетом количества чисел, так как в отсортированном массиве они будут идти группами, например 13 13 13 14 14 14 14 15 16 16...
    k = 0
    for i in range(inc):
        for j in range(count[i]):
            array[k] = i + min_num
            k += 1


data = [random.randint(13, 25) for i in range(10000)]
start = time.time()
bubbleSort(data)
end = time.time()
print(f'Время выполнения сортировки пузырьком {(end-start) * 10**3}мс')

data = [random.randint(13, 25) for i in range(10000)]
start = time.time()
size = len(data)
selectionSort(data, size)
end = time.time()
print(f'Время выполнения сортировки выбором {(end-start) * 10**3}мс')

data = [random.randint(13, 25) for i in range(10000)]
start = time.time()
heapSort(data)
end = time.time()
print(f'Время выполнения сортировки кучи {(end-start) * 10**3}мс')

data = [random.randint(13, 25) for i in range(10000)]
start = time.time()
size = len(data)
shellSort(data, size)
end = time.time()
print(f'Время выполнения сортировки Шелла {(end-start) * 10**3}мс')

data = [random.randint(13, 25) for i in range(10000)]
start = time.time()
countingSort(data, 13, 25)
end = time.time()
print(f'Время выполнения сортировки подсчетом {(end-start) * 10**3}мс')

