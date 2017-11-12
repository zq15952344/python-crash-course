#!/usr/bin/python
# -*- coding: UTF-8 -*-

for value in range(1,5):
    print value

numbers = list(range(1,6))
print numbers

even_number = list(range(2,11,2))
print even_number

squares = []
for value in range(1,100):
    square = value ** 2
    squares.insert(0,square)
print squares

print min(squares)
print max(squares)
print sum(squares)

squares2 = [value ** 2 for value in range(1,11)]
print squares2

numbers = [value ** 3 for value in range(1,11)]
print numbers


