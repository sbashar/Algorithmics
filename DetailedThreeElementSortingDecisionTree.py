import itertools

threeElementPermutation = list(itertools.permutations([1,2,3]))

for a1,a2,a3 in threeElementPermutation:
    print("Input sequence: a1 = " + str(a1) + " a2 = " + str(a2) + " a3 = " + str(a3))
    if a3 > a2:
        print("a3 > a2")
        if a1 > a2:
            print("a1 > a2")
            if a1 > a3:
                print("a1 > a3")
                print("Sorted sequence: a2 = " + str(a2) + " <= a3 = " + str(a3) + " <= a1 = " + str(a1))
            else:
                print("a1 <= a3")
                print("Sorted sequence: a2 = " + str(a2) + " <= a1 = " + str(a1) + " <= a3 = " + str(a3))
        else:
            print("a1 <= a2")
            print("Sorted sequence: a1 = " + str(a1) + " <= a2 = " + str(a2) + " <= a3 = " + str(a3))
    else:
        print("a3 <= a2")
        if a1 > a2:
            print("a1 > a2")
            print("Sorted sequence: a3 = " + str(a3) + " <= a2 = " + str(a2) + " <= a1 = " + str(a1))
        else:
            print("a1 <= a2")
            if a3 > a1:
                print("a3 > a1")
                print("Sorted sequence: a1 = " + str(a1) + " <= a3 = " + str(a3) + " <= a2 = " + str(a2))
            else:
                print("a3 <= a1")
                print("Sorted sequence: a3 = " + str(a3) + " <= a1 = " + str(a1) + " <= a2 = " + str(a2))
