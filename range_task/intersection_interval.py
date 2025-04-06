from range_task.range import Range

start = float(input("Введите начальную первого интервала: "))
end = float(input("Введите конечную точку первого интервала: "))

range = Range(start, end)

start_2 = float(input("Введите начальную точку второго интервала: "))
end_2 = float(input("Введите конечную точку второго интервала: "))

range_2 = range.get_intersection_interval(start_2, end_2)

if range_2 is None:
    print("Пересечения интервалов нет")
else:
    print(f"Интервал пересечения имеет границы {range_2}")
