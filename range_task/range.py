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

    def get_intersection(self, test_range):
        min_start = min(self.__start, test_range.start)
        max_end = max(test_range.end, self.__end)

        if self.__start == min_start and self.__end == max_end:
            return Range(test_range.start, test_range.end)
        elif test_range.start == min_start and test_range.end == max_end:
            return Range(self.__start, self.__end)
        return None

    def get_union(self, test_range):
        min_start = min(self.__start, test_range.start)
        max_end = max(test_range.end, self.__end)

        if min_start == self.__start and max_end == self.__end:
            return [Range(self.__start, self.__end)]
        elif min_start == test_range.start and max_end == test_range.end:
            return [Range(test_range.start, test_range.end)]
        elif min_start == self.__start and test_range.start < self.__end <= test_range.end:
            return [Range(self.__start, test_range.end)]
        elif min_start == test_range.start and self.__start < test_range.end <= self.__end:
            return [Range(test_range.start, self.__end)]
        return [Range(self.__start, self.__end), Range(test_range.start, test_range.end)]

    def get_difference(self, test_range):
        min_start = min(self.__start, test_range.start)
        max_end = max(test_range.end, self.__end)

        if self.__start == test_range.start and self.__end == test_range.end:
            return []
        elif min_start == self.__start and test_range.start < self.__end <= test_range.end:
            return [Range(self.__start, test_range.start)]
        elif min_start == test_range.start and self.__start < test_range.end <= self.__end:
            return [Range(test_range.end, self.__end)]
        elif min_start == self.__start and max_end == self.__end:
            return [Range(self.__start, test_range.start), Range(test_range.end, self.__end)]
        elif min_start == test_range.start and max_end == test_range.end:
            return [Range(test_range.start, self.__start), Range(self.__end, test_range.end)]
        return [Range(self.__start, self.__end)]

    def __repr__(self):
        return f"({self.__start}; {self.__end})"
