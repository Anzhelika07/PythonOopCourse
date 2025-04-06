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

    def get_intersection_interval(self, start, end):
        if self.__start <= start <= self.__end and self.__start <= end <= self.__end:
            self.__start = start
            self.__end = end
            return self.__start, self.__end
        else:
            return None

    def get_unification_intervals(self, start, end):
        if self.__start <= start <= self.__end and self.__start <= end <= self.__end:
            return [Range(self.__start, self.__end)]
        elif start < self.__start and end > self.__end:
            return [Range(start, end)]
        elif self.__start <= start <= self.__end < end:
            return [Range(self.__start, end)]
        elif start < self.__start <= end <= self.__end:
            return [Range(start, self.__end)]
        else:
            range_1 = self
            range_2 = Range(start, end)
            return [range_1, range_2]

    def get_intervals_difference(self, start, end):
        if self.__start == start and self.__end == end:
            return None
        elif self.__start <= start < self.__end and self.__start < end <= self.__end:
            if self.__start == start:
                return [Range(end + 0.1, self.__end)]
            elif self.__end == end:
                return [Range(self.__start, start - 0.1)]
            else:
                range_1 = Range(self.__start, start - 0.1)
                range_2 = Range(end + 0.1, self.__end)
                return [range_1, range_2]
        else:
            return None
