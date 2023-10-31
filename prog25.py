from itertools import permutations
w=input("Enter A word:")
for i in range(2,len(w)):
    for p in permutations(w,i):
        print(".join(p),end=' ')
