import itertools

threeElementPermutation = list(itertools.permutations(["a1","a2","a3"]))

for elementList in threeElementPermutation:
    a1,a2,a3 = elementList
    if a3 > a2:
        print("a3 > a2")
        if a1 > a2:
            print("a1 > a2")
            if a1 > a3:
                print("a1 > a3")
            else:
                print("a1 <= a3")
        else:
            print("a1 <= a2")
    else:
        print("a3 <= a2")
        if a1 > a2:
            print("a1 > a2")
        else:
            print("a1 <= a2")
            if a3 > a1:
                print("a3 > a1")
            else:
                print("a3 <= a1")
    print(elementList)
