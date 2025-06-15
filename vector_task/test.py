from vector_task.vector import Vector

v1 = Vector(3)
v2 = Vector([1.0, 2.0, 3.0])
v3 = Vector(5, [1, 2, 3])
v4 = Vector(v2)

print("v1:", v1)
print("v2:", v2)
print("v3:", v3)
print("v4:", v4)

print("v2 dimension:", v2.dimension)
print("v2 length:", v2.length)

v5 = v2 + v3
v6 = v3 - v2
v7 = v2 * 2
v8 = 2 * v2

print("v5 (v2+v3):", v5)
print("v6 (v3-v2):", v6)
print("v7 (v2*2):", v7)
print("v8 (2*v2):", v8)

print("v2[0]:", v2[0])
v2[1] = 5.0
print("v2 после изменения", v2)

print("v2 == v4:", v2 == v4)
v4[1] = 5.0
print("v2 == v4 после изменения:", v2 == v4)

s = {v2, v4}
print(len(s))

v2.negate()
print("v2 разворот вектора:", v2)
print("Скалярное произведение (v2.v4):", v2.dot_product(v4))
