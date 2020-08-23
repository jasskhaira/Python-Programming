"""
Unpacking Elements from Iterables of Arbitrary
Length

"""
"""
rec = ('Harry', 'Harryjames@gmail.com','416-147-1580','22000',"working")
name,email,*numbers,status=rec

print(name )
print(email )
print(numbers)

nm,*_,stat = rec

print(nm)
print(stat)

"""


"""
Finding the Largest or Smallest N Items
Problem
You want to make a list of the largest or smallest N items in a collection.

"""

from collections import deque
"""
import heapq

num = [1,2,3,5,4,78,8,344,87,43,2,46,97,4343,79]

print(heapq.nlargest(8,num))
print(heapq.nsmallest(8,num))

products = [{'Name ': 'Soap', 'shares':102, 'price': 190},
            {'Name ': 'Soap1', 'shares': 1102, 'price': 7100},
            {'Name ': 'Soap2', 'shares': 1202, 'price': 1500},
            {'Name ': 'Soap3', 'shares': 1302, 'price': 1050},
            {'Name ': 'Soap4', 'shares': 4102, 'price': 1040},
            {'Name ': 'Soap5', 'shares': 1602, 'price': 1030},
            {'Name ': 'Soap6', 'shares': 1702, 'price': 1040}

            ]

cheap = heapq.nsmallest(3, products, key=lambda s:s['price'])
print(cheap)


"""


"""
Implementing a Priority Queue
Problem
You want to implement a queue that sorts items by a given priority and always returns
the item with the highest priority on each pop operation.

"""

import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self._index = 0


    def push(self,item,priority):
        heapq.heappush(self.queue,(-priority,self._index,item))
        self._index += 1


    def pop(self):
        return heapq.heappop(self.queue)[-1]


q = PriorityQueue()
q.push('j',1)
q.push('m',5)
q.push('k',0)

print(q. pop()
cv2.version

