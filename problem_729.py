#!/usr/bin/python3
class MyCalendar(object):

    def __init__(self):
        self.bookings = []        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        booking = (start, end)
        def overlap(b1, b2):
            if b2[1] <= b1[0] or b2[0] >= b1[1]: 
                return False
            return True

        for b in self.bookings:
            if overlap(b,booking):
                return False
        self.bookings.append(booking)
        return True
        
    



obj = MyCalendar()

start, end = 10,20
print(obj.book(start,end))

start, end = 15,25
print(obj.book(start,end))

start, end = 20,30
print(obj.book(start,end))
