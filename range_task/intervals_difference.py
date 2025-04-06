from range_task.range import Range

start = float(input("Введите начальную точку числового диапазона: "))
end = float(input("Введите конечную точку числового диапазона: "))

range = Range(start, end)

start_2 = float(input("Введите начальную точку числового диапазона: "))
end_2 = float(input("Введите конечную точку числового диапазона: "))

objects_list = range.get_intervals_difference(start_2, end_2)

if objects_list is None:
    print("Разность интервалов = 0.")
else:
    for i in objects_list:
        print(f"Разность интервалов имеет границы: {i.start}, {i.end}")
