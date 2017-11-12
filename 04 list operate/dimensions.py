#!/usr/bin/python
# -*- coding: UTF-8 -*-

dimensions = (200,50)

print dimensions

print dimensions[0]
print dimensions[1]


print 'original dimension'
print dimensions

dimensions = (1,1,1,1, 1,1,1,1, 1,1)
print 'modified dimesion'
print dimensions
for dimension in dimensions:
    print dimension