import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s] %(message)s"
)


# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """

    def insert(self, intervals, newInterval):

        if len(newInterval) == 0:
            return intervals

        res = []
        n_min = newInterval[0]
        n_max = newInterval[len(newInterval)]
        i = 0

        # nail min
        while i < len(intervals):
            inte = intervals[i]
            if len(inte) == 0:
                i += 1
                continue
            start = inte[0]
            end = inte[1]
            if n_min < end:
                if n_min < start < n_max:
                    inte[0] = n_min
                index_min = i
                break
            i += 1




        # nail max
        while i < len(intervals):
            logging.debug("i : %s" % i)
            inte = intervals[i]
            if len(inte) == 0:
                i += 1
                continue
            start = inte[0]
            end = inte[1]
            if n_max > start:
                if n_max < end:
                    inte[1] = n_max
                index_max = i
                break
            i += 1

        # combind
        if index_min != index_max:


        return res
