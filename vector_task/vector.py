class Vector:
    def __init__(self, *args):
        if len(args) == 0:
            raise ValueError("Недопустимый аргумент")

        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, int):
                if arg <= 0:
                    raise ValueError("Размерность должна быть положительной")
                self._components = [0.0] * arg
            if isinstance(arg, (list, tuple)):
                self._components = [float(x) for x in arg]
            if isinstance(arg, Vector):
                self._components = arg._components.copy()
            else:
                raise TypeError("Неподдерживаемый тип аргумента")

        elif len(args) == 2:
            n = args[0]
            comp_list = args[1]
            if not isinstance(n, int) or n <= 0:
                raise ValueError("Размерность должна быть положительным целым числом")
            if not isinstance(comp_list, (list, tuple)):
                raise TypeError("Второй аргумент должен быть список или кортеж")

            self._components = [0.0] * n
            comp_list = [float(x) for x in comp_list]
            min_len = min(n, len(comp_list))
            self._components[:min_len] = comp_list[:min_len]

        else:
            raise TypeError("Слишком много аргументов")

    @property
    def dimension(self):
        return len(self._components)

    @property
    def length(self):
        return sum(x ** 2 for x in self._components) ** 0.5

    def __repr__(self):
        return "{" + ", ".join(str(x) for x in self._components) + "}"

    @staticmethod
    def _align_components(v1, v2):
        max_dim = max(v1.dimension, v2.dimension)
        comp1 = v1.components + [0.0] * (max_dim - v1.dimension)
        comp2 = v2.components + [0.0] * (max_dim - v2.dimension)
        return comp1, comp2

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        comp1, comp2 = Vector._align_components(self, other)
        return Vector([a + b for a, b in zip(comp1, comp2)])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        comp1, comp2 = Vector._align_components(self, other)
        return Vector([a - b for a, b in zip(comp1, comp2)])

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector([x * scalar for x in self._components])

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

