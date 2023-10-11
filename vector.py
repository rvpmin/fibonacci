#!/usr/bin/env python3

# By: revpmin
# LICENSE GNU/GPL
# My first sequence

N = 10
a = 1
b = 1 
vector = [1,1]

for x in range(1,N+1):
    c = a + b
    vector.append(c)
    a = b
    b = c

print(vector)
