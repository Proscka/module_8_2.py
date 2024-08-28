def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:

        for i in numbers:
            try:
                result += i
            except TypeError:
                incorrect_data += 1
                print(f"Некорректный тип данных подсчёта суммы -{i}")

        return result, incorrect_data
    except TypeError:
        return
def calculate_average(numbers):
    res=0
    try:
        sum_result, incorrect_data_count = personal_sum(numbers)

        try:
            average = sum_result/(len(numbers) - incorrect_data_count)
            return average
        except ZeroDivisionError:
            return 0
    except TypeError:
         print(f"В numbers записан некорректный тип данных")
         return None

print(f"Результат1:{calculate_average("1,2,3")}")
print(f"Результат 2:{calculate_average([1,"Строка",3,"Ещё строка"])}")
print(f"Результат3:{calculate_average(567)}")
print(f"Результат4:{calculate_average([42,15,36,13])}")












