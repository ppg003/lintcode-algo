class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        res = []
        for i in range(len(nestedList)):
            if isinstance(nestedList[i], int):
                res.append(nestedList[i])
            else:

