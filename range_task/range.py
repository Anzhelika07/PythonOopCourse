class Range:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end

    def get_length(self):
        return self.__end - self.start

    def is_inside(self, number):
        return self.__start <= number <= self.__end

    def get_intersection(self, other_range):
        max_start = max(self.__start, other_range.start)
        min_end = min(other_range.end, self.__end)

        if self.__start > other_range.start or self.__end < other_range.end:
            return None

        return Range(max_start, min_end)

    def get_union(self, other_range):
        min_start = min(self.__start, other_range.start)
        max_end = max(other_range.end, self.__end)

        if self.__end < other_range.start or other_range.end < self.__start:
            return [Range(self.__start, self.__end), Range(other_range.start, other_range.end)]

        return [Range(min_start, max_end)]

    def get_difference(self, other_range):
        if other_range.start > self.__start and other_range.end < self.__end:
            return [Range(self.__start, other_range.start), Range(other_range.end, self.__end)]

        if other_range.start == self.__start and other_range.end < self.__end:
            return [Range(other_range.end, self.__end)]

        if other_range.start > self.__start and other_range.end == self.__end:
            return [Range(self.__start, other_range.start)]

        return []

    def __repr__(self):
        return f"({self.__start}; {self.__end})"
