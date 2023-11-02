"""Module servant of the starting point for program execution."""
from Task import Task

if __name__ == '__main__':
    avg_1 = Task.find_average([1, 2, 3, 4, 5])
    avg_2 = Task.find_average([6, 7, 8, 9, 10])
    result = Task.comparison_average(avg_1, avg_2)

    avg_1 = Task.find_average([])

    avg_1 = Task.find_average([6, 7, 8, 9, 10])
    avg_2 = Task.find_average([1, 2, 3, 4, 5])
    result = Task.comparison_average(avg_1, avg_2)

    avg_1 = Task.find_average([1, 2, 3, 4, 5])
    avg_2 = Task.find_average([1, 2, 3, 4, 5])
    result = Task.comparison_average(avg_1, avg_2)
