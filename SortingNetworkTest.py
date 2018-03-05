import itertools
elementPermutation = list(itertools.permutations([1,2,3,4,5]))
for  a1,a2,a3,a4,a5 in elementPermutation:
    inputElement = "Input :" + " a1 = " + str(a1) + " a2 = " + str(a2) + " a3 = " + str(a3) + " a4 = " + str(a4) + " a5 = " + str(a5)
    if a4 < a2:
        a4,a2 = a2,a4
    if a4 < a3:
        a4,a3 = a3,a4
    if a5 < a4:
        a5,a4 = a4,a5
    if a4 < a3:
        a4,a3 = a3,a4
    if a3 < a2:
        a3,a2 = a2,a3
    if a2 < a1:
        a2,a1 = a1,a2
    if a3 < a2:
        a3,a2 = a2,a3
    if a4 < a3:
        a4,a3 = a3,a4
    if a5 < a4:
        a5,a4 = a4,a5
    if (a1,a2,a3,a4,a5) != (1,2,3,4,5):
        print(inputElement)
        print("Not Sorted :" + " a1 = " + str(a1) + " a2 = " + str(a2) + " a3 = " + str(a3) + " a4 = " + str(a4) + " a5 = " + str(a5))
