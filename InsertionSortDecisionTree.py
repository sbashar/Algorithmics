import itertools
elementPermutation = list(itertools.permutations(["a1", "a2", "a3", "a4"]))
print("Available leaves: " + str(len(elementPermutation)))
for elementList in elementPermutation:
    elementList = list(elementList)
    print("Input : " + str(elementList))
    for i in range(1,len(elementList)):
        j = i
        while j > 0:
            if elementList[j-1] > elementList[j]:
                print(str(j) + " > " + str(j+1))
                temp = elementList[j]
                elementList[j] = elementList[j-1]
                elementList[j-1] = temp
                j = j - 1
            else:
                print(str(j) + " <= " + str(j+1))
                break
    print("Sorted : " + str(elementList))
