from range_task.range import Range

start = float(input("Введите начальную точку числового диапазона: "))
end = float(input("Введите конечную точку числового диапазона: "))

range = Range(start, end)

start_2 = float(input("Введите начальную точку числового диапазона: "))
end_2 = float(input("Введите конечную точку числового диапазона: "))

objects_list = range.get_unification_intervals(start_2, end_2)

for i in objects_list:
    print(f"Интервал объединения имеет границы: ({i.start}, {i.end})")
