from unittest.mock import Mock

import pytest
from Tasks import Tasks


# Задание 1
def test_find_average():
    assert Tasks.find_average([10, 20, 30, 40, 50]) == 30, "не сработал, в случае нескольких значений в списке"
    assert Tasks.find_average([]) == 0, "не сработал, в случае пустого списка"
    assert Tasks.find_average([5]) == 5, "не сработал, в случае одного значения"


# Задание 2
def test_find_average_typeerror():
    with pytest.raises(TypeError):
        Tasks.find_average("Not a list")


# Задание 3
def test_person_bank_interaction():
    person = Tasks.Person(1000)
    bank = Tasks.Bank()
    person.transfer_money(500, bank)
    assert person.balance == 500
    assert bank.balance == 500


def test_person_bank_valueerror():
    with pytest.raises(ValueError):
        person = Tasks.Person(0)
        bank = Tasks.Bank()
        person.transfer_money(500, bank)


# Задание 4
"""
В предыдущем задании используйте unittest.mock для создания мок-объекта Bank. 
Напишите тест, в котором вы проверите, вызывается ли метод receive_money с правильным 
аргументом.
"""


def test_transfer_with_mock():
    person = Tasks.Person(1000)
    bank_mock = Mock()  # Создаём мок-объект для банка

    person.transfer_money(500, bank_mock)
    bank_mock.receive_money.assert_called_with(500)  # Проверяем, был ли вызван метод receive_money с аргументом 500


# Задание 5
"""
Напишите функцию divide(a, b), которая возвращает результат деления a на b. Если b равно нулю, функция должна вызывать исключение ZeroDivisionError.
Напишите тест, который проверяет, что при попытке деления на ноль функция вызывает исключение ZeroDivisionError.
"""


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        Tasks.divide(10, 0)


# Задание 6
@pytest.mark.parametrize("a, b, expected", [
    (10, 0, 0),  # Умножение на 0
    (-1, 5, -5),  # Умножение отрицательного числа на положительное
    (3, 3, 9),  # Умножение двух положительных чисел
    (-2, -2, 4),  # Умножение двух отрицательных чисел
    (0, 0, 0)  # Умножение двух нулей
])
def test_multiply(a, b, expected):
    assert Tasks.multiply(a, b) == expected


# Задание 7
"""
Напишите тест, который проверяет, что встроенная функция len возвращает корректную длину строки
"""
def test_len_string():
    assert len("Geek") == 4  # Строка из 6 символов
    assert len("") == 0  # Пустая строка
    assert len(" ") == 1  # Строка из одного пробельного символа
    assert len("Hello, World!") == 13  # Строка с пробелами и знаками препинания


# Задание 9
@pytest.mark.parametrize("test_input,expected",
                         [(2, True), (3, True), (4, False), (16, False), (17, True), (18, False)])
def test_is_prime(test_input, expected):
    assert Tasks.is_prime(test_input) == expected
