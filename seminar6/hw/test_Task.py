import pytest
from seminar6.hw.Task import Task

# Тест покрывает базовые случае поиска среднего значения
def test_find_average():
    assert Task.find_average([10, 20, 30, 40, 50]) == 30, "не сработал, в случае нескольких значений в списке"
    assert Task.find_average([]) == 0, "не сработал, в случае пустого списка"
    assert Task.find_average([5]) == 5, "не сработал, в случае одного значения"

# Тест покрывает случай передачи в метод сравнения, не списка
def test_find_average_typeError():
    with pytest.raises(TypeError):
        Task.find_average((1, 2, 3))

# Тест покрывает базовые случае сравнения двух списков
def test_comparison_average():
    assert Task.comparison_average([1, 2, 3, 4, 5],
                                   [6, 7, 8, 9, 10]) == "Второй список имеет большее среднее значение", \
        "не сработал, в случае когда второй список, больше первого"
    assert Task.comparison_average([6, 7, 8, 9, 10],
                                   [1, 2, 3, 4, 5]) == "Первый список имеет большее среднее значение", \
        "не сработал, в случае когда первый список, больше второго"
    assert Task.comparison_average([1, 1, 1, 1, 1],
                                   [1, 1, 1, 1, 1]) == "Средние значения равны", \
        "не сработал, в случае когда оба списка равны"
