from range_task.range import Range

start_1 = float(input("Введите начальную точку первого диапазона: "))
end_1 = float(input("Введите конечную точку первого диапазона: "))

range_1 = Range(start_1, end_1)

start_2 = float(input("Введите начальную точку второго диапазона: "))
end_2 = float(input("Введите конечную точку второго диапазона: "))

range_2 = Range(start_2, end_2)

intersection = range_1.get_intersection(range_2)

if intersection is None:
    print("Пересечения диапазонов нет")
else:
    print(f"Диапазон пересечения имеет границы {intersection}")

union = range_1.get_union(range_2)

for union_range in union:
    print(f"Диапазон объединения имеет границы: ({union_range.start}, {union_range.end})")

difference = range_1.get_difference(range_2)

if difference is None:
    print("Разность найти невозможно.")
else:
    for difference_range in difference:
        print(f"Разность диапазонов имеет границы: ({difference_range.start}, {difference_range.end})")
