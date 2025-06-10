from shape_task.shape import Square, Triangle, Rectangle, Circle


def get_max_area(shapes):
    return sorted(shapes, key=lambda shape: shape.get_area(), reverse=True)


square_1 = Square(10)
triangle_1 = Triangle(5, 5, 3, 1, 1, 1)
rectangle_1 = Rectangle(5, 10)
circle_1 = Circle(30)
square_2 = Square(25)
rectangle_2 = Rectangle(6, 9)
circle_2 = Circle(9.1)

shapes_list = [square_1, triangle_1, rectangle_1, circle_1, square_2, rectangle_2, circle_2]
sort_shapes_list = get_max_area(shapes_list)

print(f" {sort_shapes_list[0].__class__.__name__} {sort_shapes_list[0]}, area = {sort_shapes_list[0].get_area()}")
print(f" {sort_shapes_list[1].__class__.__name__} {sort_shapes_list[1]}, area = {sort_shapes_list[1].get_area()}")
