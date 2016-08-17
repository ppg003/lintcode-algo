class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            somme_1 = 0
            somme_2 = 1
            somme = 0
            for i in range(0, n-2):
                somme = somme_1 + somme_2
                somme_1 = somme_2
                somme_2 = somme
            return somme