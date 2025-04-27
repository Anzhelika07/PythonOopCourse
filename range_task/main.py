from range_task.range import Range

start = float(input("Введите начальную точку числового диапазона: "))
end = float(input("Введите конечную точку числового диапазона: "))
number = float(input("Введите вещественное число: "))

entered_range= Range(start, end)

if entered_range.is_inside(number):
    print("Введенное число принадлежит диапазону")
else:
    print("Введенное число не принадлежит диапазону")

print(f"Длина диапазона = {entered_range.get_length()}")
