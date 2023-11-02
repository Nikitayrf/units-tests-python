class Task:

    @staticmethod
    def find_average(numbers):
        if not isinstance(numbers, list):
            raise TypeError("Input should be a list.")
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    @staticmethod
    def comparison_average(numbers_1, numbers_2):
        if numbers_1 > numbers_2:
            return "Первый список имеет большее среднее значение"
        elif numbers_2 > numbers_1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
