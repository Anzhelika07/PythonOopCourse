from range_task.range import Range

start = float(input("Введите начальную точку числового диапазона: "))
end = float(input("Введите конечную точку числового диапазона: "))
number = float(input("Введите вещественное число: "))

range = Range(start, end)

if range.is_inside(number):
    print("Введенное число принадлежит диапазону")
else:
    print("Введенное число не принадлежит диапазону")

print(f"Длина диапазона = {range.get_length()}")
