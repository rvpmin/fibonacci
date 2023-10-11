#!/usr/bin/env python3

# By: revpmin
# LICENSE GNU/GPL
# My first sequence

N = 100
a = 1
b = 1
print(a)
print(b)

for x in range(1,N+1):
    c = a + b
    print(c)
    f = b
    a = f
    b = c
    
