from range_task.range import Range

start_1 = float(input("Введите начальную точку первого диапазона: "))
end_1 = float(input("Введите конечную точку первого диапазона: "))

range_1 = Range(start_1, end_1)

start_2 = float(input("Введите начальную точку второго диапазона: "))
end_2 = float(input("Введите конечную точку второго диапазона: "))

range_2 = Range(start_2, end_2)

if range_1.get_intersection(range_2) is None:
    print("Пересечения диапазонов нет")
else:
    print(f"Диапазон пересечения имеет границы {range_1.get_intersection(range_2)}")

union_ranges_list = range_1.get_union(range_2)

for range in union_ranges_list:
    print(f"Диапазон объединения имеет границы: ({range.start}, {range.end})")

difference_ranges_list = range_1.get_difference(range_2)

for range in difference_ranges_list:
    print(f"Разность диапазонов имеет границы: ({range.start}, {range.end})")
