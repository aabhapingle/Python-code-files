from itertools import permutations
s, k = map(str, input().split())
for i in list(permutations( sorted(s), int(k))):
    for j in i:
        print(j , end='')
    print('')