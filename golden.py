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

for l in range(len(vector) - 1):
    print(vector[l]/vector[l + 1])

gold_ratio = vector[len(vector) - 1] / vector[len(vector) - 2]
print(gold_ratio)
