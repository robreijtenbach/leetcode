#!/usr/bin/python
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        def reveal(l):
            order = list(range(l))
            res = []

            while len(order) > 1:
                res.append(order[0])
                order.append(order[1])
                order = order[2:]
            res.append(order[0])
            return res

        deck.sort()
        order = reveal(len(deck))
        print(order)

        res = [0]*len(deck)
        #res = []

        for i in range(len(deck)):
            res[order[i]] = deck[i]

        return res





s = Solution()

deck = [17,13,11,2,3,5,7]

print(s.deckRevealedIncreasing(deck))

